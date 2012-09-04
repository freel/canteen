# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui, QtWebKit
from ui.Report_Ui import Ui_Report
from Report_Form_Class import Report_Form_Class

class Report_Class(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Report()
        self.ui.setupUi(self)

        self.form = Report_Form_Class()
        self.set_reports_list()

        self.connect(self.ui.formButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_formButton()"))
        self.connect(self.ui.printButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("print_report()"))

    def set_reports_list(self):
        for report in self.form.ls:
            self.ui.typeBox.addItem(report)

    def on_click_formButton(self):
        vals = {
            'start':self.ui.startDateEdit.date().toString('yyyy-MM-dd'),
            'finish':self.ui.finishDateEdit.date().toString('yyyy-MM-dd'),
            'type':self.ui.typeBox.currentText(),
        }
        self.form.get_data(vals)
        self.view_report()

    def print_report(self):
        self.printer = QtGui.QPrinter()
        dialog = QtGui.QPrintDialog(self.printer, self)
        view = QtWebKit.QWebView(None)
        view.setHtml(self.form.report_view)
        view.print_(self.printer)
        if dialog.exec_():
            return
            #painter = QtGui.QPainter(printer)
            #view.render(painter)
            #painter.end()

    def view_report(self):
        self.ui.reportView.setHtml(self.form.report_view)