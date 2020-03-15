import cv2 as cv
import numpy as np


def match_demo():
    model = cv.imread("mark.png")
    search_img = cv.imread("img1.bmp")
    mh, mw = model.shape[:2]
    cv.imshow("search_img", search_img)
    result = cv.matchTemplate(search_img, model, cv.TM_CCOEFF_NORMED)
    cv.imshow("result", result)
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)
    print(maxVal)
    area_pt1 = maxLoc
    area_pt2 = (area_pt1[0] + mw, area_pt1[1] + mh)
    cv.rectangle(search_img, area_pt1, area_pt2, (0, 255, 0), thickness=2)
    cv.imshow("search_result", search_img)


def template_demo():
    tpl = cv.imread("mark.png")
    disp = cv.imread("img3.bmp")
    target = cv.imread("img3.bmp")
    cv.imshow("template image", tpl)
    cv.imshow("target image", target)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
            print(min_val)
        else:
            tl = max_loc
            print(max_val)
        br = (tl[0]+tw, tl[1]+th)
        cv.rectangle(disp, tl, br, (0, 0, 255), thickness=2)
        cv.imshow("match-"+np.str(md), disp)
        #cv.imshow("match-" + np.str(md), result)


print("---MatchTemplate---")
template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
