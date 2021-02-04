################################################################################
init python:
    def fOpis(opisik):
        renpy.notify("%s" % opisik)
    CurryfOpis = renpy.curry(fOpis)
    def ScrSay (postac, comowi, objectstate):
        renpy.say(postac, comowi, interact=True)
        objectstate = True
        #obj_name = name
        #obj_descr = description

    ########### TESTY ############
    def Czas (cz_pora, cz_dzien):
        x = cz_pora
        if cz_pora < 5:
            cz_pora = cz_pora + x
        else:
            cz_pora = 1
            cz_dzien = cz_dzien + 1

######################   ZMIANA EE  #########################
label zmiana_ee:
    $ ee += 1
######################   /ZMIANA EE  #########################

################################# ZMIANA CZASU #################################
################################################################################
label timechange:
    $ dt += 1
    $ licznikAkcji += 1
    if dt > 5:
        $ day += 1
        $ dt = 1
    $ weekday = day % 7
    if weekday == 0:
        $ weekdayName = _("niedziela")
    if weekday == 1:
        $ weekdayName = _("poniedziałek")
    if weekday == 2:
        $ weekdayName = _("wtorek")
    if weekday == 3:
        $ weekdayName = _("środa")
    if weekday == 4:
        $ weekdayName = _("czwartek")
    if weekday == 5:
        $ weekdayName = _("piątek")
    if weekday == 6:
        $ weekdayName = _("sobota")
    return

label spacerMiedzyLokacjami(gotoLok):
    call timechange
    if gotoLok == "town":
        jump ee_town
    if gotoLok == "tavern":
        jump ee_tavern_mainroom
    if gotoLok == "garden":
        jump ee_secretgarden
    if gotoLok == "monument":
        jump ee_monument
################################################################################
################################################################################

init:
    transform buttonzoom(z):
        zoom z

################################################################################
############################# MAPA I CZAS ###############################
################################################################################

screen devscreen():
    if config.developer:
        vbox:
            xalign 0.5 yalign 0.0 xpos 0.9
            text "lok = [lok]"
            text "czas = [dt]"
            text "dzień = [day]"
            text "licznikAkcji = [licznikAkcji]"
            text "weekday = [weekday]"
            text "[weekdayName]"
            textbutton "pora dnia -1" action [Return(),SetVariable("dt", dt-1)]
            textbutton "pora dnia +1" action [Return(),SetVariable("dt", dt+1)]
            textbutton "day -1" action [Return(),SetVariable("day", day-1)]
            textbutton "day +1" action [Return(),SetVariable("day", day+1)]

screen timeskip():
    zorder 100
    imagebutton auto "button_journal_%s" focus_mask True action ShowTransient('journal_bookmark1')
    use devscreen ########### TODO usunąć po wszystkim
    #if dt >= 5:
    #    imagebutton auto "gui/timeskip/time_%s.png" focus_mask True action [Return("dt=1"),SetVariable("dt", 1), SetVariable("day", day+1), SetVariable("licznikAkcji", licznikAkcji+1)]
    #else:
    #    imagebutton auto "gui/timeskip/time_%s.png" focus_mask True action [Return("dt+1"),SetVariable("dt", dt+1), SetVariable("licznikAkcji", licznikAkcji+1)]

    imagebutton auto "gui/timeskip/time_%s.png" focus_mask True action Call("timechange")

    vbox:
        xalign .5 yalign .005
        if dt == 1:
            text _("poranek")
        if dt == 2:
            text _("południe")
        if dt == 3:
            text _("popołudnie")
        if dt == 4:
            text _("wieczór")
        if dt >= 5:
            text _("noc")

    vbox:
        xalign 0.5 yalign 0.05
        text _("Naciśnij by przeczekać") size 15

screen obiekty():
    $ tooltip = GetTooltip()
    if tooltip:
        frame at ttobiekt_appear:
            style "ttobiekt"
            text "[tooltip]"




screen map_button():
    zorder 101
    imagebutton auto "button_map_%s" xalign 1.0 yalign 1.0 focus_mask True action Show("ee_mapka", fc)


