#-*- coding: utf-8 -*-

import sys
import os
import glob
import cv2
import numpy as np
import facemask
import lipcolorchange
import eyecolorchange
import blushcolorchange
import cartoonframe
import mirrorplus
import mirrorplus2
import drawtkinter
import faceswap1
import moustacheframe
import imageemail2
import gc
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import webbrowser

from PyQt4 import QtGui,QtCore
from PyQt4.uic import loadUi
from PyQt4.phonon import Phonon
import videoplay
import Tkinter as tk
from PIL import ImageTk,Image,ImageGrab,ImageDraw
from numpy import array
from leapmotion import LeapMotionListener
import leapmotion
import Leap

bgr1=(218, 118, 102)
bgr2=(219, 71, 75)
bgr3=(217, 75, 55)
bgr4=(234, 48, 65)
bgr5=(189, 5, 43)
bgr6=(221, 1, 11)
bgr7=(180, 46, 53)
bgr8=(165, 60, 65)
bgr9=(114, 22, 33)
bgr10=(168, 28, 55)
bgr11=(249, 75, 82)
bgr12=(175, 64, 80)

#단종돼서 바꾼거
mac1=(157, 82, 65)
mac2=(0,0,0)
mac3=(70, 29, 17)
mac4=(223, 66, 58)
mac5=(43, 31, 104)
mac6=(74, 58, 55)
mac7=(112, 43, 37)
mac8=(220, 174, 181)
mac9=(154, 33, 66)
mac10=(141, 68, 60)
mac11=(164, 90, 72)
mac12=(140, 47, 39)

m1=(157, 124, 115)
m2=(201, 151, 130)
m3=(189, 136, 138)
m4=(209, 132, 123)
m5=(206, 155, 143)
m6=(215, 133, 134)
m7=(183, 117, 97)
m8=(213, 174, 152)
m9=(191, 145, 125)
m10=(175, 99, 98)
m11=(178, 142, 127)
m12=(159, 132, 123)

ud1=(201, 106, 88)
ud2=(151, 97, 71)
ud3=(80, 53, 72)
ud4=(42, 63, 62)
ud5=(197, 129, 119)
ud6=(191, 135, 96)
ud7=(146, 106, 93)
ud8=(157, 118, 112)
ud9=(106, 66, 61)
ud10=(124, 86, 63)
ud11=(104, 71, 52)
ud12=(201, 111, 94)


ce1=(238, 127, 93)
ce2=(231, 156, 135)
ce3=(236, 146, 154)
ce4=(249, 166, 135)
ce5=(242, 144, 138)
ce6=(247, 133, 145)
ce7=(250, 141, 142)
ce8=(234, 191, 180)
ce9=(230, 124, 116)
ce10=(230, 131, 101)
ce11=(174, 138, 96)
ce12=(244, 155, 152)

n1=(194, 110, 113)
n2=(214, 146, 147)
n3=(215, 113, 158)
n4=(157, 88, 88)
n5=(195, 44, 40)
n6=(243, 142, 123)
n7=(225, 148, 149)
n8=(239, 157, 164)
n9=(218, 160, 154)
n10=(171, 86, 52)
n11=(243, 178, 191)
n12=(207, 122, 121)


class HoverButton(QtGui.QToolButton):
    def __init__(self, parent=None):
        super(HoverButton, self).__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.setStyleSheet("border: 3px solid white")

    def leaveEvent(self, event):
        self.setStyleSheet("border: 1px solid white")

class show_webcam(QWidget):
    def __init__(self):
        super(show_webcam,self).__init__()
        loadUi('untitled_copyWidget.ui',self)
        frame=videoplay.videoshow()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

        self.apple.setIcon(QtGui.QIcon('image/apple.png'))
        self.apple.setIconSize(QtCore.QSize(50, 50))

        self.Mirrortitle.setText(u"SNOWWHITE")
        self.Mirrortitle.setFont(QtGui.QFont('Agency FB', 50))
        self.Mirrortitle.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.Mirrorex.setText(u"SIMULATE YOUR COSMETIC")
        self.Mirrorex.setFont(QtGui.QFont('Agency FB', 30))
        self.Mirrorex.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.LipsButton =  HoverButton(self)
        self.EyesButton =  HoverButton(self)
        self.BlushButton =  HoverButton(self)
        self.BlingButton =  HoverButton(self)
        #self.DrawButton =  HoverButton(self)
        self.mirrorButton =  HoverButton(self)
        self.shopButton =  HoverButton(self)

        self.LipsButton.move(1560,300)
        self.EyesButton.move(1560,460)
        self.BlingButton.move(1720,300)
        self.BlushButton.move(1720,460)
        #self.DrawButton.move(1740,420)
        self.mirrorButton.move(1560,620)
        self.shopButton.move(1720, 620)

        self.mirrorButton.setIcon(QtGui.QIcon('image/mirror.jpg'))
        self.mirrorButton.setIconSize(QtCore.QSize(130, 130))
        self.mirrorButton.setStyleSheet(" border: 1px solid white")
        self.mirrorButton.clicked.connect(self.PlayClick)

        self.LipsButton.setIcon(QtGui.QIcon('image/blacklips2.jpg'))
        self.LipsButton.setIconSize(QtCore.QSize(130, 130))
        self.LipsButton.setStyleSheet(" border: 1px solid white")
        self.LipsButton.clicked.connect(self.PlayClick)

        self.EyesButton.setIcon(QtGui.QIcon('image/eye2.png'))
        self.EyesButton.setIconSize(QtCore.QSize(130, 130))
        self.EyesButton.setStyleSheet(" border: 1px solid white")
        self.EyesButton.clicked.connect(self.PlayClick)

        self.BlingButton.setIcon(QtGui.QIcon('image/shine.png'))
        self.BlingButton.setIconSize(QtCore.QSize(130, 130))
        self.BlingButton.setStyleSheet(" border: 1px solid white")
        self.BlingButton.clicked.connect(self.PlayClick)

        self.BlushButton.setIcon(QtGui.QIcon('image/blush.png'))
        self.BlushButton.setIconSize(QtCore.QSize(130, 130))
        self.BlushButton.setStyleSheet(" border: 1px solid white")
        self.BlushButton.clicked.connect(self.PlayClick)

        self.shopButton.setIcon(QtGui.QIcon('image/shop.png'))
        self.shopButton.setIconSize(QtCore.QSize(130, 130))
        self.shopButton.setStyleSheet(" border: 1px solid white")
        self.shopButton.clicked.connect(self.PlayClick)
        self.shopButton.clicked.connect(self.openShop)

        #self.DrawButton.setIcon(QtGui.QIcon('image/draw.png'))
        #self.DrawButton.setIconSize(QtCore.QSize(130, 130))
        #self.DrawButton.setStyleSheet(" border: 1px solid white")

        self.closeButton.setIcon(QtGui.QIcon('image/close3.png'))
        self.closeButton.setIconSize(QtCore.QSize(40, 40))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.timeout.connect(self.displayTime)

        self.timer.start(30)

    def openShop(self):
        url = 'http://localhost'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    def closeIt(self):
        self.close()

    def PlayClick(self):
        QSound("sound/click2.wav").play()

    def update_frame(self):
        frame=videoplay.videoshow()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def displayTime(self):

        dateTime = QtCore.QDateTime.currentDateTime().toString("hh : mm : ss")
        self.timeLabel.setText(dateTime)
        self.timeLabel.setFont(QtGui.QFont('Agency FB', 60))
        self.timeLabel.setStyleSheet("color: white;")

        dateTime = QtCore.QDateTime.currentDateTime().toString("yyyy - MM - dd")
        self.dateLabel.setText(dateTime)
        self.dateLabel.setFont(QtGui.QFont('Agency FB', 25))
        self.dateLabel.setStyleSheet("color: white;")

    #display webcam

