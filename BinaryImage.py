import cv2 as cv
import numpy as np


def threshold_func(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("GrayImage", gray)
    ret, dst = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print(ret)
    cv.imshow("Binary", dst)


def local_threshold_func(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("GrayImage", gray)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 41, 20)
    cv.imshow("Binary", dst)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 41, 5)
    cv.imshow("Binary2", dst)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 15)
    cv.imshow("Binary3", dst)


def custom_threshold_func(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("GrayImage", gray)
    h, w = gray.shape[:2]
    tmp = np.reshape(gray, [1, h * w])
    mean = tmp.sum() / (h * w)
    print(mean)
    ret, dst = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    print(ret)
    cv.imshow("customResult", dst)


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
custom_threshold_func(src)
cv.waitKey(0)
cv.destroyAllWindows()
