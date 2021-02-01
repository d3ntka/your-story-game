screen journal_base():
    # tag dziennik
    zorder 35
    add "dziennik_base"
    add "dziennik_likeindicator_base"
    if HatePath > 0:
        add "dziennik_hateindicator_lvl[HatePath]"
    use journal_bookmarks
    use journal_buttons

screen journal_buttons():
    zorder 65
    imagebutton auto "dziennik_button_dialogue_%s" focus_mask True

    imagebutton auto "dziennik_button_help_%s" focus_mask True


screen journal_bookmarks():
    zorder 55
    imagebutton auto "dziennik_button_aina_%s" focus_mask True action ShowTransient('journal_bookmark1')
    imagebutton auto "dziennik_button_cirdan_%s" focus_mask True action ShowTransient('journal_bookmark2')
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
    add "dziennik_likeindicator_like3"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark1")


screen journal_bookmark2():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    add "dziennik_likeindicator_hate3"
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark2")



screen journal_bookmark3():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark3")

screen journal_bookmark4():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark4")


screen journal_bookmark5():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark5")


screen journal_bookmark6():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark6")


screen journal_bookmark7():
    zorder 50
    modal True
    tag dziennik
    use journal_base
    imagebutton auto "dziennik_button_exit_%s" focus_mask True action Hide("journal_bookmark7")
