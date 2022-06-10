init:
    transform left_to_right:
        yalign 0.63
        linear 60.0 xalign 1.0
        repeat
    transform zabarem:
        zoom 0.88
        yalign 1.0
        yoffset -190
    ######## face change transform ########
    define fc = Dissolve(.25)
    #######################################
    image ph = Placeholder("bg")
################## IMG DO EXPLO #############################
    layeredimage forest_dn:
        if dt < 5:
            "forest_day"
        else:
            "forest_night"
    layeredimage img_pokojlii:
        if dt == 1:
            "anim_room_lia_morning"
        if dt == 2:
            "anim_room_lia_noon"
        if dt == 3:
            "anim_room_lia_goldenhour"
        if dt == 4:
            "anim_room_lia_evening"
        if dt == 5:
            "anim_room_lia_nightlight"
        if dt >= 5:
            "anim_room_lia_night"

    layeredimage img_pokojlii_dragon:
        if dt == 1:
            "anim_room_lia_morningdragon"
        if dt == 2:
            "anim_room_lia_noondragon"
        if dt == 3:
            "anim_room_lia_goldenhourdragon"
        if dt == 4:
            "anim_room_lia_eveningdragon"
        if dt == 5:
            "anim_room_lia_nightdragonlight"
        if dt >= 5:
            "anim_room_lia_nightdragon"

    layeredimage img_pokojlii_dragon0:
        if dt == 1:
            "anim_room_lia_morningdragon"
        if dt == 2:
            "anim_room_lia_noondragon"
        if dt == 3:
            "anim_room_lia_goldenhourdragon"
        if dt == 4:
            "anim_room_lia_eveningdragon"
        if dt == 5:
            "anim_room_lia_nightdragonlight"
        if dt >= 5:
            "anim_room_lia_nightdragon"

    image img_tavern_hall:
        contains:
            "tavern_hall_bg0"
        contains:
            "tavern_hall_bathroom1_idle"
        contains:
            "tavern_hall_diningroom1_idle"
        contains:
            "tavern_hall_guestroom1_idle"
        contains:
            "tavern_hall_liaroom1_idle"
        contains:
            "tavern_hall_parentsroom1_idle"
        contains:
            "tavern_hall_stairs2_idle"

###### leftroom
    image img_tavern_leftroom:
        contains:
            "tavern_leftroom_dn_bg0"
        contains:
            "tavern_leftroom_mainroom1_dn_idle"
        contains:
            "tavern_leftroom_painting1_dn_idle"
        #contains:
        #    "tavern_leftroom_decorations1_idle"
        #contains:
        #    "tavern_leftroom_shields1_idle"
        #contains:
        #    "tavern_leftroom_bottle2_idle"
        #contains:
        #    "tavern_leftroom_aina3_idle"
        #contains:
        #    "tavern_leftroom_dude3_idle"
        #contains:
        #    "tavern_leftroom_lady3_idle"

    layeredimage tavern_leftroom_dn_bg0:
        if dt<5:
            "tavern_leftroom_bg0"
        if dt>=5:
            "tavern_leftroomnight_bg0"

    layeredimage tavern_leftroom_mainroom1_dn_idle:
        if dt < 5:
            "tavern_leftroom_mainroom1_idle"
        if dt >= 5:
            "tavern_leftroomnight_mainroom1_idle"
    layeredimage tavern_leftroom_mainroom1_dn_hover:
        if dt < 5:
            "tavern_leftroom_mainroom1_hover"
        if dt >= 5:
            "tavern_leftroomnight_mainroom1_hover"

    layeredimage tavern_leftroom_painting1_dn_idle:
        if dt < 5:
            "tavern_leftroom_painting1_idle"
        if dt >= 5:
            "tavern_leftroomnight_painting1_idle"
    layeredimage tavern_leftroom_painting1_dn_hover:
        if dt < 5:
            "tavern_leftroom_painting1_hover"
        if dt >= 5:
            "tavern_leftroomnight_painting1_hover"

    layeredimage tavern_leftroom_bottle2_dn_idle:
        if dt < 5:
            "tavern_leftroom_bottle2_idle"
        if dt >= 5:
            "tavern_leftroomnight_bottle2_idle"
    layeredimage tavern_leftroom_bottle2_dn_hover:
        if dt < 5:
            "tavern_leftroom_bottle2_hover"
        if dt >= 5:
            "tavern_leftroomnight_bottle2_hover"

    layeredimage tavern_leftroom_aina3_dn_idle:
        if dt < 5:
            "tavern_leftroom_aina3_idle"
        if dt >= 5:
            "tavern_leftroomnight_aina3_idle"
    layeredimage tavern_leftroom_aina3_dn_hover:
        if dt < 5:
            "tavern_leftroom_aina3_hover"
        if dt >= 5:
            "tavern_leftroomnight_aina3_hover"

    layeredimage tavern_leftroom_dude3_dn_idle:
        if dt < 5:
            "tavern_leftroom_dude3_idle"
        if dt >= 5:
            "tavern_leftroomnight_dude3_idle"
    layeredimage tavern_leftroom_dude3_dn_hover:
        if dt < 5:
            "tavern_leftroom_dude3_hover"
        if dt >= 5:
            "tavern_leftroomnight_dude3_hover"

    layeredimage tavern_leftroom_lady3_dn_idle:
        if dt < 5:
            "tavern_leftroom_lady3_idle"
        if dt >= 5:
            "tavern_leftroomnight_lady3_idle"
    layeredimage tavern_leftroom_lady3_dn_hover:
        if dt < 5:
            "tavern_leftroom_lady3_hover"
        if dt >= 5:
            "tavern_leftroomnight_lady3_hover"




###### rightroom
    layeredimage img_tavern_rightroom:
        if dt < 5:
            "tavern_rightroom_bg0"
###### mainroom

    image img_tavern_mainroom_day:
        contains:
            "tavern_main_bg0"
        contains:
            "tavern_main_leftroom1_idle"
        contains:
            "tavern_main_rightroom1_idle"
        contains:
            "tavern_main_kitchen1_idle"
        contains:
            "tavern_main_supplies2_idle"
        contains:
            "tavern_main_shelf1_idle"
        contains:
            "tavern_main_dekoracje1_idle"
        contains:
            "tavern_main_stairs2_idle"

        contains:
            "tavern_main_menu3_idle"
        contains:
            "tavern_main_bar3_idle"
        contains:
            "tavern_main_table4_idle"
        contains:
            "tavern_main_chandelier4_idle"
        contains:
            "tavern_main_beer4_idle"
    image img_tavern_mainroom_night:
        contains:
            "tavern_main_night_bg0"
        contains:
            "tavern_main_night_leftroom1_idle"
        contains:
            "tavern_main_night_rightroom1_idle"
        contains:
            "tavern_main_night_kitchen1_idle"
        contains:
            "tavern_main_night_stairs2_idle"
        contains:
            "tavern_main_night_bar3_idle"

    layeredimage img_tavern_mainroom_night_mess:
        always "img_tavern_mainroom_night"
        if z_tablemess:
            "tavern_main_night_tablemess5_idle"
        if z_floorflourmess:
            "tavern_main_night_floorflourmess5_idle"
        if z_floorwinemess:
            "tavern_main_night_floorwinemess5_idle"
        if z_barrightmess:
            "tavern_main_night_barrightmess5_idle"
        if z_barleftmess:
            "tavern_main_night_barleftmess5_idle"

