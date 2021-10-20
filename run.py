"""
1. Setup function to make sure image correct food / armour / etc. is selected
"""

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

        # Take Screenshot for debugging purposes
        if screenshot == True:
            output = str(datetime.now())[:5:1]+ ".png"
            tools.to_png(img.rgb, img.size, output=output)
            print(output)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)
        return edged


def matchTemplate(img_template, edged, threshold):
        result = cv2.matchTemplate(edged, img_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        print("maxVal: " + str(maxVal))

        if maxVal > threshold:
            print("Threshold reached")
            return True  

def armour_select():
    print("Selecting Armour")
    pyautogui.moveTo(1000,625)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

def food_select():
    print("Selecting food")
    pyautogui.moveTo(1000,800)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1000,650)
    pyautogui.click()    

def restart():
    print("Restarting Game")
    pyautogui.moveTo(950,775)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(950,700)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(950,425)
    pyautogui.click()


################################ MAIN CODE #####################################
time.sleep(3)


# Set monitor detection WxH and offsets
mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

# Set image template
wave_complete_template = img_template("wave_complete.png")
you_died_template = img_template("you_died.png")

# Counters
wave_complete_cnt = 0

# State Machine

while(1):
    edged_img = take_image(mon,False)

    if matchTemplate(wave_complete_template, edged_img, 0.9) == True:
        print("Event: Wave Complete")
        if wave_complete_cnt > 4:
            food_select()
            wave_complete_cnt = 0
        else:
            armour_select()
        wave_complete_cnt += 1
    elif matchTemplate(you_died_template,edged_img,0.9) == True:
        print("Event: You Died!")
        restart()
