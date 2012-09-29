# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Menu_Ui import Ui_Menu
from localDb_Class import localDb_Class
from Shift_Class import Shift
from Dish_Class import Dish_Class
from productParent_Class import productDishPanel_Class, productMenuPanel_Class
#from productPanel_Class import productPanel_Class
from ui.groupPanel import Ui_groupPanel
from ui.DishCount_Ui import Ui_DishCount

class Menu_Class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.setupData()
        self.setupUi()

    def renew(self):
        """обновление данных"""
        self.clear()
        self.setupData()
        self.insertValsIntoWidget()

    def renewPortions(self):
        for num in self.productWidget:
            self.productWidget[num].portions = self.productWidget[num].select_max_portions()
            self.productWidget[num].changeCount()
            if self.productWidget[num].portions <= 0:
                self.productWidget[num].setDisabled(True)

## DATA ##

    def setupData(self):
        """Заполнение переменных и формы"""
        self.shift = self.parent.shift
        self.products = self.getProductRest()

    def getProductRest(self):
        """Выбираем остаток продуктов на складе
         ID прихода, ID продукта, остаток в граммах"""
        db = localDb_Class()
        query = "SELECT p.id, SUM(i.rest) as sum FROM income AS i, product AS p WHERE p.id=i.product AND i.rest>0 AND i.active AND p.active GROUP BY p.id"
        rows = {pid:val for pid,val in db.exec_query(query)['rows']}
        db.close_db()
        return rows

    def insertValsIntoWidget(self):
        """Создает дерево продуктов по разделам"""
        self.groupWidget = {}
        self.productWidget = {}
        self.menuWidget = {}
        map(self.setHeader,self.getSections()['rows'])
        map(self.setRow,self.getRows()['rows'])

    def getSections(self):
        """Берет список разделов"""
        db = localDb_Class()
        query = "SELECT DISTINCT s.id, s.name FROM section as s, dish as d WHERE d.section=s.id"
        vals = db.exec_query(query)
        db.close_db()
        return vals

    def getRows(self):
        """Список блюд"""
        db = localDb_Class()
        vals = db.select_all_val('dish')
        db.close_db()
        return vals

    def saveMenu(self):
        """Сохраняет меню"""
        for did in self.menuWidget:
            self.save_calculate(did)
        self.renew()

    def save_calculate(self, did):
        """Проводит запись блюда и калькуляции"""
        self.save_calc(did)
        self.save_menu_item(did)

    def save_calc(self, did):
        """Сохраняет калькуляцию"""
        db = localDb_Class()
        self.menuWidget[did].amortizate()
        for product in self.menuWidget[did].amortization:
            for income in self.menuWidget[did].amortization[product]:
                db.insert_val('calculate',(income, product, self.menuWidget[did].did, self.menuWidget[did].product[product]))
                row = db.select_val_by_id('income',income)['rows'][0]['rest']
                amortization = row - self.menuWidget[did].consumption[product] * self.menuWidget[did].amortization[product][income]
                db.update_val_by_id_name('income',income,'rest',amortization)
        db.close_db()

    def save_menu_item(self,did):
        """Сохраняет строку из меню"""
        db = localDb_Class()
        db.insert_val('menu',(did, self.shift.shift, self.menuWidget[did].portions, self.menuWidget[did].portions, self.menuWidget[did].price))
        db.close_db()


    def select_menu(self,shift):
        """Выбор строк меню"""
        db = localDb_Class()
        query = "SELECT m.id, d.name, m.price FROM menu as m,dish as d,shift as s WHERE "
        query += "s.shift=m.shift AND d.id=m.id AND s.shift=%s" % shift
        rows = db.exec_query(query)
        db.close_db()
        return rows

    def select_consumption(self):
        """Формирует цену на продукт на порцию блюда"""
        db = localDb_Class()
        query = "SELECT p.id as product, c.brutto "# i.price*i.coefficient*c.brutto/i.mass as price "
        query += "FROM consumption as c, product as p, income as i WHERE "
        query += "c.product = p.id AND i.product=p.id AND c.dish=" + "\'%s\'" % self.id
        rows = db.exec_query(query)
        db.close_db()
        return rows

