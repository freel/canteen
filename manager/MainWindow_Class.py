# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from Shift_Class import Shift
from ui.MainWindow_Ui import Ui_MainWindow
from ui.Shift_Ui import Ui_Shift
from DirectorySelect_Class import DirectorySelect_Class
from Sales_Class import Sales_Class
from Menu_Class import Menu_Class
from Storage_Class import Storage_Class
from Report_Class import Report_Class
from Unload_Class import Unload_Class
from SalesTable_Class import SalesTable_Class

class MainWindow_Class(QtGui.QMainWindow):
    """Создание главного окна приложения"""


    def __init__(self, parent):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()

        self.shift = Shift(self)
        self.shift.show()

        self.sales = SalesTable_Class(self)
        self.sales.show()


        self.connect(self.ui.openDirectoryButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openDirectoryButton()"))
        self.connect(self.ui.openSalesButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openSalesButton()"))
        self.connect(self.ui.openMenuButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openMenuButton()"))
        self.connect(self.ui.openStorageButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openStorageButton()"))
        self.connect(self.ui.openReportButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openReportButton()"))
        self.connect(self.ui.openUnloadButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_openUnloadButton()"))

        self.connect(self, QtCore.SIGNAL('dataSend()'), QtCore.SLOT('setData()'))

    #def on_start_openShiftDock(self):
        #"""Открывает окно выбора Справочников"""
        #form = Shift_Class(self)
        #form.show()

    def on_click_openSalesButton(self):
        """Открывает окно продаж"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formSales)
            self.formSales.renew()
        except:
            self.formSales = Sales_Class(self)
            tab = self.ui.tabWidget.addTab(self.formSales, u"Продажи")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.sales.setEnabled(True)
        self.sales.ui.cardEdit.setFocus()

    def on_click_openMenuButton(self):
        """Открывает создание меню"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formMenu)
            self.formMenu.renew()
        except:
            self.formMenu = Menu_Class(self)
            tab = self.ui.tabWidget.addTab(self.formMenu, u"Меню")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.formMenu.setFocus()

    def on_click_openDirectoryButton(self):
        """Открывает окно выбора Справочников"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formDirectory)
            #self.formDirectory.renew()
        except:
            self.formDirectory = DirectorySelect_Class(self)
            tab = self.ui.tabWidget.addTab(self.formDirectory, u"Справочники")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.formDirectory.setFocus()

    def on_click_openStorageButton(self):
        """Открывает окно Склада"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formStorage)
        except:
            self.formStorage = Storage_Class(self)
            tab = self.ui.tabWidget.addTab(self.formStorage, u"Склад")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.formStorage.setFocus()

    def on_click_openReportButton(self):
        """Открывает окно Склада"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formReport)
        except:
            self.formReport = Report_Class(self)
            tab = self.ui.tabWidget.addTab(self.formReport, u"Отчеты")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.formReport.setFocus()

    def on_click_openUnloadButton(self):
        """Открывает окно Склада"""
        try:
            tab = self.ui.tabWidget.indexOf(self.formUnload)
        except:
            self.formUnload = Unload_Class(self)
            tab = self.ui.tabWidget.addTab(self.formUnload, u"Выгрузка")
        self.ui.tabWidget.setCurrentIndex(tab)
        self.formUnload.setFocus()
