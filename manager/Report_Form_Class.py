# -*- coding: utf-8 -*-

"""Чтение форм отчетов, Формы из 3х частей(шапка, тело, подвал) строятся из переменных типа %таблица.переменная% при чтении заменяются соответствующими значениями"""

import sys, os
import ConfigParser
from localDb_Class import localDb_Class

class Report_Form_Class():
    def __init__(self):
        self.read_report_directory()


    def read_report_directory(self):
        """Берет список установленных отчетов из директории"""
        self.ls = os.listdir('reports/')

    def get_data(self, vals):
        """Выбирает из отчета все необходимые переменные, формирует запрос по выборке этих переменных за определенный период"""
        self.vals = vals
        self.parse_file(vals['type'])
        db = localDb_Class()
        self.report_data = db.exec_query(self.report_param['body_query'])
        db.close_db()
        self.form_report()

    def parse_file(self,filename):
        config = ConfigParser.ConfigParser()
        config.read('reports/' + filename)
        self.report_param = {
            'head_query':config.get('data', 'head_query'),
            'body_query':config.get('data', 'body_query'),
            'head':config.get('data', 'head'),
            'body':config.get('data', 'body'),
            'floor':config.get('data', 'floor'),
        }

    def form_report(self):
        body = ""
        for row in self.report_data['rows'] :
            print row
            body += unicode(self.report_param['body']).format(**row)
        self.report_view = self.report_param['head'].format(**self.vals)
        self.report_view += body.encode('utf-8')
        self.report_view += self.report_param['floor'].format(**self.vals)
        self.report_view = self.report_view.decode('utf-8')
        #self.formatted_report = {
        #    head:self.report_param['head'].format(**)
        #}