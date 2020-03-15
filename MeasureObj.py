import cv2 as cv
import numpy as np


def measure_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    print(ret)
    cv.imshow("binaryImage", binary)
    contours, hierachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print(contours)
    for i, contour in enumerate(contours):
        cv.drawContours(img, contours, i, (255, 0, 0), thickness=3)
        area = cv.contourArea(contour)
        print("Area: %s" % area)
        mm = cv.moments(contour)
        print(mm)
        x0 = int(mm["m10"] / mm["m00"])
        y0 = int(mm["m01"] / mm["m00"])
        cv.circle(img, (x0, y0), 2, (0, 0, 255), thickness=2)
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        approx_contour = cv.approxPolyDP(contour, 100, True)    #   轮廓逼近（一般运用于规则图形轮廓）
        print(approx_contour.shape)
    cv.imshow("outputImage", img)


src = cv.imread("number2.jpg")
cv.imshow("inputImage", src)
measure_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
