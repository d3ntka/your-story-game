init:
    transform zmn: #nie usuwac, używane w innym miejscu
        zoom 0.68
#######################   LIA   ######################

image lia_eyes_wink:
    "lia_eyes_relaxed" with Dissolve(0.1)
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_relaxed" with Dissolve(0.1)
    .23
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_relaxed" with Dissolve(0.1)
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_relaxed" with Dissolve(0.1)
    .13
    repeat
image lia_eyes_narrowedwink:
    "lia_eyes_narrowed" with Dissolve(0.1)
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_narrowed" with Dissolve(0.1)
    .23
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_narrowed" with Dissolve(0.1)
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_narrowed" with Dissolve(0.1)
    .13
    repeat
image lia_eyes_widenedwink:
    "lia_eyes_widened" with Dissolve(0.1)
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_widened" with Dissolve(0.1)
    .23
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_widened" with Dissolve(0.1)
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "lia_eyes_closed" with Dissolve(0.1)
    .25
    "lia_eyes_widened" with Dissolve(0.1)
    .13
    repeat

image lia_eyes_wink_player:
    "lia_eyes_relaxed_player"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_relaxed_player"
    .23
    "lia_eyes_closed"
    .25
    "lia_eyes_relaxed_player"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "lia_eyes_closed"
    .25
    "lia_eyes_relaxed_player"
    .13
    repeat
image lia_eyes_narrowedwink_player:
    "lia_eyes_narrowed_player"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_narrowed_player"
    .23
    "lia_eyes_closed"
    .25
    "lia_eyes_narrowed_player"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "lia_eyes_closed"
    .25
    "lia_eyes_narrowed_player"
    .13
    repeat
image lia_eyes_widenedwink_player:
    "lia_eyes_widened_player"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "lia_eyes_widened_player"
    .23
    "lia_eyes_closed"
    .25
    "lia_eyes_widened_player"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "lia_eyes_closed"
    .25
    "lia_eyes_widened_player"
    .13
    repeat

layeredimage lia:
    always "lia_base"

    group lips auto:
        attribute lneutral default

    group eyes:
        attribute wink default:
           "lia_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "lia_eyes_narrowedwink"
        attribute widenedwink:
            "lia_eyes_widenedwink"
        attribute wink_player:
           "lia_eyes_wink_player"
        attribute narrowedwink_player:
            "lia_eyes_narrowedwink_player"
        attribute widenedwink_player:
            "lia_eyes_widenedwink_player"
        attribute closed

    group brows auto:
        attribute bneutral default:
            "lia_brows_brelaxed"
    attribute blush:
        "lia_blush"
    if hairpin:
        "lia_hairpin"
    attribute smalltears:
        "lia_smalltears"
    attribute bigtears:
        "lia_bigtears"
    if paczka01 == "odebrana":
        "lia_package"
    attribute shadow "lia_shadow"

image p1 = LayeredImageProxy("lia", Transform(zoom=0.65))
image p1pl = LayeredImageProxy("lia", Transform(xalign=0.45,yalign=-0.15))

#######################   RAVEN   ##########################

image raven_eyes_wink:
    "raven_eyes_open"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "raven_eyes_open"
    .23
    "raven_eyes_closed"
    .25
    "raven_eyes_open"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "raven_eyes_closed"
    .25
    "raven_eyes_open"
    .13
    repeat
image raven_eyes_narrowedwink:
    "raven_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "raven_eyes_narrowed"
    .23
    "raven_eyes_closed"
    .25
    "raven_eyes_narrowed"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "raven_eyes_closed"
    .25
    "raven_eyes_narrowed"
    .13
    repeat
image raven_eyes_widenedwink:
    "raven_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "raven_eyes_widened"
    .23
    "raven_eyes_closed"
    .25
    "raven_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "raven_eyes_closed"
    .25
    "raven_eyes_widened"
    .13
    repeat

