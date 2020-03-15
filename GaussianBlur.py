import cv2 as cv
import numpy as np


def guassianblur_demo(img):
    row, col, c = img.shape
    for r in range(row):
        for c in range(col):
            rn = np.random.normal(0, 20, 3)
            for i in range(0, 2, 1):
                img[r, c, i] = img[r, c, i] + rn[i]
    cv.imshow("demoGuassImage", img)
    return img


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
dst = cv.GaussianBlur(src, (0, 0), 5)
cv.imshow("Guassian Image", dst)
dst = guassianblur_demo(src)
dst2 = cv.GaussianBlur(dst, (0, 0), 5)
cv.imshow("Guassian Image2", dst2)
cv.waitKey(0)
cv.destroyAllWindows()
