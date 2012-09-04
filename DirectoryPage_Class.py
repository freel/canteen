# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from localDb_Class import localDb_Class
from ui.DirectoryPage_Ui import Ui_DirectoryPage

class DirectoryPage_Class(QtGui.QWidget):
    """Виджет для страниц в гормошке"""
    def __init__(self, parent=None, row=None, keys=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_DirectoryPage()
        self.ui.setupUi(self)
        self.insertFull(row, keys)

    def insertFull(self, row, keys):
        for i in range(len(keys)):
            self.insertRowWithVal(row[i],keys[i])

        #self.connect(self.ui.saveRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("saveRow()"))
        #self.connect(self.ui.delRowButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("delRow()"))

    def insertRowWithVal(self, val, key):
        """Вставляет значения в ячейки"""
        itemNumber = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(itemNumber +1)

        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setVerticalHeaderItem(itemNumber, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setItem(itemNumber, 0, item)
        item = QtGui.QTableWidgetItem()
        self.ui.tableWidget.setItem(itemNumber, 1, item)

        self.ui.tableWidget.verticalHeaderItem(itemNumber).setText("%s" % (itemNumber+1))
        self.ui.tableWidget.item(itemNumber, 0).setText("%s" % key)
        self.ui.tableWidget.item(itemNumber, 1).setText("%s" % val)

    def saveRow(self):
        print "сохраняем"

    def delRow(self):
        db = localDb_Class()
        db.open_db()
        answer = db.del_row_by_id(self.table,self.ui.tableWidget.item())
        db.close_db()