############# OLD BACKUP #################
screen ee_mapka_backup():
    zorder 200
    modal True
    add "mapka_fhd"
    use obiekty

    if dt >= 5:
        #if lok != "wios":
        #    imagebutton auto "wioska_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_town")]
        if lok != "taw":
            imagebutton auto "tawerna_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_tavern_mainroom")] #tooltip _("Czas wracać do domu")
        #if lok != "secretgarden":
        #    imagebutton auto "drzewo_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_secretgarden1")]
        #if lok != "mon":
        #    imagebutton auto "monument_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_monument")]
            frame:
                style "ttobiekt"
                text _("Czas wracać do domu")
        if lok == "taw":
            frame:
                style "ttobiekt"
                text _("Jest już za późno żeby podróżować")
    else:
        if lok != "wios":
            imagebutton auto "wioska_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), SetVariable("dt", dt+1), Jump("ee_town")]
        elif lok == "wios":
            imagebutton idle "wioska_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "taw":
            imagebutton auto "tawerna_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), SetVariable("dt", dt+1), Jump("ee_tavern_mainroom")]
        elif lok == "taw":
            imagebutton idle "tawerna_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "secretgarden":
            imagebutton auto "drzewo_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), SetVariable("dt", dt+1), Jump("ee_secretgarden")]
        elif lok == "secretgarden":
            imagebutton idle "drzewo_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "mon":
            imagebutton auto "monument_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), SetVariable("dt", dt+1), Jump("ee_monument")]
        elif lok == "mon":
            imagebutton idle "monument_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")
    imagebutton auto "room_lia_exit_%s" focus_mask True action ToggleScreen("ee_mapka", dissolve)
############# /OLD BACKUP #################
###################################################################################################
screen ee_mapka():
    zorder 200
    modal True
    add "mapka_fhd"
    use obiekty

    if dt >= 5:
        #if lok != "wios":
        #    imagebutton auto "wioska_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_town")]
        if lok != "taw":
            imagebutton auto "tawerna_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), SetVariable("powrotPoNocy", powrotPoNocy+1), Jump("ee_tavern_mainroom")] #tooltip _("Czas wracać do domu")
        #if lok != "secretgarden":
        #    imagebutton auto "drzewo_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_secretgarden1")]
        #if lok != "mon":
        #    imagebutton auto "monument_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), SetVariable("licznikAkcji", licznikAkcji+1), Jump("ee_monument")]
            frame:
                style "ttobiekt"
                text _("Czas wracać do domu")
        if lok == "taw":
            frame:
                style "ttobiekt"
                text _("Jest już za późno żeby podróżować")
    else:
        if lok != "wios":
            imagebutton auto "wioska_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), Call("spacerMiedzyLokacjami", "town")]
        elif lok == "wios":
            imagebutton idle "wioska_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "taw":
            imagebutton auto "tawerna_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), Call("spacerMiedzyLokacjami", "tavern")]
        elif lok == "taw":
            imagebutton idle "tawerna_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "secretgarden":
            imagebutton auto "drzewo_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), Call("spacerMiedzyLokacjami", "garden")]
        elif lok == "secretgarden":
            imagebutton idle "drzewo_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")

        if lok != "mon":
            imagebutton auto "monument_%s" focus_mask True action [ToggleScreen("ee_mapka", dissolve), Call("spacerMiedzyLokacjami", "monument")]
        elif lok == "mon":
            imagebutton idle "monument_idle" focus_mask True action NullAction() tooltip __("Jesteś tu")
    imagebutton auto "room_lia_exit_%s" focus_mask True action ToggleScreen("ee_mapka", dissolve)




################################################################################



################################## EE WIOSKA ###################################
screen ee_town():
    tag ee
    modal True
    #add "img_festival_dn_dragon":
    #    zoom 0.46875
    use timeskip
    imagebutton auto "town_smithy_dn_%s" focus_mask True action Return("niedostepne") tooltip __("KUŹNIA")
    #if dt >= 5:
    #    imagebutton auto "town_night_smithy_%s" focus_mask True action Return("niedostepne")
    #imagebutton auto "p5_%s" xalign 0.1 yalign 1.0 focus_mask True action Return("e8_p5") #### do wyrzucenia
    use map_button
    use obiekty




