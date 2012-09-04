# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from localDb_Class import localDb_Class
from productParent_Class import *
from ui.DishCount_Ui import Ui_DishCount

#class productDishPanel_Class(productParent_Class):
    #def __init__(self, parent, row):
        #productParent_Class.__init__(self, parent, row)
        ##self.portions = self.select_max_portions()
        #self.changeCount()


    #def onClick(self):
        #portions = self.openCount()

    #def recount(self, portions):
        #self.portions -= portions
        #for product in self.consumption:
            #self.parent.products[product] -= self.consumption[product]*portions
        #if self.row[0] in self.parent.menuWidget:
            #self.changeCount()
            #self.parent.menuWidget[self.row[0]].portions += portions
            #self.parent.menuWidget[self.row[0]].setText(1, u"%s" % self.parent.menuWidget[self.row[0]].portions)
        #else:
            #widget = productMenuPanel_Class(self.parent,(self.row[0], self.row[1], portions))
            ##widget.portions = portions
            #widget.max_amortization = self.max_amortization
            ##print "dghdfhdfghdfgh"
            ##widget.price = widget.getDishPrice()
            #self.setText(1, u"%s" % self.portions)
            #widget.setText(1, u"%s" % widget.portions)
            #self.parent.menuWidget[self.row[0]] = widget
            #self.parent.ui.treeWidgetMenu.addTopLevelItem(self.parent.menuWidget[self.row[0]])
        #self.parent.renewPortions()

    #def openCount(self):
        #self.widgetCount = QtGui.QWidget(self.parent, QtCore.Qt.Window)
        #self.widgetCount.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.widgetCount.ui = Ui_DishCount()
        #self.widgetCount.ui.setupUi(self.widgetCount)
        #self.widgetCount.ui.spinBox.setMinimum(0)
        #self.widgetCount.ui.spinBox.setMaximum(self.portions)
        #self.parent.connect(self.widgetCount.ui.submitButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onSubmitCount()"))
        #self.parent.connect(self.widgetCount.ui.closeButton, QtCore.SIGNAL("clicked()"), QtCore.SLOT("onCloseCount()"))
        #self.widgetCount.show()

    #def onSubmitCount(self):
        #self.widgetCount.close()
        ##self.widgetCount.value = self.widgetCount.ui.spinBox.value()
        ##self.recount(self.widgetCount.value)

    #def onCloseCount(self):
        #self.widgetCount.close()
        ##self.widgetCount.value = None