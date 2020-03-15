import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def disp_hist(img):
    color = ('red', 'green', 'blue')
    for i, color in enumerate(color):
        hist = cv.calcHist(img, [i], None, [256], [0, 255])
        plt.plot(hist, color=color)
        plt.xlim([0, 255])
    plt.show()


src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
disp_hist(src)
cv.waitKey(0)
cv.destroyAllWindows()