################################# EE TAWERNA ###################################
###########################
screen ee_tavern_liaroom():
    tag ee
    modal True
    #add "img_pokojlii"
    imagebutton auto "room_lia_exit_%s" focus_mask True action Jump("ee_tavern_hall")
    if dt >= 5:
        imagebutton auto "room_lia_bed_%s" focus_mask True action [Return("dt+1"),SetVariable("dt", 1), SetVariable("day", day+1), SetVariable("licznikAkcji", licznikAkcji+1)]
    else:
        imagebutton auto "room_lia_bed_%s" focus_mask True action [SetVariable("dt", dt + 1), Return("spanko"), SetVariable("licznikAkcji", licznikAkcji+1)]
    use timeskip


#############################
screen ee_tavern_hall():
    tag ee
    modal True
    add "tavern_hall_bg0"

    imagebutton auto "tavern_hall_bathroom1_%s" focus_mask True action Return("ee_hall_bathroom") tooltip __("ŁAZIENKA")
    imagebutton auto "tavern_hall_diningroom1_%s" focus_mask True action Return("ee_hall_diningroom") tooltip __("JADALNIA")
    imagebutton auto "tavern_hall_guestroom1_%s" focus_mask True action Return("ee_hall_guestroom") tooltip __("POKÓJ GOŚCINNY")
    imagebutton auto "tavern_hall_liaroom1_%s" focus_mask True action Return("ee_hall_liaroom") tooltip __("POKÓJ LII")
    imagebutton auto "tavern_hall_parentsroom1_%s" focus_mask True action Return("ee_hall_parentsroom") tooltip __("POKÓJ RODZICÓW")
    imagebutton auto "tavern_hall_stairs2_%s" focus_mask True action Return("ee_hall_mainroom") tooltip __("NA DÓŁ")
    use obiekty
    use timeskip

############################
screen ee_tavern_mainroom():
    tag ee
    modal True

    add "tavern_main_bg0_dn"
    imagebutton auto "tavern_main_leftroom1_dn_%s" focus_mask True action Return("ee_tavern_leftroom") tooltip __("LEWA SALA")
    #imagebutton auto "tavern_main_rightroom1_dn_%s" focus_mask True action Return("ee_tavern_rightroom") tooltip _("PRAWA SALA") ### nie zawiera się w demo
    imagebutton idle "tavern_main_rightroom1_dn_idle" focus_mask True #action NullAction()
    if dt < 5:
        imagebutton auto "tavern_main_kitchen1_dn_%s" focus_mask True action Return("ee_tavern_kitchen") tooltip __("KUCHNIA")
    else:
        imagebutton auto "tavern_main_kitchen1_dn_%s" focus_mask True
    if dt < 5:
        if z_dekoracje:
            imagebutton auto "tavern_main_dekoracje1_dn_%s" focus_mask True #action [Return("dekoracje"), ToggleVariable("z_dekoracje")]
        else:
            imagebutton idle "tavern_main_dekoracje1_dn_idle" focus_mask True action NullAction()
        imagebutton auto "tavern_main_supplies2_dn_%s" focus_mask True #action NullAction()
        imagebutton auto "tavern_main_shelf1_dn_%s" focus_mask True #action NullAction()
        imagebutton auto "tavern_main_menu3_dn_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_stairs2_dn_%s" focus_mask True action Return("ee_tavern_hall") tooltip __("NA GÓRĘ")
    if dt == 1 and ee001_UkonczenieEpizodow['e8_p4'] and ee001_UkonczenieEpizodow['e8_p5'] and not ee001_UkonczenieEpizodow['e8_p16']:
        imagebutton auto "p3_%s" at buttonzoom(0.3) xpos 0.6 yalign 0.6 focus_mask True action Return("e8_p16")
    imagebutton auto "tavern_main_bar3_dn_%s" focus_mask True action Return("ee_tavern_mainroom_bar")
    if dt < 5:
        imagebutton auto "tavern_main_table4_dn_%s" focus_mask True #action NullAction()
        if z_zyrandole:
            imagebutton auto "tavern_main_chandelier4_dn_%s" focus_mask True #action [Return("żyrandole"), ToggleVariable("z_zyrandole")]
        else:
            imagebutton idle "tavern_main_chandelier4_dn_idle" focus_mask True action NullAction()
        if z_beer:
            imagebutton auto "tavern_main_beer4_dn_%s" focus_mask True #action [Return("beer"), ToggleVariable("z_beer")]
        else:
            imagebutton idle "tavern_main_beer4_dn_idle" focus_mask True action NullAction()
    if paczka01 == "oczekuje":
        imagebutton auto "tavern_main_package5_dn_%s" focus_mask True action [Return("paczka01"), SetVariable("paczka01","odebrana")]
    if z_tablemess:
        imagebutton auto "tavern_main_tablemess5_dn_%s" focus_mask True action [Return("tablemess"), ToggleVariable("z_tablemess")]
    if z_floorflourmess:
        imagebutton auto "tavern_main_floorflourmess5_dn_%s" focus_mask True action [Return("floorflourmess"), ToggleVariable("z_floorflourmess")]
    if z_floorwinemess:
        imagebutton auto "tavern_main_floorwinemess5_dn_%s" focus_mask True action [Return("floorwinemess"), ToggleVariable("z_floorwinemess")]
    if z_barrightmess:
        imagebutton auto "tavern_main_barrightmess5_dn_%s" focus_mask True action [Return("barrightmess"), ToggleVariable("z_barrightmess")]
    if z_barleftmess:
        imagebutton auto "tavern_main_barleftmess5_dn_%s" focus_mask True action [Return("barleftmess"), ToggleVariable("z_barleftmess")]

    ### TEST POSTACI ###
    #imagebutton auto "p8_%s" xpos 0.2 yalign 1.0 focus_mask True action NullAction()
    ###    ######    ###

    #imagebutton auto "button_map_%s" focus_mask True action ToggleScreen("ee_mapka", dissolve)

    imagebutton auto "button_exit_%s" xalign 0.02 yalign 0.96 focus_mask True action Jump("ee_tavern_outside")
    use map_button
    use timeskip
    use obiekty


