import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascade_files/haarcascade_frontalface_alt.xml')

face_mask = cv2.imread('image/mask3.png')
h_mask, w_mask = face_mask.shape[:2]

if face_cascade.empty():
    raise IOError('Unable to load the face cascade classifier xml file')

cap = cv2.VideoCapture(0)
scaling_factor = 0.5


def facemask():
    ret, frame = cap.read()

    rows, cols = frame.shape[:2]
    w = cv2.getTrackbarPos('W', 'image')
    translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
    img_t = cv2.warpAffine(frame, translation_matrix, (2 * cols, 2 * rows))

    rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
    img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

    translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
    frame = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

    #    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(gray, 1.7, 3)
    for (x, y, w, h) in face_rects:
        if h > 0 and w > 0:
            x = int(x + 0.01 * w)
            y = int(y + 0.2 * h)
            w = int(0.9 * w)
            h = int(0.9 * h)

            frame_roi = frame[y:y + h, x:x + w]
            face_mask_small = cv2.resize(face_mask, (w, h), interpolation=cv2.INTER_AREA)

            gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_mask, 150, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)
            masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
            masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask=mask_inv)
            frame[y:y + h, x:x + w] = cv2.add(masked_face, masked_frame)
            return frame

