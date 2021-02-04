screen chooseYourCard():
    modal True
    style_prefix "ttkarty"
    add "black"
    text "{size=35}What do you want from life?{/size}":
        align (0.5,0.045)
    $ tooltip = GetTooltip()
    if tooltip:
        frame at ttobiekt_appear:
            style "ttkarty"
            text "[tooltip]"

    button:
        xysize (439, 740)
        align (0.5,0.5) pos (0.25,0.45)
        add "karta_1_button"
        #focus_mask True
        action NullAction()
        tooltip __("{size=30}{color=#a6870a}NIC{/color}{/size}\n\n\"Nie chcę niczego. \"")
    button:
        xysize (439, 740)
        align (0.5,0.5) pos (0.5,0.45)
        add "karta_2_button"
        #focus_mask True
        action NullAction()
        tooltip __("{size=30}{color=#d1713d}PRZEZNACZENIE{/color}{/size}\n\n\"Może czeka na mnie coś więcej… \"")
    button:
        xysize (439, 740)
        align (0.5,0.5) pos (0.75,0.45)
        add "karta_3_button"
        #focus_mask True
        action NullAction()
        tooltip __("{size=30}{color=#ba243c}SZCZĘŚCIE I MIŁOŚĆ{/color}{/size}\n\n\"Chciałabym kogoś sobie znaleźć i być szczęśliwa.\"")
