import cv2 as cv
import numpy as np


def big_image_binary_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("GRAY.jpg", gray)
    h, w = gray.shape[:2]
    h_step = w_step = 256
    for row in range(0, h, h_step):
        for col in range(0, w, w_step):
            roi = gray[row:row + h_step, col:col + w_step]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 20)
            gray[row:row + h_step, col:col + w_step] = dst
    cv.imwrite("RESULT.jpg", gray)


def new_big_image_binary_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    h_step = w_step = 128
    for row in range(0, h, h_step):
        for col in range(0, w, w_step):
            roi = gray[row:row + h_step, col:col + w_step]
            print(np.std(roi), np.mean(roi))
            if np.std(roi) < 10:
                gray[row:row + h_step, col:col + w_step] = np.mean(roi)
            else:
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row + h_step, col:col + w_step] = dst
    cv.imwrite("RESULT.jpg", gray)


src = cv.imread("team.jpg")
# cv.namedWindow("InputImage", cv.WINDOW_FREERATIO)
# cv.imshow("InputImage", src)
new_big_image_binary_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
