# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DirectorySelect.ui'
#
# Created: Fri Sep 23 14:55:59 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DirectorySelect(object):
    def setupUi(self, DirectorySelect):
        DirectorySelect.setObjectName("DirectorySelect")
        DirectorySelect.resize(804, 518)
        self.openDishesButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openDishesButton.setGeometry(QtCore.QRect(10, 40, 186, 41))
        self.openDishesButton.setObjectName("openDishesButton")
        self.openConsumptionButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openConsumptionButton.setGeometry(QtCore.QRect(10, 110, 186, 41))
        self.openConsumptionButton.setObjectName("openConsumptionButton")
        self.openCashiersButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openCashiersButton.setGeometry(QtCore.QRect(240, 40, 186, 41))
        self.openCashiersButton.setObjectName("openCashiersButton")
        self.openSuppliersButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openSuppliersButton.setGeometry(QtCore.QRect(240, 110, 186, 41))
        self.openSuppliersButton.setObjectName("openSuppliersButton")
        self.openProductsButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openProductsButton.setGeometry(QtCore.QRect(10, 180, 186, 41))
        self.openProductsButton.setObjectName("openProductsButton")
        self.openCompaniesButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openCompaniesButton.setGeometry(QtCore.QRect(470, 40, 186, 41))
        self.openCompaniesButton.setObjectName("openCompaniesButton")
        self.openWorkersButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openWorkersButton.setGeometry(QtCore.QRect(470, 110, 186, 41))
        self.openWorkersButton.setObjectName("openWorkersButton")
        self.openMeasuresButton = QtGui.QCommandLinkButton(DirectorySelect)
        self.openMeasuresButton.setGeometry(QtCore.QRect(240, 180, 186, 41))
        self.openMeasuresButton.setObjectName("openMeasuresButton")

        self.retranslateUi(DirectorySelect)
        QtCore.QMetaObject.connectSlotsByName(DirectorySelect)

    def retranslateUi(self, DirectorySelect):
        DirectorySelect.setWindowTitle(QtGui.QApplication.translate("DirectorySelect", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.openDishesButton.setText(QtGui.QApplication.translate("DirectorySelect", "Блюда", None, QtGui.QApplication.UnicodeUTF8))
        self.openConsumptionButton.setText(QtGui.QApplication.translate("DirectorySelect", "Состав", None, QtGui.QApplication.UnicodeUTF8))
        self.openCashiersButton.setText(QtGui.QApplication.translate("DirectorySelect", "Кассиры", None, QtGui.QApplication.UnicodeUTF8))
        self.openSuppliersButton.setText(QtGui.QApplication.translate("DirectorySelect", "Поставщики", None, QtGui.QApplication.UnicodeUTF8))
        self.openProductsButton.setText(QtGui.QApplication.translate("DirectorySelect", "Продукты", None, QtGui.QApplication.UnicodeUTF8))
        self.openCompaniesButton.setText(QtGui.QApplication.translate("DirectorySelect", "Предприятия", None, QtGui.QApplication.UnicodeUTF8))
        self.openWorkersButton.setText(QtGui.QApplication.translate("DirectorySelect", "Работники", None, QtGui.QApplication.UnicodeUTF8))
        self.openMeasuresButton.setText(QtGui.QApplication.translate("DirectorySelect", "Единицы измерения", None, QtGui.QApplication.UnicodeUTF8))

