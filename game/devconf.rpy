init:
    define config.developer = "auto"






# helper stuff

label card_choice:
    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ cecha NOTHING":
                $ c_nothing = True
                $ c_destiny = False
                $ c_hal = False
                pass
            "dev/ cecha DESTINY":
                $ c_nothing = False
                $ c_destiny = True
                $ c_hal = False
                pass
            "dev/ cecha HAL":
                $ c_nothing = False
                $ c_destiny = False
                $ c_hal = True
                pass
    ########################### /devstuff #########################
    return