####
    layeredimage img_tavern_mainroom:
        if dt>=5:
            "tavern_main_night_bg0"
        if dt<5:
            "tavern_main_bg0"

        if dt>=5:
            "tavern_main_night_leftroom1_idle"
        if dt<5:
            "tavern_main_leftroom1_idle"

        if dt>=5:
            "tavern_main_night_rightroom1_idle"
        if dt<5:
            "tavern_main_rightroom1_idle"

        if dt>=5:
            "tavern_main_night_kitchen1_idle"
        if dt<5:
            "tavern_main_kitchen1_idle"

        #if dt>=5:
        #    "tavern_main_dekoracje1_idle"
        if dt<5:
            "tavern_main_dekoracje1_idle"

        if dt>=5:
            "tavern_main_night_stairs2_idle"
        if dt<5:
            "tavern_main_stairs2_idle"

        #if dt>=5:
        #    "tavern_main_supplies2_idle"
        if dt<5:
            "tavern_main_supplies2_idle"

        #if dt>=5:
        #    "tavern_main_shelf1_idle"
        if dt<5:
            "tavern_main_shelf1_idle"

        #if dt>=5:
        #    "tavern_main_menu3_idle"
        if dt<5:
            "tavern_main_menu3_idle"

        if dt>=5:
            "tavern_main_night_bar3_idle"
        if dt<5:
            "tavern_main_bar3_idle"

        #if dt>=5:
        #    "tavern_main_table4_idle"
        if dt<5:
            "tavern_main_table4_idle"

        #if dt>=5:
        #    "tavern_main_chandelier4_idle"
        if dt<5:
            "tavern_main_chandelier4_idle"

        #if dt>=5:
        #    "tavern_main_beer4_idle"
        if dt<5:
            "tavern_main_beer4_idle"

        if dt>=5 and paczka01 == "oczekuje":
            "tavern_main_night_package5_idle"
        if dt<5 and paczka01 == "oczekuje":
            "tavern_main_package5_idle"

        if dt>=5 and z_tablemess:
            "tavern_main_night_tablemess5_idle"
        if dt<5 and z_tablemess:
            "tavern_main_tablemess5_idle"

        if dt>=5 and z_floorflourmess:
            "tavern_main_night_floorflourmess5_idle"
        if dt<5 and z_floorflourmess:
            "tavern_main_floorflourmess5_idle"

        if dt>=5 and z_floorwinemess:
            "tavern_main_night_floorwinemess5_idle"
        if dt<5 and z_floorwinemess:
            "tavern_main_floorwinemess5_idle"

        if dt>=5 and z_barrightmess:
            "tavern_main_night_barrightmess5_idle"
        if dt<5 and z_barrightmess:
            "tavern_main_barrightmess5_idle"

        if dt>=5 and z_barleftmess:
            "tavern_main_night_barleftmess5_idle"
        if dt<5 and z_barleftmess:
            "tavern_main_barleftmess5_idle"
###### mainroom elementy day-night do buttonów
    layeredimage tavern_main_bg0_dn:
        if dt<5:
            "tavern_main_bg0"
        if dt>=5:
            "tavern_main_night_bg0"

    layeredimage tavern_main_leftroom1_dn_idle:
        if dt < 5:
            "tavern_main_leftroom1_idle"
        if dt >= 5:
            "tavern_main_night_leftroom1_idle"
    layeredimage tavern_main_leftroom1_dn_hover:
        if dt < 5:
            "tavern_main_leftroom1_hover"
        if dt >= 5:
            "tavern_main_night_leftroom1_hover"

    layeredimage tavern_main_rightroom1_dn_idle:
        if dt>=5:
            "tavern_main_night_rightroom1_idle"
        if dt<5:
            "tavern_main_rightroom1_idle"
    layeredimage tavern_main_rightroom1_dn_hover:
        if dt>=5:
            "tavern_main_night_rightroom1_hover"
        if dt<5:
            "tavern_main_rightroom1_hover"

    layeredimage tavern_main_kitchen1_dn_idle:
        if dt>=5:
            "tavern_main_night_kitchen1_idle"
        if dt<5:
            "tavern_main_kitchen1_idle"
    layeredimage tavern_main_kitchen1_dn_hover:
        if dt>=5:
            "tavern_main_night_kitchen1_hover"
        if dt<5:
            "tavern_main_kitchen1_hover"

    layeredimage tavern_main_dekoracje1_dn_idle:
        if dt>=5:
            "tavern_main_dekoracje1_idle"
        if dt<5:
            "tavern_main_dekoracje1_idle"
    layeredimage tavern_main_dekoracje1_dn_hover:
        if dt>=5:
            "tavern_main_dekoracje1_hover"
        if dt<5:
            "tavern_main_dekoracje1_hover"

    layeredimage tavern_main_stairs2_dn_idle:
        if dt>=5:
            "tavern_main_night_stairs2_idle"
        if dt<5:
            "tavern_main_stairs2_idle"
    layeredimage tavern_main_stairs2_dn_hover:
        if dt>=5:
            "tavern_main_night_stairs2_hover"
        if dt<5:
            "tavern_main_stairs2_hover"

    layeredimage tavern_main_supplies2_dn_idle:
        if dt>=5:
            "tavern_main_supplies2_idle"
        if dt<5:
            "tavern_main_supplies2_idle"
    layeredimage tavern_main_supplies2_dn_hover:
        if dt>=5:
            "tavern_main_supplies2_hover"
        if dt<5:
            "tavern_main_supplies2_hover"

    layeredimage tavern_main_shelf1_dn_idle:
        if dt>=5:
            "tavern_main_shelf1_idle"
        if dt<5:
            "tavern_main_shelf1_idle"
    layeredimage tavern_main_shelf1_dn_hover:
        if dt>=5:
            "tavern_main_shelf1_hover"
        if dt<5:
            "tavern_main_shelf1_hover"

    layeredimage tavern_main_menu3_dn_idle:
        if dt>=5:
            "tavern_main_menu3_idle"
        if dt<5:
            "tavern_main_menu3_idle"
    layeredimage tavern_main_menu3_dn_hover:
        if dt>=5:
            "tavern_main_menu3_hover"
        if dt<5:
            "tavern_main_menu3_hover"

    layeredimage tavern_main_bar3_dn_idle:
        if dt>=5:
            "tavern_main_night_bar3_idle"
        if dt<5:
            "tavern_main_bar3_idle"
    layeredimage tavern_main_bar3_dn_hover:
        if dt>=5:
            "tavern_main_night_bar3_hover"
        if dt<5:
            "tavern_main_bar3_hover"

    layeredimage tavern_main_table4_dn_idle:
        if dt>=5:
            "tavern_main_table4_idle"
        if dt<5:
            "tavern_main_table4_idle"
    layeredimage tavern_main_table4_dn_hover:
        if dt>=5:
            "tavern_main_table4_hover"
        if dt<5:
            "tavern_main_table4_hover"

    layeredimage tavern_main_chandelier4_dn_idle:
        if dt>=5:
            "tavern_main_chandelier4_idle"
        if dt<5:
            "tavern_main_chandelier4_idle"
    layeredimage tavern_main_chandelier4_dn_hover:
        if dt>=5:
            "tavern_main_chandelier4_hover"
        if dt<5:
            "tavern_main_chandelier4_hover"

    layeredimage tavern_main_beer4_dn_idle:
        if dt>=5:
            "tavern_main_beer4_idle"
        if dt<5:
            "tavern_main_beer4_idle"
    layeredimage tavern_main_beer4_dn_hover:
        if dt>=5:
            "tavern_main_beer4_hover"
        if dt<5:
            "tavern_main_beer4_hover"

    layeredimage tavern_main_package5_dn_idle:
        if dt>=5:
            "tavern_main_night_package5_idle"
        if dt<5:
            "tavern_main_package5_idle"
    layeredimage tavern_main_package5_dn_hover:
        if dt>=5:
            "tavern_main_night_package5_hover"
        if dt<5:
            "tavern_main_package5_hover"

    layeredimage tavern_main_tablemess5_dn_idle:
        if dt>=5:
            "tavern_main_night_tablemess5_idle"
        if dt<5:
            "tavern_main_tablemess5_idle"
    layeredimage tavern_main_tablemess5_dn_hover:
        if dt>=5:
            "tavern_main_night_tablemess5_hover"
        if dt<5:
            "tavern_main_tablemess5_hover"

    layeredimage tavern_main_floorflourmess5_dn_idle:
        if dt>=5:
            "tavern_main_night_floorflourmess5_idle"
        if dt<5:
            "tavern_main_floorflourmess5_idle"
    layeredimage tavern_main_floorflourmess5_dn_hover:
        if dt>=5:
            "tavern_main_night_floorflourmess5_hover"
        if dt<5:
            "tavern_main_floorflourmess5_hover"

    layeredimage tavern_main_floorwinemess5_dn_idle:
        if dt>=5:
            "tavern_main_night_floorwinemess5_idle"
        if dt<5:
            "tavern_main_floorwinemess5_idle"
    layeredimage tavern_main_floorwinemess5_dn_hover:
        if dt>=5:
            "tavern_main_night_floorwinemess5_hover"
        if dt<5:
            "tavern_main_floorwinemess5_hover"

    layeredimage tavern_main_barrightmess5_dn_idle:
        if dt>=5:
            "tavern_main_night_barrightmess5_idle"
        if dt<5:
            "tavern_main_barrightmess5_idle"
    layeredimage tavern_main_barrightmess5_dn_hover:
        if dt>=5:
            "tavern_main_night_barrightmess5_hover"
        if dt<5:
            "tavern_main_barrightmess5_hover"

    layeredimage tavern_main_barleftmess5_dn_idle:
        if dt>=5:
            "tavern_main_night_barleftmess5_idle"
        if dt<5:
            "tavern_main_barleftmess5_idle"
    layeredimage tavern_main_barleftmess5_dn_hover:
        if dt>=5:
            "tavern_main_night_barleftmess5_hover"
        if dt<5:
            "tavern_main_barleftmess5_hover"