layeredimage raven:
    always "raven[ravenDress]_base"

    group lips auto:
        attribute lneutral default:
            "raven_lips_lneutral"
    group eyes:
        attribute wink default:
           "raven_eyes_wink"
        attribute open
        attribute closed
        attribute narrowedwink:
            "raven_eyes_narrowedwink"
        attribute widenedwink:
            "raven_eyes_widenedwink"
    group brows auto:
        attribute bneutral default:
            "raven_brows_bneutral"
    attribute blush
    attribute smalltears
    attribute bigtears

    attribute hover_proxy:
        "raven[ravenDress]_base_hover_standard"
        pos (-48,-48)
    attribute hover_proxy_gold:
        "raven[ravenDress]_base_hover_gold"
        pos (-48,-48)
    attribute shadow:
        #"raven[ravenDress]_shadow"
        "raven_covered_shadow"

image p4_idle = LayeredImageProxy("raven", Transform(zoom=0.68))
image p4_hover:
    "raven hover_proxy"
    zoom 0.68
image p4_hover_gold:
    "raven hover_proxy_gold"
image p4 = LayeredImageProxy("raven", Transform(zoom=0.68))

#######################   MEAMIR   ######################

image meamir_eyes_wink:
    "meamir_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "meamir_eyes_neutral"
    .23
    "meamir_eyes_closed"
    .25
    "meamir_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "meamir_eyes_closed"
    .25
    "meamir_eyes_neutral"
    .13
    repeat
image meamir_eyes_narrowedwink:
    "meamir_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "meamir_eyes_narrowed"
    .23
    "meamir_eyes_closed"
    .25
    "meamir_eyes_narrowed"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "meamir_eyes_closed"
    .25
    "meamir_eyes_narrowed"
    .13
    repeat
image meamir_eyes_widenedwink:
    "meamir_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "meamir_eyes_widened"
    .23
    "meamir_eyes_closed"
    .25
    "meamir_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "meamir_eyes_closed"
    .25
    "meamir_eyes_widened"
    .13
    repeat

layeredimage meamir:
    always "meamir_base"

    group lips auto:
        attribute lneutral default

    group eyes:
        attribute wink default:
           "meamir_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "meamir_eyes_narrowedwink"
        attribute widenedwink:
            "meamir_eyes_widenedwink"
        attribute closed

    group brows auto:
        attribute bneutral default

    attribute blush:
        "meamir_blush"
    attribute smalltears:
        "meamir_smalltears"
    attribute bigtears:
        "meamir_bigtears"

    attribute shadow "meamir_shadow"
    attribute hover_proxy "meamir_base_hover"

image p5_idle = LayeredImageProxy("meamir", Transform(zoom=0.93))
image p5_hover:
    "meamir hover_proxy"
    zoom 0.93
image p5 = LayeredImageProxy("meamir", Transform(zoom=0.93))

##########################   SELENE   ############################


image selene_eyes_wink:
    "selene_eyes_open"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "selene_eyes_open"
    .23
    "selene_eyes_closed"
    .25
    "selene_eyes_open"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "selene_eyes_closed"
    .25
    "selene_eyes_open"
    .13
    repeat

layeredimage selene:
    always "selene_base"
    group face auto:
        attribute neutral default
    group eyes:
        attribute wink default:
            "selene_eyes_wink"
    attribute shadow
    attribute hover_proxy "selene_base_hover"

image p2 = LayeredImageProxy("selene")
image p2_idle = LayeredImageProxy("selene")
image p2_hover = "selene hover_proxy"

#image p2 = At("selene_neutral_1", zmn)
#image p2 neutral2 = At("selene_neutral_2", zmn)
#image p2 smile1 = At("selene_smile_1", zmn)
#image p2 smile2 = At("selene_smile_2", zmn)

############################   ZORN   #############################
image zorn_eyes_wink:
    "zorn_neutraleyes"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "zorn_neutraleyes"
    .23
    "zorn_closedeyes"
    .25
    "zorn_neutraleyes"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "zorn_closedeyes"
    .25
    "zorn_neutraleyes"
    .13
    repeat
