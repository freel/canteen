# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Shift_Ui.ui'
#
# Created: Wed Sep  5 17:50:57 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Shift(object):
    def setupUi(self, Shift):
        Shift.setObjectName("Shift")
        Shift.resize(300, 150)
        Shift.setMinimumSize(QtCore.QSize(300, 150))
        Shift.setMaximumSize(QtCore.QSize(300, 150))
        self.label = QtGui.QLabel(Shift)
        self.label.setGeometry(QtCore.QRect(0, 30, 91, 17))
        self.label.setObjectName("label")
        self.comboBoxTime = QtGui.QComboBox(Shift)
        self.comboBoxTime.setGeometry(QtCore.QRect(130, 50, 85, 27))
        self.comboBoxTime.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBoxTime.setEditable(False)
        self.comboBoxTime.setObjectName("comboBoxTime")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.labelDivision = QtGui.QLabel(Shift)
        self.labelDivision.setGeometry(QtCore.QRect(0, 0, 261, 20))
        self.labelDivision.setScaledContents(True)
        self.labelDivision.setObjectName("labelDivision")
        self.shiftSetupButton = QtGui.QPushButton(Shift)
        self.shiftSetupButton.setGeometry(QtCore.QRect(110, 120, 181, 27))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shiftSetupButton.setIcon(icon)
        self.shiftSetupButton.setObjectName("shiftSetupButton")
        self.labelShift = QtGui.QLabel(Shift)
        self.labelShift.setGeometry(QtCore.QRect(0, 60, 91, 17))
        self.labelShift.setObjectName("labelShift")
        self.comboBoxCashier = QtGui.QComboBox(Shift)
        self.comboBoxCashier.setGeometry(QtCore.QRect(130, 80, 161, 27))
        self.comboBoxCashier.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.comboBoxCashier.setObjectName("comboBoxCashier")
        self.dateEdit = QtGui.QDateEdit(Shift)
        self.dateEdit.setGeometry(QtCore.QRect(130, 20, 110, 27))
        self.dateEdit.setWrapping(False)
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.labelOperator = QtGui.QLabel(Shift)
        self.labelOperator.setGeometry(QtCore.QRect(0, 90, 91, 17))
        self.labelOperator.setObjectName("labelOperator")

        self.retranslateUi(Shift)
        QtCore.QMetaObject.connectSlotsByName(Shift)

    def retranslateUi(self, Shift):
        Shift.setWindowTitle(QtGui.QApplication.translate("Shift", "Смена", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Shift", "Дата", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTime.setItemText(0, QtGui.QApplication.translate("Shift", "Завтрак", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTime.setItemText(1, QtGui.QApplication.translate("Shift", "Обед", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTime.setItemText(2, QtGui.QApplication.translate("Shift", "Ужин", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDivision.setText(QtGui.QApplication.translate("Shift", "Подразделение ", None, QtGui.QApplication.UnicodeUTF8))
        self.shiftSetupButton.setText(QtGui.QApplication.translate("Shift", "Установить смену[S]", None, QtGui.QApplication.UnicodeUTF8))
        self.labelShift.setText(QtGui.QApplication.translate("Shift", "Смена", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("Shift", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOperator.setText(QtGui.QApplication.translate("Shift", "Оператор", None, QtGui.QApplication.UnicodeUTF8))

