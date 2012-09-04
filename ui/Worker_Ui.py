# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Worker_Ui.ui'
#
# Created: Wed Dec 28 16:20:17 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Worker(object):
    def setupUi(self, Worker):
        Worker.setObjectName("Worker")
        Worker.resize(597, 180)
        self.label = QtGui.QLabel(Worker)
        self.label.setGeometry(QtCore.QRect(0, 10, 141, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Worker)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 141, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(Worker)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 141, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(Worker)
        self.label_4.setGeometry(QtCore.QRect(0, 100, 141, 17))
        self.label_4.setObjectName("label_4")
        self.nameEdit = QtGui.QLineEdit(Worker)
        self.nameEdit.setGeometry(QtCore.QRect(150, 0, 441, 27))
        self.nameEdit.setInputMask("")
        self.nameEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.nameEdit.setPlaceholderText("")
        self.nameEdit.setObjectName("nameEdit")
        self.cardEdit = QtGui.QLineEdit(Worker)
        self.cardEdit.setGeometry(QtCore.QRect(150, 30, 181, 27))
        self.cardEdit.setObjectName("cardEdit")
        self.employeeEdit = QtGui.QLineEdit(Worker)
        self.employeeEdit.setGeometry(QtCore.QRect(150, 60, 181, 27))
        self.employeeEdit.setObjectName("employeeEdit")
        self.comboBox = QtGui.QComboBox(Worker)
        self.comboBox.setGeometry(QtCore.QRect(150, 90, 181, 27))
        self.comboBox.setObjectName("comboBox")
        self.saveButton = QtGui.QPushButton(Worker)
        self.saveButton.setGeometry(QtCore.QRect(476, 140, 111, 27))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Worker)
        QtCore.QMetaObject.connectSlotsByName(Worker)

    def retranslateUi(self, Worker):
        Worker.setWindowTitle(QtGui.QApplication.translate("Worker", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Worker", "ФИО работника", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Worker", "Номер карты", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Worker", "Табельный номер", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Worker", "Компания", None, QtGui.QApplication.UnicodeUTF8))
        self.cardEdit.setInputMask(QtGui.QApplication.translate("Worker", "999999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.employeeEdit.setInputMask(QtGui.QApplication.translate("Worker", "999999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Worker", "Сохранить[S]", None, QtGui.QApplication.UnicodeUTF8))

