# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DS\PycharmProjects\MakeUi\lips.ui'
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
    def __init__(self):
        Ui_Dialog.__init__(self)
        self.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1246, 855)
        self.imgLabel = QtGui.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(320, 90, 640, 480))
        self.imgLabel.setFrameShape(QtGui.QFrame.Box)
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))

        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 620, 1182, 121))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setStyleSheet(_fromUtf8("image: url(:/newPrefix/650001485_CT_01.jpg);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001486_CT_01.jpg\"/>\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001487_CT_01.jpg\"/>\n"
""))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtGui.QPushButton(self.widget)
        self.pushButton_5.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001488_CT_01.jpg\"/>\n"
""))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_6 = QtGui.QPushButton(self.widget)
        self.pushButton_6.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001489_CT_01.jpg\"/>\n"
""))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtGui.QPushButton(self.widget)
        self.pushButton_7.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001490_CT_01.jpg\"/>\n"
""))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_8 = QtGui.QPushButton(self.widget)
        self.pushButton_8.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001491_CT_01.jpg\"/>\n"
""))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_3 = QtGui.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001492_CT_01.jpg\"/>\n"
""))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_9 = QtGui.QPushButton(self.widget)
        self.pushButton_9.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001493_CT_01.jpg\"/>\n"
""))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtGui.QPushButton(self.widget)
        self.pushButton_10.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001494_CT_01.jpg\"/>\n"
""))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtGui.QPushButton(self.widget)
        self.pushButton_11.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001495_CT_01.jpg\"/>\n"
""))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtGui.QPushButton(self.widget)
        self.pushButton_12.setStyleSheet(_fromUtf8("<resource type=\"image\" file=\":/newPrefix/650001496_CT_01.jpg\"/>\n"
""))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout.addWidget(self.pushButton_12)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_2.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_4.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_5.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_6.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_7.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_8.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_3.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_9.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_10.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_11.setText(_translate("Dialog", "PushButton", None))
        self.pushButton_12.setText(_translate("Dialog", "PushButton", None))

