# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_Ui.ui'
#
# Created: Wed Sep  5 17:36:08 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1056, 613)
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(1056, 60))
        self.dockWidget_3.setMaximumSize(QtCore.QSize(524287, 60))
        self.dockWidget_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dockWidget_3.setFloating(False)
        self.dockWidget_3.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_3.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.dockWidget_3.setWindowTitle("")
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openSalesButton = QtGui.QCommandLinkButton(self.dockWidgetContents_3)
        self.openSalesButton.setObjectName("openSalesButton")
        self.horizontalLayout_2.addWidget(self.openSalesButton)
        self.openMenuButton = QtGui.QCommandLinkButton(self.dockWidgetContents_3)
        self.openMenuButton.setObjectName("openMenuButton")
        self.horizontalLayout_2.addWidget(self.openMenuButton)
        self.openStorageButton = QtGui.QCommandLinkButton(self.dockWidgetContents_3)
        self.openStorageButton.setObjectName("openStorageButton")
        self.horizontalLayout_2.addWidget(self.openStorageButton)
        self.openReportButton = QtGui.QCommandLinkButton(self.dockWidgetContents_3)
        self.openReportButton.setObjectName("openReportButton")
        self.horizontalLayout_2.addWidget(self.openReportButton)
        self.openUnloadButton = QtGui.QCommandLinkButton(self.dockWidgetContents_3)
        self.openUnloadButton.setObjectName("openUnloadButton")
        self.horizontalLayout_2.addWidget(self.openUnloadButton)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Столовая", None, QtGui.QApplication.UnicodeUTF8))
        self.openSalesButton.setText(QtGui.QApplication.translate("MainWindow", "Продажи [F1]", None, QtGui.QApplication.UnicodeUTF8))
        self.openSalesButton.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.openMenuButton.setText(QtGui.QApplication.translate("MainWindow", "Меню [F2]", None, QtGui.QApplication.UnicodeUTF8))
        self.openMenuButton.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.openStorageButton.setText(QtGui.QApplication.translate("MainWindow", "Склад [F3]", None, QtGui.QApplication.UnicodeUTF8))
        self.openStorageButton.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.openReportButton.setText(QtGui.QApplication.translate("MainWindow", "Отчеты [F4]", None, QtGui.QApplication.UnicodeUTF8))
        self.openReportButton.setShortcut(QtGui.QApplication.translate("MainWindow", "F4", None, QtGui.QApplication.UnicodeUTF8))
        self.openUnloadButton.setText(QtGui.QApplication.translate("MainWindow", "Выгрузка [F5]", None, QtGui.QApplication.UnicodeUTF8))
        self.openUnloadButton.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))

