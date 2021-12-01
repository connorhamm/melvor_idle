"""
TO DO:
1. Run bot & collect images for better DR gear overnight - Pending

Main issue:
- Doesn't auto heal when health is too low, this what causes early deaths ()
"""

from functions import *
import time

class idle_bot:
    def __init__(self):
        print("State: Initialization")
        # Set monitor detection WxH and offsets
        self.mon = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

        # Set image template
        self.armour_template = img_template("./states/armour.PNG")
        self.w_armour, self.h_armour = self.armour_template.shape[::-1]

        self.weapon_template = img_template("./states/weapon.PNG")
        self.w_weapon, self.h_weapon = self.weapon_template.shape[::-1]

<<<<<<< HEAD
        self.ok_template = img_template("ok.PNG")
=======
        self.ok_template = img_template("./states/ok.PNG")
>>>>>>> 75cedbbae8da165412ceb4ac08553d650af59d16
        self.w_ok, self.h_ok = self.ok_template.shape[::-1]

        self.food_template = img_template("./states/food.PNG")
        self.w_food, self.h_food = self.food_template.shape[::-1]

        self.one_x_template = img_template("./states/1x.PNG")
        self.w_one_x, self.h_one_x = self.food_template.shape[::-1]

        self.start_raid_template = img_template("./states/start_raid.PNG")
        self.w_start_raid, self.h_start_raid = self.start_raid_template.shape[::-1]

        self.wave_complete_template = img_template("./states/wave_complete.PNG")

        self.you_died_template = img_template("./states/you_died.PNG")

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

        # Weapons
        self.dragon_template = img_template("./weapon/dragon.PNG")
        self.w_dragon, self.h_dragon = self.dragon_template.shape[::-1]

        self.dragon_2h_template = img_template("./weapon/dragon_2h.PNG")
        self.w_dragon_2h, self.h_dragon_2h = self.dragon_2h_template.shape[::-1]

        # Armour
        self.dragon_g_template = img_template("./armour/dragon_g.PNG")
        self.w_dragon_g, self.h_dragon_g = self.dragon_g_template.shape[::-1]    
        
        self.rune_g_template = img_template("./armour/rune_g.PNG")
        self.w_rune_g, self.h_rune_g = self.rune_g_template.shape[::-1]  

        self.red_u_template = img_template("./armour/red_u.PNG")
        self.w_red_u, self.h_red_u = self.red_u_template.shape[::-1]  

        self.master_template = img_template("./armour/master.PNG")
        self.w_master, self.h_master = self.master_template.shape[::-1]  

        self.ragnar_template = img_template("./armour/ragnar.PNG")
        self.w_ragnar, self.h_ragnar = self.ragnar_template.shape[::-1]  

        self.glacia_template = img_template("./armour/glacia.PNG")
        self.w_glacia, self.h_glacia = self.glacia_template.shape[::-1]      

        # Misc.
        self.elite_amulet_template = img_template("./armour/elite_amulet.PNG")
        self.w_elite_amulet, self.h_elite_amulet = self.elite_amulet_template.shape[::-1]        

        self.foz_template = img_template("./armour/fury_of_zodiac.PNG")
        self.w_foz, self.h_foz = self.foz_template.shape[::-1] 

        self.infernal_cape_template = img_template("./armour/infernal_cape.PNG")
        self.w_infernal_cape, self.h_infernal_cape = self.infernal_cape_template.shape[::-1] 

        self.silver_neck_template = img_template("./armour/silver_neck.PNG")
        self.w_silver_neck, self.h_silver_neck = self.silver_neck_template.shape[::-1] 

        self.silver_ring_template = img_template("./armour/silver_ring.PNG")
        self.w_silver_ring, self.h_silver_ring = self.silver_ring_template.shape[::-1] 

        # Shield
        self.dragonfire_template = img_template("./armour/dragonfire.PNG")
        self.w_dragonfire, self.h_dragonfire = self.dragonfire_template.shape[::-1]         

        # Nothing
        self.nothing_template = img_template("./weapon/nothing.PNG")
        self.w_nothing, self.h_nothing = self.nothing_template.shape[::-1]   

        self.queue()

    def queue(self):
        print("State: Queue")
        self.wave_cnt = 0
        self.weapon_cnt = 0
        self.armour_cnt = 0
        self.food_cnt = 0
        self.death_cnt = 0

        time.sleep(3)
        
        ok = False
        start_raid = False

        while(start_raid == False):
            edged_img = take_image(self.mon,False)
            ok, loc = matchTemplate(self.ok_template, edged_img, 0.9)
            start_raid, start_raid_loc = matchTemplate(self.start_raid_template, edged_img, 0.9)

        if ok == True:
            print("Event: Clicking OK")