image zorn_angryeyes_wink:
    "zorn_angryeyes"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "zorn_angryeyes"
    .23
    "zorn_closedeyes"
    .25
    "zorn_angryeyes"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "zorn_closedeyes"
    .25
    "zorn_angryeyes"
    .13
    repeat

layeredimage zorn:
    always "zorn_base"
    group face auto:
        attribute neutral default
    group eyes:
        attribute wink default:
            "zorn_eyes_wink"
        attribute angrywink:
            "zorn_angryeyes_wink"
    attribute shadow
    attribute hover_proxy "zorn_base_hover"

image p3_idle = LayeredImageProxy("zorn")
image p3_hover = "zorn hover_proxy"
image p3 = LayeredImageProxy("zorn")

############################   MOHON   ############################
image mohon_eyes_wink:
    "mohon_neutraleyes"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "mohon_neutraleyes"
    .23
    "mohon_closedeyes"
    .25
    "mohon_neutraleyes"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "mohon_closedeyes"
    .25
    "mohon_neutraleyes"
    .13
    repeat
image mohon_angryeyes_wink:
    "mohon_angryeyes"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "mohon_angryeyes"
    .23
    "mohon_closedeyes"
    .25
    "mohon_angryeyes"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "mohon_closedeyes"
    .25
    "mohon_angryeyes"
    .13
    repeat

layeredimage mohon:
    always "mohon_neutral"
    group eyes:
        attribute wink default:
           "mohon_eyes_wink"
        attribute angrywink:
            "mohon_angryeyes_wink"
    attribute blush:
        "mohon_blush"
    attribute hover_proxy "mohon_neutral_hover"

image p6 = LayeredImageProxy("mohon")
image p6_idle = LayeredImageProxy("mohon")
image p6_hover = "mohon hover_proxy"
############################   AINA   ############################
image aina_eyes_wink:
    "aina_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "aina_eyes_neutral"
    .23
    "aina_eyes_closed"
    .25
    "aina_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "aina_eyes_closed"
    .25
    "aina_eyes_neutral"
    .13
    repeat
image aina_eyes_narrowedwink:
    "aina_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "aina_eyes_narrowed"
    .23
    "aina_eyes_closed"
    .25
    "aina_eyes_narrowed"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "aina_eyes_closed"
    .25
    "aina_eyes_narrowed"
    .13
    repeat
image aina_eyes_widenedwink:
    "aina_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "aina_eyes_widened"
    .23
    "aina_eyes_closed"
    .25
    "aina_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "aina_eyes_closed"
    .25
    "aina_eyes_widened"
    .13
    repeat


layeredimage aina:
    always "aina_base"

    group lips auto:
        attribute lneutral default:
            "aina_lips_lneutral"
    group eyes:
        attribute wink default:
           "aina_eyes_wink"
        attribute open
        attribute closed
        attribute narrowedwink:
            "aina_eyes_narrowedwink"
        attribute widenedwink:
            "aina_eyes_widenedwink"

    group brows auto:
        attribute bneutral default:
            "aina_brows_bneutral"
    attribute blush
    attribute smalltears
    attribute bigtears
    attribute shadow
    attribute hover_proxy:
        pos (-48,-48)
        "aina_base_hover"
    attribute hover_proxy_gold:
        pos (-48,-48)
        "aina_base_hover_gold"

image p7 = LayeredImageProxy("aina")
image p7_idle = LayeredImageProxy("aina")
image p7_hover = "aina hover_proxy"
image p7_hover_gold:
    "aina hover_proxy_gold"

#imagebutton auto "p7_%s" focus_mask True action Return("aina")
#imagebutton idle "p7" hover "p7_hover_gold" xpos 0.2 yalign 1.0 focus_mask True action NullAction()


