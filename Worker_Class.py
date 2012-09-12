# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Worker_Ui import Ui_Worker
from localDb_Class import localDb_Class
from Shift_Class import Shift


class Worker_Class(QtGui.QDialog):
    def __init__(self, nomcard, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Worker()
        self.ui.setupUi(self)

        self.fillWorker(nomcard)

        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_saveButton()"))

    def on_click_saveButton(self):
        self.saveData(self.getParamsFromWindow())

    def getParamsFromWindow(self):
        name = self.ui.nameEdit.text()
        card = '{:0>16}'.format(self.ui.cardEdit.text())
        employee = '{:0>16}'.format(self.ui.employeeEdit.text())
        db = localDb_Class()
        company = db.select_val_by_col("company", "name", "\'%s\'" % self.ui.comboBox.currentText())["rows"][0][0]
        db.close_db()
        param = (company, card, name, employee)
        return param

    def fillWorker(self, nomcard):
        self.ui.cardEdit.setText(nomcard)
        map(self.setCompany,self.getCompany())

    def setCompany(self,row):
        self.ui.comboBox.insertItem(row[0],row[1])

    def getCompany(self):
        db = localDb_Class()
        val = [(t[0],t[1]) for t in db.select_all_val('company')['rows']]
        db.close_db()
        return val

    def saveData(self,data):
        db = localDb_Class()
        try:
            db.insert_val('worker',data)
            self.close()
            
        except Exception as e:
            errWindow = QtGui.QWidget(self, QtCore.Qt.Window)
            errWindow.setWindowTitle(u"Ошибка")
            errWindow.setWindowModality(QtCore.Qt.WindowModal)
            errWindow.show()
        db.close_db()
