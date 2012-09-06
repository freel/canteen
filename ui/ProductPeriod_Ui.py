# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProductPeriod_Ui.ui'
#
# Created: Wed Sep  5 17:46:51 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProductPeriod(object):
    def setupUi(self, ProductPeriod):
        ProductPeriod.setObjectName("ProductPeriod")
        ProductPeriod.resize(472, 78)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProductPeriod.sizePolicy().hasHeightForWidth())
        ProductPeriod.setSizePolicy(sizePolicy)
        ProductPeriod.setMinimumSize(QtCore.QSize(472, 78))
        self.gridLayout = QtGui.QGridLayout(ProductPeriod)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(ProductPeriod)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.startDate = QtGui.QDateEdit(ProductPeriod)
        self.startDate.setMinimumSize(QtCore.QSize(200, 0))
        self.startDate.setCalendarPopup(True)
        self.startDate.setObjectName("startDate")
        self.gridLayout.addWidget(self.startDate, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ProductPeriod)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.finishDate = QtGui.QDateEdit(ProductPeriod)
        self.finishDate.setMinimumSize(QtCore.QSize(200, 0))
        self.finishDate.setCalendarPopup(True)
        self.finishDate.setObjectName("finishDate")
        self.gridLayout.addWidget(self.finishDate, 0, 3, 1, 1)
        self.label = QtGui.QLabel(ProductPeriod)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.percent = QtGui.QLineEdit(ProductPeriod)
        self.percent.setObjectName("percent")
        self.gridLayout.addWidget(self.percent, 1, 3, 1, 1)

        self.retranslateUi(ProductPeriod)
        QtCore.QMetaObject.connectSlotsByName(ProductPeriod)

    def retranslateUi(self, ProductPeriod):
        ProductPeriod.setWindowTitle(QtGui.QApplication.translate("ProductPeriod", "Период", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProductPeriod", "С:", None, QtGui.QApplication.UnicodeUTF8))
        self.startDate.setDisplayFormat(QtGui.QApplication.translate("ProductPeriod", "dd-MM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProductPeriod", "По:", None, QtGui.QApplication.UnicodeUTF8))
        self.finishDate.setDisplayFormat(QtGui.QApplication.translate("ProductPeriod", "dd-MM", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProductPeriod", "Процент:", None, QtGui.QApplication.UnicodeUTF8))
        self.percent.setInputMask(QtGui.QApplication.translate("ProductPeriod", "dd; ", None, QtGui.QApplication.UnicodeUTF8))

