# -*- coding: utf-8 -*-

import sys, os, time, serial, select, parallel
import ConfigParser

class chequePrint():
    def __init__(self, parent):
        self.shift = parent.shift
        self.parse_file()
        if self.type == "com":
            self.setCom()
        elif self.type == "lpt":
            self.setLpt()
        elif self.type == "test":
            self.setTest()

        self.printHead()

    def setTest(self):
		self.printer = open("cheque.txt","w")

    def setCom(self):
        self.printer=serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600
            )
        self.printer.open()
        self.printer.isOpen()

    def setLpt(self):
        None
        #~ self.printer = 

    def parse_file(self):
        config = ConfigParser.ConfigParser()
        config.read('config/config.ini')
        self.type = config.get('data', 'printer')

    #~ def setLtp(self):
        #~ self.printer = open("cheque.txt","w")
        #~ self.printer.write(chr(0x1b)+"t"+chr(0x11))

    def printHead(self):
        head = self.shift.today + "   %s" % self.shift.meals + "\n"
        head += u"ОАО УМПС\n".encode("cp866")
        head += "========================================\n"
        self.printer.write(head)

    def printData(self, data):
        self.printer.write("{: >5} ".format("%s".encode('cp866') % data['item']))
        self.printer.write("{: <23} ".format(data['name'].encode('cp866')))
        self.printer.write("{: >3} ".format("%s".encode('cp866') % data['count']))
        self.printer.write("{: >7}".format("%s".encode('cp866') % data['price']+"\n"))

    def printFloor(self,summ):
        self.printer.write("_______________________________________\n")
        self.printer.write(u"ИТОГО С НДС".encode('cp866')+"{: >38}".format("%s\n".encode('cp866') % summ))
        self.printer.write("\n\n\n")
        #self.printHead()
	self.printer.close()

