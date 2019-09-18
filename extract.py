import cv2
import numpy as np


def nothing(x):
    pass

def extract(img_in,s="result"):
    img = np.copy(img_in)
    res=np.copy(img_in)
    window = "orignal_image"
    result_window = "extracted_color"
    save_name="result"+s+".png"
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.namedWindow(result_window, cv2.WINDOW_NORMAL)

    uh = 'upper_h'
    us = 'upper_s'
    uv = 'upper_v'

    lh = 'lower_h'
    ls = "lower_s"
    lv = "lower_v"
    lower = np.uint8([[[0, 0, 0]]])
    high = np.uint8([[[0, 0, 0]]])

    cv2.createTrackbar(uh, window, 0, 179, nothing)
    cv2.createTrackbar(us, window, 0, 255, nothing)
    cv2.createTrackbar(uv, window, 0, 255, nothing)

    cv2.createTrackbar(lh, window, 0, 179, nothing)
    cv2.createTrackbar(ls, window, 0, 255, nothing)
    cv2.createTrackbar(lv, window, 0, 255, nothing)

    while (1):
        temp = img.copy()
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        if k ==ord('s'):
            print("done")
            cv2.imwrite(save_name,res)
            break
        uh = cv2.getTrackbarPos('upper_h', window)
        us = cv2.getTrackbarPos('upper_s', window)
        uv = cv2.getTrackbarPos('upper_v', window)

        lh = cv2.getTrackbarPos('lower_h', window)
        ls = cv2.getTrackbarPos('lower_s', window)
        lv = cv2.getTrackbarPos('lower_v', window)

        lower_color =np.array([lh,ls,lv])
        upper_color=np.array([uh,us, uv])
        lower=np.uint8([[[lh,ls,lv ]]])
        high=np.uint8([[[uh,us,uv ]]])
        print("BGR is ",cv2.cvtColor(lower, cv2.COLOR_HSV2BGR),cv2.cvtColor(high, cv2.COLOR_HSV2BGR))
        print("lower bound is{}: and higher bound is{} ".format(lower_color,upper_color))

        hsv = cv2.cvtColor(temp,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_color, upper_color)
        res = cv2.bitwise_and(temp, temp, mask=mask)

        cv2.imshow(window, img)
        cv2.imshow(result_window,res)
    print("BGR is ", cv2.cvtColor(lower, cv2.COLOR_HSV2BGR), cv2.cvtColor(high, cv2.COLOR_HSV2BGR))

def extract_no_show(img_in, s="result"):
    print(np.shape(img_in))
    temp = img_in.copy()
    print(np.shape(temp))
    save_name = "result" + s + ".png"

    uh = 179
    us = 255
    uv = 255

    lh = 0
    ls = 100
    lv = 106

    lower_color =np.array([lh,ls,lv])
    upper_color=np.array([uh,us, uv])
    lower=np.uint8([[[lh,ls,lv ]]])
    high=np.uint8([[[uh,us,uv ]]])
    print("BGR is ",cv2.cvtColor(lower, cv2.COLOR_HSV2BGR),cv2.cvtColor(high, cv2.COLOR_HSV2BGR))
    print("lower bound is{}: and higher bound is{} ".format(lower_color,upper_color))

    hsv = cv2.cvtColor(temp, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    res = cv2.bitwise_and(temp, temp, mask=mask)

    cv2.imwrite(save_name, res)


if __name__ == "__main__":
    #s="EB2"
    #s1=s+".tif"
    test_image = cv2.imread("img-5-b-1.png")
    img_in=np.copy(test_image)
    extract(img_in, "red")
    # remove white v<190

    # remove purple s=100, v=106