import cv2 as cv
import numpy as np


def fill_mask_demo():
    img = np.zeros([400, 400, 3], np.uint8)
    img[100:300, 100:300, :] = 255
    cv.imshow("binary_image", img)
    mask = np.ones([402, 402], np.uint8)
    mask[101:301, 101:301] = 0
    cv.imshow("mask_image", mask)
    cv.floodFill(img, mask, (200, 200), (126, 126, 126), cv.FLOODFILL_MASK_ONLY)
    #  cv.floodFill(img, mask, (200, 200), (0, 255, 0), (0, 30, 40), (10, 20, 25), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("filled", img)


def fill_demo(img):
    copyimg = img.copy()
    row, col = copyimg.shape[:2]
    mask = np.zeros([row + 2, col + 2], np.uint8)
    cv.floodFill(img, mask, (300, 300), (255, 0, 0), (100, 20, 10), (110, 130, 120), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("FilledImage", img)


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
fill_mask_demo()
cv.waitKey(0)
cv.destroyAllWindows()