#################################
init:
    default aina_demo_check = True
screen ee_tavern_leftroom():

    tag ee
    modal True
    add "tavern_leftroom_dn_bg0"
    imagebutton auto "tavern_leftroom_mainroom1_dn_%s" focus_mask True action Return("ee_tavern_mainroom") tooltip __("SALA GŁÓWNA")
    imagebutton auto "tavern_leftroom_painting1_dn_%s" focus_mask True action Return("ee_leftroom_painting")
    if dt < 5:
        imagebutton auto "tavern_leftroom_decorations1_%s" focus_mask True #action NullAction()
        imagebutton auto "tavern_leftroom_shields1_%s" focus_mask True #action NullAction()
    if aina_demo_check:
        if dt == 2 or dt == 4:
            imagebutton auto "tavern_leftroom_bottle2_dn_%s" focus_mask True #action NullAction()
            imagebutton auto "tavern_leftroom_aina3_dn_%s" focus_mask True action [Return("P7_D01"), ToggleVariable("aina_demo_check")]
    if dt < 5:
        if czyjestgosc1 == 1:
            imagebutton auto "tavern_leftroom_dude3_dn_%s" focus_mask True #action NullAction()
        if czyjestgosc2 == 1:
            imagebutton auto "tavern_leftroom_lady3_dn_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroomnight_levius3_%s" focus_mask True action NullAction()
    use timeskip
    use obiekty

################################
screen ee_tavern_rightroom():
    tag ee
    modal True
    add "tavern_rightroom_bg0"
    imagebutton auto "tavern_rightroom_mainroom1_%s" focus_mask True action Return("ee_tavern_mainroom") tooltip __("SALA GŁÓWNA")
    imagebutton auto "tavern_rightroom_painting1_%s" focus_mask True action Return("ee_rightroom_painting")
    imagebutton auto "tavern_rightroom_barrels1_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_decorations2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_mohon2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_harion2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_lady3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_mess3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_pickaxe3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_couple3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_chandelier4_%s" focus_mask True action #NullAction()
    use timeskip
    use obiekty

