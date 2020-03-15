import cv2 as cv
import numpy as np


def blur_demo(img):
    dst = cv.blur(img, (3, 3))
    cv.imshow("Blur Img", dst)


def median_blur_demo(img):
    dst = cv.medianBlur(img, 3)
    cv.imshow("median Img", dst)


def defined_blur_demo(img):
    # kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], np.float32)
    kernel = np.ones([3, 3], np.float32) / 9
    dst = cv.filter2D(img, -1, kernel)
    cv.imshow("def_blur Img", dst)


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
blur_demo(src)
median_blur_demo(src)
defined_blur_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