#### bar
    layeredimage tavern_main_bar_bg0_dn:
        if dt < 5:
            "tavern_main_bar_bg0"
        if dt >= 5:
            "tavern_main_night_bar_bg0"

    layeredimage tavern_main_bar_bar1_dn:
        if dt < 5:
            "tavern_main_bar_bar1"
        if dt >= 5:
            "tavern_main_night_bar_bar1"



##################################################################
########################### MONUMENT #############################
##################################################################


    image img_monument_morning:
        contains:
            "monument_morning_bg"
        contains:
            "monument_morning_firstplan"
    image img_monument_noon:
        contains:
            "monument_noon_bg"
        contains:
            "monument_noon_firstplan"
    image img_monument_afternoon:
        contains:
            "monument_afternoon_bg"
        contains:
            "monument_afternoon_firstplan"
    image img_monument_evening:
        contains:
            "monument_evening_bg"
        contains:
            "monument_evening_firstplan"
    image img_monument_night:
        contains:
            "monument_night_bg"
        contains:
            "monument_night_firstplan"

    layeredimage img_monument: # jest to wersja 4k, do użycia na fhd potrzebny zoom 0.5
        if dt == 1:
            "monument_morning_bg"
        if dt == 2:
            "monument_noon_bg"
        if dt == 3:
            "monument_afternoon_bg"
        if dt == 4:
            "monument_evening_bg"
        if dt >= 5:
            "monument_night_bg"
        if ee < 6:
            "anim_monument_dragon_bg"
        if dt == 1:
            "monument_morning_firstplan"
        if dt == 2:
            "monument_noon_firstplan"
        if dt == 3:
            "monument_afternoon_firstplan"
        if dt == 4:
            "monument_evening_firstplan"
        if dt >= 5:
            "monument_night_firstplan"
        #if dt >= 3:
        #    "anim_monument_fire"
        #if dt > 0:
        #    "monument_tablica_idle"
        #if ee < 6:
        #    "monument_dragon_firstplan"
    layeredimage img_monument_extras: # do scen
        #if dt >= 3:
        #    "anim_monument_fire"
        if dt > 0:
            "monument_tablica_idle"
        if ee < 6:
            "monument_dragon_firstplan"




    layeredimage img_monument_przejscie: #przygotowane żeby ładnie dissolve działał przy zmianie czasu # jest to wersja 4k, do użycia na fhd potrzebny zoom 0.5
        if dt == 2:
            "monument_morning_bg"
        if dt == 3:
            "monument_noon_bg"
        if dt == 4:
            "monument_afternoon_bg"
        if dt >= 5:
            "monument_evening_bg"
        if dt == 1:
            "monument_night_bg"
        if ee < 6:
            "monument_dragon_bg"
        if dt == 2:
            "monument_morning_firstplan"
        if dt == 3:
            "monument_noon_firstplan"
        if dt == 4:
            "monument_afternoon_firstplan"
        if dt >= 5:
            "monument_evening_firstplan"
        if dt == 1:
            "monument_night_firstplan"
        if dt >= 3:
            "anim_monument_fire"
        if dt > 0:
            "monument_tablica_idle"
        if ee < 6:
            "monument_dragon_firstplan"



    image tablica_blur = im.Blur("places/monument/tablica_blurowanie.png", 4.0)

    layeredimage monument_tablica_hover:
        if dt < 5:
            "monument_tablica_day_hover"
        if dt>= 5:
            "monument_tablica_night_hover"

    image monument_tablica_fhd_idle:
        contains:
            "monument_tablica_idle"
            zoom 0.5
    image monument_tablica_fhd_hover = LayeredImageProxy("monument_tablica_hover", Transform(zoom=0.5))

    image anim_monument_fire:
        contains:
            "anim_monument_fire3"
        contains:
            "anim_monument_fire2"
        contains:
            "anim_monument_fire1"
    image anim_monument_fire3:
        "monument_fire3"
        #align (.5,.5)
        alpha 0.96
        choice:
            linear .16
        choice:
            linear .12
        choice:
            linear .09
        choice:
            linear .05
        linear .2 alpha 0.65
        repeat
    image anim_monument_fire2:
        "monument_fire2"
        #align (.5,.5)
        alpha 0.88
        choice:
            linear .2
        choice:
            linear .12
        choice:
            linear .17
        choice:
            linear .05
        linear .2 alpha 0.55
        repeat
    image anim_monument_fire1:
        "monument_fire1"
        #align (.5,.5)
        alpha 0.82
        choice:
            linear .2
        choice:
            linear .12
        choice:
            linear .09
        choice:
            linear .05
        linear .2 alpha 0.58
        repeat


    image anim_monument_dragon_bg: # TODO do poprawy
        block:
            "monument_dragon_bg"
            zoom 1.1 align (.5,.5) pos (1.01,1.00)
            #choice:
            linear 3.0 pos (1.02,1.00)
            #choice:
            linear 3.0 pos (1.00,0.99)
            #choice:
            linear 3.0 pos (1.00,1.02)
            #choice:
            linear 3.0 pos (1.02,0.99)
            linear 5.0 pos (1.01,1.00)
            repeat

################################################################################
##############################    SECRET GARDEN    #############################
################################################################################

### SECRET GARDEN FULL
    layeredimage secretgarden_bg:
        if dt <5:
            "secretgarden_day0"
        else:
            "secretgarden_night0"

    layeredimage secretgarden_full_owocki_hover:
        if dt <5:
            "secretgarden_full_owocki_day_hover"
        else:
            "secretgarden_full_owocki_night_hover"

    layeredimage secretgarden_full_sus_hover:
        if dt <5:
            "secretgarden_full_sus_day_hover"
        else:
            "secretgarden_full_sus_night_hover"

    layeredimage secretgarden_full_terra_hover:
        if dt <5:
            "secretgarden_full_terra_day_hover"
        else:
            "secretgarden_full_terra_night_hover"

    layeredimage secretgarden_full_tree_hover:
        if dt <5:
            "secretgarden_full_tree_day_hover"
        else:
            "secretgarden_full_tree_night_hover"

    layeredimage secretgarden_full_water_hover:
        if dt <5:
            "secretgarden_full_water_day_hover"
        else:
            "secretgarden_full_water_night_hover"




### SECRET GARDEN 1
    layeredimage secretgarden1_bg:
        if dt <5:
            "secretgarden1_day0"
        else:
            "secretgarden1_night0"

    layeredimage secretgarden1_owocki_hover:
        if dt <5:
            "secretgarden1_day_owocki_hover"
        else:
            "secretgarden1_night_owocki_hover"
    layeredimage secretgarden1_tree_hover:
        if dt <5:
            "secretgarden1_day_tree_hover"
        else:
            "secretgarden1_night_tree_hover"
    layeredimage secretgarden1_water_hover:
        if dt <5:
            "secretgarden1_day_water_hover"
        else:
            "secretgarden1_night_water_hover"


