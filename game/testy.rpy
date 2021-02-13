
################################################################################
################################################################################
################################ TESTOWANIE ####################################
label testowanie:
    ""
    scene black







    show work3a with dissolve
    show work3b with Dissolve(1.0)
    hide work3b
    hide work3a
    pause

    show work2a with dissolve
    show work2a:
        align (0.5,0.5)
        linear 0.5 xzoom 0.0
    pause 0.5
    show work1a:
        align (0.5,0.5)
        xzoom 0.0
        linear 0.5 xzoom 1.0
    pause 1.0
    ""
    return





############################## / TESTOWANIE ####################################
################################################################################
################################################################################



############################### TESTY #########################################


label trailerstuff:
    $ quick_menu = False

    image sss_anim_tavern_outside: # do trailera / bez birbow
        contains:
            "tavern_outside_day"
            zoom 0.75
        contains:
            "anim_tavern_outside_smoke"
            xpos 0.52
            zoom 0.75
        contains:
            "tavern_outside_dayfp"
            zoom 0.75
    "dzien w noc"
    window hide
    pause 2

    image trailer_anim_tavern_outside:
        "sss_anim_tavern_outside" with Dissolve(2.0)
        1.8
        "anim_tavern_nighttime" with Dissolve(2.0)
        1.8
        repeat

    scene sss_anim_tavern_outside with Dissolve(1.5)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(1.5)
    pause 0.5
    scene sss_anim_tavern_outside with Dissolve(1.5)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(1.5)
    pause 0.5
    scene sss_anim_tavern_outside with Dissolve(1.5)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(1.5)
    pause 0.5
    scene sss_anim_tavern_outside with Dissolve(1.5)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(1.5)
    pause 0.5
    pause


    scene sss_anim_tavern_outside with Dissolve(1.0)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(.8)
    pause 0.2
    scene sss_anim_tavern_outside with Dissolve(1.0)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(.8)
    pause 0.2
    scene sss_anim_tavern_outside with Dissolve(1.0)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(.8)
    pause 0.2
    scene sss_anim_tavern_outside with Dissolve(1.0)
    pause 0.5
    scene anim_tavern_nighttime with Dissolve(.8)
    pause 0.2
    pause

    show ziomeczki at left_to_right
    show ziomeczki2 at right
    show ziomeczki3 at left

    $ quick_menu = True
    return

label testy:

    menu:
        "testy postaci lokacji etc":
            pass

label testy_postaci:
    $ quick_menu = False
    scene anim_room_lia
    pause
    $ quick_menu = True
    scene black


############################### PO TESTACH ####################################
label screeny:
    ############################


    scene anim_tavern_outside:
        zoom 0.75
    #show ziomki at left_to_right
    show p1 at left:
        xoffset 200
    show p4 at center:
        xoffset 50
    #xoffset -200
    p1 "You can stay here."
    pause

    ############################
    scene bg tavern 0
    show p1 at center
        #pos (0.5, 0.15)
    show tavern_table
    p1 "\ \ \ \ \ \ \ \ \ \ I've had so much fun yesterday! All thanks to you!"

    window hide
    hide p1
    show piwo_1 at left:
        zoom 0.9, yanchor 1.15
    with dissolve
    pause 0.5
    show piwo_2 at center:
        zoom 0.9, yanchor 1.15
    with dissolve
    pause 0.5
    show piwo_3 at right:
        zoom 0.9, yanchor 1.15
    with dissolve
    pause
    p1 "Order 66 ready!"
    hide piwo_1
    hide piwo_2
    hide piwo_3

    window show
    ################ zmienilismy postaci wiec beda bugi tu ###################
    hide p1
    show lia at center:
        yanchor 0.75
    p1 "I've had so much fun yesterday! All thanks to you!"

    #########################
    scene raven_window_clear
    p4 "Sure, come in. I wanted to speak with you anyway..."

    #########################
    scene cg tavern wall
    "She leaned tiredly against the wall, listening to the silence disturbed only by the crackling embers in the fireplace."
    #########################
    scene bg forest postac
    show lia widenedwink bsurprised lopen at right:
        yanchor 0.75
        xoffset -200
    p1 "Wait, what was that? Did you hear that too?"
    #########################
    scene bg tavern 0
    show p4 bangry narrowedwink at left:
        xoffset 400
    show tavern_table
    show p1 langry narrowedwink at center:
        xoffset 300
    p4 "I can take care of myself!"
    ##########################
    return
