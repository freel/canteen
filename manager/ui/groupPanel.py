# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupPanel.ui'
#
# Created: Fri Dec 16 13:12:43 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_groupPanel(object):
    def setupUi(self, groupPanel):
        groupPanel.setObjectName("groupPanel")
        groupPanel.resize(611, 96)
        self.gridLayout_2 = QtGui.QGridLayout(groupPanel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(groupPanel)
        self.groupBox.setObjectName("groupBox")
        self.groupLayout = QtGui.QGridLayout(self.groupBox)
        self.groupLayout.setObjectName("groupLayout")
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 2)

        self.retranslateUi(groupPanel)
        QtCore.QMetaObject.connectSlotsByName(groupPanel)

    def retranslateUi(self, groupPanel):
        groupPanel.setWindowTitle(QtGui.QApplication.translate("groupPanel", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("groupPanel", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))

