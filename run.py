"""
Main issue:
- Miss clicks on food/armour due to the text box being different sizes based on the item
- Doesn't select good items w/ damage reduction
- Doesn't auto heal when health is too low
- You want fast reaction time to health bar, so when running will need a seperate check, this feature will be added later

5. Add in a template for each category button, re-roll, armour, weapon, food
6. Add in a template for all DR equipment
7. Add in a template for all best weapons
8. Add in a template for all best food
9. Implement a new feature for checking on health percentage - pending
    - If bar falls below 60% then eat
"""

import cv2
import pyautogui
from mss import mss
from mss import tools
import time
import numpy as np
from datetime import datetime

# returns image template
def img_template(file):
    template = cv2.imread(file)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    return template

# returns image to run comparison for matchTemplate
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

# returns True/False if threshold is met
# returns location variable
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

################################ MAIN CODE #####################################

# Set monitor detection WxH and offsets
mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

# Set image template
armour_template = img_template("armour.png")
w1, h1 = armour_template.shape[::-1]

ok_template = img_template("ok.png")
w2, h2 = ok_template.shape[::-1]

food_template = img_template("food.png")
w3, h3, = food_template.shape[::-1]

# Counters
armour_cnt = 0

# State Machine
time.sleep(3)

while(1):
    edged_img = take_image(mon,False)

    armour, armour_loc = matchTemplate(armour_template, edged_img, 0.9)
    food, food_loc = matchTemplate(food_template, edged_img, 0.9)
    if armour == True and armour_cnt < 5:
        print("Event: Selecting Armour")
        matched_click(armour_loc, w1, h1)
        armour_cnt += 1
    elif armour == True and armour_cnt >= 5:
        print("Event: Selecting Food")
        matched_click(food_loc, w3, h3)
    
    # ok, loc = matchTemplate(ok_template, edged_img, 0.9)
    # if ok == True:
    #     print("Event: You Died!")
    #     print("Event: Clicking Restart")
    #     matched_click(loc, w1, h1)