import cv2 as cv
import numpy as np


def contours_detect_demo(img):
    dst = cv.pyrMeanShiftFiltering(img, 10, 100)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        print(i)
        print(contour)
        cv.drawContours(img, contours, i, (255, 0, 255), thickness=2)
    cv.imshow("result", img)


src = cv.imread("coins.jpg")
cv.imshow("inputImage", src)
contours_detect_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