########################### STRAŻNICY ################################
image p11 = "guard_blue"
image p12 = "guard"
########################### ARCHITEKT ################################
image architect_eyes_wink:
    "architect_eyes_open"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "architect_eyes_open"
    .23
    "architect_eyes_closed"
    .25
    "architect_eyes_open"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "architect_eyes_closed"
    .25
    "architect_eyes_open"
    .13
    repeat

layeredimage architect:
    always "architect_base"
    group face auto:
        attribute neutral default
    group eyes:
        attribute wink default:
            "architect_eyes_wink"
    attribute hover_proxy "architect_base_hover"

image p13_idle = LayeredImageProxy("architect")
image p13_hover:
    "architect hover_proxy"
image p13 = LayeredImageProxy("architect")
image p13_monument_button_hover:
    "p13_hover"
    xzoom -1
    zoom 0.5
image p13_monument_button_idle:
    "p13_idle"
    xzoom -1
    zoom 0.5




################################# HENRIETTA ####################################


image henrietta_eyes_wink:
    "henrietta_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "henrietta_eyes_neutral"
    .23
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_neutral"
    .13
    repeat
image henrietta_eyes_narrowedwink:
    "henrietta_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "henrietta_eyes_narrowed"
    .23
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_narrowed"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_narrowed"
    .13
    repeat
image henrietta_eyes_widenedwink:
    "henrietta_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "henrietta_eyes_widened"
    .23
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "henrietta_eyes_closed"
    .25
    "henrietta_eyes_widened"
    .13
    repeat

layeredimage henrietta:
    always "henrietta_base"

    group lips auto:
        attribute lneutral default

    #warstwa BRWI pod warstwą OCZY bo ma doczepiony makijaż
    group brows auto:
        attribute bneutral default

    group eyes:
        attribute wink default:
           "henrietta_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "henrietta_eyes_narrowedwink"
        attribute widenedwink:
            "henrietta_eyes_widenedwink"
        attribute closed

    attribute blush:
        "henrietta_blush"
    attribute smalltears:
        "henrietta_smalltears"
    attribute bigtears:
        "henrietta_bigtears"

    attribute shadow "henrietta_shadow"
    attribute hover_proxy:
        pos (-48,-96)
        "henrietta_base_hover"
    attribute hover_proxy_gold:
        pos (-48,-96)
        "henrietta_base_hover_gold"

image p8_idle = LayeredImageProxy("henrietta")
image p8_hover:
    "henrietta hover_proxy"

image p8_hover_gold:
    "henrietta hover_proxy_gold"
image p8 = LayeredImageProxy("henrietta")
#imagebutton idle "p8" hover "p8_hover_gold" xpos 0.2 yalign 1.0 focus_mask True action NullAction()


################################# CIRDAN ####################################


image cirdan_eyes_wink:
    "cirdan_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "cirdan_eyes_neutral"
    .23
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_neutral"
    .13
    repeat
image cirdan_eyes_narrowedwink:
    "cirdan_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "cirdan_eyes_narrowed"
    .23
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_narrowed"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_narrowed"
    .13
    repeat
image cirdan_eyes_widenedwink:
    "cirdan_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "cirdan_eyes_widened"
    .23
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "cirdan_eyes_closed"
    .25
    "cirdan_eyes_widened"
    .13
    repeat

layeredimage cirdan:
    always "cirdan_base"

    group eyes:
        attribute wink default:
           "cirdan_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "cirdan_eyes_narrowedwink"
        attribute widenedwink:
            "cirdan_eyes_widenedwink"
        attribute closed

    group lips auto:
        attribute lneutral default

    group brows auto:
        attribute bneutral default

    attribute blush:
        "cirdan_blush"
    attribute smalltears:
        "cirdan_smalltears"
    attribute bigtears:
        "cirdan_bigtears"

    attribute shadow "cirdan_shadow"
    attribute hover_proxy:
        pos (-48,-48)
        "cirdan_base_hover"
    attribute hover_proxy_gold:
        pos (-48,-48)
        "cirdan_base_hover_gold"

image p16_idle = LayeredImageProxy("cirdan")
image p16_hover:
    "cirdan hover_proxy"

