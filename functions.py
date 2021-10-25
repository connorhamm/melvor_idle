import cv2
import pyautogui
from mss import mss
from mss import tools
import time
import numpy as np
from datetime import datetime

def img_template(file):
    template = cv2.imread(file)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    return template

def take_image(monitor, screenshot):
    with mss() as sct:
        img = sct.grab(monitor)

        if screenshot == True:
            now = datetime.now() # current date and time
            time = now.strftime("%H-%M-%S")
            output = "./screenshots/" + str(time) + ".png"
            tools.to_png(img.rgb, img.size, output=output)
            print(output)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)
        return edged

def matchTemplate(img_template, edged, threshold):
        result = cv2.matchTemplate(edged, img_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        loc = np.where( result >= threshold)

        print("maxVal: " + str(maxVal))

        if maxVal > threshold:
            print("Threshold reached")
            return True, loc
        else:
            return False, 0

def matched_click(loc, w, h):
    x = loc[1][0] + w / 2
    y = loc[0][0] + h / 2
    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(10,10)
    time.sleep(1)