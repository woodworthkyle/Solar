# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poc.ui'
#
# Created: Mon Mar 23 22:51:05 2015
#      by: PyQt4 UI code generator 4.6.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(318, 298)
        self.dial = QtGui.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(10, 60, 181, 181))
        self.dial.setObjectName("dial")
        self.verticalSlider = QtGui.QSlider(Dialog)
        self.verticalSlider.setGeometry(QtCore.QRect(240, 70, 19, 171))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 101, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(220, 40, 62, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Speedometer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Battery", None, QtGui.QApplication.UnicodeUTF8))

