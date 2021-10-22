"""
TO DO

Main issue:
- Doesn't select good items w/ damage reduction
- Doesn't auto heal when health is too low, this what causes early deaths ()
- Doesn't select good weapon

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

Weapon
1. Take img of best weapons
2. Setup templates for best weapons
3. Use elif to select different weapons
- if not what you want, keep selecting weapon, else select nothing
- 1st part, available equipment up to lvl 69
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

        self.wave_complete_template = img_template("wave_complete.PNG")
        self.w7, self.h7 = self.wave_complete_template.shape[::-1]

        self.you_died_template = img_template("you_died.PNG")

        # Food
        self.angler_fish_template = img_template("./food/angler_fish.PNG")
        self.w_angler, self.h_angler = self.angler_fish_template.shape[::-1]

        self.apple_pie_template = img_template("./food/apple_pie.PNG")
        self.w_apple, self.h_apple = self.apple_pie_template.shape[::-1]

        self.beef_pie_template = img_template("./food/beef_pie.PNG")
        self.w_beef_pie, self.h_beef_pie = self.beef_pie_template.shape[::-1]

        self.carp_template = img_template("./food/carp.PNG")
        self.w_carp, self.h_carp = self.carp_template.shape[::-1]

        self.cave_fish_template = img_template("./food/cave_fish.PNG")
        self.w_cave, self.h_cave = self.cave_fish_template.shape[::-1]

        self.cherry_cupcake_template = img_template("./food/cherry_cupcake.PNG")
        self.w_cherry_cupcake, self.h_cherry_cupcake = self.cherry_cupcake_template.shape[::-1]

        self.fanfish_template = img_template("./food/fanfish.PNG")
        self.w_fanfish, self.h_fanfish = self.fanfish_template.shape[::-1]

        self.manta_ray_template = img_template("./food/manta_ray.PNG")
        self.w_manta_ray, self.h_manta_ray = self.manta_ray_template.shape[::-1]

        self.shark_template = img_template("./food/shark.PNG")
        self.w_shark, self.h_shark = self.shark_template.shape[::-1]

        self.strawberry_cake_template = img_template("./food/strawberry_cake.PNG")
        self.w_strawberry_cake, self.h_strawberry_cake = self.strawberry_cake_template.shape[::-1]

        self.swordfish_template = img_template("./food/swordfish.PNG")
        self.w_swordfish, self.h_swordfish = self.swordfish_template.shape[::-1]

        self.whale_template = img_template("./food/whale.PNG")
        self.w_whale, self.h_whale = self.whale_template.shape[::-1]

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
                start_raid, start_raid_loc = matchTemplate(self.start_raid_template, edged_img, 0.9)
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
                    self.armour_cnt = 0
                    self.queue()

    def equipment(self):
        print("State: Equipment Selection")
        armour, armour_loc = matchTemplate(self.armour_template, self.edged_img, 0.9)

        food, food_loc = matchTemplate(self.food_template, self.edged_img, 0.9)

        if (armour == True) and (self.armour_cnt < 3):
            print("Event: Selecting Armour")
            matched_click(armour_loc, self.w1, self.h1)
            time.sleep(1)
            self.armour()

        elif (self.armour_cnt >= 3) and (food == True):
            print("Event: Selecting Food")
            matched_click(food_loc, self.w3, self.h3)
            self.armour_cnt = -3
            time.sleep(1)
            self.food()

    def food(self):
        print("State: Food Selection")
        edged_img = take_image(self.mon,False)
        whale, whale_loc = matchTemplate(self.whale_template, edged_img, 0.6)
        strawberry, strawberry_loc = matchTemplate(self.strawberry_cake_template, edged_img, 0.6)
        manta_ray, manta_ray_loc = matchTemplate(self.manta_ray_template, edged_img, 0.6)
        cave_fish, cave_fish_loc = matchTemplate(self.cave_fish_template, edged_img, 0.6)
        apple_pie, apple_pie_loc = matchTemplate(self.apple_pie_template, edged_img, 0.6)
        shark, shark_loc = matchTemplate(self.shark_template, edged_img, 0.6)
        carp, carp_loc = matchTemplate(self.carp_template, edged_img, 0.6)
        beef_pie, beef_pie_loc = matchTemplate(self.beef_pie_template, edged_img, 0.6)
        fanfish, fanfish_loc = matchTemplate(self.fanfish_template, edged_img, 0.6)
        sword_fish, sword_fish_loc = matchTemplate(self.swordfish_template, edged_img, 0.6)
        angler, angler_loc = matchTemplate(self.angler_fish_template, edged_img, 0.6)
        cherry_cupcake, cherry_cupcake_loc = matchTemplate(self.cherry_cupcake_template, edged_img, 0.6)

        if whale == True:
            matched_click(whale_loc, self.w_whale, self.h_whale)
        elif manta_ray == True:
            matched_click(manta_ray_loc, self.w_manta_ray, self.h_manta_ray)
        elif strawberry == True:
            matched_click(strawberry_loc, self.w_strawberry_cake, self.h_strawberry_cake)
        elif beef_pie == True:
            matched_click(beef_pie_loc, self.w_beef_pie, self.h_beef_pie)
        elif cave_fish == True:
            matched_click(cave_fish_loc, self.w_cave, self.h_cave)
        elif apple_pie == True:
            matched_click(apple_pie_loc, self.w_apple, self.h_apple)
        elif shark == True:
            matched_click(shark_loc, self.w_shark, self.h_shark)
        elif carp == True:
            matched_click(carp_loc, self.w_carp, self.h_carp)
        elif fanfish == True:
            matched_click(fanfish_loc, self.w_fanfish, self.h_fanfish)
        elif sword_fish == True:
            matched_click(sword_fish_loc, self.w_swordfish, self.h_swordfish)
        elif angler == True:
            matched_click(angler_loc, self.w_angler, self.h_angler)
        elif cherry_cupcake == True:
            matched_click(cherry_cupcake_loc, self.w_cherry_cupcake, self.h_cherry_cupcake)        
        else:
            _, item_loc = matchTemplate(self.one_x_template, edged_img, 0.6)
            matched_click(item_loc, self.w4, self.h4)
        time.sleep(1)

    def armour(self):
        print("State: Armour Selection")
        edged_img = take_image(self.mon,False)
        item, item_loc = matchTemplate(self.one_x_template, edged_img, 0.5)
        matched_click(item_loc, self.w4, self.h4)
        self.armour_cnt += 1
        print(self.armour_cnt)
    
    def weapon(self):
        print("State: Weapon Selection")


################################ MAIN CODE #####################################

print("Slyturtle's Mevlor Idle Bot")
idle_bot()