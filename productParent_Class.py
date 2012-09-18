# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from localDb_Class import localDb_Class
from ui.productPanel import Ui_productPanel
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
        self.max_amortization = {}
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
        num = 0
        for row in self.consumption:
            rest = self.portions
            product_prices = self.getProductPrice(row)['rows']
            self.max_amortization[row] = {}
            self.product[row] = round(product_prices[0]['price'],2)
            print row, self.product[row]
            for income_price in product_prices:
                if rest-income_price['count']<=0:
                    self.max_amortization[row][income_price['id']] = rest
                    rest=0
                else:
                    self.max_amortization[row][income_price['id']] = income_price['count']
                    rest -= income_price['count']
        price = round(self.product[row], 2)
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
        return rows

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

    def removePortions(self, portions):
        """Удаление указанного количества порций, добавляет в меню"""
        self.portions -= portions

    def addPortions(self, portions):
        self.portions += portions

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

    #~ def delFromMenu(self):
        

class productDishPanel_Class(productParent_Class):
    """Панель доступных продуктов"""
    def __init__(self, parent, row):
        productParent_Class.__init__(self, parent, row)
        #self.portions = self.select_max_portions()
        self.changeCount()
