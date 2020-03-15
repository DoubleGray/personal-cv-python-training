import cv2 as cv


def not_image(image):
    not_image = cv.bitwise_not(image)
    cv.imshow("not_image", not_image)


def and_image(m1, m2):
    and_image = cv.bitwise_and(m1, m2)
    cv.imshow("and_image", and_image)


def or_image(m1, m2):
    or_image = cv.bitwise_or(m1, m2)
    cv.imshow("or_image", or_image)


src1 = cv.imread("LinuxLogo.jpg")
src2 = cv.imread("WindowsLogo.jpg")
#  cv.namedWindow("Image",cv.WINDOW_AUTOSIZE)
cv.imshow("Image1", src1)
cv.imshow("Image2", src2)
not_image(src1)
not_image(src2)
and_image(src1, src2)
or_image(src1, src2)
mean, dev = cv.meanStdDev(src1)
print(mean)
print(dev)
cv.waitKey(0)
cv.destroyAllWindows()
