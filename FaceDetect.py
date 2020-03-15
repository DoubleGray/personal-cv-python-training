import cv2 as cv


def face_demo(img):
    face_detection = cv.CascadeClassifier(
        "D:/Program Files/opencv/opencv-3.4.2/build/etc/haarcascades/haarcascade_frontalface_alt2.xml")
    faces = face_detection.detectMultiScale(img, 1.1, 3)
    print(faces)
    for x, y, w, h in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow("detect_result", img)


def face_cam_demo():
    print("Opening...")
    capture = cv.VideoCapture(0)
    face_detector = cv.CascadeClassifier(
        "D:/Program Files/opencv/opencv-3.4.2/build/etc/haarcascades/haarcascade_smile.xml")
    print("Success!")
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.1, 4)
        print(faces)
        for x, y, w, h in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow("Video", frame)
        c = cv.waitKey(10)
        if c == 27:
            break


def body_detect_demo():
    print("Opening...")
    capture = cv.VideoCapture("vtest.avi")
    face_detector = cv.CascadeClassifier(
        "D:/Program Files/opencv/opencv-3.4.2/build/etc/haarcascades/haarcascade_fullbody.xml")
    print("Success!")
    while True:
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        #  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(frame, 1.1, 2, minSize=(25, 50), maxSize=(60, 120))
        print(faces)
        for x, y, w, h in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.imshow("Video", frame)
        c = cv.waitKey(10)
        if c == 27:
            break


src = cv.imread("IMG_4166.PNG")
cv.namedWindow("detect_result", cv.WINDOW_FREERATIO)
#   cv.imshow("detect_result", src)
#   face_demo(src)
#   face_cam_demo()
body_detect_demo()
cv.waitKey(0)
cv.destroyAllWindows()
