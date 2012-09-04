# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compare_Ui.ui'
#
# Created: Wed May 16 08:50:47 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Compare(object):
    def setupUi(self, Compare):
        Compare.setObjectName("Compare")
        Compare.resize(772, 686)
        self.compareTableWidget = QtGui.QTableWidget(Compare)
        self.compareTableWidget.setGeometry(QtCore.QRect(0, 30, 771, 611))
        self.compareTableWidget.setObjectName("compareTableWidget")
        self.compareTableWidget.setColumnCount(2)
        self.compareTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.compareTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.compareTableWidget.setHorizontalHeaderItem(1, item)
        self.saveButton = QtGui.QCommandLinkButton(Compare)
        self.saveButton.setGeometry(QtCore.QRect(0, 640, 185, 41))
        self.saveButton.setObjectName("saveButton")
        self.addProductButton = QtGui.QCommandLinkButton(Compare)
        self.addProductButton.setGeometry(QtCore.QRect(580, 640, 185, 41))
        self.addProductButton.setObjectName("addProductButton")

        self.retranslateUi(Compare)
        QtCore.QMetaObject.connectSlotsByName(Compare)

    def retranslateUi(self, Compare):
        Compare.setWindowTitle(QtGui.QApplication.translate("Compare", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.compareTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Compare", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.compareTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Compare", "Сопоставление", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Compare", "Сохранить[F12]", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setShortcut(QtGui.QApplication.translate("Compare", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.addProductButton.setText(QtGui.QApplication.translate("Compare", "Добавить продукт[F9]", None, QtGui.QApplication.UnicodeUTF8))
        self.addProductButton.setShortcut(QtGui.QApplication.translate("Compare", "F9", None, QtGui.QApplication.UnicodeUTF8))