## UI ##

    def setupUi(self):

        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        self.insertValsIntoWidget()
        self.connect(self.ui.saveMenuButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveMenu()"))
        self.connect(self.ui.addDishButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("addDish()"))
        self.connect(self.ui.treeWidgetDish, QtCore.SIGNAL("itemClicked ( QTreeWidgetItem*, int )"), self.onClick)
        self.connect(self.ui.addToMenuButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("addToMenu()"))
        self.connect(self.ui.delFromMenuButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("delFromMenu()"))

    def clear(self):
        """Очистка формы"""
        self.ui.treeWidgetDish.clear()
        self.ui.treeWidgetMenu.clear()

    def setHeader(self,row):
        """Расстановка заголовков разделов"""
        widget = QtGui.QTreeWidgetItem(0)
        widget.setText(0,u"%s" % row[1])

        self.groupWidget[row['id']] = widget
        self.ui.treeWidgetDish.addTopLevelItem(self.groupWidget[row['id']])
        self.ui.treeWidgetDish.setFirstItemColumnSpanned(self.groupWidget[row['id']],True)
        self.groupWidget[row['id']].setExpanded(True)

    def setRow(self,row):
        """Заполнение списка блюд"""
        #widget = productDishPanel_Class(self, (row['id'], row['name']))

        #try:
        #~ print (row['id'], row['name'])
        widget = productDishPanel_Class(self, (row['id'], row['name']))
        self.productWidget[row['id']] = widget
        self.groupWidget[int(row['section'])].insertChild(0,self.productWidget[row['id']])
        #except:
        #    None

    def addDish(self):
        """Добавляет блюдо"""
        form = Dish_Class(self)
        form.show()

    #~ def delFromMenu(self):
        #~ """Удаление строки из меню"""
        #~ self.renew()
        #~ item = self.ui.treeWidgetMenu.currentItem()
        #~ item.delFromMenu()
        #~ self.ui.treeWidgetMenu.removeRow(self.ui.treeWidgetMenu.currentRow())

    def addToMenu(self):
        item = self.ui.treeWidgetDish.currentItem()
        self.onClick(item)
        

    def onClick(self, item, column = None ):
        """item это объект productDishPanel_Class """
        self.openCount(item)

## WidgetCount ##

    def openCount(self,item):
        """Открывается окно с количеством добавляемых блюд
        По нажаию на ОК выполняется onSubmitCount()"""
        self.widgetCount = QtGui.QWidget(self.parent, QtCore.Qt.Window)
        self.widgetCount.setWindowModality(QtCore.Qt.ApplicationModal)
        self.widgetCount.ui = Ui_DishCount()
        self.widgetCount.ui.setupUi(self.widgetCount)
        self.widgetCount.item = item
        self.widgetCount.ui.spinBox.setMinimum(0)
        self.widgetCount.ui.spinBox.setMaximum(self.widgetCount.item.portions)

        self.connect(self.widgetCount.ui.submitButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onSubmitCount()"))
        self.connect(self.widgetCount.ui.closeButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onCloseCount()"))
        self.widgetCount.show()

    def onSubmitCount(self):
        """Вызывается при принятии окна с количеством
        Добаввляет в меню блюдо в указанном количестве"""
        self.widgetCount.close()
        self.widgetCount.value = self.widgetCount.ui.spinBox.value()
        item = self.widgetCount.item
        portions = self.widgetCount.value
        item.removePortions(portions)
        for product in item.consumption:
            self.products[product] -= item.consumption[product]*portions
        if item.did in self.menuWidget:
            item.changeCount()
            self.menuWidget[item.did].portions += portions
            self.menuWidget[item.did].setText(1, u"%s" % self.menuWidget[item.did].portions)
        else:
            widget = productMenuPanel_Class(self,(item.did, item.name, portions))
            #widget.portions = portions
            widget.max_amortization = item.max_amortization
            #widget.price = widget.getDishPrice()
            item.setText(1, u"%s" % item.portions)
            widget.setText(1, u"%s" % widget.portions)
            self.menuWidget[item.did] = widget
            self.ui.treeWidgetMenu.addTopLevelItem(self.menuWidget[item.did])
        self.renewPortions()

    def onCloseCount(self):
        """Вызывается при закрытии окна с количеством"""
        self.widgetCount.close()
        self.widgetCount.value = None

    def delFromMenu(self):
        """Удаляет из меню"""
        item = self.ui.treeWidgetMenu.currentItem()
        portions = item.portions
        item.removePortions(portions)
        for product in item.consumption:
            self.products[product] += item.consumption[product]*portions
        if item.did in self.productWidget:
            item.changeCount()
            self.productWidget[item.did].portions += portions
            self.productWidget[item.did].setText(1, u"%s" % self.productWidget[item.did].portions)
        else:
            widget = productDishPanel_Class(self,(item.did, item.name, portions))
            #widget.portions = portions
            widget.max_amortization = item.max_amortization
            #widget.price = widget.getDishPrice()
            item.setText(1, u"%s" % item.portions)
            widget.setText(1, u"%s" % widget.portions)
            self.productWidget[item.did] = widget
            self.ui.treeWidgetDish.addTopLevelItem(self.productWidget[item.did])
        self.ui.treeWidgetMenu.takeTopLevelItem(self.ui.treeWidgetMenu.indexOfTopLevelItem(item))
        del self.menuWidget[item.did]
        self.renewPortions()
