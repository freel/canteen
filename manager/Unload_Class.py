# -*- coding: utf-8 -*-

import sys
from PySide import QtCore, QtGui
from ui.Unload_Ui import Ui_Unload
from ui.Compare_Ui import Ui_Compare
from ui.CompareTable_Ui import Ui_CompareTable
from localDb_Class import localDb_Class
from lxml import etree

class Unload_Class(QtGui.QDialog):
    """Класс для работы с загрузкой выгрузкой данных"""
    #порядок импорта таблиц не ошибиться с названиями
    import_order = (
        'cashier',
        'shift',
        'measure',
        'supplier',
        'section',
        'product',
        'dish',
        'consumption',
        'income',
        'calculate',
        'menu',
        'company',
        'worker',
        'sale'
        )

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.parent = parent
        self.shift = parent.shift
        self.ui = Ui_Unload()
        self.ui.setupUi(self)

        self.connect(self.ui.formButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_to1CButton()"))
        self.connect(self.ui.saveButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_saveButton()"))
        self.connect(self.ui.uploadButton, QtCore.SIGNAL("clicked()"),QtCore.SLOT("on_click_loadButton()"))

    def on_click_to1CButton(self):
        self.get_date()
        rootXML = etree.Element(u"ФайлПунктПитания")

        self.valToXML(rootXML,u"НачалоПериода",self.start)
        self.valToXML(rootXML,u"КонецПериода",self.finish)


        db = localDb_Class()
        query = "SELECT * FROM worker WHERE company='101' AND active=1"
        workers = db.exec_query(query)['rows']
        db.close_db()

        for worker in workers:
            infoXML = etree.SubElement(rootXML, u"СВЕДЕНИЯ_ЗА_ПЕРИОД")
            self.valToXML(infoXML,u"Фамилия",worker['name'].split(" ")[0])
            self.valToXML(infoXML,u"Имя",worker['name'].split(" ")[1])
            self.valToXML(infoXML,u"Отчество",worker['name'].split(" ")[2])
            self.valToXML(infoXML,u"ТабНомер",u"%s" % worker['employee'])
            self.valToXML(infoXML,u"СуммаЗаПериод",u"%s" % self.getSumByWorker(worker['employee']))

        with open('export/sum.xml', 'w') as f:
            f.write(etree.tostring(rootXML, pretty_print=True, encoding="Windows-1251"))

    def getSumByWorker(self,worker):
        db = localDb_Class()
        query = "SELECT SUM(m.price*s.number) AS sum FROM worker AS w, menu AS m, sale AS s WHERE s.menu=m.id AND s.worker='%s'" % worker
        result = db.exec_query(query)['rows'][0]['sum']
        db.close_db()
        return result

    def valToXML(self,parent,child,text):
        val = etree.Element(child)
        val.text = text
        parent.append(val)

    def on_click_saveButton(self):
        self.get_date()
        self.export_base()

    def on_click_loadButton(self):
        self.import_base()

    def get_date(self):
        self.start = self.ui.startDateEdit.date().toString('yyyy-MM-dd 00:00:00')
        self.finish = self.ui.finishDateEdit.date().toString('yyyy-MM-dd 23:59:59')
        self.base = self.shift.base
        print self.base

    def export_base(self):
        db = localDb_Class()

        rootXML = etree.Element("root", base = "%s" % self.base, start = self.start, finish = self.finish)
        tables = db.exec_query("SELECT name FROM sqlite_master WHERE type='table' AND name <> 'sqlite_sequence'")['rows']
        for table in tables:
            try:
                tableXML = etree.SubElement(rootXML, "%s" % table[0])
                try:
                    query = db.exec_query("SELECT * FROM {} WHERE date>='{}' AND date<='{}' AND base='{}'".format(table[0],self.start,self.finish,self.base))
                except:
                    query = db.exec_query("SELECT * FROM {} WHERE date>='{}' AND date<='{}'".format(table[0],self.start,self.finish))
                rows, keys = query['rows'], query['keys']
                for row in rows:
                    rowXML = etree.SubElement(tableXML, "row", value = "%s" % row["id"])
                    for key in keys:
                        rowXML.append(etree.Element("data", field = "%s" % key, value = "%s" % row["%s" % key]))
            except:
                None
        db.close_db()
        with open('export/base_%s.xml' % self.shift.base, 'w') as f:
            f.write(etree.tostring(rootXML, pretty_print=True, encoding="UTF-8"))

    def import_base(self):
        self.open_compare()
        db = localDb_Class()
        for table_tag in self.import_order:
            print table_tag
            self.open_compareTable(table_tag)
            element = etree.iterparse('import/base_%s' % +self.shift.base+'.xml', events = ('end',), tag = table_tag)
            for event, elem in element:
                for element_id in elem.iter(tag="id"):
                    data = {i.get('field'):i.get('value') for i in element_id.iter(tag='data')}
                    getattr(self, 'import_%s' % table_tag)(data)
                elem.clear()
                while elem.getprevious() is not None:
                    del elem.getparent()[0]
            del element
        db.close_db()

    def open_compare(self):
        """Открвает окно сравнения"""
        self.compareWindow = QtGui.QWidget(self.parent, QtCore.Qt.Window)
        self.compareWindow.setWindowModality(QtCore.Qt.WindowModal)
        self.compareWindow.ui = Ui_Compare()
        self.compareWindow.ui.setupUi(self.compareWindow)
        self.compareWindow.show()
        self.tab = {}

    def open_compareTable(self, tag):
        """Вставляет вкладку с таблицей"""
        try:
            tab = self.compareWindow.ui.tabWidget.indexOf(self.tab[tag])
            #~ self.formMenu.renew()
        except:
            self.tab[tag] = QtGui.QWidget(self.compareWindow)
            self.tab[tag].ui = Ui_CompareTable()
            self.tab[tag].ui.setupUi(self.tab[tag])
            tab = self.compareWindow.ui.tabWidget.addTab(self.tab[tag], u"%s" % tag)

    def check_value(self,table,val,col = 'id'):
        """Сравнивает на наличие подобной записи"""
        try:
            self.save_data(table, val)
        except:
            db = localDb_Class()
            print val
            answer = db.select_val_by_col(table,col,val[col])
            db.close_db()
            self.save_to_compare(table, answer['rows'], val)

    def save_data(self, table, val):
        """Записывает """
        db = localDb_Class()
        query = "INSERT INTO %s " % table
        query += " (%s) " % ",".join([ "%s" % field for field in val])
        query += " VALUES (%s) " % ",".join([ "'%s'" % val[field] for field in val])
        print query
        db.exec_query(query)
        db.close_db()

    def save_to_compare(self, tag, exist_vals, changed_vals):
        """Сохраняет список для сравнения существующих записей"""
        compared = {"exist":exist_vals,"changed":changed_vals}
        print exist_vals
        exist_item = QtGui.QTableWidgetItem()
        exist_item.setText(u"%s" % exist_vals[0][1])
        change_item = QtGui.QTableWidgetItem(u"%s" % changed_vals['id'])
        self.tab[tag].ui.compareTable.setRowCount(self.tab[tag].ui.compareTable.rowCount() + 1)
        self.tab[tag].ui.compareTable.setItem(self.tab[tag].ui.compareTable.rowCount()-1,1,exist_item)
        self.tab[tag].ui.compareTable.setItem(self.tab[tag].ui.compareTable.rowCount()-1,2,change_item)
        
    def import_cashier(self,val):
        self.check_value('cashier', val)

    def import_shift(self,val):
        val['base'] = self.shift.base
        self.check_value('shift', val)


    def import_measure(self,val):
        None

    def import_supplier(self,val):
        None

    def import_section(self,val):
        self.check_value('section', val)

    def import_product(self,val):
        self.check_value('product', val)

    def import_dish(self,val):
        self.check_value('dish', val)

    def import_consumption(self,val):
        self.check_value('consumption', val)

    def import_income(self,val):
        self.check_value('income', val)

    def import_calculate(self,val):
        val['base'] = self.shift.base
        self.check_value('calculate', val)
        #~ self.save_data('calculate',val)

    def import_menu(self,val):
        val['base'] = self.shift.base
        self.check_value('menu', val)

    def import_company(self,val):
        self.check_value('company', val)

    def import_worker(self,val):
        self.check_value('worker', val)

    def import_sale(self,val):
        self.check_value('product', val)
