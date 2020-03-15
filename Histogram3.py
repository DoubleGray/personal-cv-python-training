import cv2 as cv
import numpy as np


def newdemo(img):
    dst = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    newimg = cv.equalizeHist(dst)
    cv.imshow("dst", dst)
    cv.imshow("output", newimg)


src = cv.imread("1.jpg")
cv.namedWindow("InputImage", cv.WINDOW_AUTOSIZE)
cv.imshow("InputImage", src)
newdemo(src)
cv.waitKey(0)
cv.destroyAllWindows()