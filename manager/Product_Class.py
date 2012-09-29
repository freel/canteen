# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Product_Ui import Ui_Product
from ui.ProductPeriod_Ui import Ui_ProductPeriod
from localDb_Class import localDb_Class


class Product_Class(QtGui.QDialog):
    periods = []
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Product()
        self.ui.setupUi(self)
        self.parent = parent

        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveProduct()"))
        self.connect(self.ui.addPeriodButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("addPeriod()"))

    def saveProduct(self):
        data = self.ui.nameEdit.text()
        if self.ui.checkBoxGoods.checkState():
            sale = 1
        else:
            sale = 0
        db = localDb_Class()
        try:
            db.insert_val('product',(data, sale))
        except:
            None
        try:
            pid = db.select_val_by_col('product', 'name', "'%s'" % data)['rows'][0]['id']
            for period in self.periods:
                period.saveData(db, pid)
        except:
            None
        db.close_db()
        self.close()
        self.parent.renew()

    def addPeriod(self):
        period = Period_Class(self)
        self.periods.append(period)
        self.ui.periodLayout.addWidget(self.periods[-1])


class Period_Class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_ProductPeriod()
        self.ui.setupUi(self)

    def getData(self,pid):
        data = (pid, self.ui.startDate.date().toString('dd-MM'), self.ui.finishDate.date().toString('dd-MM'), self.ui.percent.text())
        return data

    def saveData(self,db,pid):
        db.insert_val('coefficient',self.getData(pid))