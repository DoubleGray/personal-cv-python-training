import cv2 as cv
import numpy as np

src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)

# gray = ["gray", "This is one", 'math', 0, 3, 3.12]
# print(gray[0:])
# gray[0] = 'gary'
# print(gray[0:])
# print(gray[1:2])

cv.waitKey(0)
cv.destroyAllWindows()
