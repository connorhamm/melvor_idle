"""
Main issue:
- Doesn't select good items w/ damage reduction
- Doesn't select good healing items w/ high health recovery
- Doesn't auto heal when health is too low, this what causes early deaths ()
- Doesn't select good weapon

Select better healing items - complete today if its fun to do so
1.  Add template for items with 2x 0's in HP recovery. - pending screenshot
2.  test functionality - pending

Auto Heal - Step 1 - complete today if its fun to do so
1. Add template for wave complete / died / ok - pending new screenshot and monitor dimensions
2. Implement template to only move into equipment phase if wave complete template is detected - done
3. Test feature - pending

Auto Heal - Step 2 
1. Change picture position for health bar
2. Add template for target health missing
3. Test feature to ensure health missing is detected
4. Find location of where to click for healing
5. Add template for click to heal
6. Implement click to heal feature

DR Reduction
1. Look into method for being able to check if good item is already equipped
2. Create list of best in slot melee gear if best in slot is not available, select something else.
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

def matched_click(loc, w, h):
    x = loc[1][0] + w / 2
    y = loc[0][0] + h / 2
    pyautogui.moveTo(x,y)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(10,10)
    time.sleep(1)

#################### State Machine ############################
class idle_bot:
    def __init__(self):
        # Set monitor detection WxH and offsets
        self.mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

        # Set image template
        self.armour_template = img_template("armour.PNG")
        self.w1, self.h1 = self.armour_template.shape[::-1]

        self.ok_template = img_template("ok.PNG")
        self.w2, self.h2 = self.ok_template.shape[::-1]

        self.food_template = img_template("food.PNG")
        self.w3, self.h3 = self.food_template.shape[::-1]

        self.one_x_template = img_template("1x.PNG")
        self.w4, self.h4 = self.food_template.shape[::-1]

        self.start_raid_template = img_template("start_raid.PNG")
        self.w5, self.h5 = self.start_raid_template.shape[::-1]

        # self.good_food_template = img_template("good_food.PNG")
        # self.w6, self.h6 = self.good_food_template.shape[::-1]

        self.wave_complete_template = img_template("wave_complete.PNG")
        self.w7, self.h7 = self.wave_complete_template.shape[::-1]

        print("Init Complete")
        self.queue()

    def queue(self):
        print("In Queue")
        time.sleep(3)
        while(1):
            edged_img = take_image(self.mon,False)
            ok, loc = matchTemplate(self.ok_template, edged_img, 0.9)
            if ok == True:
                print("Event: Clicking OK")
                matched_click(loc, self.w1, self.h1)  
            else:
                start_raid, start_raid_loc = matchTemplate(self.start_raid_template, edged_img, 0.9)
                if start_raid == True:
                    print("Event: Starting Raid!")
                    matched_click(start_raid_loc, self.w5, self.h5)
                    self.combat()

    def combat(self):
        while(1):
            print("Auto-eat")
            edged_img = take_image(self.mon,False)


    def equipment(self):
        print("selecting equipment")

idle_bot()


################################ MAIN CODE #####################################




# # Set monitor detection WxH and offsets
# mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

# # Set image template
# armour_template = img_template("armour.PNG")
# w1, h1 = armour_template.shape[::-1]

# ok_template = img_template("ok.PNG")
# w2, h2 = ok_template.shape[::-1]

# food_template = img_template("food.PNG")
# w3, h3 = food_template.shape[::-1]

# one_x_template = img_template("1x.PNG")
# w4, h4 = food_template.shape[::-1]

# start_raid_template = img_template("start_raid.PNG")
# w5, h5 = start_raid_template.shape[::-1]

# good_food_template = img_template("good_food.PNG")
# w6, h6 = good_food_template.shape[::-1]

# wave_complete_template = img_template("wave_complete.PNG")
# w7, h7 = wave_complete_template.shape[::-1]

# # Counters
# armour_cnt = 0

# while(1):
#     wave_complete = False
#     edged_img = take_image(mon,False)

#     # Check if dead or in equipment state
#     wave_complete, _ = matchTemplate(wave_complete_template, edged_img, 0.9)
#     if wave_complete == True:
#         armour, armour_loc = matchTemplate(armour_template, edged_img, 0.9)
#         food, food_loc = matchTemplate(food_template, edged_img, 0.9)

#         if armour == True and armour_cnt < 5:
#             print("Event: Selecting Armour")
#             matched_click(armour_loc, w1, h1)
#             time.sleep(1)
#             edged_img = take_image(mon,False)
#             item, item_loc = matchTemplate(one_x_template, edged_img, 0.5)
#             matched_click(item_loc, w4, h4)
#             armour_cnt += 1

#         elif armour == True and armour_cnt >= 5:
#             print("Event: Selecting Food")
#             matched_click(food_loc, w3, h3)
#             time.sleep(1)
#             edged_img = take_image(mon,False)
#             item, item_loc = matchTemplate(good_food_template, edged_img, 0.5)
#             if item == True:
#                 matched_click(item_loc, w4, h4)
#             else:
#                 item, item_loc = matchTemplate(one_x_template, edged_img, 0.5)
#                 matched_click(item_loc, w6, h6)
#             armour = 0