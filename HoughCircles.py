import cv2 as cv
import numpy as np


def HoughCircles_demo(img):
    src = cv.pyrMeanShiftFiltering(img, 5, 100)
    #  src = cv.medianBlur(src, 3)
    cv.imshow("removeNoise", src)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)
    edge = cv.Canny(gray, 50, 150)
    cv.imshow("EDGE", edge)
    circles = cv.HoughCircles(edge, cv.HOUGH_GRADIENT, 1, 30, param1=50, param2=20, minRadius=20, maxRadius=80)
    print(circles)
    for circle in circles:
        print(circle)
        for mcircle in circle:
            print(mcircle)
            x0, y0, r0 = mcircle[:]
            cv.circle(img, (x0, y0), r0, (0, 255, 0), thickness=5)
            cv.circle(img, (x0, y0), 2, (255, 0, 0), thickness=2)
    cv.imshow("outputImage", img)


def HoughCircles2_demo(img):
    src = cv.pyrMeanShiftFiltering(img, 5, 100)
    #  src = cv.medianBlur(src, 3)
    cv.imshow("removeNoise", src)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    cv.imshow("Gray", gray)
    edge = cv.Canny(gray, 50, 150)
    cv.imshow("EDGE", edge)
    circles = cv.HoughCircles(edge, cv.HOUGH_GRADIENT, 1, 30, param1=50, param2=20, minRadius=20, maxRadius=80)
    circles = np.uint16(circles)
    print(circles)
    for circle in circles[0]:
        print(circle)
        x0, y0, r0 = circle[:]
        cv.circle(img, (x0, y0), r0, (0, 255, 0), thickness=5)
        cv.circle(img, (x0, y0), 2, (255, 0, 0), thickness=2)
    cv.imshow("outputImage", img)


src = cv.imread("coins.jpg")
cv.imshow("inputImage", src)
HoughCircles2_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