<<<<<<< HEAD
            matched_click(loc, self.w_ok, self.h_ok)
            time.sleep(1)
=======
            matched_click(loc, self.w_ok, self.h_ok)  
>>>>>>> 75cedbbae8da165412ceb4ac08553d650af59d16
        elif start_raid == True:
            print("Event: Starting Raid!")
            matched_click(start_raid_loc, self.w_start_raid, self.h_start_raid)
            self.combat()

    def combat(self):
        time.sleep(1)
        while(1):
            print("State: Combat")
            edged_img = take_image(self.mon,False)
            wave_complete, _ = matchTemplate(self.wave_complete_template, edged_img, 0.7)
            start_raid, _ = matchTemplate(self.start_raid_template, edged_img, 0.9)
            you_died, _ = matchTemplate(self.you_died_template, edged_img, 0.7)
            if wave_complete == True:
                self.wave_cnt += 1
                print("Event: Wave Completed - " + str(self.wave_cnt))
                self.equipment()
            elif start_raid == True:
                self.death_cnt += 1
                print("Event: Death - " + str(self.death_cnt))
                break
            elif you_died == True:
                self.death_cnt += 1
                print("Event: Death - " + str(self.death_cnt))
                break
        self.queue()

    def equipment(self):
        print("State: Equipment Selection")
        time.sleep(1)

        edged_img = take_image(self.mon,False)
        _, armour_loc = matchTemplate(self.armour_template, edged_img, 0.9)
        _, food_loc = matchTemplate(self.food_template, edged_img, 0.9)
        _, weapon_loc = matchTemplate(self.weapon_template, edged_img, 0.9)

        if (self.wave_cnt % 7 == 0):
            self.weapon_cnt += 1
            print("Event: Selecting Weapon - " + str(self.weapon_cnt))
            matched_click(weapon_loc, self.w_weapon, self.h_weapon)
            time.sleep(1)
            self.weapon()

        elif (self.wave_cnt % 5 == 0):
            self.food_cnt += 1
            print("Event: Selecting Food - " + str(self.food_cnt))
            matched_click(food_loc, self.w_food, self.h_food)
            time.sleep(1)
            self.food()
        
        else:
            self.armour_cnt += 1
            print("Event: Selecting Armour - " + str(self.armour_cnt))
            matched_click(armour_loc, self.w_armour, self.h_armour)
            time.sleep(1)
            self.armour()

    def food(self):
        print("State: Food Selection")
        time.sleep(1)

        edged_img = take_image(self.mon,False)

        whale, whale_loc = matchTemplate(self.whale_template, edged_img, 0.7)
        strawberry, strawberry_loc = matchTemplate(self.strawberry_cake_template, edged_img, 0.7)
        manta_ray, manta_ray_loc = matchTemplate(self.manta_ray_template, edged_img, 0.7)
        cave_fish, cave_fish_loc = matchTemplate(self.cave_fish_template, edged_img, 0.7)
        apple_pie, apple_pie_loc = matchTemplate(self.apple_pie_template, edged_img, 0.7)
        shark, shark_loc = matchTemplate(self.shark_template, edged_img, 0.7)
        carp, carp_loc = matchTemplate(self.carp_template, edged_img, 0.7)
        beef_pie, beef_pie_loc = matchTemplate(self.beef_pie_template, edged_img, 0.7)
        fanfish, fanfish_loc = matchTemplate(self.fanfish_template, edged_img, 0.7)
        sword_fish, sword_fish_loc = matchTemplate(self.swordfish_template, edged_img, 0.7)
        angler, angler_loc = matchTemplate(self.angler_fish_template, edged_img, 0.7)
        cherry_cupcake, cherry_cupcake_loc = matchTemplate(self.cherry_cupcake_template, edged_img, 0.7)

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
            matched_click(item_loc, self.w_one_x, self.h_one_x)

    def armour(self):
        print("State: Armour Selection")
        edged_img = take_image(self.mon,True)
        
        silver_ring, silver_ring_loc = matchTemplate(self.silver_ring_template, edged_img, 0.7)
        silver_neck, silver_neck_loc = matchTemplate(self.silver_neck_template, edged_img, 0.7)
        elite_amulet, elite_amulet_loc = matchTemplate(self.elite_amulet_template, edged_img, 0.7)
        foz, foz_loc = matchTemplate(self.foz_template, edged_img, 0.7)        
        infernal_cape, infernal_cape_loc = matchTemplate(self.infernal_cape_template, edged_img, 0.7)        
        dragonfire, dragonfire_loc = matchTemplate(self.dragonfire_template, edged_img, 0.7)
        dragon_g, dragon_g_loc = matchTemplate(self.dragon_g_template, edged_img, 0.83)
        rune_g, rune_g_loc = matchTemplate(self.rune_g_template, edged_img, 0.7)
        master, master_loc = matchTemplate(self.master_template, edged_img, 0.7)
        red_u, red_u_loc = matchTemplate(self.red_u_template, edged_img, 0.7)
        ragnar, ragnar_loc = matchTemplate(self.ragnar_template, edged_img, 0.7)
        glacia, glacia_loc = matchTemplate(self.glacia_template, edged_img, 0.7)
        _, nothing_loc = matchTemplate(self.nothing_template, edged_img, 0.6)

        if dragonfire == True:
            matched_click(dragonfire_loc, self.w_dragonfire, self.h_dragonfire)
        elif foz == True:
            matched_click(foz_loc, self.w_foz, self.h_foz)
        elif infernal_cape == True:
            matched_click(infernal_cape_loc, self.w_infernal_cape, self.h_infernal_cape)
        elif elite_amulet == True:
            matched_click(elite_amulet_loc, self.w_elite_amulet, self.h_elite_amulet)
        elif silver_ring == True:
            matched_click(silver_ring_loc, self.w_silver_ring, self.h_silver_ring)
        elif silver_neck == True:
            matched_click(silver_neck_loc, self.w_silver_neck, self.h_silver_neck)
        elif dragonfire == True:
            matched_click(dragonfire_loc, self.w_dragonfire, self.h_dragonfire)
        elif dragon_g == True and self.wave_cnt < 20:
            print("Event: Selecting Dragon (G) Gear")
            matched_click(dragon_g_loc, self.w_dragon_g, self.h_dragon_g)
        elif master == True and self.wave_cnt < 20:
            print("Event: Selecting Master Gear")
            matched_click(master_loc, self.w_master, self.h_master)
        elif rune_g == True and self.wave_cnt < 20:
            print("Event: Selecting Rune (G) Gear")
            matched_click(rune_g_loc, self.w_rune_g, self.h_rune_g)
        elif red_u == True and self.wave_cnt < 20:
            print("Event: Selecting Red (U) Gear")
            matched_click(red_u_loc, self.w_red_u, self.h_red_u)
        elif glacia == True and self.wave_cnt >= 20:
            print("Event: Selecting Glacia Gear")
            matched_click(glacia_loc, self.w_glacia, self.h_glacia)
        elif ragnar == True and self.wave_cnt >= 20:
            print("Event: Selecting Ragnar Gear")
            matched_click(ragnar_loc, self.w_ragnar, self.h_ragnar)
        elif self.wave_cnt < 10:
            _, item_loc = matchTemplate(self.one_x_template, edged_img, 0.6)
            matched_click(item_loc, self.w_one_x, self.h_one_x)
        else:
            matched_click(nothing_loc, self.w_nothing, self.h_nothing)
    
    def weapon(self):
        print("State: Weapon Selection")
        edged_img = take_image(self.mon,True)
        dragon, dragon_loc = matchTemplate(self.dragon_template, edged_img, 0.6)
        dragon_2h, _ = matchTemplate(self.dragon_2h_template, edged_img, 0.6)
        _, nothing_loc = matchTemplate(self.nothing_template, edged_img, 0.6)

        if dragon == True and dragon_2h == False:
            print("Event: Selecting Dragon Weapon")
            matched_click(dragon_loc, self.w_dragon, self.h_dragon)
        else:
            matched_click(nothing_loc, self.w_nothing, self.h_nothing)
        time.sleep(1)
                    
################################ MAIN CODE #####################################
print("Slyturtle's Mevlor Idle Bot")
idle_bot()