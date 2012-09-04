# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.DirectorySelect_Ui import Ui_DirectorySelect
from Directory_Class import Directory_Class

class DirectorySelect_Class(QtGui.QDialog):

    def __init__(self, parent=None):
        """Окно выбора справочников, при нажатии на кнопки открывает соответствующий справочник"""
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DirectorySelect()
        self.ui.setupUi(self)
        self.connect(self.ui.openDishesButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openDish()"))
        self.connect(self.ui.openConsumptionButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openConsumption()"))
        self.connect(self.ui.openCashiersButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openCashier()"))
        self.connect(self.ui.openSuppliersButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openSupplier()"))
        self.connect(self.ui.openProductsButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openProduct()"))
        self.connect(self.ui.openCompaniesButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openCompany()"))
        self.connect(self.ui.openWorkersButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openWorker()"))
        self.connect(self.ui.openMeasuresButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("openMeasure()"))

    def openDish(self):
        self.openDirectory('dish')

    def openConsumption(self):
        self.openDirectory('consumption')

    def openCashier(self):
        self.openDirectory('cashier')

    def openSupplier(self):
        self.openDirectory('supplier')

    def openProduct(self):
        self.openDirectory('product')

    def openCompany(self):
        self.openDirectory('company')

    def openWorker(self):
        self.openDirectory('worker')

    def openMeasure(self):
        self.openDirectory('measure')

    def openDirectory(self,table):
        directory = Directory_Class(table,self)
        directory.show()
