default jb = 1
init:
    style journal_names:
        xalign 0.5
        xpos 0.36
        ypos 0.08
        color "#210505"
        font "Cookie-Regular.ttf"
        size 70

    style journal_date:
        font "Cinzel-Regular.ttf"
        xalign 0.5
        xpos 0.75
        ypos 0.06
        color "#210505"
        size 20

    style journal_titles:
        font "Cinzel-Regular.ttf"
        color "#210505"
        size 42

    style journal_about:
        font "Caveat-Regular.ttf"
        color "#210505"
        size 24




screen journal_base():
    # tag dziennik
    zorder 35
    add "dziennik_bg"
    add "dziennik_base"
    add "dziennik_likeindicator_base"
    text "[weekdayName!u] [day]" style "journal_date"
    text __("Notatki:") xpos 0.22 ypos 0.15 style "journal_titles"
    text __("Do zrobienia:") xpos 0.22 ypos 0.49 style "journal_titles"
    text __("Najważniejsze:") xpos 0.63 ypos 0.1 style "journal_titles"
    text __("Opcjonalne:") xpos 0.63 ypos 0.49 style "journal_titles"
    if HatePath > 0:
        add "dziennik_hateindicator_lvl[HatePath]"
    if LovePath > 0:
        add "dziennik_loveindicator_lvl[LovePath]"
    use journal_bookmarks
    use journal_buttons

screen journal_buttons():
    zorder 65
    # imagebutton auto "dziennik_button_dialogue_%s" focus_mask True

    imagebutton auto "dziennik_button_help_%s" focus_mask True


screen journal_bookmarks():
    zorder 55
    imagebutton auto "dziennik_button_aina_%s" focus_mask True action ShowTransient('journal_bookmark1')
    imagebutton auto "dziennik_button_cirdan_%s" focus_mask True action  ShowTransient('journal_bookmark2')
    imagebutton auto "dziennik_button_henrietta_%s" focus_mask True action ShowTransient('journal_bookmark3')
    imagebutton auto "dziennik_button_levius_%s" focus_mask True action ShowTransient('journal_bookmark4')
    imagebutton auto "dziennik_button_meamir_%s" focus_mask True action ShowTransient('journal_bookmark5')
    imagebutton auto "dziennik_button_raven_%s" focus_mask True action ShowTransient('journal_bookmark6')
    imagebutton auto "dziennik_button_others_%s" focus_mask True action ShowTransient('journal_bookmark7')


screen journal_bookmark1():
    zorder 50

    modal True
    tag dziennik
    use journal_base
    if AinaHate > 0:
        add "dziennik_hateindicator_lvl[AinaHate]"
    if AinaLove > 0:
        add "dziennik_loveindicator_lvl[AinaLove]"

    text "Aina" style "journal_names"

    # about
    fixed:
        area (.22,.21,530,500)
        text "Przybieżeli do Betlejem pasterze Grając skocznie Dzieciąteczku na lirze Chwała na wysokości, chwała na wysokości, a pokój na ziemi Chwała na wysokości, chwała na wysokości, a pokój na ziemi Oddawali swe ukłony w pokorze Tobie z serca ochotnego, o Boże! Chwała na wysokości, chwała na wysokości, a pokój na ziemi Chwała na wysokości, chwała na wysokości, a pokój na ziemi Anioł Pański sam ogłosił te dziwy Których oni nie słyszeli, jak żywi Chwała na wysokości, chwała na wysokości, a pokój na ziemi" style "journal_about"
    #todo
    fixed:
        area (.22,.55,530,500)
        text " - Nulla senserit doctrina do quem a te dolore nescius. \n - Expetendis minim export ullamco velit, fugiat voluptate o duis dolore, a hic graviterque, veniam admodum ab labore tempor.\n - Duis mandaremus ad quem malis, sed amet arbitrantur, de export consequat, \n - occaecat esse sunt iudicem nulla." style "journal_about"

    #najważniejsze
    fixed:
        area (.63,.16,480,500)
        text " - Nulla senserit doctrina do quem a te dolore nescius. \n - Expetendis minim export ullamco velit, fugiat voluptate o duis dolore, a hic graviterque, veniam admodum ab labore.\n - Duis mandaremus ad quem malis, sed amet arbitrantur, de export consequat, \n - occaecat esse sunt iudicem nulla." style "journal_about"

    #opcjonalne
    fixed:
        area (.63,.55,480,500)
        text " - Nulla senserit doctrina do quem a te dolore nescius. \n - Expetendis minim export ullamco velit, fugiat voluptate o duis dolore, a hic graviterque, veniam admodum.\n - Duis mandaremus ad quem malis, sed amet arbitrantur, de export consequat" style "journal_about"



    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark1")

screen journal_bookmark2():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    if CirdanHate > 0:
        add "dziennik_hateindicator_lvl[CirdanHate]"
    if CirdanLove > 0:
        add "dziennik_loveindicator_lvl[CirdanLove]"
    text "Cirdan" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark2")

screen journal_bookmark3():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    if HenriettaHate > 0:
        add "dziennik_hateindicator_lvl[HenriettaHate]"
    if HenriettaLove > 0:
        add "dziennik_loveindicator_lvl[HenriettaLove]"
    text "Henrietta" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark3")

screen journal_bookmark4():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    if LeviusHate > 0:
        add "dziennik_hateindicator_lvl[LeviusHate]"
    if LeviusLove > 0:
        add "dziennik_loveindicator_lvl[LeviusLove]"
    text "Levius" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark4")

screen journal_bookmark5():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    if MeamirHate > 0:
        add "dziennik_hateindicator_lvl[MeamirHate]"
    if MeamirLove > 0:
        add "dziennik_loveindicator_lvl[MeamirLove]"
    text "Meamir" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark5")

screen journal_bookmark6():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    if RavenHate > 0:
        add "dziennik_hateindicator_lvl[RavenHate]"
    if RavenLove > 0:
        add "dziennik_loveindicator_lvl[RavenLove]"
    text "Raven" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark6")

screen journal_bookmark7():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    text "Inni" style "journal_names"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark7")
