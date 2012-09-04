# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui.Shift_Ui import Ui_Shift
from datetime import datetime
from localDb_Class import localDb_Class
import tempfile

class Shift(QtGui.QWidget):
    """Первоначальное заполнение данными
    TODO ой как неправильно тут всё
    и удалять темп файл, и первоначально ставить сегодняшнюю смену"""
    today = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.renew()


    def renew(self):
        self.setupData()
        self.setupUi()


## DATA ##

    def setupData(self):
        db = localDb_Class()
        #self.last = db.get_last_shift()
        """выдернуть время крайней смены и из сравнения с текущим временем, рассчитать какая смена и сколько пропущено смен"""
        self.meals = self.getTime()
        self.shift = self.currentShift(self.today,self.meals)
        self.cashier = 1
        self.addShift() #Порядковый номер смены
        self.cashierlist = self.getCashierList() #Список кассиров
        db.close_db()

    def getTime(self):
        """
        0 - завтрак
        1 - обед
        2 - ужин
        """
        if self.time < "10:00:00":
            return 0
        elif self.time < "15:00:00":
            return 1
        else:
            return 2

    def currentShift(self,day,meals):
        """текущая смена, разница между первой сменой и текущей"""
        db = localDb_Class()
        first_shift = db.get_first_shift()
        db.close_db()
        daydiff = abs(datetime.strptime(day,"%Y-%m-%d") - datetime.strptime(first_shift['actual_date'].encode(),"%Y-%m-%d"))
        shiftdiff = daydiff.days*3 + (meals - first_shift['period'])
        return shiftdiff+1

    def addShift(self):
        """Выбираем из базы по номеру смены, если пусто, то записываем"""
        db = localDb_Class()
        if not db.select_val_by_col('shift','shift',"%s" % self.shift)['rows']:
            db.insert_val('shift',(self.shift,self.today,self.meals,self.cashier))
        db.close_db()
        f = open("temp.data","w")
        f.write("%s" % self.shift)
        f.close()


    def getCashierList(self):
        """Список кассиров"""
        db = localDb_Class()
        return db.select_all_val('cashier')['rows']
        db.close_db()

    def getCashierId(self,cName):
        """Номер кассира по имени"""
        db = localDb_Class()
        cashierId = db.select_val_by_col('cashier','name',"\'%s\'" % cName)['rows'][0]['id']
        db.close_db()
        return cashierId

    def setShift(self,date,meals,cashier=1):
        """Устанавливаем смену"""
        self.today = date
        self.meals = meals
        self.cashier = cashier
        self.shift = self.currentShift(date,meals)
        self.addShift()


## GUI ##

    def setupUi(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QtCore.QDate.fromString(self.today,"yyyy-MM-dd"))
        self.ui.comboBoxTime.setCurrentIndex(self.getTime())
        self.ui.labelShift.setText(u"Смена № " + "%s" % self.shift)
        self.setCashiers()

        self.connect(self.ui.shiftSetupButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_shiftSetupButton()"))

        dockWidget = QtGui.QDockWidget(self.parent)
        dockWidget.setWidget(self)
        self.parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockWidget)

    def on_click_shiftSetupButton(self):
        """При изменении смены записывает используемую смену"""
        cashier = self.getCashierId(self.ui.comboBoxCashier.currentText())
        date = self.ui.dateEdit.date().toString('yyyy-MM-dd')
        meals = self.ui.comboBoxTime.currentIndex()
        self.setShift(date,meals,cashier)
        self.ui.labelShift.setText(u"Смена № " + "%s" % self.shift)

    def setCashiers(self):
        """Заполняет список продавцов"""
        for cashier in self.cashierlist:
            self.ui.comboBoxCashier.addItem(cashier[1])
