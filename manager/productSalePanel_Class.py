# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from localDb_Class import localDb_Class
from productParent_Class import productParent_Class

class productSalePanel_Class(productParent_Class):
    def __init__(self, parent, row):
        productParent_Class.__init__(self, parent, row)

        #self.connect(self.ui.productButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("onClick()"))
        #self.connect(self.ui.productButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("dataSend()"))
        #self.parent.connect(self.ui.productButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("onClick()"))

    def onClick(self):
        #item = QtGui.QTableWidgetItem()
        #item.setText(self.name)
        if self.portions > 0:
            self.portions -= 1
            self.changeCount()
            self.parent.saleClick(self.row)
        else:
            self.setDisabled(True)
        #self.parent.parent.sales.ui.salesTableWidget.addItem(0, 0, item)
        #self.emit(QtCore.SIGNAL('dataSend()'))