### SECRET GARDEN 2
    layeredimage secretgarden2_bg:
        if dt <5:
            "secretgarden2_day0"
        else:
            "secretgarden2_night0"

    layeredimage secretgarden2_owocki_hover:
        if dt <5:
            "secretgarden2_day_owocki_hover"
        else:
            "secretgarden2_night_owocki_hover"

    layeredimage secretgarden2_tree_hover:
        if dt <5:
            "secretgarden2_day_tree_hover"
        else:
            "secretgarden2_night_tree_hover"

    layeredimage secretgarden2_sus_hover:
        if dt <5:
            "secretgarden2_day_sus_hover"
        else:
            "secretgarden2_night_sus_hover"

    layeredimage secretgarden2_terra_hover:
        if dt <5:
            "secretgarden2_day_terra_hover"
        else:
            "secretgarden2_night_terra_hover"



######################
######################
######################

    layeredimage town_smithy_dn_idle_nozoom:
        if dt < 5:
            "town_day_smithy_idle"
        if dt >= 5:
            "town_night_smithy_idle"
    layeredimage town_smithy_dn_hover_nozoom:
        if dt < 5:
            "town_day_smithy_hover"
        if dt >= 5:
            "town_night_smithy_hover"



    image town_smithy_dn_idle = LayeredImageProxy("town_smithy_dn_idle_nozoom", Transform(zoom=0.46875))
    image town_smithy_dn_hover = LayeredImageProxy("town_smithy_dn_hover_nozoom", Transform(zoom=0.46875))






############## animacje do mapy ############
    image drzewo_hover:
        "drzewo hover"
        0.15
        "drzewo hover obrot 2"
        0.15
        "drzewo hover obrot 4"
        0.15
        #"drzewo hover"
        repeat
    image wioska_hover:
        "wioska hover o0"
        0.15
        "wioska hover o2"
        0.15
        "wioska hover o4"
        0.15
        repeat
    image monument_hover:
        "monument hover o0"
        0.15
        "monument hover o2"
        0.15
        "monument hover o4"
        0.15
        repeat
    image tawerna_hover:
        "tawerna hover o0"
        0.15
        "tawerna hover o2"
        0.15
        "tawerna hover o4"
        0.15
        repeat

################## CG Zorn beat'em'up przy tawernie w ep6 ####################

    image zorncg_blur1 = im.Blur("cg/zorn angel/cg_zorn_helping_raven.png", 2.0)
    image zorncg_blur2 = im.Blur("cg/zorn angel/cg_zorn_helping_raven.png", 4.5)
    image zorncg_blur3 = im.Blur("cg/zorn angel/cg_zorn_helping_raven.png", 6.5)

    transform tr_beatupbyzorn:
        align (0.5,0.5) pos (0.5,0.5) zoom 1.06
        ease 3 zoom 1.08
        ease 3 zoom 1.06
        repeat

    image zorntheangel 1:
            "zorncg_blur3" with Dissolve(1.0)
            pause 1.5
            "zorncg_blur2" with Dissolve(1.0)
            pause 1.5
            repeat
    image zorntheangel 2:
            "zorncg_blur2" with Dissolve(1.0)
            pause 1.5
            "zorncg_blur1" with Dissolve(1.0)
            pause 1.5
            repeat
    image zorntheangel 3:
            "zorncg_blur1" with Dissolve(1.0)
            pause 1.5
            "cg_zorn_helping_raven" with Dissolve(1.0)
            pause 1.5
            repeat

    image anim_beatupblink:
        contains:
            "effect_blinkingpov_top"
            align (0.5,0.5)
            block:
                ease 3 ypos .12
                pause .2
                ease 3 ypos -0.05
                pause .5
                ease 2 ypos -0.1
                repeat
        contains:
            "effect_blinkingpov_bottom"
            align (0.5,0.5)
            block:
                ease 3 ypos .88
                pause .2
                ease 3 ypos 1.1
                pause .5
                ease 2 ypos 1.2
                repeat

    image anim_zorngonnabeatya:
        contains:
            "zorntheangel 1"
            align (0.5,0.5) pos (0.5,0.5) zoom 1.06
            ease 3 zoom 1.1
            ease 3 zoom 1.06
            repeat
        contains:
            "effect_blinkingpov_top"
            align (0.5,0.5)
            block:
                ease 3 ypos .12
                pause .2
                ease 3 ypos -0.05
                pause .5
                ease 2 ypos -0.1
                repeat
        contains:
            "effect_blinkingpov_bottom"
            align (0.5,0.5)
            block:
                ease 3 ypos .88
                pause .2
                ease 3 ypos 1.1
                pause .5
                ease 2 ypos 1.2
                repeat #nieużywane, zastąpione przez zmianę blurowanego zorna w tekscie i nalozenie blinkowania
            ### nieuzywane
################################################################################

################# animacje pylkow w pokoju Lii ############################
    $ t_pylk = 6 #czas wedrowania pylkow

    image anim_room_lia_morning_pylki:
        contains:
            "room_lia_morning_pylki"
            align (0.5,0.5)
            pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
        contains:
            "room_lia_morning_pylki"
            align (0.5,0.5) alpha 0
            linear t_pylk pos (.51,.49) alpha 1.0
            linear t_pylk pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
            repeat
        contains:
            "room_lia_morning_pylki"
            linear t_pylk*2 alpha 0
            block:
                align (0.5,0.5) alpha 0
                linear t_pylk pos (.51,.49) alpha 1.0
                linear t_pylk pos (.52,.49) alpha 0.8
                linear t_pylk pos (.53,.49) alpha 0.0
                linear t_pylk alpha 0.0
                repeat

    image anim_room_lia_noon_pylki:
        contains:
            "room_lia_noon_pylki"
            align (0.5,0.5)
            pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
        contains:
            "room_lia_noon_pylki"
            align (0.5,0.5) alpha 0
            linear t_pylk pos (.51,.49) alpha 1.0
            linear t_pylk pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
            repeat
        contains:
            "room_lia_noon_pylki"
            linear t_pylk*2 alpha 0
            block:
                align (0.5,0.5) alpha 0
                linear t_pylk pos (.51,.49) alpha 1.0
                linear t_pylk pos (.52,.49) alpha 0.8
                linear t_pylk pos (.53,.49) alpha 0.0
                linear t_pylk alpha 0.0
                repeat

    image anim_room_lia_ghandevening_pylki:
        contains:
            "room_lia_ghandevening_pylki"
            align (0.5,0.5)
            pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
        contains:
            "room_lia_ghandevening_pylki"
            align (0.5,0.5) alpha 0
            linear t_pylk pos (.51,.49) alpha 1.0
            linear t_pylk pos (.52,.49) alpha 0.8
            linear t_pylk pos (.53,.49) alpha 0.0
            linear t_pylk alpha 0.0
            repeat
        contains:
            "room_lia_ghandevening_pylki"
            linear t_pylk*2 alpha 0
            block:
                align (0.5,0.5) alpha 0
                linear t_pylk pos (.51,.49) alpha 1.0
                linear t_pylk pos (.52,.49) alpha 0.8
                linear t_pylk pos (.53,.49) alpha 0.0
                linear t_pylk alpha 0.0
                repeat

    image anim_room_lia_night_pylki:
        contains:
            "room_lia_night_pylki"
            align (0.5,0.5)
            pos (.52,.48) alpha 0.8
            linear t_pylk pos (.53,.47) alpha 0.0
            linear t_pylk alpha 0.0
        contains:
            "room_lia_night_pylki"
            align (0.5,0.5) alpha 0
            linear t_pylk pos (.51,.49) alpha 1.0
            linear t_pylk pos (.52,.48) alpha 0.5
            linear t_pylk pos (.53,.47) alpha 0.0
            linear t_pylk alpha 0.0
            repeat
        contains:
            "room_lia_night_pylki"
            linear t_pylk*2 alpha 0
            block:
                align (0.5,0.5) alpha 0
                linear t_pylk pos (.51,.49) alpha 1.0
                linear t_pylk pos (.52,.48) alpha 0.5
                linear t_pylk pos (.53,.47) alpha 0.0
                linear t_pylk alpha 0.0
                repeat

    image anim_room_lia_morning:
        contains:
            "room_lia_morning"
        contains:
            "anim_room_lia_morning_pylki"
            ypos 0.1
    image anim_room_lia_noon:
        contains:
            "room_lia_noon"
        contains:
            "anim_room_lia_noon_pylki"
            ypos 0.1
    image anim_room_lia_goldenhour:
        contains:
            "room_lia_goldenhour"
        contains:
            "anim_room_lia_ghandevening_pylki"
            ypos 0.1
    image anim_room_lia_evening:
        contains:
            "room_lia_evening"
        contains:
            "anim_room_lia_ghandevening_pylki"
            #ypos 0.1
    image anim_room_lia_night:
        contains:
            "room_lia_night"
        contains:
            "anim_room_lia_night_pylki"
            ypos 0.1
    image anim_room_lia_nightlight:
        contains:
            "room_lia_nightlight"
        contains:
            "anim_room_lia_night_pylki"
