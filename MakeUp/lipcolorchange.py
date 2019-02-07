import cv2
import dlib
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import numpy as np
cascade_path = "cascade_files/haarcascade_frontalface_alt.xml"
predictor_path= "shape_predictor_68_face_landmarks.dat"
faceCascade = cv2.CascadeClassifier(cascade_path)
predictor = dlib.shape_predictor(predictor_path)


def lipcolorstart(image,bgrcolor):

        point_x = []
        point_y = []
        points = []
        pos = []

        w = cv2.getTrackbarPos('W', 'image')

        rows, cols = image.shape[:2]
        translation_matrix = np.float32([[1, 0, int(0.5 * cols)], [0, 1, int(0.5 * rows)]])
        img_t = cv2.warpAffine(image, translation_matrix, (2 * cols, 2 * rows))

        rotation_matrix = cv2.getRotationMatrix2D((cols, rows), -90, 1)
        img_r = cv2.warpAffine(img_t, rotation_matrix, (2 * cols, 2 * rows))

        translation_matrix = np.float32([[1, 0, -int(cols - (0.5 * rows))], [0, 1, -int(rows - (0.5 * cols))]])
        image = cv2.warpAffine(img_r, translation_matrix, (rows, cols))

        kernel = np.ones((10, 10), np.uint8)

        pilimg = Image.new("RGBA", (rows, cols), "white")
        draw = ImageDraw.Draw(pilimg)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))

            detected_landmarks = predictor(image, dlib_rect).parts()

            landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])

            image_copy = image.copy()
            image_copy_copy = image.copy()
            for idx, point in enumerate(landmarks):

                pos = (point[0, 0], point[0, 1])
                if idx > 47 and idx < 80:
                    points.append(pos)
                    cv2.circle(image_copy_copy, pos, 3, color=(255, 0, 0))

                cv2.putText(image_copy, str(idx), pos,
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.4,
                            color=(0, 0, 255))

            draw.polygon((points), bgrcolor)
            pilimg = np.array(pilimg)

            bgr = cv2.cvtColor(pilimg, cv2.COLOR_RGB2BGR)

            mask_inv = cv2.bitwise_not(bgr)
            mask_inv = cv2.medianBlur(mask_inv, 5)
            mask_inv = cv2.GaussianBlur(mask_inv, (15, 15), 0)

            return cv2.addWeighted(mask_inv, float(100 - w) * 0.0015, image, float(w) * 0.0040, 0)
        else:
            return image
