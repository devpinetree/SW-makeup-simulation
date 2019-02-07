#-*- coding: utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

msg = MIMEMultipart()
msg['Subject'] = '<Snow White> 당신의 사진이 도착했어요'

me = "a01084668556@gmail.com"
you = open('getEmail.txt', 'r').read().strip()
#you = "snowwhitesmart@naver.com"

msg['From'] = me
msg['To'] = you
msg.preamble = '<Snow White> 당신의 사진이 도착했어요'


def sendEmail():
    f = open("ImageNum.txt", 'r')
    data = f.read()
    data = int(data)
    data -= 1
    newdata = str(data)
    f.close()
    ImgFileName = 'C:\Apache24\htdocs\email/captureImage_%s.jpg' % (data,)

    img_data = open(ImgFileName, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP_SSL('smtp.gmail.com',465)
    s.login("a01084668556@gmail.com", "rlatnfls00")
    s.sendmail(me, you, msg.as_string())
    s.quit()

