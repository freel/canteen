# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Directory_Ui.ui'
#
# Created: Fri Sep 23 18:05:56 2011
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Directory(object):
    def setupUi(self, Directory):
        Directory.setObjectName("Directory")
        Directory.resize(653, 583)
        self.toolBox = QtGui.QToolBox(Directory)
        self.toolBox.setGeometry(QtCore.QRect(0, 0, 651, 511))
        self.toolBox.setFrameShape(QtGui.QFrame.Box)
        self.toolBox.setObjectName("toolBox")
        self.addRowButton = QtGui.QCommandLinkButton(Directory)
        self.addRowButton.setGeometry(QtCore.QRect(0, 520, 186, 41))
        self.addRowButton.setObjectName("addRowButton")

        self.retranslateUi(Directory)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Directory)

    def retranslateUi(self, Directory):
        Directory.setWindowTitle(QtGui.QApplication.translate("Directory", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.addRowButton.setText(QtGui.QApplication.translate("Directory", "Добавить запись", None, QtGui.QApplication.UnicodeUTF8))

