# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui.SalesTable_Ui import Ui_SalesTable
from localDb_Class import localDb_Class
from Worker_Class import Worker_Class
from productSalePanel_Class import productSalePanel_Class
from chequePrint import chequePrint
from cardreader import cardreader

class SalesTable_Class(QtGui.QWidget):
    summ = 0
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.shift = self.parent.shift
        self.setupData()
        self.ui = Ui_SalesTable()
        self.ui.setupUi(self)
        self.setSum()

        self.connect(self.ui.cardEdit, QtCore.SIGNAL("returnPressed()"),QtCore.SLOT("on_cardSubmit()"))
        #self.connect(self, QtCore.SIGNAL('dataSend()'), QtCore.SLOT('setData()'))
        self.connect(self.ui.chequeButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_save()"))

        self.card = cardreader()
        self.timer = QtCore.QTimer(self)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.checkCard)
        
        dockWidget = QtGui.QDockWidget(parent)
        dockWidget.setWidget(self)
        dockWidget.setFeatures(0x00)
        parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockWidget)

## DATA ##
    def setupData(self):
        self.salesRow = {}
        self.summ = 0
        self.printer = chequePrint(self)

    def on_cardSubmit(self):
        """Берем номер карты и дополняем спереди нулями до нужной длины
        если длина маленькая, то говорим это
        Выбираем имя по номеру из базы, если нет, то создать"""
        card = '{:0>16}'.format(self.ui.cardEdit.text().strip())
        if len(card)>6:
            worker = self.select_card(card)
            if worker['rows']:
                self.setWorkerData(worker['rows'][0])
                self.parent.formSales.setEnabled(True)
            else:
                self.addWorker()
            print 
            self.worker = worker['rows'][0]
        else:
            self.say_shortCard()

    def select_card(self,card):
        """Выбирает данные по номеру карты"""
        db = localDb_Class()
        rows = db.select_val_by_col('worker','card',"'%s'" % card)
        db.close_db
        return rows

    def say_shortCard(self):
        """TO DO : ошибка - мало символов """

    def addDish(self,dish):
        try:
            self.salesRow[dish[0]]["count"] += 1
            self.addToRow(self.salesRow[dish[0]])
        except:
            self.salesRow[dish[0]] = {
                "name":dish[1],
                "count":1,
                "price":dish[3],
            }
            self.salesRow[dish[0]]["item"] = self.newRow(self.salesRow[dish[0]])
        self.summ += self.salesRow[dish[0]]["price"]
        self.setSum()

    def on_save(self):
        self.get_sale()
        self.parent.ui.openSalesButton.emit(QtCore.SIGNAL("clicked()"))
        #TODO переформировать

    def save_sale(self,row):
        """Записывает данные о продажах в базу"""
        db = localDb_Class()
        db.insert_val('sale',(row['menu_id'],row['shift'],row['worker'],row['portions']))
        balance = db.select_val_by_id('menu', row['menu_id'])['rows'][0]['balance']
        db.update_val_by_id_name('menu', row['menu_id'], 'balance', balance-row['portions'])
        db.close_db()

    def save_for_sale(self,row):
        """Записывает данные о продажах в базу"""
        db = localDb_Class()
        income = db.select_val_by_id('income', row['menu_id'])['rows'][0]
        balance = int(income['rest'])-int(income['mass'])*row['portions']
        db.update_val_by_id_name('income', row['menu_id'], 'rest', balance)
        db.close_db()

    def print_cheque(self, data):
        self.printer.printData(data)
        """Печать чеков на фискальный кассовый аппарат"""

## GUI ##


    def setWorkerData(self, worker):
        """Заполняем форму данными пользователя"""
        self.ui.workerNameEdit.setText(worker['name'])
        self.ui.cardEdit.setEnabled(False)
        self.ui.salesTableWidget.setEnabled(True)
        self.ui.chequeButton.setEnabled(True)

    def get_sale(self):
        """Собирает данные об отмеченных продуктах в списке: id, количество"""
        for row in self.salesRow:
            data = {'menu_id':"%s" % row,
                'shift':self.shift.shift,
                'portions':self.salesRow[row]["count"],
                'worker':self.worker[0],
            }
            if data['menu_id'][0]=='s':
                data['menu_id'] = data['menu_id'][1:]
                self.print_cheque(self.salesRow[row])
                self.save_for_sale(data)
            else:
                self.print_cheque(self.salesRow[row])
                self.save_sale(data)
        self.printer.printFloor(self.summ)

    def addToRow(self, row):
        self.ui.salesTableWidget.item(row["item"],1).setText("%s" % row["count"])

    def newRow(self, row):
        item = QtGui.QTableWidgetItem()
        item.setText("%s" % row["name"])
        itemNumber = self.ui.salesTableWidget.rowCount()
        self.ui.salesTableWidget.setRowCount(itemNumber +1)
        self.ui.salesTableWidget.setItem(itemNumber,0,item)
        item = QtGui.QTableWidgetItem()
        item.setText("%s" % row["count"])
        self.ui.salesTableWidget.setItem(itemNumber,1,item)
        item = QtGui.QTableWidgetItem()
        item.setText("%s" % row["price"])
        self.ui.salesTableWidget.setItem(itemNumber,2,item)
        #item = QtGui.QTableWidgetItem()
        #item.setText('%s' % dish[2])
        #self.ui.salesTableWidget.setItem(itemNumber,3,item)
        return itemNumber

    def setSum(self):
        self.ui.labelSumm.setText("%s" % self.summ)

    def addWorker(self):
        """Окно добавления работника"""
        nomcard = self.ui.cardEdit.text()
        print nomcard
        form = Worker_Class(nomcard, self)
        form.show()

    def clear(self):
        self.setupData()
        #self.ui.salesTableWidget.clearContents()
        for i in range(self.ui.salesTableWidget.rowCount()):
            self.ui.salesTableWidget.removeRow(0)
        self.ui.workerNameEdit.clear()
        self.ui.cardEdit.clear()
        self.ui.cardEdit.setEnabled(True)
        self.ui.salesTableWidget.setEnabled(False)
        self.setSum()
        
    def getCard(self):
        self.filter = cardEvent(self)
        self.ui.cardEdit.installEventFilter(self.filter)
        self.ui.cardEdit.setFocus()
        self.card = cardreader()
        
        self.timer.start(1000)
            
    def checkCard(self):
        if self.card.tic():
            self.ui.cardEdit.setText("%s" % self.card.cardnum)
            self.timer.stop()
            self.on_cardSubmit()

class cardEvent(QtCore.QObject):
    def __init__(self,parent=None):
        super(cardEvent, self).__init__(parent)
        self.events = False

    def eventFilter(self,  obj,  event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.events = True
        return False
