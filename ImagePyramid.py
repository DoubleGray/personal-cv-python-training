import cv2 as cv
import numpy as np


def image_pyramid(img):
    row, col, channel = img.shape[:]
    py_image = np.zeros([int(row / 2), int(col / 2), channel], np.uint8)
    for r in range(0, row, 2):
        for c in range(0, col, 2):
            for ch in range(0, channel, 1):
                py_image[int(r / 2), int(c / 2), ch] = img[r, c, ch]
    # cv.namedWindow("py", cv.WINDOW_FREERATIO)
    cv.imshow("py", py_image)


def pyramid(img):
    level = 3
    py_img = img.copy()
    list_py_img = []
    for i in range(level):
        list_py_img.append(py_img)
        dst = cv.pyrDown(py_img)
        up_dst = cv.pyrUp(dst)
        cv.imshow("py_img" + str(i + 1), dst)
        cv.imshow("up_img" + str(i + 1), up_dst)
        lpls = cv.subtract(py_img, up_dst)
        cv.imshow("lpls_img" + str(i + 1), lpls)
        py_img = dst.copy()
    list_py_img.append(py_img)
    return list_py_img


def lpls_pyramid(img):
    list_py_img = pyramid(img)
    for i in range(len(list_py_img) - 1, 0, -1):
        up_dst = cv.pyrUp(list_py_img[i])
        lpls = cv.subtract(list_py_img[i - 1], up_dst)
        cv.imshow("lpls2_img" + str(i), lpls)


src = cv.imread("lena.png")
cv.namedWindow("InputImage", cv.WINDOW_AUTOSIZE)
cv.imshow("InputImage", src)
pyramid(src)
cv.waitKey(0)
cv.destroyAllWindows()
