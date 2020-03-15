import cv2 as cv
import pytesseract as tess
from PIL import Image


def ocr_recog_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    binary = cv.bitwise_not(binary)
    cv.imshow("binary2", binary)
    textImage = Image.fromarray(img)
    text = tess.image_to_string(textImage, lang='chi_sim')
    print(text)


src = cv.imread("chirecog.png")
cv.imshow("src", src)
ocr_recog_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
