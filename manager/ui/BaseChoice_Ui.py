# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseChoice_Ui.ui'
#
# Created: Mon May 28 14:05:19 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_BaseChoice(object):
    def setupUi(self, BaseChoice):
        BaseChoice.setObjectName("BaseChoice")
        BaseChoice.resize(400, 300)
        self.comboBox = QtGui.QComboBox(BaseChoice)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 341, 27))
        self.comboBox.setObjectName("comboBox")
        self.commandLinkButton = QtGui.QCommandLinkButton(BaseChoice)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 90, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(BaseChoice)
        QtCore.QMetaObject.connectSlotsByName(BaseChoice)

    def retranslateUi(self, BaseChoice):
        BaseChoice.setWindowTitle(QtGui.QApplication.translate("BaseChoice", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("BaseChoice", "Продолжить", None, QtGui.QApplication.UnicodeUTF8))

