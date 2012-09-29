# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Unload_Ui.ui'
#
# Created: Mon May 28 15:44:17 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Unload(object):
    def setupUi(self, Unload):
        Unload.setObjectName("Unload")
        Unload.resize(332, 288)
        self.startDateEdit = QtGui.QDateEdit(Unload)
        self.startDateEdit.setGeometry(QtCore.QRect(40, 10, 110, 27))
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.finishDateEdit = QtGui.QDateEdit(Unload)
        self.finishDateEdit.setGeometry(QtCore.QRect(200, 10, 110, 27))
        self.finishDateEdit.setCalendarPopup(True)
        self.finishDateEdit.setObjectName("finishDateEdit")
        self.formButton = QtGui.QPushButton(Unload)
        self.formButton.setGeometry(QtCore.QRect(180, 50, 131, 27))
        self.formButton.setObjectName("formButton")
        self.saveButton = QtGui.QPushButton(Unload)
        self.saveButton.setGeometry(QtCore.QRect(180, 90, 131, 27))
        self.saveButton.setObjectName("saveButton")
        self.label = QtGui.QLabel(Unload)
        self.label.setGeometry(QtCore.QRect(20, 20, 21, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Unload)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 21, 17))
        self.label_2.setObjectName("label_2")
        self.uploadButton = QtGui.QPushButton(Unload)
        self.uploadButton.setGeometry(QtCore.QRect(180, 130, 131, 27))
        self.uploadButton.setObjectName("uploadButton")

        self.retranslateUi(Unload)
        QtCore.QMetaObject.connectSlotsByName(Unload)

    def retranslateUi(self, Unload):
        Unload.setWindowTitle(QtGui.QApplication.translate("Unload", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.startDateEdit.setDisplayFormat(QtGui.QApplication.translate("Unload", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.finishDateEdit.setDisplayFormat(QtGui.QApplication.translate("Unload", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.formButton.setText(QtGui.QApplication.translate("Unload", "Выгрузить в 1С", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Unload", "Сохранить[F12]", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setShortcut(QtGui.QApplication.translate("Unload", "F12", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Unload", "С:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Unload", "По:", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadButton.setText(QtGui.QApplication.translate("Unload", "Загрузить[F7]", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadButton.setShortcut(QtGui.QApplication.translate("Unload", "F7", None, QtGui.QApplication.UnicodeUTF8))

