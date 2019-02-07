import cv2
import numpy as np


def cartoonize_image(img, ds_factor=4):
    rows, cols = img.shape[:2]
    translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
    img_t = cv2.warpAffine(img, translation_matrix, (2 * cols, 2 * rows))

    rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
    img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

    translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
    img = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)

    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    #    img_small = cv2.resize(img, None, fx=1.0/ds_factor, fy=1.0/ds_factor, interpolation=cv2.INTER_AREA)
    #    img_small = cv2.resize(img, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_AREA)
    num_repetitions = 10
    sigma_color = 5
    sigma_space = 7
    size = 5
    for i in range(num_repetitions):
        img = cv2.bilateralFilter(img, size, sigma_color, sigma_space)
    #        img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space)

    #    img_output = cv2.resize(img_small, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_LINEAR)
    #    img_output = cv2.resize(img_small, None, fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

    dst = np.zeros(img_gray.shape)
    #    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    dst = cv2.bitwise_and(img, img, mask=mask)

    return dst
