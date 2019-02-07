import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_mcs_mouth.xml')

moustache_mask = cv2.imread('image/moustache4.png')
h_mask, w_mask = moustache_mask.shape[:2]

if mouth_cascade.empty():
    raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture(0)
scaling_factor = 0.5

def mousframe(frame):
    rows, cols = frame.shape[:2]
    translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
    img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

    rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
    img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

    translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
    frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))
    #    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.3, 50)

    if len(mouth_rects) > 0:
        (x, y, w, h) = mouth_rects[0]
        h, w = int(0.6 * h), int(1.2 * w)
        x -= int(0.05 * w)
        y -= int(0.55 * h)
        frame_roi = frame[y:y + h, x:x + w]
        moustache_mask_small = cv2.resize(moustache_mask, (w, h), interpolation=cv2.INTER_AREA)

        gray_mask = cv2.cvtColor(moustache_mask_small, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_mask, 50, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)
        masked_mouth = cv2.bitwise_and(moustache_mask_small, moustache_mask_small, mask=mask)
        masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
        frame[y:y + h, x:x + w] = cv2.add(masked_mouth, masked_frame)
        cv2.putText(frame, 'moustache frame', (300, 1000), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2.2, (255, 255, 255), 4)
        return frame

        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # ret, frame = cv2.threshold(frame, 100, 255, cv2.THRESH_BINARY_INV)

        #return frame
    else:
        return []