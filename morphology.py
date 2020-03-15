import cv2 as cv
import numpy as np


def morphology(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(ret)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    erode = cv.morphologyEx(binary, cv.MORPH_ERODE, kernel=kernel)
    cv.imshow("erode", erode)
    dilate = cv.morphologyEx(binary, cv.MORPH_DILATE, kernel=kernel)
    cv.imshow("dilate", dilate)
    opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel=kernel)
    cv.imshow("open", opening)
    closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel=kernel)
    cv.imshow("close", closing)
    

src = cv.imread("numOCR.jpg")
cv.imshow("InputImage", src)
morphology(src)
cv.waitKey(0)
cv.destroyAllWindows()