########## wersje ze smokiem #########
    image anim_room_lia_noondragon:
        contains:
            "room_lia_noondragon"
        contains:
            "anim_room_lia_noon_pylki"
            ypos 0.1
#    image anim_room_lia_eveningdragon:
#        contains:
#            "room_lia_eveningdragon"
#        contains:
#            "anim_room_lia_ghandevening_pylki"
#            ypos 0.1
    image anim_room_lia_nightdragon:
        contains:
            "room_lia_nightdragon"
        contains:
            "anim_room_lia_night_pylki"
            ypos 0.1
    image anim_room_lia_nightdragonlight:
        contains:
            "room_lia_nightdragonlight"
        contains:
            "anim_room_lia_night_pylki"


    image anim_room_lia: # a do gifa czy coś
        "room_lia_night" with Dissolve(1.0)
        2
        "room_lia_morning" with Dissolve(2.0)
        2
        "room_lia_noon" with Dissolve(2.0)
        2
        "room_lia_evening" with Dissolve(2.0)
        2
        "room_lia_goldenhour" with Dissolve(2.0)
        2
        "room_lia_nightlight" with Dissolve(2.0)
        2
        "room_lia_night" with Dissolve(2.0)

    image anim_room_lia_morningdragon:
        contains:
            "anim_room_lia_morning"
        contains:
            "dragonfestival_on"


    image anim_room_lia_goldenhourdragon:
        contains:
            "anim_room_lia_goldenhour"
        contains:
            "dragonfestival_on"

    image anim_room_lia_eveningdragon:
        contains:
            "anim_room_lia_evening"
        contains:
            "dragonfestival_on"

############## rzeczy do galerii ######################

    image anim_cg_tavern_wall: # do galerii
        contains:
            "tavern_door_lia_eyesclosed"
            align (0,0)
            linear 5 zoom 1.03
            "tavern_door_lia_eyesopened" with Dissolve(1.0)
            align (0,0) zoom 1.03
            linear 4 zoom 1.05
        contains:
            "tavern_door_lights1"
            linear 50 zoom 1.2
            pause 0.3
            linear 50 zoom 1.0
            repeat
        contains:
            "tavern_door_lights2"
            zoom 1.2 alpha 0.8
            block:
                linear 77 zoom 1.0 alpha 0.9
                pause 0.3
                linear 100 zoom 1.2 alpha 0.8
                repeat

######################## FESTIWAL ########################

    layeredimage img_festival_dn_dragon:
        if dt < 5:
            "anim_festival_day_dragon"
        if dt >= 5:
            "anim_festival_night_dragon"
    image anim_festivallights:
        contains:
            "festival_lights4"
            linear 1.7 alpha 0.8
            linear 2.0 alpha 1.0
            repeat
        contains:
            "festival_lights3"
            linear 0.8 alpha 0.7
            linear 0.8 alpha 1.0
            repeat
        contains:
            "festival_lights2"
            linear 0.5 alpha 0.6
            linear 1.5 alpha 1.0
            repeat
        contains:
            "festival_lights1"
            linear 1.2 alpha 0.5
            linear 1.2 alpha 1.0
            repeat
    image anim_hoomans:
        contains:
            "festival_hoomans1"
            choice:
                4
            choice:
                2
            choice:
                3
            ease 2 alpha 0.0
            choice:
                4
            choice:
                2
            choice:
                3
            ease 2 alpha 1.0
            repeat
        contains:
            "festival_hoomans2"
            choice:
                3.5
            choice:
                2.5
            choice:
                4.5
            ease 2 alpha 1.0
            choice:
                4
            choice:
                2
            choice:
                3
            ease 2 alpha 0.0
            repeat
        contains:
            "festival_hoomans3"
            choice:
                6
            choice:
                4
            choice:
                1
            ease 2 alpha 1.0
            choice:
                4
            choice:
                2
            choice:
                3
            ease 2 alpha 0.0
            repeat
        contains:
            "festival_hoomans4"
            alpha 0.0
            block:
                choice:
                    5
                choice:
                    4
                choice:
                    7
                ease 2 alpha 1.0
                choice:
                    4
                choice:
                    2
                choice:
                    3
                ease 2 alpha 0.0
                repeat
        contains:
            "festival_hoomans5"
            choice:
                8
            choice:
                4
            choice:
                3
            ease 2 alpha 0.0
            choice:
                4
            choice:
                2
            choice:
                3
            ease 2 alpha 1.0
            repeat
        contains:
            "festival_hoomans6"
            alpha 0.0
            block:
                choice:
                    6.5
                choice:
                    2.5
                choice:
                    3.5
                ease 2 alpha 0.0
                choice:
                    4
                choice:
                    2
                choice:
                    3
                ease 2 alpha 1.0
                repeat
    image anim_festival_night_dragon:
        contains:
            "festival_night_dragonsky"
        contains:
            "festival_dragon"
            align (.5,.5) pos (1.07,0.70)
            choice:
                linear 3.0 pos (1.08,0.70)
            choice:
                linear 3.0 pos (1.06,0.69)
            choice:
                linear 3.0 pos (1.06,0.72)
            choice:
                linear 3.0 pos (1.08,0.69)
            linear 5.0 pos (1.07,0.70)
            repeat
        contains:
            "festival_night_firstplannoppl"
        contains:
            "anim_hoomans"
        contains:
            "anim_festivallights"
    image anim_festival_day:
        contains:
            "festival_day_clearsky"
        contains:
            "festival_day_firstplannoppl_clear"
        contains:
            "anim_hoomans"
    image anim_festival_walking_shadows:
        contains:
            "angry_man1"
            align(.1,1.0)
            choice:
                xzoom -1.0
                linear 10.0 xalign 1.3
            choice:
                xzoom 1.0
                linear 10.0 xalign -0.3
            block:
                choice:
                    xalign -0.3 xzoom -1.0
                    linear 10.0 xalign 1.3
                choice:
                    xalign 1.3 xzoom 1.0
                    linear 10.0 xalign -0.3
                repeat
        contains:
            "blacksmith_shadow"
            align(-.3,1.0)
            choice:
                xzoom -1.0
                linear 10.0 xalign 1.5
            choice:
                xzoom 1.0
                linear 10.0 xalign -0.5
            block:
                choice:
                    xalign -0.5 xzoom -1.0
                    linear 15.0 xalign 1.5
                choice:
                    xalign 1.5 xzoom 1.0
                    linear 15.0 xalign -0.5
                repeat
        contains:
            "elf_shadow"
            align(1.5,1.0)
            choice:
                xzoom -1.0
                linear 13.0 xalign 1.3
            choice:
                xzoom 1.0
                linear 13.0 xalign -0.3
            block:
                choice:
                    xalign -0.3 xzoom -1.0
                    linear 13.0 xalign 1.3
                choice:
                    xalign 1.3 xzoom 1.0
                    linear 13.0 xalign -0.3
                repeat
        contains:
            "noble_lady"
            align(-.4,1.0)
            choice:
                xzoom -1.0
                linear 25.0 xalign 1.3
            choice:
                xzoom 1.0
                linear 25.0 xalign -0.3
            block:
                choice:
                    xalign -0.3 xzoom -1.0
                    linear 25.0 xalign 1.3
                choice:
                    xalign 1.3 xzoom 1.0
                    linear 25.0 xalign -0.3
                repeat
        contains:
            "old_lady"
            align(.9,1.0)
            choice:
                xzoom -1.0
                linear 20.0 xalign 1.5
            choice:
                xzoom 1.0
                linear 20.0 xalign -0.5
            block:
                choice:
                    xalign -0.5 xzoom -1.0
                    linear 20.0 xalign 1.5
                choice:
                    xalign 1.5 xzoom 1.0
                    linear 20.0 xalign -0.5
                repeat
    image anim_festival_day_dragon:
        contains:
            "festival_day_dragonsky"
        contains:
            "festival_dragon"
            align (.5,.5) pos (1.07,0.70)
            choice:
                linear 3.0 pos (1.08,0.70)
            choice:
                linear 3.0 pos (1.06,0.69)
            choice:
                linear 3.0 pos (1.06,0.72)
            choice:
                linear 3.0 pos (1.08,0.69)
            linear 5.0 pos (1.07,0.70)
            repeat
        contains:
            "festival_day_firstplannoppl"
        contains:
            "anim_hoomans"
        contains:
            "anim_festivallights"
