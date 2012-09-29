# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui.Shift_Ui import Ui_Shift
from datetime import time, datetime
from localDb_Class import localDb_Class
import tempfile

class Shift(QtGui.QWidget):
    """НОМЕР БАЗЫ"""
    base = 1

    """Первоначальное заполнение данными"""
    today = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.setupData()
        self.setupUi()
        # События по таймеру
        self.timer = QtCore.QTimer()
        #~ time =
        #~ self.timer.singleShot(1, self.renew)
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.renew)
        self.timer.start(300000)

    def renew(self):
        if not self.manual:
            print self.toShot.total_seconds()
            self.time = datetime.now().strftime("%H:%M:%S")
            self.renewData()
            self.renewUi()
            #~ self.timer.singleShot(self.toShot.total_seconds(), self, QtCore.SLOT("renew()"))

## DATA ##

    def setupData(self):
        """выдернуть время крайней смены и из сравнения с текущим временем, рассчитать какая смена и сколько пропущено смен"""
        self.cashier = 1
        self.renewData()
        self.cashierlist = self.getCashierList() #Список кассиров

    def renewData(self):
        self.meals = self.getTime()
        self.shift = self.currentShift(self.today,self.meals)
        self.addShift() #Порядковый номер смены


    def getTime(self):
        """
        0 - завтрак
        1 - обед
        2 - ужин
        """
        breakfast = "15:06:00"
        lunch = "15:07:00"
        dinner = "19:00:00"
        if self.time < breakfast:
            #~ self.toShot = datetime.strptime("%s %s" % (self.today, breakfast), "%Y-%m-%d %H:%M:%S") - datetime.now()
            return 0
        elif self.time < lunch:
            #~ self.toShot = datetime.strptime("%s %s" % (self.today, lunch), "%Y-%m-%d %H:%M:%S") - datetime.now()
            return 1
        else:
            #~ self.toShot = datetime.strptime("%s %s" % (self.today, dinner), "%Y-%m-%d %H:%M:%S") - datetime.now()
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
        self.mnual = True
        self.shift = self.currentShift(date,meals)
        self.addShift()


## GUI ##

    def setupUi(self):
        self.ui = Ui_Shift()
        self.ui.setupUi(self)
        self.setCashiers()

        self.connect(self.ui.shiftSetupButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_shiftSetupButton()"))

        dockWidget = QtGui.QDockWidget(self.parent)
        dockWidget.setWidget(self)
        dockWidget.setFeatures(0x00)
        self.parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockWidget)

    def renewUi(self):
        self.ui.dateEdit.setDate(QtCore.QDate.fromString(self.today,"yyyy-MM-dd"))
        self.ui.comboBoxTime.setCurrentIndex(self.getTime())
        self.ui.labelShift.setText(u"Смена № " + "%s" % self.shift)

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
