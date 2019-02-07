import cv2
import numpy
import matplotlib

image = cv2.imread("mac/mac12.jpg")
cols, rows=image.shape[:2]


b,g,r = cv2.split(image)       # get b,g,r
rgb_img = cv2.merge([r,g,b])
colrow=cols*rows
B=int(numpy.mean(b))
G=int(numpy.mean(g))
R=int(numpy.mean(r))

print (R,G,B)

