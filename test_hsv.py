import cv2
import numpy as np
from matplotlib import pyplot as plt


# Function documentation can be found in https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=createtrackbar

def nothing(x):
    pass


def createImg():

    return img


if __name__ == "__main__":
    # print a color manually
    green = np.uint8([[[78, 51, 150]]])
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    print ("hsv code is",hsv_green)

    img = np.zeros((200, 200, 3), dtype=np.uint8)
    #flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
    #print (flags)
    window = "hsv"

    h="h"
    s="s"
    v="v"

    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.createTrackbar(h, window, 0, 179, nothing)
    cv2.createTrackbar(s, window, 0, 255, nothing)
    cv2.createTrackbar(v, window, 0, 255, nothing)
    while (1):
        temp = img.copy()
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        h= cv2.getTrackbarPos('h', window)
        s = cv2.getTrackbarPos('s', window)
        v= cv2.getTrackbarPos('v', window)
        test_color=np.uint8([[[h, s, v]]])
        hsv_color = cv2.cvtColor(test_color, cv2.COLOR_HSV2BGR)

        B=np.int(hsv_color[0][0][0])
        G=np.int(hsv_color[0][0][1])
        R=np.int(hsv_color[0][0][2])
        #print("color is",B, G, R)
        cv2.circle(temp, (100, 100), 30, (B, G, R), 50)
        cv2.imshow(window, temp)
