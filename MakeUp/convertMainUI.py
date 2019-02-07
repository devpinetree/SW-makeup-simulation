# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DS\PycharmProjects\MakeUi\untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1177, 922)
        Dialog.setStyleSheet(_fromUtf8(""))

        self.imgLabel = QtGui.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(270, 60, 640, 480))
        self.imgLabel.setFrameShape(QtGui.QFrame.Box)
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))

        self.LipsButton = QtGui.QPushButton(Dialog)
        self.LipsButton.setEnabled(True)
        self.LipsButton.setGeometry(QtCore.QRect(265, 600, 151, 151))
        self.LipsButton.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/lips.png);"))
        self.LipsButton.setText(_fromUtf8(""))
        self.LipsButton.setObjectName(_fromUtf8("LipsButton"))

        self.EyesButton = QtGui.QPushButton(Dialog)
        self.EyesButton.setGeometry(QtCore.QRect(520, 600, 151, 151))
        self.EyesButton.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/eye.png);"))
        self.EyesButton.setText(_fromUtf8(""))
        self.EyesButton.setObjectName(_fromUtf8("EyesButton"))

        self.BlingButton = QtGui.QPushButton(Dialog)
        self.BlingButton.setGeometry(QtCore.QRect(760, 600, 151, 151))
        self.BlingButton.setStyleSheet(_fromUtf8("background-image: url(:/newPrefix/bling.png);"))
        self.BlingButton.setText(_fromUtf8(""))
        self.BlingButton.setObjectName(_fromUtf8("BlingButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))

import test_rc