################################
screen ee_tavern_kitchen():
    tag ee
    modal True
    #add "room_kitchenday"
    imagebutton auto "room_lia_exit_%s" focus_mask True action Return("ee_tavern_mainroom")
##############################
screen ee_tavern_mainroom_bar():
    tag ee
    modal True
    add "tavern_main_bar_bg0_dn"
    if ee001_UkonczenieEpizodow['e8_p4'] and ee001_UkonczenieEpizodow['e8_p5']:
        if dt == 1 and not ee001_UkonczenieEpizodow['e8_p16']:
            imagebutton auto "p3_%s" at zabarem xalign 0.5 focus_mask True action Return("e8_p16")
    add "tavern_main_bar_bar1_dn"
    imagebutton auto "room_lia_exit_%s" focus_mask True action Return("ee_tavern_mainroom")



#############################
screen ee_tavern_outside():
    tag ee
    modal True
    #if dt >= 5:
    #    add "anim_tavern nighttime dragon"
    #elif dt < 5:
    #    add "anim_tavern outside dragon"
    if klik_tent1:
        imagebutton auto "tavern_outside_tent_%s" focus_mask True action Return("namiot")
    imagebutton auto "tavern_outside_door_%s" focus_mask True action Return("tawerna")

    use map_button
    use timeskip




############################### EE SECRET GARDEN ##############################

#init:
    #default SetGardenPosition = ui.adjustment()
screen ee_secretgarden():
    #default xadj = ui.adjustment("sg")

    tag ee
    modal True
    viewport id "sg":
        child_size (3840, 1080)
        draggable True
        #mousewheel "horizontal"
        edgescroll (300,150)
        xadjustment xadj
        #xinitial xadj.value/1920
        add "secretgarden_bg"
        imagebutton auto "secretgarden_full_water_%s" focus_mask True action Return("secretgarden_water")
        imagebutton auto "secretgarden_full_tree_%s" focus_mask True action Return("secretgarden_tree")
        imagebutton auto "secretgarden_full_sus_%s" focus_mask True action Return("secretgarden_sus")
        imagebutton auto "secretgarden_full_terra_%s" focus_mask True action Return("secretgarden_terra")
        imagebutton auto "secretgarden_full_owocki_%s" focus_mask True action Return("secretgarden_owocki")
    #bar value XScrollValue("sg")


    use map_button
    use timeskip

################################# EE MONUMENT ##################################3
init:
    image guard11_monument_small_hover:
        "guard_monument_hover"
        zoom 0.5
    image guard11_monument_small_idle:
        "guard_monument_idle"
        zoom 0.5
    image guard12_monument_small_hover:
        "festival_guard_hover"
        xzoom -1
        zoom 0.73
    image guard12_monument_small_idle:
        "festival_guard_idle"
        xzoom -1
        zoom 0.73

screen ee_monument():
    tag ee
    modal True
    imagebutton auto "monument_tablica_fhd_%s" focus_mask True action ToggleScreen("scr_tablica", dissolve)
    #if dt >= 3:
    #    add "anim_monument_fire":
    #        zoom 0.5
    if dt < 4:
        imagebutton auto "guard11_monument_small_%s" focus_mask True xalign 0.6 yalign 1.0 action Return("guard11_talk")
    else:
        imagebutton auto "guard12_monument_small_%s" focus_mask True xalign 0.4 yalign 1.0 action Return("guard12_talk")
    if dt == 2 or dt == 3:
        imagebutton auto "p13_monument_button_%s" focus_mask True xalign 0.3 yalign 1.0 action Return("architect_talk")

    if ee < 6:
        add "monument_dragon_firstplan":
            zoom 0.5
    use map_button
    use timeskip

screen scr_tablica():
    modal True
    add "img_monument":
        xalign 0.5 yalign 1.0
    add "img_monument_extras":
        xalign 0.5 yalign 1.0
    imagebutton auto "button_exit_%s" xalign 0.02 yalign 0.96 focus_mask True action ToggleScreen("scr_tablica", dissolve)

