# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dish_Ui.ui'
#
# Created: Wed Jun  6 15:32:54 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dish(object):
    def setupUi(self, Dish):
        Dish.setObjectName("Dish")
        Dish.resize(714, 596)
        self.gridLayout = QtGui.QGridLayout(Dish)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dish)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.sectionBox = QtGui.QComboBox(Dish)
        self.sectionBox.setEditable(True)
        self.sectionBox.setObjectName("sectionBox")
        self.gridLayout.addWidget(self.sectionBox, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Dish)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.consumptionTableWidget = QtGui.QTableWidget(Dish)
        self.consumptionTableWidget.setObjectName("consumptionTableWidget")
        self.consumptionTableWidget.setColumnCount(3)
        self.consumptionTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.consumptionTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.consumptionTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.consumptionTableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.consumptionTableWidget, 5, 0, 1, 3)
        self.saveButton = QtGui.QCommandLinkButton(Dish)
        self.saveButton.setMinimumSize(QtCore.QSize(190, 36))
        self.saveButton.setMaximumSize(QtCore.QSize(190, 36))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 6, 2, 1, 1)
        self.label_3 = QtGui.QLabel(Dish)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dish)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.addProductButton = QtGui.QCommandLinkButton(Dish)
        self.addProductButton.setMinimumSize(QtCore.QSize(190, 36))
        self.addProductButton.setMaximumSize(QtCore.QSize(190, 36))
        self.addProductButton.setObjectName("addProductButton")
        self.gridLayout.addWidget(self.addProductButton, 6, 0, 1, 1)
        self.nameEdit = QtGui.QLineEdit(Dish)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 2, 1, 1)
        self.massEdit = QtGui.QLineEdit(Dish)
        self.massEdit.setObjectName("massEdit")
        self.gridLayout.addWidget(self.massEdit, 3, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Dish)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.idEdit = QtGui.QLineEdit(Dish)
        self.idEdit.setObjectName("idEdit")
        self.gridLayout.addWidget(self.idEdit, 0, 2, 1, 1)

        self.retranslateUi(Dish)
        QtCore.QMetaObject.connectSlotsByName(Dish)
        Dish.setTabOrder(self.idEdit, self.nameEdit)
        Dish.setTabOrder(self.nameEdit, self.sectionBox)
        Dish.setTabOrder(self.sectionBox, self.massEdit)
        Dish.setTabOrder(self.massEdit, self.addProductButton)
        Dish.setTabOrder(self.addProductButton, self.saveButton)
        Dish.setTabOrder(self.saveButton, self.consumptionTableWidget)

    def retranslateUi(self, Dish):
        Dish.setWindowTitle(QtGui.QApplication.translate("Dish", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dish", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dish", "Раздел", None, QtGui.QApplication.UnicodeUTF8))
        self.consumptionTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dish", "Наименование продукта", None, QtGui.QApplication.UnicodeUTF8))
        self.consumptionTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dish", "Брутто", None, QtGui.QApplication.UnicodeUTF8))
        self.consumptionTableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dish", "Нетто", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Dish", "Сохранить[F12]", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setShortcut(QtGui.QApplication.translate("Dish", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dish", "Выход", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dish", "Состав", None, QtGui.QApplication.UnicodeUTF8))
        self.addProductButton.setText(QtGui.QApplication.translate("Dish", "Добавить продукт[F9]", None, QtGui.QApplication.UnicodeUTF8))
        self.addProductButton.setShortcut(QtGui.QApplication.translate("Dish", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dish", "Калькуляционная карточка", None, QtGui.QApplication.UnicodeUTF8))

