# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Product_Ui.ui'
#
# Created: Wed Sep  5 17:47:48 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Product(object):
    def setupUi(self, Product):
        Product.setObjectName("Product")
        Product.resize(535, 514)
        self.gridLayout = QtGui.QGridLayout(Product)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Product)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 2)
        self.saveButton = QtGui.QCommandLinkButton(Product)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 0, 2, 2, 1)
        self.checkBoxGoods = QtGui.QCheckBox(Product)
        self.checkBoxGoods.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBoxGoods.setTristate(False)
        self.checkBoxGoods.setObjectName("checkBoxGoods")
        self.gridLayout.addWidget(self.checkBoxGoods, 3, 1, 1, 1)
        self.addPeriodButton = QtGui.QCommandLinkButton(Product)
        self.addPeriodButton.setObjectName("addPeriodButton")
        self.gridLayout.addWidget(self.addPeriodButton, 3, 2, 1, 1)
        self.widget = QtGui.QWidget(Product)
        self.widget.setMinimumSize(QtCore.QSize(517, 381))
        self.widget.setObjectName("widget")
        self.periodLayout = QtGui.QGridLayout(self.widget)
        self.periodLayout.setContentsMargins(0, 0, 0, 0)
        self.periodLayout.setObjectName("periodLayout")
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 3)
        self.nameEdit = QtGui.QLineEdit(Product)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 2, 1, 1, 1)

        self.retranslateUi(Product)
        QtCore.QMetaObject.connectSlotsByName(Product)

    def retranslateUi(self, Product):
        Product.setWindowTitle(QtGui.QApplication.translate("Product", "Новый продукт", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Product", "Наименование продукта", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Product", "Сохранить[F12]", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setShortcut(QtGui.QApplication.translate("Product", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxGoods.setText(QtGui.QApplication.translate("Product", "Отоварка", None, QtGui.QApplication.UnicodeUTF8))
        self.addPeriodButton.setText(QtGui.QApplication.translate("Product", "Добавить период[F9]", None, QtGui.QApplication.UnicodeUTF8))
        self.addPeriodButton.setShortcut(QtGui.QApplication.translate("Product", "F9", None, QtGui.QApplication.UnicodeUTF8))

