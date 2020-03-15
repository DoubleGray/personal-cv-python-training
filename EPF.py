import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 30, 15)
    cv.namedWindow("bi_demo", cv.WINDOW_GUI_NORMAL)
    cv.imshow("bi_demo", dst)
    #  cv.imwrite("D\:newpikaqiu.jpg",dst)



def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 180, 10)
    cv.namedWindow("shift_demo", cv.WINDOW_GUI_NORMAL)
    cv.imshow("shift_demo", dst)


src = cv.imread("1.jpg")
cv.namedWindow("Image", cv.WINDOW_GUI_NORMAL)
cv.imshow("Image", src)
bi_demo(src)
#  shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
