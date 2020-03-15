import cv2 as cv
import numpy as np


def access_pixel(image):
    print(image.shape)
    width = image.shape[0]
    height = image.shape[1]
    channels = image.shape[2]
    print("width: %s, height: %s, channels :%s" % (width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("OutputImage", image)





src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
t1 = cv.getTickCount()
access_pixel(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print("it takes %s s" % time)
cv.waitKey(0)
cv.destroyAllWindows()
