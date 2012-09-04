# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sales_Ui.ui'
#
# Created: Tue Jan 10 09:47:52 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Sales(object):
    def setupUi(self, Sales):
        Sales.setObjectName("Sales")
        Sales.resize(747, 577)
        self.gridLayout_2 = QtGui.QGridLayout(Sales)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtGui.QTabWidget(Sales)
        self.tabWidget.setObjectName("tabWidget")
        self.canteenTab = QtGui.QWidget()
        self.canteenTab.setObjectName("canteenTab")
        self.gridLayout_4 = QtGui.QGridLayout(self.canteenTab)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.canteenBox = QtGui.QGroupBox(self.canteenTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canteenBox.sizePolicy().hasHeightForWidth())
        self.canteenBox.setSizePolicy(sizePolicy)
        self.canteenBox.setAutoFillBackground(False)
        self.canteenBox.setFlat(False)
        self.canteenBox.setCheckable(False)
        self.canteenBox.setObjectName("canteenBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.canteenBox)
        self.gridLayout_3.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.treeWidgetMenu = QtGui.QTreeWidget(self.canteenBox)
        self.treeWidgetMenu.setObjectName("treeWidgetMenu")
        self.gridLayout_3.addWidget(self.treeWidgetMenu, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.canteenBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.canteenTab, "")
        self.goodsTab = QtGui.QWidget()
        self.goodsTab.setObjectName("goodsTab")
        self.gridLayout_6 = QtGui.QGridLayout(self.goodsTab)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.goodsBox = QtGui.QGroupBox(self.goodsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goodsBox.sizePolicy().hasHeightForWidth())
        self.goodsBox.setSizePolicy(sizePolicy)
        self.goodsBox.setAutoFillBackground(False)
        self.goodsBox.setFlat(False)
        self.goodsBox.setCheckable(False)
        self.goodsBox.setObjectName("goodsBox")
        self.gridLayout_5 = QtGui.QGridLayout(self.goodsBox)
        self.gridLayout_5.setContentsMargins(0, 3, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.treeWidgetGoods = QtGui.QTreeWidget(self.goodsBox)
        self.treeWidgetGoods.setObjectName("treeWidgetGoods")
        self.gridLayout_5.addWidget(self.treeWidgetGoods, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.goodsBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.goodsTab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Sales)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Sales)

    def retranslateUi(self, Sales):
        Sales.setWindowTitle(QtGui.QApplication.translate("Sales", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.canteenBox.setTitle(QtGui.QApplication.translate("Sales", "Меню", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetMenu.headerItem().setText(0, QtGui.QApplication.translate("Sales", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetMenu.headerItem().setText(1, QtGui.QApplication.translate("Sales", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetMenu.headerItem().setText(2, QtGui.QApplication.translate("Sales", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canteenTab), QtGui.QApplication.translate("Sales", "Столовая", None, QtGui.QApplication.UnicodeUTF8))
        self.goodsBox.setTitle(QtGui.QApplication.translate("Sales", "Меню", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetGoods.headerItem().setText(0, QtGui.QApplication.translate("Sales", "Наименование", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetGoods.headerItem().setText(1, QtGui.QApplication.translate("Sales", "Количество", None, QtGui.QApplication.UnicodeUTF8))
        self.treeWidgetGoods.headerItem().setText(2, QtGui.QApplication.translate("Sales", "Цена", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.goodsTab), QtGui.QApplication.translate("Sales", "Отоварка", None, QtGui.QApplication.UnicodeUTF8))

