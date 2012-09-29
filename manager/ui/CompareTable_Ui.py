# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CompareTable_Ui.ui'
#
# Created: Wed Sep 26 19:23:21 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CompareTable(object):
    def setupUi(self, CompareTable):
        CompareTable.setObjectName("CompareTable")
        CompareTable.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(CompareTable)
        self.gridLayout.setObjectName("gridLayout")
        self.compareTable = QtGui.QTableWidget(CompareTable)
        self.compareTable.setObjectName("compareTable")
        self.compareTable.setColumnCount(3)
        self.compareTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.compareTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.compareTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.compareTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.compareTable, 0, 0, 1, 1)

        self.retranslateUi(CompareTable)
        QtCore.QMetaObject.connectSlotsByName(CompareTable)

    def retranslateUi(self, CompareTable):
        CompareTable.setWindowTitle(QtGui.QApplication.translate("CompareTable", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.compareTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("CompareTable", "Отметка", None, QtGui.QApplication.UnicodeUTF8))
        self.compareTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("CompareTable", "Исходное значение", None, QtGui.QApplication.UnicodeUTF8))
        self.compareTable.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("CompareTable", "Новое значение", None, QtGui.QApplication.UnicodeUTF8))