class LipsDialog(QWidget):
    def __init__(self, parent=None):
        super(LipsDialog, self).__init__(parent)
        loadUi('lips_copyWidget.ui',self)

        self.imgLabel.move(490,0)
        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        self.returnButton.setIcon(QtGui.QIcon('image/return.png'))
        self.returnButton.setIconSize(QtCore.QSize(100, 100))

        self.b1.setIcon(QtGui.QIcon('image/lip/etude/1.jpg'))
        self.b1.setIconSize(QtCore.QSize(150, 150))
        self.b1.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b1.clicked.connect(self.PlayClick)

        self.b2.setIcon(QtGui.QIcon('image/lip/etude/2.jpg'))
        self.b2.setIconSize(QtCore.QSize(150, 150))
        self.b2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b2.clicked.connect(self.PlayClick)

        self.b3.setIcon(QtGui.QIcon('image/lip/etude/3.jpg'))
        self.b3.setIconSize(QtCore.QSize(150, 150))
        self.b3.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b3.clicked.connect(self.PlayClick)

        self.b4.setIcon(QtGui.QIcon('image/lip/etude/4.jpg'))
        self.b4.setIconSize(QtCore.QSize(150, 150))
        self.b4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b4.clicked.connect(self.PlayClick)

        self.b5.setIcon(QtGui.QIcon('image/lip/etude/5.jpg'))
        self.b5.setIconSize(QtCore.QSize(150, 150))
        self.b5.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b5.clicked.connect(self.PlayClick)

        self.b6.setIcon(QtGui.QIcon('image/lip/etude/6.jpg'))
        self.b6.setIconSize(QtCore.QSize(150, 150))
        self.b6.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b6.clicked.connect(self.PlayClick)

        self.b7.setIcon(QtGui.QIcon('image/lip/etude/7.jpg'))
        self.b7.setIconSize(QtCore.QSize(150, 150))
        self.b7.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b7.clicked.connect(self.PlayClick)

        self.b8.setIcon(QtGui.QIcon('image/lip/etude/8.jpg'))
        self.b8.setIconSize(QtCore.QSize(150, 150))
        self.b8.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b8.clicked.connect(self.PlayClick)

        self.b9.setIcon(QtGui.QIcon('image/lip/etude/9.jpg'))
        self.b9.setIconSize(QtCore.QSize(150, 150))
        self.b9.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b9.clicked.connect(self.PlayClick)

        self.b10.setIcon(QtGui.QIcon('image/lip/etude/10.jpg'))
        self.b10.setIconSize(QtCore.QSize(150, 150))
        self.b10.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b10.clicked.connect(self.PlayClick)

        self.b11.setIcon(QtGui.QIcon('image/lip/etude/11.jpg'))
        self.b11.setIconSize(QtCore.QSize(150, 150))
        self.b11.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b11.clicked.connect(self.PlayClick)

        self.b12.setIcon(QtGui.QIcon('image/lip/etude/12.jpg'))
        self.b12.setIconSize(QtCore.QSize(150, 150))
        self.b12.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b12.clicked.connect(self.PlayClick)

        self.cameraButton.setIcon(QtGui.QIcon('image/cameraicon.jpg'))
        self.cameraButton.setIconSize(QtCore.QSize(150, 150))

        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/emailDisabled.png'), QtGui.QIcon.Disabled)

        self.EmailButton.setIcon(emailIcon)
        self.EmailButton.setIconSize(QtCore.QSize(150, 150))
        self.tabWidget.setStyleSheet("""QTabWidget::pane { border: 0;}
                  QTabWidget>QWidget>QWidget{
                       background: rgb(20,20,20);
                       border-top-right-radius: 15px;
                       border-bottom-left-radius: 15px;
                       border-bottom-right-radius: 15px;
                       }
                  QTabBar::tab {width: 120px;}
                  QTabBar::tab:selected {
                       font-family: Agency FB;
                       font-size: 20px;
                       font: Bold;
                       color: rgb(0,0,0,255);
                       background: rgb(234,234,234,255);
                       border-top-left-radius: 8px;
                       border-top-right-radius: 8px;
                       padding: 20px 50px 20px 24px;}
                  QTabBar::tab:!selected{
                       font-family: Agency FB;
                       font-size: 20px;
                       font: Bold;
                       color: rgb(255,255,255,255);
                       background: rgb(175,175,175,255);
                       border-top-left-radius: 8px;
                       border-top-right-radius: 8px;
                       padding: 20px 50px 10px 24px;}""")

        self.b1_2.setIcon(QtGui.QIcon('image/lip/mac/mac1.jpg'))
        self.b1_2.setIconSize(QtCore.QSize(150, 150))
        self.b1_2.clicked.connect(self.PlayClick)
        self.b1_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")

        self.b2_2.setIcon(QtGui.QIcon('image/lip/mac/mac2.png'))
        self.b2_2.setIconSize(QtCore.QSize(150, 150))
        self.b2_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b2_2.clicked.connect(self.PlayClick)

        self.b3_2.setIcon(QtGui.QIcon('image/lip/mac/mac3.jpg'))
        self.b3_2.setIconSize(QtCore.QSize(150, 150))
        self.b3_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b3_2.clicked.connect(self.PlayClick)

        self.b4_2.setIcon(QtGui.QIcon('image/lip/mac/mac4.jpg'))
        self.b4_2.setIconSize(QtCore.QSize(150, 150))
        self.b4_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b4_2.clicked.connect(self.PlayClick)

        self.b5_2.setIcon(QtGui.QIcon('image/lip/mac/mac5.jpg'))
        self.b5_2.setIconSize(QtCore.QSize(150, 150))
        self.b5_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b5_2.clicked.connect(self.PlayClick)

        self.b6_2.setIcon(QtGui.QIcon('image/lip/mac/mac6.jpg'))
        self.b6_2.setIconSize(QtCore.QSize(150, 150))
        self.b6_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b6_2.clicked.connect(self.PlayClick)

        self.b7_2.setIcon(QtGui.QIcon('image/lip/mac/mac7.jpg'))
        self.b7_2.setIconSize(QtCore.QSize(150, 150))
        self.b7_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b7_2.clicked.connect(self.PlayClick)

        self.b8_2.setIcon(QtGui.QIcon('image/lip/mac/mac8.jpg'))
        self.b8_2.setIconSize(QtCore.QSize(150, 150))
        self.b8_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b8_2.clicked.connect(self.PlayClick)

        self.b9_2.setIcon(QtGui.QIcon('image/lip/mac/mac9.jpg'))
        self.b9_2.setIconSize(QtCore.QSize(150, 150))
        self.b9_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b9_2.clicked.connect(self.PlayClick)

        self.b10_2.setIcon(QtGui.QIcon('image/lip/mac/mac10.jpg'))
        self.b10_2.setIconSize(QtCore.QSize(150, 150))
        self.b10_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b10_2.clicked.connect(self.PlayClick)

        self.b11_2.setIcon(QtGui.QIcon('image/lip/mac/mac11.jpg'))
        self.b11_2.setIconSize(QtCore.QSize(150, 150))
        self.b11_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b11_2.clicked.connect(self.PlayClick)

        self.b12_2.setIcon(QtGui.QIcon('image/lip/mac/mac12.jpg'))
        self.b12_2.setIconSize(QtCore.QSize(150, 150))
        self.b12_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b12_2.clicked.connect(self.PlayClick)

        self.shopButton.setIcon(QtGui.QIcon('image/shop.png'))
        self.shopButton.setIconSize(QtCore.QSize(130, 130))
        self.shopButton.clicked.connect(self.openShop)

        self.start_webcam()

    def openShop(self):
        url='http://localhost'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    def PlayClick(self):
        QSound("sound/t1.wav").play()

    def enableEmailandCapture(self):
        #ImgLabel의 웹캠 frame 캡쳐
        p= QPixmap.grabWidget(self.imgLabel)

        #txt파일에 저장해놓은 이미지 번호 읽어오기
        f = open("ImageNum.txt", 'r')
        data = f.read()
        f.close()

        #캡쳐 이미지 번호대로 저장
        if data == 1:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
        else:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
            f = open("ImageNum.txt", 'w')
            data=int(data)
            data += 1
            newdata = str(data)
            f.write(newdata)
            f.close()
     # 찰칵 효과음
        self.EmailButton.setEnabled(True)
        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/email.png'), QtGui.QIcon.Active)
        self.EmailButton.setIcon(emailIcon)

    def start_webcam(self):

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1920)
        self.capture.set(4, 1080)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(0)


    def update_frame(self):
        gc.collect()
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)

        self.imgLabel.setPixmap(pix)

    def lip1_start_webcam(self):
        self.colorName.setText(u":  피치 못한 베이지")
        self.colorName.setFont(QtGui.QFont("Swagger TTF", 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
       # self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.lip1_update_frame)
        self.timer.start(5)

    def lip1_update_frame(self):
        ret, frame = self.capture.read()
        frame =lipcolorchange.lipcolorstart(frame,bgr1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip2_start_webcam(self):
        self.colorName.setText(u":  어제보다 로제")
        self.colorName.setFont(QtGui.QFont('Swagger TTF ', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)

        self.timer.timeout.connect(self.lip2_update_frame)
        self.timer.start(5)

    def lip2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip3_start_webcam(self):
        self.colorName.setText(u":  얼마나 오렌지")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip3_update_frame)
        self.timer.start(0)

    def lip3_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip4_start_webcam(self):
        self.colorName.setText(u":  예리한 핑크")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip4_update_frame)
        self.timer.start(0)

    def lip4_update_frame(self):
        gc.collect()

        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip5_start_webcam(self):
        self.colorName.setText(u":  워 아이린 레드")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip5_update_frame)
        self.timer.start(0)

    def lip5_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip6_start_webcam(self):
        self.colorName.setText(u":  상큼하조이 자몽")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip6_update_frame)
        self.timer.start(0)

    def lip6_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip7_start_webcam(self):
        self.colorName.setText(u":  준비된 레디 레드")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip7_update_frame)
        self.timer.start(0)

    def lip7_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip8_start_webcam(self):
        self.colorName.setText(u":  오늘은 웬디 브라운")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip8_update_frame)
        self.timer.start(0)

    def lip8_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip9_start_webcam(self):
        self.colorName.setText(u":  슬기로운 버건디")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip9_update_frame)
        self.timer.start(0)

    def lip9_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip10_start_webcam(self):
        self.colorName.setText(u":  생각보다 자주")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip10_update_frame)
        self.timer.start(0)

    def lip10_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip11_start_webcam(self):
        self.colorName.setText(u":  윙크하는 핑크")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip11_update_frame)
        self.timer.start(0)

    def lip11_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip12_start_webcam(self):
        self.colorName.setText(u":  로맨스엔 로즈")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 45))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip12_update_frame)
        self.timer.start(0)

    def lip12_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,bgr12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip1_2_start_webcam(self):
        self.colorName.setText(u":  TAUPE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        # self.b1.setStyleSheet("QIcon {border: 1px solid red}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
       # self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.lip1_2_update_frame)
        self.timer.start(0)

    def lip1_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =lipcolorchange.lipcolorstart(frame,mac1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip2_2_start_webcam(self):
        self.colorName.setText(u":  4EVA")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.lip2_2_update_frame)
        self.timer.start(0)

    def lip2_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip3_2_start_webcam(self):
        self.colorName.setText(u":  ANTIQUE VELVET")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip3_2_update_frame)
        self.timer.start(0)

    def lip3_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip4_2_start_webcam(self):
        self.colorName.setText(u":  TROPIC TONIC")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip4_2_update_frame)
        self.timer.start(0)

    def lip4_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip5_2_start_webcam(self):
        self.colorName.setText(u":  MATTE ROYAL")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip5_2_update_frame)
        self.timer.start(0)

    def lip5_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip6_2_start_webcam(self):
        self.colorName.setText(u":  IN MY FASHION")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip6_2_update_frame)
        self.timer.start(0)

    def lip6_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip7_2_start_webcam(self):
        self.colorName.setText(u":  SIN")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip7_2_update_frame)
        self.timer.start(0)

    def lip7_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip8_2_start_webcam(self):
        self.colorName.setText(u":  LAZY LULLABY")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip8_2_update_frame)
        self.timer.start(0)

    def lip8_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip9_2_start_webcam(self):
        self.colorName.setText(u":  DIVA")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip9_2_update_frame)
        self.timer.start(0)

    def lip9_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip10_2_start_webcam(self):
        self.colorName.setText(u":  WHIRL")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip10_2_update_frame)
        self.timer.start(0)

    def lip10_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip11_2_start_webcam(self):
        self.colorName.setText(u":  VELVET TEDDY")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip11_2_update_frame)
        self.timer.start(0)

    def lip11_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def lip12_2_start_webcam(self):
        self.colorName.setText(u":  MARRAKESH")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.lip12_2_update_frame)
        self.timer.start(0)

    def lip12_2_update_frame(self):
        ret, frame = self.capture.read()
       # bgrcolor=lipcolorextract.lipcolorextraction('image/1.jpg')
       # print bgrcolor
        # My webcam yields frames in BGR format
        frame =lipcolorchange.lipcolorstart(frame,mac12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

class EyesDialog(QWidget):
    def __init__(self, parent=None):
        super(EyesDialog, self).__init__(parent)
        loadUi('eyes_Widget.ui',self)
        self.imgLabel.move(490,0)

        self.b1.setIcon(QtGui.QIcon('image/eyes/missha/m1.jpg'))
        self.b1.setIconSize(QtCore.QSize(150, 150))
        self.b1.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b1.clicked.connect(self.PlayClick)

        self.b2.setIcon(QtGui.QIcon('image/eyes/missha/m2.jpg'))
        self.b2.setIconSize(QtCore.QSize(150, 150))
        self.b2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b2.clicked.connect(self.PlayClick)

        self.b3.setIcon(QtGui.QIcon('image/eyes/missha/m3.jpg'))
        self.b3.setIconSize(QtCore.QSize(150, 150))
        self.b3.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b3.clicked.connect(self.PlayClick)

        self.b4.setIcon(QtGui.QIcon('image/eyes/missha/m4.jpg'))
        self.b4.setIconSize(QtCore.QSize(150, 150))
        self.b4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b4.clicked.connect(self.PlayClick)

        self.b5.setIcon(QtGui.QIcon('image/eyes/missha/m5.jpg'))
        self.b5.setIconSize(QtCore.QSize(150, 150))
        self.b5.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b5.clicked.connect(self.PlayClick)

        self.b6.setIcon(QtGui.QIcon('image/eyes/missha/m6.jpg'))
        self.b6.setIconSize(QtCore.QSize(150, 150))
        self.b6.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b6.clicked.connect(self.PlayClick)

        self.b7.setIcon(QtGui.QIcon('image/eyes/missha/m7.jpg'))
        self.b7.setIconSize(QtCore.QSize(150, 150))
        self.b7.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b7.clicked.connect(self.PlayClick)

        self.b8.setIcon(QtGui.QIcon('image/eyes/missha/m8.jpg'))
        self.b8.setIconSize(QtCore.QSize(150, 150))
        self.b8.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b8.clicked.connect(self.PlayClick)

        self.b9.setIcon(QtGui.QIcon('image/eyes/missha/m9.jpg'))
        self.b9.setIconSize(QtCore.QSize(150, 150))
        self.b9.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b9.clicked.connect(self.PlayClick)

        self.b10.setIcon(QtGui.QIcon('image/eyes/missha/m10.jpg'))
        self.b10.setIconSize(QtCore.QSize(150, 150))
        self.b10.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b10.clicked.connect(self.PlayClick)

        self.b11.setIcon(QtGui.QIcon('image/eyes/missha/m11.jpg'))
        self.b11.setIconSize(QtCore.QSize(150, 150))
        self.b11.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b11.clicked.connect(self.PlayClick)

        self.b12.setIcon(QtGui.QIcon('image/eyes/missha/m12.jpg'))
        self.b12.setIconSize(QtCore.QSize(150, 150))
        self.b12.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b12.clicked.connect(self.PlayClick)

        self.b1_4.setIcon(QtGui.QIcon('image/eyes/ud/UD1.jpg'))
        self.b1_4.setIconSize(QtCore.QSize(150, 150))
        self.b1_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b1_4.clicked.connect(self.PlayClick)

        self.b2_4.setIcon(QtGui.QIcon('image/eyes/ud/UD2.jpg'))
        self.b2_4.setIconSize(QtCore.QSize(150, 150))
        self.b2_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b2_4.clicked.connect(self.PlayClick)

        self.b3_4.setIcon(QtGui.QIcon('image/eyes/ud/UD3.jpg'))
        self.b3_4.setIconSize(QtCore.QSize(150, 150))
        self.b3_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b3_4.clicked.connect(self.PlayClick)

        self.b4_4.setIcon(QtGui.QIcon('image/eyes/ud/UD4.jpg'))
        self.b4_4.setIconSize(QtCore.QSize(150, 150))
        self.b4_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b4_4.clicked.connect(self.PlayClick)

        self.b5_4.setIcon(QtGui.QIcon('image/eyes/ud/UD5.jpg'))
        self.b5_4.setIconSize(QtCore.QSize(150, 150))
        self.b5_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b5_4.clicked.connect(self.PlayClick)

        self.b6_4.setIcon(QtGui.QIcon('image/eyes/ud/UD6.jpg'))
        self.b6_4.setIconSize(QtCore.QSize(150, 150))
        self.b6_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b6_4.clicked.connect(self.PlayClick)

        self.b7_4.setIcon(QtGui.QIcon('image/eyes/ud/UD7.jpg'))
        self.b7_4.setIconSize(QtCore.QSize(150, 150))
        self.b7_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b7_4.clicked.connect(self.PlayClick)

        self.b8_4.setIcon(QtGui.QIcon('image/eyes/ud/UD8.jpg'))
        self.b8_4.setIconSize(QtCore.QSize(150, 150))
        self.b8_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b8_4.clicked.connect(self.PlayClick)

        self.b9_4.setIcon(QtGui.QIcon('image/eyes/ud/UD9.jpg'))
        self.b9_4.setIconSize(QtCore.QSize(150, 150))
        self.b9_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b9_4.clicked.connect(self.PlayClick)

        self.b10_4.setIcon(QtGui.QIcon('image/eyes/ud/UD10.jpg'))
        self.b10_4.setIconSize(QtCore.QSize(150, 150))
        self.b10_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b10_4.clicked.connect(self.PlayClick)

        self.b11_4.setIcon(QtGui.QIcon('image/eyes/ud/UD11.jpg'))
        self.b11_4.setIconSize(QtCore.QSize(150, 150))
        self.b11_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b11_4.clicked.connect(self.PlayClick)

        self.b12_4.setIcon(QtGui.QIcon('image/eyes/ud/UD12.jpg'))
        self.b12_4.setIconSize(QtCore.QSize(150, 150))
        self.b12_4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b12_4.clicked.connect(self.PlayClick)


        self.returnButton.setIcon(QtGui.QIcon('image/return.png'))
        self.returnButton.setIconSize(QtCore.QSize(100, 100))
        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        self.cameraButton.setIcon(QtGui.QIcon('image/cameraicon.jpg'))
        self.cameraButton.setIconSize(QtCore.QSize(150, 150))

        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/emailDisabled.png'), QtGui.QIcon.Disabled)
        self.EmailButton.setIcon(emailIcon)
        self.EmailButton.setIconSize(QtCore.QSize(150, 150))
        self.tabWidget.setStyleSheet("""QTabWidget::pane { border: 0;}
               QTabWidget>QWidget>QWidget{
                    background: rgb(20,20,20);
                    border-top-right-radius: 15px;
                    border-bottom-left-radius: 15px;
                    border-bottom-right-radius: 15px;
                    }
               QTabBar::tab {width: 120px;}
               QTabBar::tab:selected {
                    font-family: Agency FB;
                    font-size: 20px;
                    font: Bold;
                    color: rgb(0,0,0,255);
                    background: rgb(234,234,234,255);
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;
                    padding: 20px 50px 20px 24px;}
               QTabBar::tab:!selected{
                    font-family: Agency FB;
                    font-size: 20px;
                    font: Bold;
                    color: rgb(255,255,255,255);
                    background: rgb(175,175,175,255);
                    border-top-left-radius: 8px;
                    border-top-right-radius: 8px;
                    padding: 20px 50px 10px 24px;}""")

        self.shopButton.setIcon(QtGui.QIcon('image/shop.png'))
        self.shopButton.setIconSize(QtCore.QSize(130, 130))
        self.shopButton.clicked.connect(self.openShop)

        self.start_webcam()

    def openShop(self):
        url = 'http://localhost'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    def PlayClick(self):
        QSound("sound/t1.wav").play()

    def enableEmailandCapture(self):
        # QPixmap.grabWidget(self.imgLabel).save('Image/captureImage_1.jpg', 'jpg')
        # 처음 저장은 1
        p = QPixmap.grabWidget(self.imgLabel)

        f = open("ImageNum.txt", 'r')
        data = f.read()
        f.close()

        if data == 1:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
        else:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
            f = open("ImageNum.txt", 'w')
            data = int(data)
            data += 1
            newdata = str(data)
            f.write(newdata)
            f.close()

        #        p.save(filename, 'jpg')

        # 찰칵 소리 넣기
        self.EmailButton.setEnabled(True)
        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/email.png'), QtGui.QIcon.Active)
        self.EmailButton.setIcon(emailIcon)

    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        # My webcam yields frames in BGR format
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)

        self.imgLabel.setPixmap(pix)


    def eye1_start_webcam(self):
        self.colorName.setText(u":  코코아머랭")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye1_update_frame)
        self.timer.start(0)

    def eye1_update_frame(self):
        ret, frame = self.capture.read()


        frame = eyecolorchange.eyecolorstart(frame, m1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye2_start_webcam(self):
        self.colorName.setText(u":  피넛 쿠키")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye2_update_frame)
        self.timer.start(0)

    def eye2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye3_start_webcam(self):
        self.colorName.setText(u":  로즈 폼폼")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye3_update_frame)
        self.timer.start(0)

    def eye3_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye4_start_webcam(self):
        self.colorName.setText(u":  마멀레이드")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye4_update_frame)
        self.timer.start(0)

    def eye4_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye5_start_webcam(self):
        self.colorName.setText(u":  피치 스무디")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye5_update_frame)
        self.timer.start(0)

    def eye5_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye6_start_webcam(self):
        self.colorName.setText(u":  핑크 벨")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye6_update_frame)
        self.timer.start(0)

    def eye6_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye7_start_webcam(self):
        self.colorName.setText(u":  시나몬 파이")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye7_update_frame)
        self.timer.start(0)

    def eye7_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye8_start_webcam(self):
        self.colorName.setText(u":  메리문")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye8_update_frame)
        self.timer.start(0)

    def eye8_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye9_start_webcam(self):
        self.colorName.setText(u":  허니유")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye9_update_frame)
        self.timer.start(0)

    def eye9_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye10_start_webcam(self):
        self.colorName.setText(u":  뷰티헌트")
        self.colorName.setFont(QtGui.QFont('Swagger TTF ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye10_update_frame)
        self.timer.start(0)

    def eye10_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye11_start_webcam(self):
        self.colorName.setText(u":  레이디세이션")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye11_update_frame)
        self.timer.start(0)

    def eye11_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye12_start_webcam(self):
        self.colorName.setText(u":  소울 시티")
        self.colorName.setFont(QtGui.QFont('Swagger TTF', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye12_update_frame)
        self.timer.start(0)

    def eye12_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, m12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye1_2_start_webcam(self):
        self.colorName.setText(u":  FIRE BALL")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye1_2_update_frame)
        self.timer.start(0)

    def eye1_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye2_2_start_webcam(self):
        self.colorName.setText(u":  RIFF")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye2_2_update_frame)
        self.timer.start(0)

    def eye2_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye3_2_start_webcam(self):
        self.colorName.setText(u":  ROCKSTAR")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye3_2_update_frame)
        self.timer.start(0)

    def eye3_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye4_2_start_webcam(self):
        self.colorName.setText(u":  LOADED")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye4_2_update_frame)
        self.timer.start(0)

    def eye4_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye5_2_start_webcam(self):
        self.colorName.setText(u":  SNATCH")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye5_2_update_frame)
        self.timer.start(0)

    def eye5_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye6_2_start_webcam(self):
        self.colorName.setText(u":  HALF BAKED")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye6_2_update_frame)
        self.timer.start(0)

    def eye6_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye7_2_start_webcam(self):
        self.colorName.setText(u":  MIDNIGHT RODEO")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye7_2_update_frame)
        self.timer.start(0)

    def eye7_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye8_2_start_webcam(self):
        self.colorName.setText(u":  MIDNIGHT COWBOY")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye8_2_update_frame)
        self.timer.start(0)

    def eye8_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye9_2_start_webcam(self):
        self.colorName.setText(u":  ROACH")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye9_2_update_frame)
        self.timer.start(0)

    def eye9_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye10_2_start_webcam(self):
        self.colorName.setText(u":  SMOG")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye10_2_update_frame)
        self.timer.start(0)

    def eye10_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye11_2_start_webcam(self):
        self.colorName.setText(u":  SNAKE BITE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye11_2_update_frame)
        self.timer.start(0)

    def eye11_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def eye12_2_start_webcam(self):
        self.colorName.setText(u":  FREE LOVE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.eye12_2_update_frame)
        self.timer.start(0)

    def eye12_2_update_frame(self):
        ret, frame = self.capture.read()
        frame = eyecolorchange.eyecolorstart(frame, ud12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

class BlingDialog(QWidget):
    def __init__(self, parent=None):
        super(BlingDialog, self).__init__(parent)
        loadUi('bling_Widget.ui',self)
        self.imgLabel.move(500,0)

        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        self.Button1.setIcon(QtGui.QIcon('image/question.png'))
        self.Button1.setIconSize(QtCore.QSize(100, 100))
        self.Button2.setIcon(QtGui.QIcon('image/moustacheemo.png'))
        self.Button2.setIconSize(QtCore.QSize(100, 100))
        self.Button3.setIcon(QtGui.QIcon('image/emoticon.png'))
        self.Button3.setIconSize(QtCore.QSize(100, 100))
        self.Button4.setIcon(QtGui.QIcon('image/mask2.png'))
        self.Button4.setIconSize(QtCore.QSize(100, 100))
        self.returnButton.setIcon(QtGui.QIcon('image/return.png'))
        self.returnButton.setIconSize(QtCore.QSize(100, 100))
        self.cameraButton.setIcon(QtGui.QIcon('image/cameraicon.jpg'))
        self.cameraButton.setIconSize(QtCore.QSize(150, 150))

        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/emailDisabled.png'), QtGui.QIcon.Disabled)
        self.EmailButton.setIcon(emailIcon)
        self.EmailButton.setIconSize(QtCore.QSize(150, 150))
        self.start_webcam()

    def enableEmailandCapture(self):
        # QPixmap.grabWidget(self.imgLabel).save('Image/captureImage_1.jpg', 'jpg')
        # 처음 저장은 1
        p = QPixmap.grabWidget(self.imgLabel)

        f = open("ImageNum.txt", 'r')
        data = f.read()
        f.close()

        if data == 1:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
        else:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
            f = open("ImageNum.txt", 'w')
            data = int(data)
            data += 1
            newdata = str(data)
            f.write(newdata)
            f.close()

        #        p.save(filename, 'jpg')

        # 찰칵 소리 넣기
        self.EmailButton.setEnabled(True)
        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/email.png'), QtGui.QIcon.Active)
        self.EmailButton.setIcon(emailIcon)

    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))
        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def start_faceswap1(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_faceswap1)
        self.timer.start(0)

    def update_faceswap1(self):
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

        frame = faceswap1.faceswap()
        cv2.imshow("zz", frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def start_faceswap2(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_faceswap2)
        self.timer.start(0)

    def update_faceswap2(self):
        ret, frame = self.capture.read()
        frame = moustacheframe.mousframe(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def start_faceswap3(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_faceswap3)
        self.timer.start(0)

    def update_faceswap3(self):
        ret, frame = self.capture.read()
        frame = cartoonframe.cartoonize_image(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def start_faceswap4(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_faceswap4)
        self.timer.start(0)

    def update_faceswap4(self):
        ret, frame = self.capture.read()
        frame = facemask.facemask()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

class BlushDialog(QWidget):
    def __init__(self, parent=None):
        super(BlushDialog, self).__init__(parent)
        loadUi('blush_Widget.ui',self)
        #웹캠 화면
        self.imgLabel.move(490, 0)
        #돌아가기 버튼
        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        #블러셔 버튼들
        self.b1.setIcon(QtGui.QIcon('image/blusher/3ce/ce1.jpg'))
        self.b1.setIconSize(QtCore.QSize(150,150))
        self.b1.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b1.clicked.connect(self.PlayClick)

        self.b2.setIcon(QtGui.QIcon('image/blusher/3ce/ce2.jpg'))
        self.b2.setIconSize(QtCore.QSize(150,150))
        self.b2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b2.clicked.connect(self.PlayClick)

        self.b3.setIcon(QtGui.QIcon('image/blusher/3ce/ce3.jpg'))
        self.b3.setIconSize(QtCore.QSize(150,150))
        self.b3.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b3.clicked.connect(self.PlayClick)

        self.b4.setIcon(QtGui.QIcon('image/blusher/3ce/ce4.jpg'))
        self.b4.setIconSize(QtCore.QSize(150,150))
        self.b4.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b4.clicked.connect(self.PlayClick)

        self.b5.setIcon(QtGui.QIcon('image/blusher/3ce/ce5.jpg'))
        self.b5.setIconSize(QtCore.QSize(150,150))
        self.b5.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b5.clicked.connect(self.PlayClick)

        self.b6.setIcon(QtGui.QIcon('image/blusher/3ce/ce6.jpg'))
        self.b6.setIconSize(QtCore.QSize(150,150))
        self.b6.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b6.clicked.connect(self.PlayClick)

        self.b7.setIcon(QtGui.QIcon('image/blusher/3ce/ce7.jpg'))
        self.b7.setIconSize(QtCore.QSize(150,150))
        self.b7.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b7.clicked.connect(self.PlayClick)

        self.b8.setIcon(QtGui.QIcon('image/blusher/3ce/ce8.jpg'))
        self.b8.setIconSize(QtCore.QSize(150,150))
        self.b8.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b8.clicked.connect(self.PlayClick)

        self.b9.setIcon(QtGui.QIcon('image/blusher/3ce/ce9.jpg'))
        self.b9.setIconSize(QtCore.QSize(150,150))
        self.b9.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b9.clicked.connect(self.PlayClick)

        self.b10.setIcon(QtGui.QIcon('image/blusher/3ce/ce10.jpg'))
        self.b10.setIconSize(QtCore.QSize(150,150))
        self.b10.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b10.clicked.connect(self.PlayClick)

        self.b11.setIcon(QtGui.QIcon('image/blusher/3ce/ce11.jpg'))
        self.b11.setIconSize(QtCore.QSize(150,150))
        self.b11.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b11.clicked.connect(self.PlayClick)

        self.b12.setIcon(QtGui.QIcon('image/blusher/3ce/ce12.jpg'))
        self.b12.setIconSize(QtCore.QSize(150,150))
        self.b12.setStyleSheet("QPushButton:pressed { border: 5px solid yellow}")
        self.b12.clicked.connect(self.PlayClick)

        self.b1_2.setIcon(QtGui.QIcon('image/blusher/nars/n1.jpg'))
        self.b1_2.setIconSize(QtCore.QSize(150, 150))
        self.b1_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b1_2.clicked.connect(self.PlayClick)

        self.b2_2.setIcon(QtGui.QIcon('image/blusher/nars/n2.jpg'))
        self.b2_2.setIconSize(QtCore.QSize(150, 150))
        self.b2_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b2_2.clicked.connect(self.PlayClick)

        self.b3_2.setIcon(QtGui.QIcon('image/blusher/nars/n3.jpg'))
        self.b3_2.setIconSize(QtCore.QSize(150, 150))
        self.b3_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b3_2.clicked.connect(self.PlayClick)

        self.b4_2.setIcon(QtGui.QIcon('image/blusher/nars/n4.jpg'))
        self.b4_2.setIconSize(QtCore.QSize(150, 150))
        self.b4_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b4_2.clicked.connect(self.PlayClick)

        self.b5_2.setIcon(QtGui.QIcon('image/blusher/nars/n5.jpg'))
        self.b5_2.setIconSize(QtCore.QSize(150, 150))
        self.b5_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b5_2.clicked.connect(self.PlayClick)

        self.b6_2.setIcon(QtGui.QIcon('image/blusher/nars/n6.jpg'))
        self.b6_2.setIconSize(QtCore.QSize(150, 150))
        self.b6_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b6_2.clicked.connect(self.PlayClick)

        self.b7_2.setIcon(QtGui.QIcon('image/blusher/nars/n7.jpg'))
        self.b7_2.setIconSize(QtCore.QSize(150, 150))
        self.b7_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b7_2.clicked.connect(self.PlayClick)

        self.b8_2.setIcon(QtGui.QIcon('image/blusher/nars/n8.jpg'))
        self.b8_2.setIconSize(QtCore.QSize(150, 150))
        self.b8_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b8_2.clicked.connect(self.PlayClick)

        self.b9_2.setIcon(QtGui.QIcon('image/blusher/nars/n9.jpg'))
        self.b9_2.setIconSize(QtCore.QSize(150, 150))
        self.b9_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b9_2.clicked.connect(self.PlayClick)

        self.b10_2.setIcon(QtGui.QIcon('image/blusher/nars/n10.jpg'))
        self.b10_2.setIconSize(QtCore.QSize(150, 150))
        self.b10_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b10_2.clicked.connect(self.PlayClick)

        self.b11_2.setIcon(QtGui.QIcon('image/blusher/nars/n11.jpg'))
        self.b11_2.setIconSize(QtCore.QSize(150, 150))
        self.b11_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b11_2.clicked.connect(self.PlayClick)

        self.b12_2.setIcon(QtGui.QIcon('image/blusher/nars/n12.jpg'))
        self.b12_2.setIconSize(QtCore.QSize(150, 150))
        self.b12_2.setStyleSheet("QPushButton:pressed { border: 5px solid yellow }")
        self.b12_2.clicked.connect(self.PlayClick)

        self.returnButton.setIcon(QtGui.QIcon('image/return.png'))
        self.returnButton.setIconSize(QtCore.QSize(100, 100))
        self.cameraButton.setIcon(QtGui.QIcon('image/cameraicon.jpg'))
        self.cameraButton.setIconSize(QtCore.QSize(150, 150))

        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/emailDisabled.png'), QtGui.QIcon.Disabled)
        self.EmailButton.setIcon(emailIcon)
        self.EmailButton.setIconSize(QtCore.QSize(150, 150))
        self.tabWidget.setStyleSheet("""QTabWidget::pane { border: 0;}
                      QTabWidget>QWidget>QWidget{
                           background: rgb(20,20,20);
                           border-top-right-radius: 15px;
                           border-bottom-left-radius: 15px;
                           border-bottom-right-radius: 15px;
                           }
                      QTabBar::tab {width: 120px;}
                      QTabBar::tab:selected {
                           font-family: Agency FB;
                           font-size: 18px;
                           font: Bold;
                           color: rgb(0,0,0,255);
                           background: rgb(234,234,234,255);
                           border-top-left-radius: 8px;
                           border-top-right-radius: 8px;
                           padding: 20px 50px 20px 24px;}
                      QTabBar::tab:!selected{
                           font-family: Agency FB;
                           font-size: 18px;
                           font: Bold;
                           color: rgb(255,255,255,255);
                           background: rgb(175,175,175,255);
                           border-top-left-radius: 8px;
                           border-top-right-radius: 8px;
                           padding: 20px 50px 10px 24px;}""")

        self.shopButton.setIcon(QtGui.QIcon('image/shop.png'))
        self.shopButton.setIconSize(QtCore.QSize(130, 130))
        self.shopButton.clicked.connect(self.openShop)

        self.start_webcam()
    #구매페이지 url 연결
    def openShop(self):
        url='http://localhost'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    #버튼 효과음
    def PlayClick(self):
        QSound("sound/t1.wav").play()

    def enableEmailandCapture(self):
        # QPixmap.grabWidget(self.imgLabel).save('Image/captureImage_1.jpg', 'jpg')
        # 처음 저장은 1
        p = QPixmap.grabWidget(self.imgLabel)

        f = open("ImageNum.txt", 'r')
        data = f.read()
        f.close()

        if data == 1:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
        else:
            filename = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)
            p.save(filename, 'jpg')
            f = open("ImageNum.txt", 'w')
            data = int(data)
            data += 1
            newdata = str(data)
            f.write(newdata)
            f.close()

        #        p.save(filename, 'jpg')

        # 찰칵 소리 넣기
        self.EmailButton.setEnabled(True)
        emailIcon = QIcon()
        emailIcon.addPixmap(QPixmap('image/email.png'), QtGui.QIcon.Active)
        self.EmailButton.setIcon(emailIcon)

    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))
        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush1_start_webcam(self):
        self.colorName.setText(u":  MY MUSE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush1_update_frame)
        self.timer.start(0)

    def blush1_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush2_start_webcam(self):
        self.colorName.setText(u":  PEACH SLEEVE")
        self.colorName.setFont(QtGui.QFont('Agency FB ', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush2_update_frame)
        self.timer.start(0)

    def blush2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush3_start_webcam(self):
        self.colorName.setText(u":  VALENTINE PINK")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush3_update_frame)
        self.timer.start(0)

    def blush3_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush4_start_webcam(self):
        self.colorName.setText(u":  MAYBE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush4_update_frame)
        self.timer.start(0)

    def blush4_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush5_start_webcam(self):
        self.colorName.setText(u":  LOVE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush5_update_frame)
        self.timer.start(0)

    def blush5_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush6_start_webcam(self):
        self.colorName.setText(u":  SHY SHY")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush6_update_frame)
        self.timer.start(0)

    def blush6_update_frame(self):

        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush7_start_webcam(self):
        self.colorName.setText(u":  COTTON CANDY")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush7_update_frame)
        self.timer.start(0)

    def blush7_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush8_start_webcam(self):
        self.colorName.setText(u":  KIND & LOVE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush8_update_frame)
        self.timer.start(0)

    def blush8_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush9_start_webcam(self):
        self.colorName.setText(u":  UNDER THE STAR")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush9_update_frame)
        self.timer.start(0)

    def blush9_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush10_start_webcam(self):
        self.colorName.setText(u":  ORANGISH")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush10_update_frame)
        self.timer.start(0)

    def blush10_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)


    def blush11_start_webcam(self):
        self.colorName.setText(u":  UNDER THE STAR")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush11_update_frame)
        self.timer.start(0)

    def blush11_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush12_start_webcam(self):
        self.colorName.setText(u":  ORANGISH")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush12_update_frame)
        self.timer.start(0)

    def blush12_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,ce12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush1_2_start_webcam(self):
        self.colorName.setText(u":  AMORE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush1_2_update_frame)
        self.timer.start(0)

    def blush1_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush2_2_start_webcam(self):
        self.colorName.setText(u":  DEEP THROAT")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush2_2_update_frame)
        self.timer.start(0)

    def blush2_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush3_2_start_webcam(self):
        self.colorName.setText(u":  DESIRE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush3_2_update_frame)
        self.timer.start(0)

    def blush3_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush4_2_start_webcam(self):
        self.colorName.setText(u":  DOLCE VITA")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush4_2_update_frame)
        self.timer.start(0)

    def blush4_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush5_2_start_webcam(self):
        self.colorName.setText(u":  EXHIBIT A")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush5_2_update_frame)
        self.timer.start(0)

    def blush5_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n5)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush6_2_start_webcam(self):
        self.colorName.setText(u":  FINAL CUT")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush6_2_update_frame)
        self.timer.start(0)

    def blush6_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n6)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush7_2_start_webcam(self):
        self.colorName.setText(u":  LOVE")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush7_2_update_frame)
        self.timer.start(0)

    def blush7_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n7)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush8_2_start_webcam(self):
        self.colorName.setText(u":  ORGASM")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush8_2_update_frame)
        self.timer.start(0)

    def blush8_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n8)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush9_2_start_webcam(self):
        self.colorName.setText(u":  SEX APPEAL")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush9_2_update_frame)
        self.timer.start(0)

    def blush9_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n9)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush10_2_start_webcam(self):
        self.colorName.setText(u":  TAJ MAHAL")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush10_2_update_frame)
        self.timer.start(0)

    def blush10_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n10)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush11_2_start_webcam(self):
        self.colorName.setText(u":  SEX FANTASY")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush9_2_update_frame)
        self.timer.start(0)

    def blush11_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n11)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

    def blush12_2_start_webcam(self):
        self.colorName.setText(u":  SUPER ORGASM")
        self.colorName.setFont(QtGui.QFont('Agency FB', 50))
        self.colorName.setStyleSheet("QTextEdit {color:white;background-color: black; border: 1px solid black;}")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.blush10_2_update_frame)
        self.timer.start(0)

    def blush12_2_update_frame(self):
        ret, frame = self.capture.read()
        frame =blushcolorchange.blushchange(frame,n12)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

