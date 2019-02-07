# OpenCV 라이브러리 임포트
import cv2
import numpy as np

img_color = cv2.imread('image/email.png', cv2.IMREAD_COLOR )
cv2.imshow( 'Landscape', img_color )

height, width, channel = img_color.shape  

out_img = np.zeros( (height,width), np.uint8 )

for y in range(0, height):  
    for x in range(0, width):  
        b = img_color[y,x,0]  
        g = img_color[y,x,1]  
        r = img_color[y,x,2]  
 
        gray = (int(b)+int(g)+int(r))/3.0
     	gray = gray -150

        if gray>255:  
            gray=255
        elif gray<0:
            gray=0
  
        out_img[y,x]=int(gray)

cv2.imshow('output', out_img)

# ESC 키 입력 시 Windows 닫음
cv2.waitKey(0)
cv2.destroyAllWindows()
