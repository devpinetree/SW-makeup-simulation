import cv2
import numpy as np



##########
# Scaling
def plus(image):
    rows, cols = image.shape[:2]
    w = cv2.getTrackbarPos('W', 'image')
    translation_matrix = np.float32([[2.0, 0, int(0.5 * cols)], [0, 2.0, int(0.5 * rows)]])
    img_t = cv2.warpAffine(image, translation_matrix, (2 * cols, 2 * rows))

    rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
    img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

    translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
    image = cv2.warpAffine(img_r, translation_matrix, (rows, cols))


    return image