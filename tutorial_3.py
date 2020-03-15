import cv2 as cv
import numpy as np

def cameraopen():
    capture = cv.VideoCapture("第一条线.mp4")
    while True:
        ret, frame = capture.read()
        if ret == False:
            print("视频播放结束")
            break
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower = np.array([100,43,46])
        upper = np.array([124,255,255])
        dst = cv.inRange(hsv,lowerb=lower,upperb=upper)
        dst2 = cv.bitwise_and(frame, frame, mask=dst)
        cv.imshow("Video", frame)
        cv.imshow("Output", dst)
        cv.imshow("Output2", dst2)
        c = cv.waitKey(30)
        if c == 27:
            break

src = cv.imread("lena.png")
cv.namedWindow("Image", cv.WINDOW_AUTOSIZE)
cv.imshow("Image", src)
cameraopen()
cv.waitKey(0)
cv.destroyAllWindows()