################################################################################
#################################### EE-000 ####################################
################################################################################


screen ee000_tavern_liaroom():
    tag ee000
    modal True
    #add "anim_room_lia_morning"
    imagebutton auto "room_lia_exit_%s" focus_mask True action Return("ee000_tavern_hall")
    #imagebutton auto "room_lia_bed_%s" focus_mask True action Return("")  #łóżko - tędy chyba nie ma wyjścia obecnie - może będzie komentarz od Lii


screen ee000_tavern_hall():
    tag ee000
    modal True
    #add "tavern_hall_bg0"
    imagebutton auto "tavern_hall_bathroom1_%s" focus_mask True action Return("ee000_hall_bathroom")
    imagebutton auto "tavern_hall_diningroom1_%s" focus_mask True action Return("ee000_hall_diningroom")
    imagebutton auto "tavern_hall_guestroom1_%s" focus_mask True action Return("ee000_hall_guestroom")
    imagebutton auto "tavern_hall_liaroom1_%s" focus_mask True action Return("ee000_hall_liaroom")
    imagebutton auto "tavern_hall_parentsroom1_%s" focus_mask True action Return("ee000_hall_parentsroom")
    imagebutton auto "tavern_hall_stairs2_%s" focus_mask True action Return("ee000_hall_mainroom")

screen ee000_tavern_mainroom():
    tag ee000
    modal True
    add "tavern_main_bg0"
    #imagebutton auto "tavern_main_rightroom1_%s" focus_mask True action Return("ee000_tavern_rightroom") tooltip _("PRAWA SALA")
    imagebutton idle "tavern_main_rightroom1_idle" focus_mask True action NullAction()
    imagebutton auto "tavern_main_leftroom1_%s" focus_mask True action Return("ee000_tavern_leftroom") tooltip __("LEWA SALA")
    imagebutton auto "tavern_main_kitchen1_%s" focus_mask True action Return("ee000ep8") tooltip __("KUCHNIA") # wyjście do epizodu
    imagebutton auto "tavern_main_dekoracje1_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_stairs2_%s" focus_mask True action Return("ee000_tavern_hall") tooltip __("NA GÓRĘ")
    imagebutton auto "tavern_main_supplies2_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_shelf1_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_menu3_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_bar3_%s" focus_mask True action Return("ee000_tavern_main_bar")
    imagebutton auto "tavern_main_table4_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_chandelier4_%s" focus_mask True #action NullAction()
    imagebutton auto "tavern_main_beer4_%s" focus_mask True #action NullAction()

    use obiekty


screen ee000_tavern_leftroom():
    tag ee000
    modal True
    add "tavern_leftroom_bg0"
    imagebutton auto "tavern_leftroom_mainroom1_%s" focus_mask True action Return("ee000_tavern_mainroom") tooltip __("SALA GŁÓWNA")
    #imagebutton auto "tavern_leftroom_painting1_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroom_decorations1_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroom_shields1_%s" focus_mask True #action NullAction()
    imagebutton idle "tavern_leftroom_painting1_idle" focus_mask True #action NullAction()      \
    imagebutton idle "tavern_leftroom_decorations1_idle" focus_mask True #action NullAction()    |### na czas demo
    imagebutton idle "tavern_leftroom_shields1_idle" focus_mask True #action NullAction()       /
    #imagebutton auto "tavern_leftroom_bottle2_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroom_aina3_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroom_dude3_%s" focus_mask True #action NullAction()
    #imagebutton auto "tavern_leftroom_lady3_%s" focus_mask True #action NullAction()


screen ee000_tavern_rightroom():
    tag ee000
    modal True
    add "tavern_rightroom_bg0"
    imagebutton auto "tavern_rightroom_mainroom1_%s" focus_mask True action Return("ee000_tavern_mainroom")
    imagebutton auto "tavern_rightroom_painting1_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_barrels1_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_decorations2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_mohon2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_harion2_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_lady3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_mess3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_pickaxe3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_couple3_%s" focus_mask True action #NullAction()
    imagebutton auto "tavern_rightroom_chandelier4_%s" focus_mask True action #NullAction()



################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