##############################   TAWERNA    ####################################

########### Wnętrze Tawerny do epizodów ###########
    image ep_img_tavern_mainroom_nozoom:
        contains:
            "tavern_main_bg0"
        contains:
            "tavern_main_leftroom1_idle"
        contains:
            "tavern_main_rightroom1_idle"
        contains:
            "tavern_main_kitchen1_idle"
        contains:
            "tavern_main_shelf1_idle"
        contains:
            "tavern_main_dekoracje1_idle"
        contains:
            "tavern_main_stairs2_idle"
        contains:
            "tavern_main_supplies2_idle"
        contains:
            "tavern_main_menu3_idle"
        contains:
            "tavern_main_bar3_idle"
        #contains:
        #    "tavern_main_table4_idle"
        contains:
            "tavern_main_chandelier4_idle"
        contains:
            "tavern_main_beer4_idle"
    image ep_img_tavern_mainroom:
        contains:
            "ep_img_tavern_mainroom_nozoom"
            zoom 1.2
            align (.5,.5)


########### Buttony na zewnątrz tawerny do eksploracji ###########
    layeredimage tavern_outside_tent_hover:
        if dt >= 5:
            "tavern_outside_night_tent_hover"
        else:
            "tavern_outside_day_tent_hover"

    layeredimage tavern_outside_door_hover:
        if dt >= 5:
            "tavern_outside_night_door_hover"
        else:
            "tavern_outside_day_door_hover"

##### ELEMENTY DO ANIMACJI TAWERNY ##########
    image anim_tavern_birbs:
        "tavern_outside_birbs1" with Dissolve(0.2)
        zoom .75
        choice:
            .5
        choice:
            .3
        choice:
            .6
        choice:
            1.0
        "tavern_outside_birbs2" with Dissolve(0.2)
        zoom .75
        choice:
            .3
        choice:
            .6
        choice:
            .5
        choice:
            1.0
        repeat
    image anim_tavern_outside_smokenight:
        contains:
            VBox ("tavern_outside_smokenight","tavern_outside_smokenight")
            ypos 0.1 alpha .8
            linear 40 alpha 0.4 ypos -0.5
            repeat
        contains:
            "tavern_outside_smokenight"
            xzoom -0.8 xoffset 60 ypos 0.5 alpha .8
            linear 30 alpha 0.4 ypos -0.5
            repeat
        contains:
            "tavern_outside_smokenight"
            linear 2 alpha .6
            linear 2 alpha 0.9
            repeat
    image anim_tavern_outside_smoke:
        contains:
            VBox ("tavern_outside_smoke","tavern_outside_smoke")
            ypos 0.3 alpha .8
            linear 40 alpha 0.4 ypos -0.5
            repeat
        contains:
            "tavern_outside_smoke"
            xzoom -0.8 xoffset 60 ypos 0.5 alpha .8
            linear 30 alpha 0.4 ypos -0.5
            repeat
        contains:
            "tavern_outside_smoke"
            linear 2 alpha .6
            linear 2 alpha 0.9
            repeat

##### ANIMACJA TAWERNY DZIENNA ##########

    image anim_tavern outside:
        contains:
            "tavern_outside_day"
            zoom 0.75
        contains:
            "anim_tavern_birbs"
            zoom 0.75 xalign renpy.random.random()/2 yalign renpy.random.random()/5
            linear 40 xpos 1.1 zoom 0.5
            block:
                "anim_tavern_birbs"
                zoom 0.5 + renpy.random.random()/2 xalign -0.1 yalign renpy.random.random()/4
                linear 40 xpos 1.1 zoom 0.5
                repeat
        contains:
            "cloud_day"
            xalign renpy.random.random()/2 yalign -0.35
            linear 60.0 xalign 3.0
            block:
                "cloud_day"
                xalign -0.7-renpy.random.random()/3 yalign -0.35
                linear 60.0 xalign 3.0
                repeat
        contains:
            "anim_tavern_outside_smoke"
            xpos 0.52
            zoom 0.75
        contains:
            "tavern_outside_dayfp"
            zoom 0.75

##### ANIMACJA TAWERNY NOCNA ##########
    image anim_tavern nighttime:
        contains:
            "tavern_outside_nightsky"
            zoom 0.75
        #contains:
        #    "cloud_night1"
        #    #HBox ("cloud_night1","cloud_night1")
        #    zoom 0.7 xalign 0.5 yalign 0.05
        #    linear 100.0 xalign 3.0
        #contains:
        #    zoom 0.7 xalign -1.0 yalign 0.05
        #    linear 100.0 xalign 3.0
        #    repeat
        contains:
            "cloud_night1"
            xalign renpy.random.random()/2 yalign -0.35
            linear 60.0 xalign 3.0
            block:
                "cloud_night1"
                xalign -1.0 yalign -0.35
                linear 80.0 xalign 3.0
                repeat
        #contains:
        #    "cloud_night1"
        #    #HBox ("cloud_night1","cloud_night1")
        #    xzoom 1.5 xalign -2.0 yalign -0.25
        #    linear 60.0 xalign 3.0
        #    repeat
        contains:
            "anim_tavern_outside_smokenight"
            xpos 0.52
            zoom 0.75
        contains:
            "tavern_outside_nightfp"
            zoom 0.75

################ ANIMACJA TAWERNY DZIENNA WERSJA ZE SMOKIEM ####################
    image anim_tavern outside dragon:
        contains:
            "tavern_outside_dragonday"
            zoom 0.75
        contains:
            "anim_tavern_birbs"
            zoom 0.75 xalign renpy.random.random()/2 yalign renpy.random.random()/5
            linear 40 xpos 1.1 zoom 0.5
            block:
                "anim_tavern_birbs"
                zoom 0.5 + renpy.random.random()/2 xalign -0.1 yalign renpy.random.random()/4
                linear 40 xpos 1.1 zoom 0.5
                repeat
        contains:
            "cloud_day"
            xalign renpy.random.random()/2 yalign -0.35
            linear 60.0 xalign 3.0
            block:
                "cloud_day"
                xalign -0.7-renpy.random.random()/3 yalign -0.35
                linear 60.0 xalign 3.0
                repeat
        contains:
            "anim_tavern_outside_smoke"
            xpos 0.52
            zoom 0.75
        contains:
            "tavern_outside_dragondayfp"
            zoom 0.75

