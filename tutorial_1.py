import cv2 as cv
import numpy as np


def video_demo():
    # print("正在打开摄像头...")
    capture = cv.VideoCapture("第一条线.mp4")
    # print("摄像头打开成功")
    while True:
        ret, frame = capture.read()
        # frame = cv.flip(frame, 1)
        cv.namedWindow("video", cv.WINDOW_AUTOSIZE)
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:    # 27表键盘“ESC”键位
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


src = cv.imread("1.jpg")
cv.namedWindow("InputImage", cv.WINDOW_AUTOSIZE)
cv.imshow("InputImage", src)
video_demo()
#  get_image_info(src)
cv.waitKey(0)
cv.destroyAllWindows()
