import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def back_projection_demo():
    sample = cv.imread("sample_green.png")
    target = cv.imread("WindowsLogo.jpg")
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    # h, s, v = cv.split(roi_hsv)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show images
    cv.imshow("sample", sample)
    cv.imshow("target", target)
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 179, 0, 255])
    cv.imshow("roiHist", roiHist)
    plt.imshow(roiHist, interpolation='nearest')
    plt.show()
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0, 180, 0, 256], 1)

    target_color = cv.bitwise_and(target, target, mask=dst)  # 采用bitwise_or也适用
    cv.imshow("target1", target)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [32, 32], [0, 180, 0, 256])
    # cv.imshow("hist2d", hist)
    plt.imshow(hist, interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()


def back_projection_demo_v2():
    target = cv.imread("lena.png")
    sample_width = 10
    sample_height = 10
    sample_x = 150
    sample_y = 420
    sample = target[sample_y:sample_y + sample_height, sample_x:sample_x + sample_width]
    # sample = np.zeros([sample_height, sample_width, 3], np.uint8)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)

    # show images
    cv.namedWindow("sample", cv.WINDOW_KEEPRATIO)
    cv.imshow("sample", sample)
    # cv.imshow("roi_hsv", roi_hsv)
    # cv.imshow("target_hsv", target_hsv)
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0.0, 180.0, 0.0, 256.0])
    cv.imshow("roiHist", roiHist)
    print(roiHist[:, 10])
    plt.imshow(roiHist, interpolation='nearest')
    plt.show()
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)

    dst = cv.calcBackProject([target_hsv], [0, 1], roiHist, [0.0, 180.0, 0.0, 256.0], 1)
    ret, dst = cv.threshold(dst, 0, 255, cv.THRESH_BINARY)
    print(ret)
    dst_hist = cv.calcHist([dst], [0], None, [256], [0, 256])
    print(dst_hist[255, 0])

    target_color = cv.bitwise_and(target, target, mask=dst)  # 采用bitwise_or也适用
    cv.imshow("target1", dst)
    cv.imshow("target_color", target_color)


print("--------- Hello Python ---------")
src = cv.imread("sample.png")
# hist2d_demo(src)
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
back_projection_demo_v2()
cv.waitKey(0)

cv.destroyAllWindows()
