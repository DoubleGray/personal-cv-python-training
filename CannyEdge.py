import cv2 as cv
import numpy as np


def Canny_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.namedWindow("GrayImage", cv.WINDOW_FREERATIO)
    cv.imshow("GrayImage", gray)
    edge = cv.Canny(gray, 60, 120)
    cv.namedWindow("CannyEdge", cv.WINDOW_FREERATIO)
    cv.imshow("CannyEdge", edge)


src = cv.imread("LinuxLogo.jpg")
print(src)
cv.namedWindow("InputImage", cv.WINDOW_FREERATIO)
cv.imshow("InputImage", src)
Canny_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
