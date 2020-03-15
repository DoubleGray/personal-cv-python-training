import cv2 as cv


def add_image(m1, m2):
    add_image = cv.add(m1, m2)
    cv.imshow("add", add_image)


def sub_image(m1, m2):
    sub_image = cv.subtract(m1, m2)
    cv.imshow("sub", sub_image)


src1 = cv.imread("LinuxLogo.jpg")
src2 = cv.imread("WindowsLogo.jpg")
#  cv.namedWindow("Image",cv.WINDOW_AUTOSIZE)
cv.imshow("Image1", src1)
cv.imshow("Image2", src2)
add_image(src1,src2)
sub_image(src1,src2)
mean, dev = cv.meanStdDev(src1)
print(mean)
print(dev)
cv.waitKey(0)
cv.destroyAllWindows()
