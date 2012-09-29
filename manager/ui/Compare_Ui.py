# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Compare_Ui.ui'
#
# Created: Wed Sep 26 13:27:30 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Compare(object):
    def setupUi(self, Compare):
        Compare.setObjectName("Compare")
        Compare.resize(793, 540)
        self.gridLayout = QtGui.QGridLayout(Compare)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(Compare)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        self.saveTab_Button = QtGui.QCommandLinkButton(Compare)
        self.saveTab_Button.setObjectName("saveTab_Button")
        self.gridLayout.addWidget(self.saveTab_Button, 1, 0, 1, 1)
        self.substitution_Button = QtGui.QCommandLinkButton(Compare)
        self.substitution_Button.setObjectName("substitution_Button")
        self.gridLayout.addWidget(self.substitution_Button, 1, 1, 1, 1)

        self.retranslateUi(Compare)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Compare)

    def retranslateUi(self, Compare):
        Compare.setWindowTitle(QtGui.QApplication.translate("Compare", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.saveTab_Button.setText(QtGui.QApplication.translate("Compare", "Принять", None, QtGui.QApplication.UnicodeUTF8))
        self.substitution_Button.setText(QtGui.QApplication.translate("Compare", "Заменить отмеченные", None, QtGui.QApplication.UnicodeUTF8))

