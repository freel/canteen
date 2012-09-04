# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DishCount_Ui.ui'
#
# Created: Thu Apr 26 17:54:41 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DishCount(object):
    def setupUi(self, DishCount):
        DishCount.setObjectName("DishCount")
        DishCount.resize(229, 123)
        self.gridLayout = QtGui.QGridLayout(DishCount)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = QtGui.QSpinBox(DishCount)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.spinBox.setFont(font)
        self.spinBox.setWrapping(False)
        self.spinBox.setAccelerated(False)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 0, 0, 1, 2)
        self.submitButton = QtGui.QPushButton(DishCount)
        self.submitButton.setObjectName("submitButton")
        self.gridLayout.addWidget(self.submitButton, 1, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(DishCount)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 1, 1, 1, 1)

        self.retranslateUi(DishCount)
        QtCore.QMetaObject.connectSlotsByName(DishCount)

    def retranslateUi(self, DishCount):
        DishCount.setWindowTitle(QtGui.QApplication.translate("DishCount", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setText(QtGui.QApplication.translate("DishCount", "Принять", None, QtGui.QApplication.UnicodeUTF8))
        self.submitButton.setShortcut(QtGui.QApplication.translate("DishCount", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("DishCount", "Отмена", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setShortcut(QtGui.QApplication.translate("DishCount", "Esc", None, QtGui.QApplication.UnicodeUTF8))

