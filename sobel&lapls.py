import cv2 as cv
import numpy as np


def sobel_demo(img):
    grad_x = cv.Sobel(img, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(img, cv.CV_32F, 0, 1)
    grad_x_convert = cv.convertScaleAbs(grad_x)
    grad_y_convert = cv.convertScaleAbs(grad_y)
    cv.imshow("grad_x", grad_x_convert)
    cv.imshow("grad_y", grad_y_convert)
    grad = cv.addWeighted(grad_x_convert, 0.5, grad_y_convert, 0.5, 0)
    cv.imshow("grad", grad)


def lapalian_demo(img):
    dst = cv.Laplacian(img, cv.CV_32F)
    cv.imshow("dst", dst)
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst = cv.filter2D(img, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", dst)


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_GUI_NORMAL)
cv.imshow("Image", src)
lapalian_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
