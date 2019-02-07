import cv2
import numpy as np
import matplotlib

def lipcolorextraction(image):
   # image = cv2.imread('C:\image\ 1.png')
    cols, rows=image.shape[:2]

    b,g,r = cv2.split(image)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])
    colrow=cols*rows
    B=np.mean(b)
    G=np.mean(g)
    R=np.mean(r)

    return  (B,G,R)

