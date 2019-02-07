import cv2
import numpy
import matplotlib

image = cv2.imread("12.jpg")
cols, rows=image.shape[:2]

b,g,r = cv2.split(image)       # get b,g,r
rgb_img = cv2.merge([r,g,b])
colrow=cols*rows
B=numpy.mean(b)
G=numpy.mean(g)
R=numpy.mean(r)

print (R,G,B)


