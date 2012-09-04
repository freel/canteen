# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error_Ui.ui'
#
# Created: Thu Apr 26 10:58:53 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ERROR(object):
    def setupUi(self, ERROR):
        ERROR.setObjectName("ERROR")
        ERROR.setWindowModality(QtCore.Qt.ApplicationModal)
        ERROR.resize(392, 277)
        ERROR.setModal(True)
        self.pushButton = QtGui.QPushButton(ERROR)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 98, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtGui.QLabel(ERROR)
        self.label.setGeometry(QtCore.QRect(10, 10, 371, 221))
        self.label.setObjectName("label")

        self.retranslateUi(ERROR)
        QtCore.QMetaObject.connectSlotsByName(ERROR)

    def retranslateUi(self, ERROR):
        ERROR.setWindowTitle(QtGui.QApplication.translate("ERROR", "ОШИБКА!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("ERROR", "OK [Esc]", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setShortcut(QtGui.QApplication.translate("ERROR", "Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ERROR", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

