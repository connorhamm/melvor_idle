"""
1. Add image of item selection
2. Verify image detection is working w/ correct threshold
3. Add in item selection functionality
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

def detection(monitor, img_template, threshold):
    with mss() as sct:
        img = sct.grab(monitor)

        # Take Screenshot for debugging
        # output = str(datetime.now()) + ".png"
        # tools.to_png(img.rgb, img.size, output=output)
        # print(output)

        img = np.array(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(gray, 50, 200)

        result = cv2.matchTemplate(edged, img_template, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        print("maxVal: " + str(maxVal))

        if maxVal > threshold:
            print("Threshold reached")
            return True  

def item_select():
    print("Selecting Item")

################################ MAIN CODE #####################################

# Set monitor detection WxH and offsets
mon = {'top': 180, 'left': 90, 'width': 930, 'height': 480}

# Set image template
test_template = img_template("Test.png")

# State Machine
if detection(mon,test_template,0.9) == True:
    print("Selecting an Item")
    item_select()
