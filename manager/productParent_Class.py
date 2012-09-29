# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from localDb_Class import localDb_Class
from ui.productPanel import Ui_productPanel
from ui.DishCount_Ui import Ui_DishCount
from datetime import datetime

class productParent_Class(QtGui.QTreeWidgetItem):
    def __init__(self, parent, row):
        QtGui.QTreeWidgetItem.__init__(self)
        self.parent = parent
        self.row = row
        self.renew()

    def renew(self):
        self.setupData()
        self.setupUi()

## DATA ##

    def setupData(self):
        """
        Итак расскажем что же тут происходит на самом деле
        (эткая запутанная детективная пьеса)
        did, name - передали с родителя,
        consumption - состав,
        amortization -
        """
        self.did = self.row[0]
        self.name = self.row[1]
        self.amortization = {}
        self.product = {}
        self.consumption = self.select_consumption()

        try:
            self.portions = self.row[2]
        except:
            self.portions = self.select_max_portions()

        try:
            self.price = self.row[3]
        except:
            if self.portions:
                self.price = self.getDishPrice()
            else:
                self.price = 0

    def getDishPrice(self):
        """Считает цену продукта"""
        summ = 0
        #num = 0
        #for row in self.consumption:
        #    rest = self.portions
        #    product_prices = self.getProductPrice(row)['rows']
        #    self.max_amortization[row] = {}
        #    for income_price in product_prices:
        #        if rest-income_price['count']<=0:
        #            summ += rest*income_price['price']
        #            self.max_amortization[row][income_price['id']] = rest
        #            rest=0
        #        else:
        #            summ += income_price['count']*income_price['price']
        #            self.max_amortization[row][income_price['id']] = income_price['count']
        #            rest -= income_price['count']
        #price = round(summ / self.portions, 2)
        for row in self.consumption:
            self.product[row] = self.getProductPrice(row)
            summ += self.product[row]
        price = round(summ, 2)
        print price
        return price

    def select_max_portions(self):
        """Возвращает максимально возможное количество порций
        Формула:
        кол-во = минимум ( остаток продукта / массу в порции для продуктов в блюде )
        """
        try:
            lst = {self.parent.products[num] // self.consumption[num] for num in self.consumption}
            return min(lst)
        except:
            return None

    def getProductPrice(self,prid):
        db = localDb_Class()
        query = "SELECT i.rest/{0} as count, i.price*{0}/i.mass as price, i.id as id ".format(self.consumption[prid])
        query += "FROM income as i WHERE "
        query += "i.product=" + "\'%s\'" % prid
        query += "ORDER BY date"
        rows = db.exec_query(query)
        db.close_db()
        return round(rows['rows'][0]['price'],2)

    #def getAvailableCount(self):
        #"""Определяет максимальное количество порций блюда, исходя из наличия продуктов на складе"""
        #available = self.select_max_portions()[0][0]
        #return available

    def select_consumption(self):
        """Формирует цену на продукт на порцию блюда"""
        db = localDb_Class()
        query = "SELECT p.id as product, c.brutto "# i.price*i.coefficient*c.brutto/i.mass as price "
        query += "FROM consumption as c, product as p, income as i WHERE "
        query += "c.product = p.id AND i.product=p.id AND c.dish=" + "\'%s\'" % self.did
        rows = db.exec_query(query)
        db.close_db()
        consumption = {}
        for row in rows['rows']:
            if row[1] == 0:
                self.select_brutto(row[0])
            else:
                consumption[row[0]] = row[1]
        return consumption

        def select_brutto(self, pid):
            db = localDb_Class()
            data = (pid, datetime.now().strftime("%d-%m"))
            query = "SELECT c.percent FROM coefficient as c, product as p WHERE p.id = c.product AND p.id={0} AND period_start<={1} AND period_finish>={1}".format(data)
            #print query
            db.exec_query(query)
            db.close_db()

    #def select_max_portions(self):
        #db = localDb_Class()
        #query = "SELECT MIN(i.rest / c.brutto) AS count FROM income AS i, consumption AS c, dish AS d WHERE d.id={} AND c.dish=d.id AND c.product=i.product".format(self.id)
        #rows = db.exec_query(query)
        #db.close_db()
        #return rows['rows']

## GUI ##

    def setupUi(self):
        self.setText(0,u"%s" % self.row[1])
        self.setText(1,u"%s" % self.portions)
        self.setText(2,u"%s" % self.price)
        #self.ui = Ui_productPanel()
        #self.ui.setupUi(self)
        #self.setMinimumSize(QtCore.QSize(200, 50))
        #self.ui.productButton.setText(self.name)
        #self.ui.priceLabel.setText(u"%s" % self.price)
        #self.changeCount()

    def changeCount(self):
        self.setText(1,u"%s" % self.portions)

class productMenuPanel_Class(productParent_Class):
    """Панель продуктов в меню"""
    def __init__(self, parent, row):
        productParent_Class.__init__(self, parent, row)

    #def getDishPrice(self):
        #self.price = self.row[2]

    def amortizate(self):
        for product in self.consumption:
            rest = self.portions
            self.amortization[product] = {}
            for income in self.max_amortization[product]:
                if self.max_amortization[product][income] - rest <= 0:
                    self.amortization[product][income] = self.max_amortization[product][income]
                    rest -= self.max_amortization[product][income]
                else:
                    self.amortization[product][income] = rest
                    rest = 0

class productDishPanel_Class(productParent_Class):
    """Панель доступных продуктов"""
    def __init__(self, parent, row):
        productParent_Class.__init__(self, parent, row)
        #self.portions = self.select_max_portions()
        self.changeCount()


    def onClick(self):
        portions = self.openCount()

    def recount(self, portions):
        self.portions -= portions
        for product in self.consumption:
            self.parent.products[product] -= self.consumption[product]*portions
        if self.row[0] in self.parent.menuWidget:
            self.changeCount()
            self.parent.menuWidget[self.row[0]].portions += portions
            self.parent.menuWidget[self.row[0]].setText(1, u"%s" % self.parent.menuWidget[self.row[0]].portions)
        else:
            widget = productMenuPanel_Class(self.parent,(self.row[0], self.row[1], portions))
            #widget.portions = portions
            widget.max_amortization = self.max_amortization
            #print "dghdfhdfghdfgh"
            #widget.price = widget.getDishPrice()
            self.setText(1, u"%s" % self.portions)
            widget.setText(1, u"%s" % widget.portions)
            self.parent.menuWidget[self.row[0]] = widget
            self.parent.ui.treeWidgetMenu.addTopLevelItem(self.parent.menuWidget[self.row[0]])
        self.parent.renewPortions()

    def openCount(self):
        self.widgetCount = QtGui.QWidget(self.parent, QtCore.Qt.Window)
        self.widgetCount.setWindowModality(QtCore.Qt.ApplicationModal)
        self.widgetCount.ui = Ui_DishCount()
        self.widgetCount.ui.setupUi(self.widgetCount)
        self.widgetCount.ui.spinBox.setMinimum(0)
        self.widgetCount.ui.spinBox.setMaximum(self.portions)
        self.parent.connect(self.widgetCount.ui.submitButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onSubmitCount()"))
        self.parent.connect(self.widgetCount.ui.closeButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onCloseCount()"))
        self.widgetCount.show()

    def onSubmitCount(self):
        self.widgetCount.close()
        #self.widgetCount.value = self.widgetCount.ui.spinBox.value()
        #self.recount(self.widgetCount.value)

    def onCloseCount(self):
        self.widgetCount.close()
        #self.widgetCount.value = None
