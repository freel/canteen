# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Sales_Ui import Ui_Sales
from Worker_Class import Worker_Class
from localDb_Class import localDb_Class
from Shift_Class import Shift
from productSalePanel_Class import productSalePanel_Class

class Sales_Class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.parent = parent
        self.setupData()
        self.setupUi()
        #self.connect(self.ui.cardEdit, QtCore.SIGNAL("returnPressed()"),QtCore.SLOT("on_cardSubmit()"))
        #self.connect(self.ui.tableWidget, QtCore.SIGNAL("itemDoubleclicked()"),QtCore.SLOT("on_rowClicked()"))
        #self.connect(self.ui.chequeButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_save()"))

        #self.ui.tableWidget.installEventFilter(self)

        #parent.setCentralWidget(self)

    def renew(self):
        self.clear()
        self.setupData()
        self.fillUi()

## DATA ##

    def setupData(self):
        self.shift = self.parent.shift

    def select_menu(self,shift):
        """Выбираем сегодняшнее меню из базы"""
        db = localDb_Class()
        query = "SELECT m.id, d.name, m.balance, m.price FROM menu as m,dish as d,shift as s WHERE "
        query += "s.shift=m.shift AND d.id=m.dish AND s.shift='%s'" % shift
        rows = db.exec_query(query)
        db.close_db()
        return rows

    def select_from_old_menu(self,shift):
        """Выбираем сегодняшнее меню из базы"""
        db = localDb_Class()
        query = "SELECT m.id, '[С] ' || d.name, m.balance, m.price  FROM menu as m,dish as d,shift as s WHERE "
        query += "s.shift=m.shift AND d.id=m.dish AND s.shift<'%s' AND m.balance>0" % shift
        rows = db.exec_query(query)
        db.close_db()
        return rows

    def select_from_goods(self,shift):
        """Выбираем сегодняшнее меню из базы"""
        db = localDb_Class()
        query = "SELECT 's' || i.id, i.name, i.rest / i.mass as rest, i.price FROM product as p, income as i WHERE "
        query += "p.for_sale AND p.id=i.product AND i.product=p.id AND i.rest>0"
        rows = db.exec_query(query)
        db.close_db()
        return rows

## UI ##

    def setupUi(self):
        self.ui = Ui_Sales()
        self.ui.setupUi(self)
        self.fillUi()
        self.connect(self.ui.treeWidgetMenu, QtCore.SIGNAL("itemClicked ( QTreeWidgetItem*, int )"), self.onClick)
        self.connect(self.ui.treeWidgetGoods, QtCore.SIGNAL("itemClicked ( QTreeWidgetItem*, int )"), self.onClick)

    def fillUi(self):
        self.setEnabled(False)
        self.menu = {}
        self.getMenu()


    def getMenu(self):
        """Заполняем таблицу с меню из базы"""
        """Из сегодняшнего"""
        answer = self.select_menu(self.shift.shift)
        self.setCanteenIntoTable(answer)
        """Остатки от предыдущего"""
        answer = self.select_from_old_menu(self.shift.shift)
        self.setCanteenIntoTable(answer)
        #"Отоварка"
        answer = self.select_from_goods(self.shift.shift)
        self.setGoodsIntoTable(answer)

    def setCanteenIntoTable(self, answer):
        for row in answer['rows']:
            widget = productSalePanel_Class(self,row)
            self.menu[row[0]] = widget
            self.ui.treeWidgetMenu.addTopLevelItem(self.menu[row[0]])
            #ro = self.ui.canteenLayout.count() // 3
            #col = self.ui.canteenLayout.count() - ro * 3
            #self.ui.canteenLayout.addWidget(self.menu[row[0]], ro+1, col+1, 1, 3)

    def setGoodsIntoTable(self, answer):
        for row in answer['rows']:
            widget = productSalePanel_Class(self,row)
            self.menu[row[0]] = widget
            self.ui.treeWidgetGoods.addTopLevelItem(self.menu[row[0]])
            #ro = self.ui.goodsLayout.count() // 3
            #col = self.ui.goodsLayout.count() - ro * 3
            #self.ui.goodsLayout.addWidget(self.menu[row[0]], ro+1, col+1, 1, 3)

    def on_rowClicked(self):
        """По щелчку на строке смотрим если еще ни одного не заказано, то ставим 1, считаем
        если уже чтото заказано, то прибавляем туда еще один
        TO DO прицепить к кнопкам"""
        row = self.ui.tableWidget.currentRow()
        table = self.ui.tableWidget
        try:
            num = int(table.item(row,3).text())+1
            summ = num*float(table.item(row,2).text())
            table.item(row,3).setText("%s" % num)
            table.item(row,4).setText("%s" % summ)
        except:
            item_1 = QtGui.QTableWidgetItem()
            table.setItem(row, 3, item_1)
            item_1.setText(u"%s" % 1)
            item_2 = QtGui.QTableWidgetItem()
            table.setItem(row, 4, item_2)
            item_2.setText(u"%s" % float(table.item(row,2).text()))

    def saleClick(self,dish):
        self.parent.sales.addDish(dish)

    def onClick(self, item, column ):
        item.onClick()

    def clear(self):
        self.ui.treeWidgetMenu.clear()
        self.ui.treeWidgetGoods.clear()
        self.parent.sales.clear()

    def eventFilter(self,  obj,  event):
        """То же что и выше.
        ЗАЧЕМ????"""
        if event.type() == QtCore.QEvent.KeyPress:
            try:
                {QtCore.Qt.Key_Space:self.ui.tableWidget.emit,
                QtCore.Qt.Key_Enter:self.ui.tableWidget.emit,
                }[event.key()](QtCore.SIGNAL("itemDoubleclicked()"))
                return True
            except KeyError as e:
                return False
        return False