class MirrorDialog(QWidget):
    def __init__(self, parent=None):
        super(MirrorDialog, self).__init__(parent)
        loadUi('mirror_Widget.ui',self)
        self.imgLabel.move(490,0)
        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        self.b1.setIcon(QtGui.QIcon('image/plus2.png'))
        self.b1.setIconSize(QtCore.QSize(100, 100))
        self.b3.setIcon(QtGui.QIcon('image/again.png'))
        self.b3.setIconSize(QtCore.QSize(100, 100))

        self.start_webcam()


    def start_webcam(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1)

    def update_frame(self):
        ret, frame = self.capture.read()
        rows, cols = frame.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))
        # My webcam yields frames in BGR format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)


    def plus_start_webcam(self):

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1080)
        self.capture.set(4, 1920)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.plus_update_frame)
        self.timer.start(1)

    def plus_update_frame(self):
        ret, frame = self.capture.read()
        frame=mirrorplus.plus(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pix = QPixmap.fromImage(img)
        self.imgLabel.setPixmap(pix)

class captureDialog(QWidget):
    def __init__(self,parent=None):
        super(captureDialog, self).__init__(parent)
        loadUi('capture_Widget.ui',self)

        self.yesbutton =HoverButton(self)
        self.nobutton =HoverButton(self)
        self.yesbutton.move(1500, 110)
        self.nobutton.move(1500, 230)

        self.yesbutton.setIcon(QtGui.QIcon('image/send.png'))
        self.yesbutton.setIconSize(QtCore.QSize(271, 91))
        self.yesbutton.setStyleSheet(" border: 1px solid white")

        self.nobutton.setIcon(QtGui.QIcon('image/cancel.png'))
        self.nobutton.setIconSize(QtCore.QSize(271, 91))
        self.nobutton.setStyleSheet(" border: 1px solid white")

        f = open("ImageNum.txt", 'r')
        data = f.read()
        data=int(data)
        data-=1
        newdata=str(data)
        f.close()
        pix = QPixmap('C:\Apache24\htdocs\email/captureImage_%s.jpg' % (newdata,))
        self.imgLabel.setPixmap(pix)

        #pix = QPixmap('image/captureImage_%d.jpg' % (count,))
        #self.imgLabel.setPixmap(pix)

        self.EmailButton.setIcon(QtGui.QIcon('image/email.png'))
        self.EmailButton.setIconSize(QtCore.QSize(150, 150))
        self.emailEdit.setFont(QtGui.QFont('Agency FB', 36))
        self.comboBox.setFont(QtGui.QFont('Agency FB', 36))
        self.label.setFont(QtGui.QFont('Agency FB', 36))
        self.popupText.setFont(QtGui.QFont('Agency FB', 36))

        self.popupText.hide()
        self.yesbutton.clicked.connect(self.readEmail)
        self.yesbutton.clicked.connect(self.PlaySend)
        self.saveButton.clicked.connect(self.saveEmail)
        self.saveButton.setIcon(QtGui.QIcon('image/save.png'))
        self.saveButton.setIconSize(QtCore.QSize(150, 150))

    #재입력없이 불러오기 위해 이메일 저장
    def saveEmail(self):
        with open('getEmail.txt', 'r') as f:
            for line in f:
                x = line.index('@')
                a = line[:x]
                b = line[x + 1:]
                self.emailEdit.insertPlainText(a)
                index = self.comboBox.findText(b, QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.comboBox.setCurrentIndex(index)

    def PlaySend(self):
        QSound("sound/send.wav").play()
    #저장한 이메일 불러오기
    def readEmail(self):
        UserEmail1 = self.emailEdit.toPlainText()
        UserEmail2 = unicode(self.comboBox.currentText())
        self.popupText.show()
        with open('getEmail.txt', 'a') as f:
            f.truncate()
            f.write(UserEmail1+"@"+UserEmail2)
            imageemail2.sendEmail()
            # 불러와서 _부분 전 지우고 이메일으로 파일 이름 바꾸기
            folder = "C:\Apache24\htdocs\email/"
            FileList = os.listdir(folder)
            for files in FileList:
                if files.startswith("captureImage"):
                    NewName = files.replace("captureImage", UserEmail1+"@"+UserEmail2)
                    os.rename(os.path.join(folder, files), os.path.join(folder, NewName))

        #불러와서 _부분 전 지우고 이메일으로 파일 이름 바꾸기

class DrawDialog(QWidget):
    global drawRGB
    drawRGB = (0, 0, 0)
    def __init__(self, parent=None):
        super(DrawDialog, self).__init__(parent)
        loadUi('draw_Widget.ui',self)
        self.imgLabel.move(490, 50)
        self.gobackButton.setIcon(QtGui.QIcon('image/goback.png'))
        self.gobackButton.setIconSize(QtCore.QSize(100, 100))
        self.returnButton.setIcon(QtGui.QIcon('image/return.png'))
        self.returnButton.setIconSize(QtCore.QSize(100, 100))
        self.cameraButton.setIcon(QtGui.QIcon('image/cameraicon.jpg'))
        self.cameraButton.setIconSize(QtCore.QSize(150, 150))
        self.drawButton.setIcon(QtGui.QIcon('image/skt.jpg'))
        self.drawButton.setIconSize(QtCore.QSize(800, 600))
        self.folderButton.setIcon(QtGui.QIcon('image/forder.png'))
        self.folderButton.setIconSize(QtCore.QSize(100, 100))

        self.start_webcam()

    def start_webcam(self):

        frame=cv2.imread('image/jolie2.jpg')


    def draw_start_webcam(self):
        global img

        img= cv2.imread('image/jolie2.jpg')



        def interactive_drawing(event, x, y, flags, param):
            global ix, iy, drawing, mode

            cv2.namedWindow('zz')
            while (1):
                if event == cv2.EVENT_LBUTTONDOWN:
                    drawing = True
                    ix = x
                    iy = y
                if event == cv2.EVENT_RBUTTONDOWN:
                    drawing = False

                if event == cv2.EVENT_MOUSEMOVE:
                    if drawing == True:
                        cv2.circle(img, (x, y), 1, drawRGB, -1)
                elif event == cv2.EVENT_LBUTTONUP:
                    drawing = False
                    cv2.circle(img, (x, y), 1, drawRGB, -1)

                if (drawing == True):
                    cv2.line(img, (ix, iy), (x, y),drawRGB, 10)  # draw line between former and present pixel
                    ix = x  # save former x coordinate
                    iy = y  # save former y coordinate

                return x, y

        cv2.namedWindow('zz')
        cv2.setMouseCallback('zz', interactive_drawing)

        while (1):
            cv2.imshow('zz', img)
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            img2 = QImage(img2, img2.shape[1], img2.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img2)
            self.imgLabel.setPixmap(pix)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

    def draw_start_webcam11(self):

        app = drawtkinter.ExampleApp()
        app.mainloop()

    def openfile(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1000,800)
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")
        self.startFirstWindow()

    def startCaptureWindow(self):
        self.Window  =captureDialog(self)
        self.setWindowTitle("Cap Page")
        self.setCentralWidget(self.Window)

        self.Window.nobutton.clicked.connect(self.startFirstWindow)
        self.Window.popupText.clicked.connect(self.startFirstWindow)
        self.Window.nobutton.clicked.connect(self.PlayCancel)

        self.show()

    def startFirstWindow(self):
        self.Window = show_webcam()
        self.setWindowTitle("First Page")
        self.setCentralWidget(self.Window)
        self.Window.mirrorButton.clicked.connect(self.startsixthWindow)
        self.Window.LipsButton.clicked.connect(self.startSecondWindow)
        self.Window.EyesButton.clicked.connect(self.startThirdWindow)
        self.Window.BlingButton.clicked.connect(self.startForthWindow)
        self.Window.BlushButton.clicked.connect(self.startFifthWindow)


        #self.Window.DrawButton.clicked.connect(self.startsenventhWindow)
        self.Window.closeButton.clicked.connect(QCoreApplication.instance().quit)
        self.show()

    def PlayCancel(self):
        QSound("sound/cancel.wav").play()

    def PlayCamera(self):
        QSound("sound/camera_shutter.wav").play()

    def PlayEmail(self):
        QSound("sound/email.wav").play()

    def startSecondWindow(self):
      #  self.Window.capture.release()
        self.Window = LipsDialog(self)
        self.setWindowTitle("Second Page")
        self.setCentralWidget(self.Window)

        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.EmailButton.clicked.connect(self.startCaptureWindow)
        self.Window.EmailButton.clicked.connect(self.PlayEmail)

        self.Window.cameraButton.clicked.connect(self.Window.enableEmailandCapture)
        self.Window.cameraButton.clicked.connect(self.PlayCamera)

        self.Window.b1.clicked.connect(self.Window.lip1_start_webcam)
        self.Window.b2.clicked.connect(self.Window.lip2_start_webcam)
        self.Window.b3.clicked.connect(self.Window.lip3_start_webcam)
        self.Window.b4.clicked.connect(self.Window.lip4_start_webcam)
        self.Window.b5.clicked.connect(self.Window.lip5_start_webcam)
        self.Window.b6.clicked.connect(self.Window.lip6_start_webcam)
        self.Window.b7.clicked.connect(self.Window.lip7_start_webcam)
        self.Window.b8.clicked.connect(self.Window.lip8_start_webcam)
        self.Window.b9.clicked.connect(self.Window.lip9_start_webcam)
        self.Window.b10.clicked.connect(self.Window.lip10_start_webcam)
        self.Window.b11.clicked.connect(self.Window.lip11_start_webcam)
        self.Window.b12.clicked.connect(self.Window.lip12_start_webcam)

        self.Window.b1_2.clicked.connect(self.Window.lip1_2_start_webcam)
        self.Window.b2_2.clicked.connect(self.Window.lip2_2_start_webcam)
        self.Window.b3_2.clicked.connect(self.Window.lip3_2_start_webcam)
        self.Window.b4_2.clicked.connect(self.Window.lip4_2_start_webcam)
        self.Window.b5_2.clicked.connect(self.Window.lip5_2_start_webcam)
        self.Window.b6_2.clicked.connect(self.Window.lip6_2_start_webcam)
        self.Window.b7_2.clicked.connect(self.Window.lip7_2_start_webcam)
        self.Window.b8_2.clicked.connect(self.Window.lip8_2_start_webcam)
        self.Window.b9_2.clicked.connect(self.Window.lip9_2_start_webcam)
        self.Window.b10_2.clicked.connect(self.Window.lip10_2_start_webcam)
        self.Window.b11_2.clicked.connect(self.Window.lip11_2_start_webcam)
        self.Window.b12_2.clicked.connect(self.Window.lip12_2_start_webcam)

        self.Window.returnButton.clicked.connect(self.Window.start_webcam)

        self.show()


    def startThirdWindow(self):
        #self.Window.capture.release()
        self.Window = EyesDialog(self)
        self.setWindowTitle("Third Page")
        self.setCentralWidget(self.Window)
        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.cameraButton.clicked.connect(self.Window.enableEmailandCapture)
        self.Window.cameraButton.clicked.connect(self.PlayCamera)

        self.Window.EmailButton.clicked.connect(self.startCaptureWindow)
        self.Window.EmailButton.clicked.connect(self.PlayEmail)

        self.Window.b1.clicked.connect(self.Window.eye1_start_webcam)
        self.Window.b2.clicked.connect(self.Window.eye2_start_webcam)
        self.Window.b3.clicked.connect(self.Window.eye3_start_webcam)
        self.Window.b4.clicked.connect(self.Window.eye4_start_webcam)
        self.Window.b5.clicked.connect(self.Window.eye5_start_webcam)
        self.Window.b6.clicked.connect(self.Window.eye6_start_webcam)
        self.Window.b7.clicked.connect(self.Window.eye7_start_webcam)
        self.Window.b8.clicked.connect(self.Window.eye8_start_webcam)
        self.Window.b9.clicked.connect(self.Window.eye9_start_webcam)
        self.Window.b10.clicked.connect(self.Window.eye10_start_webcam)
        self.Window.b11.clicked.connect(self.Window.eye11_start_webcam)
        self.Window.b12.clicked.connect(self.Window.eye12_start_webcam)

        self.Window.b1_4.clicked.connect(self.Window.eye1_2_start_webcam)
        self.Window.b2_4.clicked.connect(self.Window.eye2_2_start_webcam)
        self.Window.b3_4.clicked.connect(self.Window.eye3_2_start_webcam)
        self.Window.b4_4.clicked.connect(self.Window.eye4_2_start_webcam)
        self.Window.b5_4.clicked.connect(self.Window.eye5_2_start_webcam)
        self.Window.b6_4.clicked.connect(self.Window.eye6_2_start_webcam)
        self.Window.b7_4.clicked.connect(self.Window.eye7_2_start_webcam)
        self.Window.b8_4.clicked.connect(self.Window.eye8_2_start_webcam)
        self.Window.b9_4.clicked.connect(self.Window.eye9_2_start_webcam)
        self.Window.b10_4.clicked.connect(self.Window.eye10_2_start_webcam)
        self.Window.b11_4.clicked.connect(self.Window.eye11_2_start_webcam)
        self.Window.b12_4.clicked.connect(self.Window.eye12_2_start_webcam)


        self.Window.returnButton.clicked.connect(self.Window.start_webcam)


        self.show()


    def startForthWindow(self):
        #self.Window.capture.release()
        self.Window = BlingDialog(self)
        self.setWindowTitle("Forth Page")
        self.setCentralWidget(self.Window)
        self.Window.cameraButton.clicked.connect(self.Window.enableEmailandCapture)
        self.Window.cameraButton.clicked.connect(self.PlayCamera)

        self.Window.EmailButton.clicked.connect(self.startCaptureWindow)
        self.Window.EmailButton.clicked.connect(self.PlayEmail)

        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.Button1.clicked.connect(self.Window.start_faceswap1)
        self.Window.Button2.clicked.connect(self.Window.start_faceswap2)
        self.Window.Button3.clicked.connect(self.Window.start_faceswap3)
        self.Window.Button4.clicked.connect(self.Window.start_faceswap4)
        self.Window.returnButton.clicked.connect(self.Window.start_webcam)


        self.show()

    def startFifthWindow(self):
        #self.Window.capture.release()
        self.Window = BlushDialog(self)
        self.setWindowTitle("Fifth Page")
        self.setCentralWidget(self.Window)
        self.Window.cameraButton.clicked.connect(self.Window.enableEmailandCapture)
        self.Window.cameraButton.clicked.connect(self.PlayCamera)

        self.Window.EmailButton.clicked.connect(self.startCaptureWindow)
        self.Window.EmailButton.clicked.connect(self.PlayEmail)

        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.b1.clicked.connect(self.Window.blush1_start_webcam)
        self.Window.b2.clicked.connect(self.Window.blush2_start_webcam)
        self.Window.b3.clicked.connect(self.Window.blush3_start_webcam)
        self.Window.b4.clicked.connect(self.Window.blush4_start_webcam)
        self.Window.b5.clicked.connect(self.Window.blush5_start_webcam)
        self.Window.b6.clicked.connect(self.Window.blush6_start_webcam)
        self.Window.b7.clicked.connect(self.Window.blush7_start_webcam)
        self.Window.b8.clicked.connect(self.Window.blush8_start_webcam)
        self.Window.b9.clicked.connect(self.Window.blush9_start_webcam)
        self.Window.b10.clicked.connect(self.Window.blush10_start_webcam)
        self.Window.b11.clicked.connect(self.Window.blush11_start_webcam)
        self.Window.b12.clicked.connect(self.Window.blush12_start_webcam)

        self.Window.b1_2.clicked.connect(self.Window.blush1_2_start_webcam)
        self.Window.b2_2.clicked.connect(self.Window.blush2_2_start_webcam)
        self.Window.b3_2.clicked.connect(self.Window.blush3_2_start_webcam)
        self.Window.b4_2.clicked.connect(self.Window.blush4_2_start_webcam)
        self.Window.b5_2.clicked.connect(self.Window.blush5_2_start_webcam)
        self.Window.b6_2.clicked.connect(self.Window.blush6_2_start_webcam)
        self.Window.b7_2.clicked.connect(self.Window.blush7_2_start_webcam)
        self.Window.b8_2.clicked.connect(self.Window.blush8_2_start_webcam)
        self.Window.b9_2.clicked.connect(self.Window.blush9_2_start_webcam)
        self.Window.b10_2.clicked.connect(self.Window.blush10_2_start_webcam)
        self.Window.b11_2.clicked.connect(self.Window.blush11_2_start_webcam)
        self.Window.b12_2.clicked.connect(self.Window.blush12_2_start_webcam)
        self.Window.returnButton.clicked.connect(self.Window.start_webcam)

        self.show()

    def startsixthWindow(self):
      #  self.Window.capture.release()
        self.Window = MirrorDialog(self)
        self.setWindowTitle("Sixth Page")
        self.setCentralWidget(self.Window)

        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.b1.clicked.connect(self.Window.plus_start_webcam)
        self.Window.b3.clicked.connect(self.Window.start_webcam)

    #self.Window.gobackButton.clicked.connect(self.startFirstWindow)
    def startsenventhWindow(self):
      #  self.Window.capture.release()
        self.Window =DrawDialog(self)
       # self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % color.name())
        self.setWindowTitle("Seventh Page")
        self.setCentralWidget(self.Window)
        self.Window.gobackButton.clicked.connect(self.startFirstWindow)
        self.Window.folderButton.clicked.connect(self.Window.openfile)
        self.Window.drawButton.clicked.connect(self.Window.draw_start_webcam11)



if __name__ =='__main__':

    app=QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('title!')
    window.show()

    sys.exit(app.exec_())