################ ANIMACJA TAWERNY NOCNA WERSJA ZE SMOKIEM ######################
    image anim_tavern nighttime dragon:
        contains:
            "tavern_outside_dragonnight"
            zoom 0.75
        #contains:
        #    "cloud_night1"
        #    #HBox ("cloud_night1","cloud_night1")
        #    zoom 0.7 xalign 0.5 yalign 0.05
        #    linear 100.0 xalign 3.0
        #contains:
        #    zoom 0.7 xalign -1.0 yalign 0.05
        #    linear 100.0 xalign 3.0
        #    repeat
        contains:
            "cloud_night1"
            xalign renpy.random.random()/2 yalign -0.35
            linear 60.0 xalign 3.0
            block:
                "cloud_night1"
                xalign -1.0 yalign -0.35
                linear 80.0 xalign 3.0
                repeat
        #contains:
        #    "cloud_night1"
        #    #HBox ("cloud_night1","cloud_night1")
        #    xzoom 1.5 xalign -2.0 yalign -0.25
        #    linear 60.0 xalign 3.0
        #    repeat
        contains:
            "anim_tavern_outside_smokenight"
            xpos 0.52
            zoom 0.75
        contains:
            "tavern_outside_dragonnightfp"
            zoom 0.75

##### Animacja przejscia tawerny dzien w noc #####
    image anim_tavern daytonight:
        "anim_tavern outside"
        1.8
        "anim_tavern nighttime" with Dissolve(2.0)
        1.8
    image anim_tavern nighttoday:
        "anim_tavern nighttime"
        1.8
        "anim_tavern outside" with Dissolve(2.0)
        1.8

##### Animacja przejscia tawerny dzien w noc wersja smocza #####
    image anim_tavern daytonight dragon:
        "anim_tavern outside dragon"
        1.8
        "anim_tavern nighttime dragon" with Dissolve(2.0)
        1.8
    image anim_tavern nighttoday dragon:
        "anim_tavern nighttime dragon"
        1.8
        "anim_tavern outside dragon" with Dissolve(2.0)
        1.8



##### animacje do dreams #######
    image img_dream_good:
        contains:
            4
            "cg_dream_good"
            alpha 0.0
            align (.5,.8) zoom 1.0
            parallel:
                linear 8 alpha 1.0
            parallel:
                ease 16 align (0.5,.0) zoom 0.8
        contains:
            5
            "white_sparkles1"
            zoom 1.3 alpha 0.0 align (0.5,0.5) ypos 0.0
            ease 13 ypos 0.5 alpha 1.0 zoom 1.6
            block:
                linear .3 alpha 1.0
                .2
                linear .5 alpha 0.7
                .1
                repeat
        contains:
            6
            "white_sparkles2"
            zoom 1.0 alpha 0.0 align (0.5,0.5) ypos -0.2
            ease 3 alpha 1.0
            parallel:
                ease 13 ypos 0.5 zoom 1.5
            parallel:
                block:
                    linear .3 alpha 1.0
                    .2
                    linear .5 alpha 0.7
                    .1
                    repeat
        contains:
            10
            "white_sparkles2"
            zoom 1.2 alpha 0.0 align (0.5,0.5) ypos 0.5
            ease 3 alpha 1.0
            parallel:
                ease 13 ypos -0.2 zoom 1.5
            parallel:
                block:
                    linear .3 alpha 1.0
                    .2
                    linear .5 alpha 0.7
                    .1
                    repeat
        contains:
            "fog2"
            align (.2,.4)
            alpha 0.9
            parallel:
                linear 8 xalign .6
            parallel:
                linear 6 alpha .2
        contains:
            "fog1"
            align (.4,.7)
            alpha 0.9
            parallel:
                linear 20 xalign .8
            parallel:
                linear 6 alpha .2
        contains:
            "anim_dreams_border"



    image img_dream_bad:
        contains:
            "anim_forest_night_man"
            alpha 0.0
            linear 4 alpha 0.0
            align (0.5,0.5) zoom 0.6 pos (0.3,0.2)
            parallel:
                linear 8 alpha 1.0
            parallel:
                ease 12 pos (-0.5,0.0) zoom 1.0
        contains: #wczytywane od razu, ujawnia się po 16s
            "cg_dream_bad"
            alpha 0.0
            16
            alpha 1.0
        contains: #wczytywane od razu, ujawnia się po 16.1s po czarnym przejściu
            "anim_forest_night_noman"
            alpha 0.0
            16.3
            alpha 1.0 align (0.5,0.5) pos (-0.5,0.0) zoom 1.0
        contains:
            "fog2"
            align (.2,.4)
            alpha 0.9
            parallel:
                linear 20 xalign .6
            parallel:
                linear 6 alpha .5
        contains:
            "fog1"
            align (.4,.7)
            alpha 0.9
            parallel:
                linear 40 xalign .8
            parallel:
                linear 6 alpha .5
        contains:
            "anim_dreams_border"



    image anim_forest_night_noman:
        contains:
            "forest_night"
        contains:
            "forest_night_torch"
        contains:
            "anim_torchonground"
            linear 16 alpha 1.0
            linear 5 alpha 0.0

    image anim_forest_justforest:
        contains:
            "forest_justforest"
        contains:
            HBox ("fog1","fog2")
            zoom 0.7 xalign -0.5 yalign 0.09
            linear 100.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog2")
            xalign -0.5 yalign 0.06
            linear 60.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog1")
            xzoom 1.5 xalign -0.5 yalign 0.0
            linear 60.0 xalign 1.5
            repeat #DO SNU POZYTYWNEGO
    image anim_dreams_border:
        "dreams_border"
        align (.5,.5) pos (.5,.5) zoom 0.52
        linear 8 zoom 0.5
        linear 8 zoom 0.52
        repeat

    image anim_forest_justforest2: # do epizodu
        contains:
            "forest_justforest"
        contains:
            "fog1"
            xalign 0.0 yalign 0.06 alpha 0.8
            linear 40.0 xalign 1.5
        contains:
            "fog1"
            xalign -2.0 yalign 0.06 alpha 0.8
            linear 40.0 xalign 1.5
            repeat
        contains:
            "fog2"
            xalign -2.0 yalign 0.0 alpha 0.7
            linear 60.0 xalign 1.5
            repeat

    image anim_forest_night_man:
        contains:
            "forest_night_man"
        contains:
            "anim_pochodnia"
    image anim_forest_night_sen:
        contains:
            "anim_forest_night_man"
            8.0
            "black"
            0.5
            "anim_forest_night_noman"
        contains:
            HBox ("fog1","fog2")
            zoom 0.7 xalign 0.5 yalign 0.7
            linear 100.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog2")
            xalign 0.5 yalign 0.5
            linear 60.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog1")
            xzoom 1.5 xalign 0.5 yalign 0.5
            linear 60.0 xalign 1.5
            repeat
    image forest_day_fog:
        contains:
            "forest_day"
        contains:
            HBox ("fog1","fog2")
            zoom 0.7 xalign 0.5 yalign 0.7
            linear 100.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog2")
            xalign 0.5 yalign 0.5
            linear 60.0 xalign 1.5
            repeat
        contains:
            HBox ("fog1","fog1")
            xzoom 1.5 xalign 0.5 yalign 0.5
            linear 60.0 xalign 1.5
            repeat
    image tdr2:
        contains:
            "tavern_door_lights2"
            yanchor 0.0 alpha 0.0 zoom 1.0
            linear 2.0 yanchor 0.02 alpha 0.5
            linear 2.0 yanchor 0.04 alpha 1.0
            linear 2.0 yanchor 0.06 alpha 0.5
            linear 2.0 yanchor 0.08 alpha 0.0
            repeat
        contains:
            "tavern_door_lights2"
            xanchor 0.2 zoom 1.2 yanchor -0.12 alpha 0.0
            linear 6.0 yanchor -0.06 alpha 0.0
            linear 3.0 yanchor -0.04 alpha 0.5
            linear 3.0 yanchor -0.02 alpha 1.0
            linear 3.0 yanchor 0.00 alpha 0.5
            linear 3.0 yanchor 0.02 alpha 0.0
            repeat

