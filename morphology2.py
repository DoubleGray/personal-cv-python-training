import cv2 as cv
import numpy as np


def top_black_hat_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    # print(ret)
    cv.imshow("binary", gray)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    cv.imshow("tophat", top_hat)
    black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
    cv.imshow("blackhat", black_hat)


def gradient_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    gradient = cv.morphologyEx(binary, cv.MORPH_GRADIENT, kernel)
    cv.imshow("gradient", gradient)
    em = cv.dilate(binary, kernel)
    im = cv.erode(binary, kernel)
    external = cv.subtract(em, binary)
    internal = cv.subtract(binary, im)
    cv.imshow("external", external)
    cv.imshow("internal", internal)


src = cv.imread("LinuxLogo.jpg")
cv.imshow("InputImage", src)
gradient_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
