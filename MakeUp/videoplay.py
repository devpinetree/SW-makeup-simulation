import cv2
import numpy as np

cap = cv2.VideoCapture('media/EvilQueen.mp4')


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
def videoshow():

    while (cap):
        ret, frame = cap.read()
        if ret == True:
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            return frame
        # Break the loop
        else:
            return 0




