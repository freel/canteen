# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directory_Page_Ui.ui'
#
# Created: Fri Sep 23 12:13:08 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DirectoryPage(object):
    def setupUi(self, DirectoryPage):
        DirectoryPage.setObjectName("DirectoryPage")
        DirectoryPage.resize(665, 300)
        self.delRowButton = QtGui.QPushButton(DirectoryPage)
        self.delRowButton.setGeometry(QtCore.QRect(550, 190, 97, 27))
        self.delRowButton.setObjectName("delRowButton")
        self.tableWidget = QtGui.QTableWidget(DirectoryPage)
        self.tableWidget.setGeometry(QtCore.QRect(0, 10, 651, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.saveRowButton = QtGui.QCommandLinkButton(DirectoryPage)
        self.saveRowButton.setGeometry(QtCore.QRect(10, 200, 186, 41))
        self.saveRowButton.setObjectName("saveRowButton")

        self.retranslateUi(DirectoryPage)
        QtCore.QMetaObject.connectSlotsByName(DirectoryPage)

    def retranslateUi(self, DirectoryPage):
        DirectoryPage.setWindowTitle(QtGui.QApplication.translate("DirectoryPage", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.delRowButton.setText(QtGui.QApplication.translate("DirectoryPage", "Удалить", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("DirectoryPage", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("DirectoryPage", "Значение", None, QtGui.QApplication.UnicodeUTF8))
        self.saveRowButton.setText(QtGui.QApplication.translate("DirectoryPage", "Сохранить", None, QtGui.QApplication.UnicodeUTF8))