############################# swiatlo ####################
    image anim_mrygajace_swiatlo:
        contains:
            "light_orange"
            align (.5,.5) alpha .3
            zoom .7
            choice:
                .14
            choice:
                .1
            choice:
                .25
            choice:
                .05
            linear .2 alpha 0.28
            repeat
        contains:
            "light_orangish"
            align (.5,.5) alpha .8
            zoom .4
            choice:
                .2
            choice:
                .12
            choice:
                .17
            choice:
                .05
            linear .2 alpha 0.6
            repeat
        contains:
            "light_yellow"
            align (.5,.5) alpha 1.0
            zoom .13
            choice:
                .2
            choice:
                .12
            choice:
                .09
            choice:
                .05
            linear .2 alpha 0.8
            repeat
        contains:
            "light_yellowish"
            align (.5,.5) alpha 1.0
            zoom .1
            choice:
                .1
            choice:
                .14
            choice:
                .19
            choice:
                .06
            linear .2 alpha 0.9
            repeat
    image anim_pochodnia:
        contains:
            "las_ogien3"
            #align (.5,.5)
            alpha 0.38
            choice:
                linear .2
            choice:
                linear .12
            choice:
                linear .17
            choice:
                linear .05
            linear .2 alpha 0.15
            repeat
        contains:
            "las_ogien2"
            #align (.5,.5)
            alpha 0.4
            choice:
                linear .2
            choice:
                linear .12
            choice:
                linear .09
            choice:
                linear .05
            linear .2 alpha 0.18
            repeat
        contains:
            "las_ogien1"
            #align (.5,.5)
            alpha 0.3
            choice:
                linear .1
            choice:
                linear .14
            choice:
                linear .19
            choice:
                linear .06
            linear .2 alpha 0.2
            repeat

    image anim_torchonground:
        contains:
            "forest_night_torchfire3"
            #align (.5,.5)
            alpha 0.96
            choice:
                linear .16
            choice:
                linear .12
            choice:
                linear .09
            choice:
                linear .05
            linear .2 alpha 0.65
            repeat
        contains:
            "forest_night_torchfire2"
            #align (.5,.5)
            alpha 0.88
            choice:
                linear .2
            choice:
                linear .12
            choice:
                linear .17
            choice:
                linear .05
            linear .2 alpha 0.55
            repeat
        contains:
            "forest_night_torchfire1"
            #align (.5,.5)
            alpha 0.82
            choice:
                linear .2
            choice:
                linear .12
            choice:
                linear .09
            choice:
                linear .05
            linear .2 alpha 0.58
            repeat
        contains:
            "forest_night_torchfire"
            #align (.5,.5)
            alpha 0.78
            choice:
                linear .1
            choice:
                linear .14
            choice:
                linear .19
            choice:
                linear .06
            linear .2 alpha 0.5
            repeat



############################# inne ####################
    image anim_cg_tavern_wall1: #proxy do main screen -> start gry
        contains:
            "tavern_door_lia_eyesclosed"
            align (0,0)
        contains:
            "tavern_door_lights1"
            linear 50 zoom 1.2
            pause 0.3
            linear 50 zoom 1.0
            repeat
        contains:
            "tavern_door_lights2"
            zoom 1.2 alpha 0.8
            block:
                linear 77 zoom 1.0 alpha 0.9
                pause 0.3
                linear 100 zoom 1.2 alpha 0.8
                repeat
    image cg_tavern_wall1_mainscreen: #main screen jesli bedzie lia
        contains:
            "tavern_door_lia_eyesclosed"
            align (0,0)
        contains:
            "tavern_door_lights1"
        contains:
            "tavern_door_lights2"
            zoom 1.2 alpha 0.8


################################################################################
#################################   MINIGRA   ##################################
############################   WYCIERANIE STOLU   ##############################
################################################################################

# przycisk do wcześniejszego wychodzenia z czyszczenia stołu (troche zmniejszam wielkość)
image czyszcz_but1 = im.FactorScale("gui/button/choice_idle_background.png", 0.5)
image czyszcz_but2 = im.FactorScale("gui/button/choice_hover_background.png", 0.5)

default n = 0
default n_max = 6
default v_pl1 = False
default v_pl2 = False
default v_pl3 = False
default v_pl4 = False
default v_pl5 = False
default v_pl6 = False
default v_pl7 = True
default v_pl8 = True
default v_pl9 = True
default v_pl10 = True



image zoomnastol:
    contains:
        pos renpy.get_mouse_pos()
        "cloth"
        ypos -0.2
        linear 0.25 xpos -0.2
        linear 0.25 xpos 0.1
        linear 0.25 xpos -0.2
        linear 0.25 xpos 0.1
        linear 0.25 xpos -0.2
        linear 0.25 xpos 0.1


screen wytrzyjstol():
    #$ config.mouse = {"default" :[("images/inne/table minigame/clothcursor.png", 10, 3)]}
    tag sprzataniestolu
    modal True
    add "stol"
    if n < 2:
        fixed:
            text _("[[Wytrzyj stół klikając na brud]") xalign 0.5 yalign 0.05
    if v_pl1 == False:
        imagebutton:
            focus_mask True
            pos (v_pl1_posx,v_pl1_posy)
            idle "stain2"
            action [SetVariable("v_pl1", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl2 == False:
        imagebutton:
            focus_mask True
            pos (v_pl2_posx,v_pl2_posy)
            idle "crumbs1"
            action [SetVariable("v_pl2", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl3 == False:
        imagebutton:
            focus_mask True
            pos (v_pl3_posx,v_pl3_posy)
            idle "stain3"
            action [SetVariable("v_pl3", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl4 == False:
        imagebutton:
            focus_mask True
            pos (v_pl4_posx,v_pl4_posy)
            idle "handprint1"
            action [SetVariable("v_pl4", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl5 == False:
        imagebutton:
            focus_mask True
            pos (v_pl5_posx,v_pl5_posy)
            idle "dirt1"
            action [SetVariable("v_pl5", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl6 == False:
        imagebutton:
            focus_mask True
            pos (v_pl6_posx,v_pl6_posy)
            idle "crumbs2"
            action [SetVariable("v_pl6", True), SetVariable("n", n+1), ShowTransient("czyszczenie")]
    if v_pl7 == False:
        imagebutton:
            focus_mask True
            pos (0.5,0.4)
            idle "handprint2"
            action [SetVariable("v_pl7", True), SetVariable("n", n+1), Show("czyszczenie")]
    if v_pl8 == False:
        imagebutton:
            focus_mask True
            pos (0.3,0.2)
            idle "stain1"
            action [SetVariable("v_pl8", True), SetVariable("n", n+1), Show("czyszczenie")]
    if v_pl9 == False:
        imagebutton:
            focus_mask True
            pos (0.4,0.6)
            idle "crumbs3"
            action [SetVariable("v_pl9", True), SetVariable("n", n+1), Show("czyszczenie")]
    if v_pl10 == False:
        imagebutton:
            focus_mask True
            pos (0.7,0.5)
            idle "handprint3"
            action [SetVariable("v_pl10", True), SetVariable("n", n+1), Show("czyszczenie")]
    if n >= 1:
        imagebutton:
            #focus_mask True
            align (0.5,0.92)
            idle "czyszcz_but1"
            hover "czyszcz_but2"
            action Return("wystarczy") #Jump("poczyszczeniustolu")
        text _("Chyba wystarczy") align (0.5,0.9)
        #textbutton "Chyba wystarczy" align (0.5,0.9) action Jump("poczyszczeniustolu")


screen czyszczenie():
    #tag sprzataniestolu
    modal True
    add "zoomnastol" pos renpy.get_mouse_pos()
    timer 2.0 action [Show("wytrzyjstol"),Return()]

label czyszcz:
    $ v_pl1_posx = renpy.random.random()*0.2
    $ v_pl1_posy = renpy.random.random()*0.35
    $ v_pl2_posx = renpy.random.random()*0.35 + 0.2
    $ v_pl2_posy = renpy.random.random()*0.2
    $ v_pl3_posx = renpy.random.random()*0.35 + 0.6
    $ v_pl3_posy = renpy.random.random()*0.4
    $ v_pl4_posx = renpy.random.random()*0.4
    $ v_pl4_posy = renpy.random.random()*0.5 + 0.2
    $ v_pl5_posx = renpy.random.random()*0.4 + 0.3
    $ v_pl5_posy = renpy.random.random()*0.5 + 0.4
    $ v_pl6_posx = renpy.random.random()*0.4 + 0.5
    $ v_pl6_posy = renpy.random.random()*0.5 + 0.3
    call screen wytrzyjstol with dissolve
    while _return != "wystarczy":
        call screen wytrzyjstol
    jump poczyszczeniustolu
    return
