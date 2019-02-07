import numpy as np
import cv2
import dlib
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

points = []
points_l = []
eyebrow1 = []
eyebrow2 = []
mideyebrow = []

cascade_path = "cascade_files/haarcascade_frontalface_alt.xml"
predictor_path = "shape_predictor_68_face_landmarks.dat"
faceCascade = cv2.CascadeClassifier(cascade_path)
predictor = dlib.shape_predictor(predictor_path)
cam = cv2.VideoCapture(0)


def eyecolorstart(image, bgrcolor):
    point_x = []
    point_y = []
    points_l = []

    points = []
    pos = []
    posadd = []
    posladd = []
    ret_val, image = cam.read()
    rows, cols = image.shape[:2]
    w = cv2.getTrackbarPos('W', 'image')
    translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
    img_t = cv2.warpAffine(image, translation_matrix, (2 * cols, 2 * rows))

    rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
    img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

    translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
    image = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

    pilimg = Image.new("RGB", (rows, cols), "white")
    draw = ImageDraw.Draw(pilimg)

    # pilimg2 = Image.new("RGB", (cols, rows))
    # draw = ImageDraw.Draw(pilimg2)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    print("Found {0} faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        print dlib_rect

        detected_landmarks = predictor(image, dlib_rect).parts()

        landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])
        image_copy = image.copy()
        image_copy_copy = image.copy()

        for idx, point in enumerate(landmarks):
            pos = (point[0, 0], point[0, 1])
            posadd = (point[0, 0] - 7, point[0, 1])

            if idx == 36:
                points.append(posadd)
                cv2.circle(image_copy_copy, posadd, 3, color=(255, 0, 0))

            if idx > 36 and idx < 40:
                points.append(pos)
                cv2.circle(image_copy_copy, pos, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posadd = (point[0, 0], point[0, 1] - 5)

            if idx == 39:
                points.append(posadd)
                cv2.circle(image_copy_copy, posadd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posadd = (point[0, 0], point[0, 1] - 7)

            if idx == 38:
                points.append(posadd)
                cv2.circle(image_copy_copy, posadd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posadd = (point[0, 0], point[0, 1] - 10)

            if idx == 37:
                points.append(posadd)
                cv2.circle(image_copy_copy, posadd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posadd = (point[0, 0] - 5, point[0, 1] - 12)

            if idx == 36:
                points.append(posadd)
                cv2.circle(image_copy_copy, posadd, 3, color=(255, 0, 0))

        draw.polygon((points), bgrcolor)

        for idx, point in enumerate(landmarks):
            pos = (point[0, 0], point[0, 1])
            posladd = (point[0, 0] + 7, point[0, 1])

            if idx > 41 and idx < 45:
                points_l.append(pos)
                cv2.circle(image_copy_copy, pos, 3, color=(255, 0, 0))
            if idx == 45:
                points_l.append(posladd)
                cv2.circle(image_copy_copy, posladd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posladd = (point[0, 0] + 5, point[0, 1] - 12)

            if idx == 45:
                points_l.append(posladd)
                cv2.circle(image_copy_copy, posladd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posladd = (point[0, 0], point[0, 1] - 10)

            if idx == 44:
                points_l.append(posladd)
                cv2.circle(image_copy_copy, posladd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posladd = (point[0, 0], point[0, 1] - 7)

            if idx == 43:
                points_l.append(posladd)
                cv2.circle(image_copy_copy, posladd, 3, color=(255, 0, 0))

        for idx, point in enumerate(landmarks):
            posladd = (point[0, 0], point[0, 1] - 5)

            if idx == 42:
                points_l.append(posladd)
                cv2.circle(image_copy_copy, posladd, 3, color=(255, 0, 0))
        draw.polygon((points_l), bgrcolor)

        pilimg = np.array(pilimg)
        bgr = cv2.cvtColor(pilimg, cv2.COLOR_RGB2BGR)

        mask_inv = cv2.bitwise_not(bgr)
        mask_inv = cv2.medianBlur(mask_inv, 5)
        mask_inv = cv2.GaussianBlur(mask_inv, (15, 15), 0)

        return cv2.addWeighted(mask_inv, float(100 - w) * 0.0025, image, float(w) * 0.0034, 0)

    if cv2.waitKey(1) == 27:
        return image
