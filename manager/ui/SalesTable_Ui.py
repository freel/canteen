# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalesTable_Ui.ui'
#
# Created: Tue Jan 10 10:41:33 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SalesTable(object):
    def setupUi(self, SalesTable):
        SalesTable.setObjectName("SalesTable")
        SalesTable.setEnabled(False)
        SalesTable.resize(300, 310)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SalesTable.sizePolicy().hasHeightForWidth())
        SalesTable.setSizePolicy(sizePolicy)
        SalesTable.setMinimumSize(QtCore.QSize(300, 310))
        self.gridLayout = QtGui.QGridLayout(SalesTable)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(SalesTable)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cardEdit = QtGui.QLineEdit(SalesTable)
        self.cardEdit.setCursorPosition(0)
        self.cardEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.cardEdit.setObjectName("cardEdit")
        self.gridLayout.addWidget(self.cardEdit, 0, 1, 1, 1)
        self.workerNameEdit = QtGui.QLineEdit(SalesTable)
        self.workerNameEdit.setEnabled(False)
        self.workerNameEdit.setObjectName("workerNameEdit")
        self.gridLayout.addWidget(self.workerNameEdit, 1, 0, 1, 2)
        self.company = QtGui.QLabel(SalesTable)
        self.company.setObjectName("company")
        self.gridLayout.addWidget(self.company, 2, 0, 1, 2)
        self.salesTableWidget = QtGui.QTableWidget(SalesTable)
        self.salesTableWidget.setEnabled(False)
        self.salesTableWidget.setObjectName("salesTableWidget")
        self.salesTableWidget.setColumnCount(4)
        self.salesTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.salesTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.salesTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.salesTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.salesTableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.salesTableWidget, 3, 0, 1, 2)
        self.total = QtGui.QLabel(SalesTable)
        self.total.setObjectName("total")
        self.gridLayout.addWidget(self.total, 4, 0, 1, 1)
        self.chequeButton = QtGui.QPushButton(SalesTable)
        self.chequeButton.setObjectName("chequeButton")
        self.gridLayout.addWidget(self.chequeButton, 5, 0, 1, 2)
        self.labelSumm = QtGui.QLabel(SalesTable)
        self.labelSumm.setText("")
        self.labelSumm.setObjectName("labelSumm")
        self.gridLayout.addWidget(self.labelSumm, 4, 1, 1, 1)

        self.retranslateUi(SalesTable)
        QtCore.QMetaObject.connectSlotsByName(SalesTable)

    def retranslateUi(self, SalesTable):
        SalesTable.setWindowTitle(QtGui.QApplication.translate("SalesTable", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SalesTable", "Номер карты", None, QtGui.QApplication.UnicodeUTF8))
        self.cardEdit.setInputMask(QtGui.QApplication.translate("SalesTable", "9999990000000000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.workerNameEdit.setText(QtGui.QApplication.translate("SalesTable", "ФИО", None, QtGui.QApplication.UnicodeUTF8))
        self.company.setText(QtGui.QApplication.translate("SalesTable", "Предприятие", None, QtGui.QApplication.UnicodeUTF8))
        self.salesTableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("SalesTable", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.salesTableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("SalesTable", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        self.salesTableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("SalesTable", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.total.setText(QtGui.QApplication.translate("SalesTable", "Итого:", None, QtGui.QApplication.UnicodeUTF8))
        self.chequeButton.setText(QtGui.QApplication.translate("SalesTable", "Печать [P]", None, QtGui.QApplication.UnicodeUTF8))

