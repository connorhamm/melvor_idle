"""
TO DO

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

from functions import *
import time

class idle_bot:
    def __init__(self):
        print("State: Initialization")
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

        self.you_died_template = img_template("you_died.PNG")

        self.armour_cnt = 0

        self.queue()

    def queue(self):
        print("State: Queue")
        time.sleep(3)
        while(1):
            edged_img = take_image(self.mon,False)
            ok, loc = matchTemplate(self.ok_template, edged_img, 0.9)
            if ok == True:
                print("Event: Clicking OK")
                matched_click(loc, self.w1, self.h1)  
            else:
                start_raid, start_raid_loc = matchTemplate(self.start_raid_template, edged_img, 0.3)
                if start_raid == True:
                    print("Event: Starting Raid!")
                    matched_click(start_raid_loc, self.w5, self.h5)
                    self.combat()

    def combat(self):
        while(1):
            self.edged_img = take_image(self.mon,False)
            print("State: Combat")
            # Check for death, or in equipment state
            wave_complete, _ = matchTemplate(self.wave_complete_template, self.edged_img, 0.9)
            if wave_complete == True:
                self.equipment()
            else:
                you_died, _ = matchTemplate(self.you_died_template, self.edged_img, 0.9)
                if you_died == True:
                    print("Event: Death Detected")
                    self.queue()

    def equipment(self):
        print("State: Equipment Selection")
        armour, armour_loc = matchTemplate(self.armour_template, self.edged_img, 0.9)

        food, food_loc = matchTemplate(self.food_template, self.edged_img, 0.9)

        if armour == True and self.armour_cnt < 5:
            print("Event: Selecting Armour")
            matched_click(armour_loc, self.w1, self.h1)
            time.sleep(1)
            self.armour()

        elif armour == True and self.armour_cnt >= 5 and food == True:
            print("Event: Selecting Food")
            matched_click(food_loc, self.w3, self.h3)
            self.armour_cnt = 0
            time.sleep(1)
            self.food()

    def food(self):
        print("State: Food Selection")
        edged_img = take_image(self.mon,False)
        item, item_loc = matchTemplate(self.good_food_template, edged_img, 0.5)
        if item == True:
            matched_click(item_loc, self.w4, self.h4)
        else:
            item, item_loc = matchTemplate(self.one_x_template, edged_img, 0.5)
            matched_click(item_loc, self.w6, self.h6)

    def armour(self):
        print("State: Armour Selection")
        edged_img = take_image(self.mon,False)
        item, item_loc = matchTemplate(self.one_x_template, edged_img, 0.5)
        matched_click(item_loc, self.w4, self.h4)
        self.armour_cnt += 1
    
    def weapon(self):
        print("State: Weapon Selection")

    def restart(self):
        print("State: Restart")

################################ MAIN CODE #####################################

print("Slyturtle's Mevlor Idle Bot")
idle_bot()