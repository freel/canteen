# -*- coding: utf-8 -*-

import sys, os, time, serial, select
import ConfigParser

class cardreader():
    def __init__(self):
        self.parse_file()
        if self.type == "com":
            self.setCom()
        if self.type == "test":
            self.setTest()

    def setTest(self):
		self.reader = open("cardnumber.txt","w")

    def setCom(self):
        self.reader=serial.Serial(
            port='/dev/ttyUSB0',
            baudrate=9600
            )
        self.reader.open()
        self.reader.isOpen()
        
    def parse_file(self):
        config = ConfigParser.ConfigParser()
        config.read('config/config.ini')
        self.type = config.get('data', 'reader')

    def getcard(self):
        if self.type == "com":
            self.getcardcom()
        if self.type == "test":
            self.getcardtest()

    def getcardcom(self):
        flag = 1
        self.al=[]
        self.reader.write(chr(0x53)+chr(0x45)+chr(0x00))
        while flag:
            if self.kbhit():
                flag = 0
                break
            out=''
            #time.sleep(0.5)
            while self.reader.inWaiting()>0:
                out += self.reader.read(1)
            if out !='':
                if len(out)>=16:
                    flag = 0
        return out

    def getcardtest(self):
        None
        
    def tic(self):
        out=''
        if self.type == "com":
            time.sleep(0.5)
            while self.reader.inWaiting()>0:
                out += self.reader.read(1)
        if out !='':
            if len(out)>=16:
                self.cardnum=out
                return 1
        return None

    def kbhit(self):
        r,w,e = select.select([sys.stdin],[],[])
        print r,w,e
        return bool(r[0])
