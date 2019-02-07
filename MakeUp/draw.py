import cv2
import numpy as np

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve


# mouse callback function
def interactive_drawing(event, x, y, flags, param):
    global ix, iy, drawing, mode
    cv2.namedWindow('zz')
    global img
    img=cv2.imread('image/jolie2.jpg')
    while (1):
        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
        if event == cv2.EVENT_RBUTTONDOWN:
            drawing = False

        if event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                if mode == True:
                    cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
                    print x, y
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            if mode == True:
                cv2.circle(img, (x, y), 1, (0, 0, 255), -1)
                # print x,y
                # cv2.line(img,(x,y),(x,y),(0,0,255),10)

        if (drawing == True):
            cv2.line(img, (ix, iy), (x, y), (0, 0, 255), 10)  # draw line between former and present pixel
            ix = x  # save former x coordinate
            iy = y  # save former y coordinate
        return x,y

def getimg():
    return img
