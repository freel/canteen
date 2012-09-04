# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Report_Ui.ui'
#
# Created: Sun Apr 29 10:58:17 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Report(object):
    def setupUi(self, Report):
        Report.setObjectName("Report")
        Report.resize(834, 776)
        self.gridLayout = QtGui.QGridLayout(Report)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Report)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Report)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.reportView = QtWebKit.QWebView(Report)
        self.reportView.setUrl(QtCore.QUrl("about:blank"))
        self.reportView.setObjectName("reportView")
        self.gridLayout.addWidget(self.reportView, 4, 0, 1, 4)
        self.typeBox = QtGui.QComboBox(Report)
        self.typeBox.setObjectName("typeBox")
        self.gridLayout.addWidget(self.typeBox, 1, 1, 1, 1)
        self.startDateEdit = QtGui.QDateEdit(Report)
        self.startDateEdit.setCalendarPopup(True)
        self.startDateEdit.setObjectName("startDateEdit")
        self.gridLayout.addWidget(self.startDateEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Report)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.finishDateEdit = QtGui.QDateEdit(Report)
        self.finishDateEdit.setCalendarPopup(True)
        self.finishDateEdit.setObjectName("finishDateEdit")
        self.gridLayout.addWidget(self.finishDateEdit, 0, 3, 1, 1)
        self.printButton = QtGui.QPushButton(Report)
        self.printButton.setObjectName("printButton")
        self.gridLayout.addWidget(self.printButton, 3, 3, 1, 1)
        self.formButton = QtGui.QPushButton(Report)
        self.formButton.setObjectName("formButton")
        self.gridLayout.addWidget(self.formButton, 1, 3, 1, 1)

        self.retranslateUi(Report)
        QtCore.QMetaObject.connectSlotsByName(Report)

    def retranslateUi(self, Report):
        Report.setWindowTitle(QtGui.QApplication.translate("Report", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Report", "С:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Report", "Тип отчета:", None, QtGui.QApplication.UnicodeUTF8))
        self.startDateEdit.setDisplayFormat(QtGui.QApplication.translate("Report", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Report", "По:", None, QtGui.QApplication.UnicodeUTF8))
        self.finishDateEdit.setDisplayFormat(QtGui.QApplication.translate("Report", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setText(QtGui.QApplication.translate("Report", "Печать[F8]", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setShortcut(QtGui.QApplication.translate("Report", "F8", None, QtGui.QApplication.UnicodeUTF8))
        self.formButton.setText(QtGui.QApplication.translate("Report", "Сформировать[F9]", None, QtGui.QApplication.UnicodeUTF8))
        self.formButton.setShortcut(QtGui.QApplication.translate("Report", "F9", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
