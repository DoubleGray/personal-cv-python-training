import cv2 as cv
import numpy as np


def HoughLines_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("grayImage", gray)
    edge = cv.Canny(gray, 50, 150)
    cv.imshow("edgeImage", edge)
    lines = cv.HoughLines(edge, 1, np.pi / 180, 250)
    print(lines)
    for line in lines:
        rho, theta = line[0]
        x0 = rho * np.cos(theta)
        y0 = rho * np.sin(theta)
        x1 = int(x0 + 1000 * np.sin(theta))
        y1 = int(y0 - 1000 * np.cos(theta))
        x2 = int(x0 - 1000 * np.sin(theta))
        y2 = int(y0 + 1000 * np.cos(theta))
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=1)
    cv.imshow("outputImage", img)


def HoughLinesP_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("grayImage", gray)
    edge = cv.Canny(gray, 50, 150)
    cv.imshow("edgeImage", edge)
    lines = cv.HoughLinesP(edge, 1, np.pi / 180, 100, minLineLength=30, maxLineGap=8)
    print(lines)
    for line in lines:
        x0, y0, x1, y1 = line[0, :]
        cv.line(img, (x0, y0), (x1, y1), (255, 255, 0))
    cv.imshow("OutputImage", img)


src = cv.imread("lines.png")
cv.imshow("InputImage", src)
HoughLinesP_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