image p16_hover_gold:
    "cirdan hover_proxy_gold"
image p16 = LayeredImageProxy("cirdan")
#imagebutton idle "p8" hover "p8_hover_gold" xpos 0.2 yalign 1.0 focus_mask True action NullAction()


################################# CIRDAN ####################################

image ove_eyes_wink:
    "ove_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "ove_eyes_neutral"
    .23
    "ove_eyes_closed"
    .25
    "ove_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "ove_eyes_closed"
    .25
    "ove_eyes_neutral"
    .13
    repeat
image ove_eyes_narrowedwink:
    "ove_eyes_angry"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "ove_eyes_angry"
    .23
    "ove_eyes_closed"
    .25
    "ove_eyes_angry"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "ove_eyes_closed"
    .25
    "ove_eyes_angry"
    .13
    repeat

layeredimage ove:
    always "ove_base"

    group eyes:
        attribute wink default:
           "ove_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "ove_eyes_narrowedwink" # to jest wersja 'angry' oczu u p10
        attribute closed

    group brows auto:
        attribute bneutral default

    attribute shadow "ove_shadow"
    attribute hover_proxy:
        pos (-48,-48)
        "ove_base_hover_standard"
    attribute hover_proxy_gold:
        pos (-48,-48)
        "ove_base_hover_gold"

image p10_idle = LayeredImageProxy("ove")
image p10_hover:
    "ove hover_proxy"

image p10_hover_gold:
    "ove hover_proxy_gold"
image p10 = LayeredImageProxy("ove")
#imagebutton idle "p10" hover "p10_hover_gold" xpos 0.2 yalign 1.0 focus_mask True action NullAction()




image levius_eyes_wink:
    "levius_eyes_neutral"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "levius_eyes_neutral"
    .23
    "levius_eyes_closed"
    .25
    "levius_eyes_neutral"
    choice:
        .91
    choice:
        1.4
    #choice:
    #    4.5
    "levius_eyes_closed"
    .25
    "levius_eyes_neutral"
    .13
    repeat
image levius_eyes_narrowedwink:
    "levius_eyes_narrowed"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "levius_eyes_narrowed"
    .23
    "levius_eyes_closed"
    .25
    "levius_eyes_narrowed"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "levius_eyes_closed"
    .25
    "levius_eyes_narrowed"
    .13
    repeat
image levius_eyes_widenedwink:
    "levius_eyes_widened"
    choice:
        2.2
    choice:
        3.0
    choice:
        4.3
    choice:
        3.5
    "levius_eyes_widened"
    .23
    "levius_eyes_closed"
    .25
    "levius_eyes_widened"
    .91
    #choice:
    #    1.2
    #choice:
    #    2.5
    "levius_eyes_closed"
    .25
    "levius_eyes_widened"
    .13
    repeat

layeredimage levius:
    always "levius_base"

    group eyes:
        attribute wink default:
           "levius_eyes_wink"
        attribute narrowedwink: # zdefiniowane powyżej
            "levius_eyes_narrowedwink"
        attribute widenedwink:
            "levius_eyes_widenedwink"
        attribute closed

    group lips auto:
        attribute lneutral default

    group brows auto:
        attribute bneutral default

    attribute blush:
        "levius_blush"
    attribute smalltears:
        "levius_smalltears"
    attribute bigtears:
        "levius_bigtears"

    attribute shadow "levius_shadow"
    attribute hover_proxy:
        pos (-48,-48)
        "levius_base_hover"
    attribute hover_proxy_gold:
        pos (-48,-48)
        "levius_base_hover_gold"

image p9_idle = LayeredImageProxy("levius")
image p9_hover:
    "levius hover_proxy"

image p9_hover_gold:
    "levius hover_proxy_gold"
image p9 = LayeredImageProxy("levius")
#imagebutton idle "p8" hover "p8_hover_gold" xpos 0.2 yalign 1.0 focus_mask True action NullAction()
