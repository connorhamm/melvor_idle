"""
Main issue:
- Miss clicks on food/armour due to the text box being different sizes based on the item
- Doesn't select good items w/ armour reduction
- Doesn't auto heal when health is too low

1. Find identifier for amour/food/etc. - nah, need to use icon
2. Can I move to location based on the image? Test this feature and implement if possible. - yes, feature work
3. Implement feature - Done
4. Add in database of all food/armour/etc?  If specific item not found select food?  Or select any item until a certain point?
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
        loc = np.where( result >= threshold)

        print("maxVal: " + str(maxVal))

        if maxVal > threshold:
            print("Threshold reached")
            return True, loc
        else:
            return False, 0

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
w1, h1 = wave_complete_template.shape[::-1]

you_died_template = img_template("you_died.png")
w2, h2 = you_died_template.shape[::-1]

# Counters
wave_complete_cnt = 0

# State Machine
while(1):
    edged_img = take_image(mon,False)

    wave_complete, loc = matchTemplate(wave_complete_template, edged_img, 0.9)
    if wave_complete == True:
        print("Event: Wave Complete")
        if wave_complete_cnt > 4:
            food_select()
            wave_complete_cnt = 0
        else:
            armour_select()
        wave_complete_cnt += 1
    
    you_died, loc = matchTemplate(you_died_template, edged_img, 0.9)
    if you_died == True:
        print("Event: You Died!")
        restart()