# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Storage_Ui.ui'
#
# Created: Wed Sep  5 17:51:40 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Storage(object):
    def setupUi(self, Storage):
        Storage.setObjectName("Storage")
        Storage.resize(820, 494)
        self.gridLayout = QtGui.QGridLayout(Storage)
        self.gridLayout.setObjectName("gridLayout")
        self.tableStorageWidget = QtGui.QTableWidget(Storage)
        self.tableStorageWidget.setTabKeyNavigation(False)
        self.tableStorageWidget.setDragDropOverwriteMode(False)
        self.tableStorageWidget.setCornerButtonEnabled(False)
        self.tableStorageWidget.setObjectName("tableStorageWidget")
        self.tableStorageWidget.setColumnCount(8)
        self.tableStorageWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableStorageWidget.setHorizontalHeaderItem(7, item)
        self.gridLayout.addWidget(self.tableStorageWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addIncomeButton = QtGui.QCommandLinkButton(Storage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addIncomeButton.sizePolicy().hasHeightForWidth())
        self.addIncomeButton.setSizePolicy(sizePolicy)
        self.addIncomeButton.setMaximumSize(QtCore.QSize(16777215, 37))
        self.addIncomeButton.setObjectName("addIncomeButton")
        self.verticalLayout.addWidget(self.addIncomeButton)
        self.delIncomeButton = QtGui.QCommandLinkButton(Storage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delIncomeButton.sizePolicy().hasHeightForWidth())
        self.delIncomeButton.setSizePolicy(sizePolicy)
        self.delIncomeButton.setMaximumSize(QtCore.QSize(16777215, 37))
        self.delIncomeButton.setObjectName("delIncomeButton")
        self.verticalLayout.addWidget(self.delIncomeButton)
        self.importFrom1CButton = QtGui.QCommandLinkButton(Storage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importFrom1CButton.sizePolicy().hasHeightForWidth())
        self.importFrom1CButton.setSizePolicy(sizePolicy)
        self.importFrom1CButton.setMaximumSize(QtCore.QSize(16777215, 37))
        self.importFrom1CButton.setObjectName("importFrom1CButton")
        self.verticalLayout.addWidget(self.importFrom1CButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.retranslateUi(Storage)
        QtCore.QMetaObject.connectSlotsByName(Storage)

    def retranslateUi(self, Storage):
        Storage.setWindowTitle(QtGui.QApplication.translate("Storage", "Склад", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Storage", "№", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Storage", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Storage", "Ед.изм", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Storage", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Storage", "Остаток", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("Storage", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("Storage", "Отоварка", None, QtGui.QApplication.UnicodeUTF8))
        self.tableStorageWidget.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("Storage", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        self.addIncomeButton.setText(QtGui.QApplication.translate("Storage", "Приход [F9]", None, QtGui.QApplication.UnicodeUTF8))
        self.addIncomeButton.setShortcut(QtGui.QApplication.translate("Storage", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.delIncomeButton.setText(QtGui.QApplication.translate("Storage", "Удалить[Shift+Del]", None, QtGui.QApplication.UnicodeUTF8))
        self.delIncomeButton.setShortcut(QtGui.QApplication.translate("Storage", "Shift+Del", None, QtGui.QApplication.UnicodeUTF8))
        self.importFrom1CButton.setText(QtGui.QApplication.translate("Storage", "Импорт из 1С", None, QtGui.QApplication.UnicodeUTF8))

