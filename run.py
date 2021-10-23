"""
TO DO

Main issue:
- Doesn't select good items w/ damage reduction
- Doesn't auto heal when health is too low, this what causes early deaths ()

Auto Heal - Step 2 
1. Change picture position for health bar
2. Add template for target health missing
3. Test feature to ensure health missing is detected
4. Find location of where to click for healing
5. Add template for click to heal
6. Implement click to heal feature

DR Reduction - complete core function today if its fun to do so
1. Test current template and comment out picture I haven't taken - pending

Weapon - complete core function today if its fun to do so
1. Test current template and comment out pictures I haven't taken - pending
2. Test w/ new pictures - pending

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

        self.weapon_template = img_template("weapon.PNG")
        self.w_weapon, self.h_weapon = self.weapon_template.shape[::-1]

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

        # Weapons < lvl 69 (rune, dragon, desert sabre)
        self.dragon_sword_template = img_template("./weapon/dragon_sword.PNG")
        self.w_dragon_sword, self.h_dragon_sword = self.dragon_sword_template.shape[::-1]        

        self.dragon_battleaxe_template = img_template("./weapon/dragon_battleaxe.PNG")
        self.w_dragon_battleaxe, self.h_dragon_battleaxe = self.dragon_battleaxe_template.shape[::-1]

        self.dragon_scim_template = img_template("./weapon/dragon_scim.PNG")
        self.w_dragon_scim, self.h_dragon_scim = self.dragon_scim_template.shape[::-1]

        self.dragon_claw_template = img_template("./weapon/dragon_claw.PNG")
        self.w_dragon_claw, self.h_dragon_claw = self.dragon_claw_template.shape[::-1]

        self.rune_sword_template = img_template("./weapon/rune_sword.PNG")
        self.w_rune_sword, self.h_rune_sword = self.rune_sword_template.shape[::-1]        

        self.rune_battleaxe_template = img_template("./weapon/rune_battleaxe.PNG")
        self.w_rune_battleaxe, self.h_rune_battleaxe = self.rune_battleaxe_template.shape[::-1]

        self.rune_scim_template = img_template("./weapon/rune_scim.PNG")
        self.w_rune_scim, self.h_rune_scim = self.rune_scim_template.shape[::-1]

        self.desert_sabre_template = img_template("./weapon/desert_sabre.PNG")
        self.w_desert_sabre, self.h_desert_sabre = self.desert_sabre_template.shape[::-1]

        self.miolite_sceptre_template = img_template("./weapon/miolite_sceptre.PNG")
        self.w_miolite_sceptre, self.h_miolite_sceptre = self.miolite_sceptre_template.shape[::-1]
 
        # Weapons > lvl 69 
        self.ancient_claw_template = img_template("./weapon/ancient_claw.PNG")
        self.w_ancient_claw, self.h_ancient_claw = self.ancient_claw_template.shape[::-1]

        # Armour < lvl 69
        self.armour1_template = img_template("./armour/armour1.PNG")
        self.w_armour1, self.h_armour1 = self.armour1_template.shape[::-1]        

        self.armour_cnt = 0
        self.weapon_cnt = 0
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
        weapon, weapon_loc = matchTemplate(self.weapon_template, self.edged_img, 0.9)

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

        elif (self.weapon_cnt >= 5) and (weapon == True):
            print("Event: Selecting Weapon")
            matched_click(weapon_loc, self.w_weapon, self.h_weapon)
            self.weapon_cnt = -3
            time.sleep(1)
            self.weapon()


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
        
        armour1, armour1_loc = matchTemplate(self.armour1_template, edged_img, 0.6)

        if armour1 == True:
            matched_click(armour1_loc, self.w_armour1, self.h_armour1)
        else:
            item, item_loc = matchTemplate(self.one_x_template, edged_img, 0.5)
            matched_click(item_loc, self.w4, self.h4)
        self.armour_cnt += 1
    
    def weapon(self):
        print("State: Weapon Selection")
        edged_img = take_image(self.mon,False)

        rune_sword, rune_sword_loc = matchTemplate(self.rune_sword_template, edged_img, 0.6)
        rune_battleaxe, rune_battleaxe_loc = matchTemplate(self.rune_battleaxe_template, edged_img, 0.6)
        rune_scim, rune_scim_loc = matchTemplate(self.rune_scim_template, edged_img, 0.6)
        dragon_sword, dragon_sword_loc = matchTemplate(self.dragon_sword_template, edged_img, 0.6)
        dragon_battleaxe, dragon_battleaxe_loc = matchTemplate(self.dragon_battleaxe_template, edged_img, 0.6)
        dragon_scim, dragon_scim_loc = matchTemplate(self.dragon_scim_template, edged_img, 0.6)
        dragon_claw, dragon_claw_loc = matchTemplate(self.dragon_claw_template, edged_img, 0.6)
        desert_sabre, desert_sabre_loc = matchTemplate(self.desert_sabre_template, edged_img, 0.6)
        miolite_sceptre, miolite_sceptre_loc = matchTemplate(self.miolite_sceptre_template, edged_img, 0.6)

        if dragon_claw == True:
            matched_click(dragon_claw_loc, self.w_dragon_claw, self.h_dragon_claw)
        elif dragon_sword == True:
            matched_click(dragon_sword_loc, self.w_dragon_sword, self.h_dragon_sword)
        elif dragon_scim == True:
            matched_click(dragon_scim_loc, self.w_dragon_scim, self.h_dragon_scim)
        elif dragon_battleaxe == True:
            matched_click(dragon_battleaxe_loc, self.w_dragon_battleaxe, self.h_dragon_battleaxe)
        elif miolite_sceptre == True:
            matched_click(miolite_sceptre_loc, self.w_miolite_sceptre, self.h_miolite_sceptre)
        elif desert_sabre == True:
            matched_click(desert_sabre_loc, self.w_desert_sabre, self.h_desert_sabre)
        elif rune_sword == True:
            matched_click(rune_sword_loc, self.w_rune_sword, self.h_rune_sword)
        elif rune_scim == True:
            matched_click(rune_scim_loc, self.w_rune_scim, self.h_rune_scim)
        elif rune_battleaxe == True:
            matched_click(rune_battleaxe_loc, self.w_rune_battleaxe, self.h_rune_battleaxe)
        else:
            _, item_loc = matchTemplate(self.one_x_template, edged_img, 0.6)
            matched_click(item_loc, self.w4, self.h4)
        self.weapon_cnt += 1
        time.sleep(1)
                    
################################ MAIN CODE #####################################

print("Slyturtle's Mevlor Idle Bot")
idle_bot()