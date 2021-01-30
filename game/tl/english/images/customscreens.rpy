################################################################################
## Initialization
################################################################################

init offset = 0


######################## KARTY ##############################

image card1_text = Text("siabadaba1")
image card2_text = Text("To teraz jeszcze pytanie co z tekstem XD pisać go na kartach? czy może dopiero będzie się pojawiał jak się obróci?")
image card3_text = Text("napis na górze będzie z info co to w ogóle tu się dzieje")

image karta_1:
    "card_nothing"
image karta_2:
    "card_destiny"
image karta_3:
    "card_love"
image karta_back:
    "card_back"

image karta_1_back:
    "karta_1"
    xsize 439
    linear 0.1 xsize 0
    "karta_back"
    xsize 0
    linear 0.1 xsize 439

image karta_back_1:
    "karta_back"
    xsize 439
    linear 0.1 xsize 0
    "karta_1"
    xsize 0
    linear 0.1 xsize 439

image karta_2_back:
    "karta_2"
    xsize 439
    linear 0.1 xsize 0
    "karta_back"
    xsize 0
    linear 0.1 xsize 439

image karta_back_2:
    "karta_back"
    xsize 439
    linear 0.1 xsize 0
    "karta_2"
    xsize 0
    linear 0.1 xsize 439

image karta_3_back:
    "karta_3"
    xsize 439
    linear 0.1 xsize 0
    "karta_back"
    xsize 0
    linear 0.1 xsize 439

image karta_back_3:
    "karta_back"
    xsize 439
    linear 0.1 xsize 0
    "karta_3"
    xsize 0
    linear 0.1 xsize 439

image karta_1_button:
    #"karta_1"
    align (0.5,0.5)
    on idle:
        "karta_1_back"
    on hover:
        "karta_back_1"

image karta_2_button:
    #"karta_back"
    align (0.5,0.5)
    on idle:
        "karta_2_back"
    on hover:
        "karta_back_2"

image karta_3_button:
    #"karta_3"
    align (0.5,0.5)
    on idle:
        "karta_3_back"
    on hover:
        "karta_back_3"


screen chooseYourCard():
    modal True
    style_prefix "ttkarty"
    add "black"
    text __("{size=35}Czego oczekujesz od życia?{/size}"):
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


############################## / KARTY #########################################
