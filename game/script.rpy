# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    image grtextbox = Image("gui/main_button_hover.png") #testowy zamienny textbox

define gr = Character(_("Ty"), color=gui.text_color, what_color="#e46d70") #, window_background="grtextbox")
define p1 = Character("Lia", color="#e46d70", image="p1")
define p2 = Character("Selene", color="#45428c")
define p3 = Character("Zorn", color="#9b2121")
define p4 = Character("Raven", color="#e2622a", image="p4")
define p5 = Character("Meamir", color="#794890", image="p5")
define p5q = Character("???", color="#794890")
define p6 = Character("Mohon", color="#a39700")
define p7 = Character("Aina", color="#9c3636")
define p7q = Character("???", color="#9c3636")
define p8 = Character("Henrietta", color="#bb7949")
define p9 = Character("Levius", color="#465a78")
define p9q = Character("Levius", color="#465a78")
define p10 = Character("Ove", color="#646464")
define p11 = Character(_("Strażnik"), color="#60c090")
define p12 = Character(_("Strażnik"), color="#7d9999")
define p13 = Character(_("Architekt"), color="#1b7523")
define p16 = Character("Cirdan", color="#9b7e79")
define p16q = Character("???", color="#9b7e79")


#define p14 = Character(_("Starsza pani"), color="#d0cbcb") #"Old Lady" w tłumaczeniu
#define p15 = Character("Aurora", color="#fbf49d")

define r1 = Character(_("Gość"))
define b1 = Character(_("Bandyta 1"))
define b2 = Character(_("Bandyta 2"))
define tg1 = Character("???", color="#6b2e0d")
define tg2 = Character("???", color="#757e55")
define tg3 = Character("???", color="#9d7a59")



default timeout = 10.0 #The amount of time in seconds before the choice times out. Set this variable to whatever default amount of time you want it to be.
default timeout_label = None #The label to jump to when the choice times out



###### decyzje

default d_koszmar = False
default d_e1_senmarzen = False
default d_e1_senneutral = False
default persistent.nicniemow = 0
default d_gofestiwal = False
default d_krotkienogiklamstwa = 0
default persistent.galleryunlock = False


###### zmienne

default day = 1
default dt = 1 ######### zmienna czasu iksde
default weekday = 1
default weekdayName = "poniedziałek"
default lok = "taw"
default licznikAkcji = 0
default powrotPoNocy = 0
default ee = 0 ##Etap Eksploracji
default ravenDress = "_covered" #sluzy do uzupelnienia nazwy pliku zeby korzystalo ze starej sukienki do czasu e8_p4 gdzie jest to zamienione na "" dla nowej sukienki
default jakoscDrzewa = "" #zrobic skale od 1 do 6 czy iles i dodac do nazwy pliku tj ravenDress

default zm_tutorial_jrnl_done = False

######### cechy
default c_destiny = False
default c_hal = False
default c_nothing = False
default hairpin = True
default paczka01 = "pusto" #"oczekuje", "odebrana", "oddana"


######### cienka granica między miłością a nienawiścią
default LovePath = 0
default HatePath = 0
default RavenLove = 0
default RavenHate = 0
default MeamirLove = 0
default MeamirHate = 0
default LeviusLove = 0
default LeviusHate = 0
default HenriettaLove = 0
default HenriettaHate = 0
default CirdanLove = 0
default CirdanHate = 0
default AinaLove = 0
default AinaHate = 0

###### dodatkowe zmienne
default StrazWiedza = 0
default ArchitektWiedza = 0


######### main room stuff
default z_zyrandole = True
default z_dekoracje = True
default z_beer = True
#Syf w mainroom:
default z_tablemess = False
default z_floorflourmess = False
default z_floorwinemess = False
default z_barrightmess = False
default z_barleftmess = False


#zmienne eventow:

default akt1_UkonczenieEpizodow = { 'e7_p5': False, 'e7_p4': False, 'e7_n': False }

default ee001_UkonczenieEpizodow = { 'e8_p16': False, 'e8_p4': False, 'e8_p5': False,
                                    'e8_work1': False, 'e8_work2': False, 'e9': False
                                    }

default ee001_UkonczenieDialogow = {'p2_d01': False, 'p2_d02': False,
                                    'p3_d00': False, 'p3_d01': False, 'p3_d02': False,
                                    'p4_d00': False,
                                    'p5_d00': False,
                                    'p6_d00': False, 'p6_d01': False,
                                    'p7_d00': False, 'p7_d01': False, 'p7_d02': False, 'p7_d03': False,
                                    'p8_d00': False,
                                    'p9_d00': False,
                                    }

default akt2_ep10_UkonczenieRozmow = {  'p4': False, 'p5': False, 'p7': False,
                                        'p8': False, 'p9': False,
                                        'p16a': False, 'p16b': False
                                        }

default PaczkaRozrabiaka = False



###### kanaly audio
init python:
    renpy.music.register_channel("sfx","sfx",False)
    renpy.music.register_channel("ambient","sfx",True,tight=True)
    renpy.music.register_channel("music2","music",True)
    renpy.music.register_channel("musictight","music",True,tight=True)



####### definiowane obrazy podstawowe
image black = "#000"
image white = "#FFF"
image grey = "#060606"


default updatetest_demo4_0 = True  # przy persistent zmieniać datę i if'a niżej w label splashscreen

label splashscreen:
    call screen splash
    if updatetest_demo4_0: #aktualizowac date przy nowym update
        call screen nowosci
        $ updatetest_demo4_0 = False #aktualizowac date przy nowym update
    return

# JEDZIEMY Z TYM KOKSEM
label start:
################################################################################
########################## przeskok do gry własciwej ###########################
    stop music
    if config.developer:
        jump devskroty
    else:
        jump begin
################################################################################
################################################################################

    show text "This is only a game" at truecenter
    with dissolve
    show text "This is not  a game" at truecenter with Dissolve(0.1)
    pause 0.1
    show text "This is only a game" at truecenter
    pause 1
    show text "This is not  a game" at truecenter with Dissolve(0.1)
    pause 0.1
    show text "This is only a game" at truecenter
    pause 1
    hide text
    with dissolve

################################################################################

label devskroty hide:
    menu:
        #"testy i inne":
        #    jump metastuff
        "dev/ testy":
            jump testowanie
        "dev/ mapka do demo":
            jump testymapy
        "dev/ epizody":
            call screen wyborepizodow

    #menu metastuff:
    #    "testy":
    #        jump testy
    #    "rzeczy do trailera":
    #        jump trailerstuff
    #    "allor, screeny!":
    #        jump screeny
    #    "zobaczmy mape":
    #        jump akt2_mapa

label testymapy:
    jump ee_tavern_liaroom






screen wyborepizodow():
    add "anim_cg_tavern_wall"

    grid 4 8:
        align (.5,.5)
        #xfill True
        #yfill True
        textbutton "epizod 1" action Jump("begin")
        textbutton "epizod 1a" action Jump("e1a")
        textbutton "epizod 1b" action Jump("e1b")
        null

        textbutton "epizod 2a" action Jump("e2a")
        textbutton "epizod 2b" action Jump("e2b")
        textbutton "epizod 3" action Jump("e3")
        null

        textbutton "epizod 4" action [SetVariable("d_gofestiwal", True), Jump("e4")]
        textbutton "epizod 5" action Jump("e5")
        textbutton "epizod 6" action Jump("e6")
        null

        textbutton "epizod 7 P4" action Jump("epizod7p4")
        textbutton "epizod 7 P5" action Jump("epizod7p5")
        textbutton "epizod 7 N" action Jump("epizod7n")
        null

        textbutton "epizod 8 intro" action Jump("epizod8")
        textbutton "epizod 8 P4" action Jump("e8_p4")
        textbutton "epizod 8 P5" action Jump("e8_p5")
        null

        null
        null
        null
        null

        textbutton "ee000" action Jump("ee000")
        textbutton "testymapy" action Jump("testymapy")
        null
        null

        null
        null
        null
        null

################################################################################
####################     AKT PIERWSZY       ####################################
#############################   EPIZOD PIERWSZY    #############################
################################################################################
label begin:

    ######################## napis demo #######################
    show screen demo
    screen demo():
        zorder 99
        if ee == 0:
            add "demo_version"
        elif ee >= 0:
            add "demo_version_ee"
    ###########################################################

    # $ preferences.system_cursor = False

    jump e1



################################################################################
###############################   EE-000  ######################################
label ee000:
    if config.developer:
        scene black
        show text "ee000" at truecenter
        pause 1

    if akt1_UkonczenieEpizodow["e7_p4"] == True:
        $ jrnl_raven_about = jrnl_raven_about_n02_chosen
        $ jrnl_meamir_about = jrnl_meamir_about_n02_notchosen
        $ jrnl_meamir_todo_1 = jrnl_meamir_todo_n02_notchosen
    elif akt1_UkonczenieEpizodow["e7_p5"] == True:
        $ jrnl_meamir_about = jrnl_meamir_about_n02_chosen
        $ jrnl_meamir_todo_1 = jrnl_meamir_todo_n02_chosen
        $ jrnl_raven_about = jrnl_raven_about_n02_notchosen
    else:
        $ jrnl_meamir_about = jrnl_meamir_about_n02_notchosen
        $ jrnl_meamir_todo_1 = jrnl_meamir_todo_n02_notchosen
        $ jrnl_raven_about = jrnl_raven_about_n02_notchosen

    $ jrnl_raven_todo_1 = jrnl_raven_todo_n02
    $ jrnl_important_1 = jrnl_important_n02

    play music alexander_nakarada_adventure fadein 3.0 fadeout 5.0 volume 0.5
    scene anim_room_lia_morning with fc
    show p1pl wink_player with fc
    p1 "Uh... Możesz przejąć stery na chwilę? Sporo emocji po wczoraj i zbyt zamyślona jestem."
    p1 "Powinnam zejść na śniadanie do kuchni."
    jump ee000_tavern_liaroom


################################################################################
##############################   EPIZOD 8   ####################################
label epizod8:
    if config.developer:
        scene black
        show text "epizod8" at truecenter
        pause
    default p2_d01_check = False
    ### Epizod 8 zaczyna się w kuchni
    scene room_kitchenday
    #Na ekranie: Kuchnia, całkiem po lewej stoi Raven oraz Selen skierowane do siebie (jakby rozmawiały), na prawo od nich stoi Zorn patrząc także na nich. W momencie gdy wchodzi Lia Zorn odwraca się do niej pierwszy
    show p4:
        align (-0.01,1.0)
    show p2:
        align (0.3,1.0)
    show p3:
        align (0.6,1.0)
        xzoom -1
    with dissolve
    show p1:
        align (1.1,1.0)
        linear 2 align (0.95,1.0)
    show p3 with fc:
        xzoom 1
    p3 "Dzień dobry, co to się stało, że wstałaś tak wcześnie?"
    p1 "Dzień dobry. Nic konkretnego... po prostu wstałam i tyle."
    "Zorn nie kontynuował, wiedział, że nie ma to chyba żadnego sensu."
    "Lia zerknęła lekko po wszystkich, trafiła chyba na moment ciszy."
    "Zwróciła uwagę, że jej mama wpatruje się w Raven oczekując odpowiedzi."
    show p2 with fc:
        xzoom -1
    # Selene obraca się w stronę Lii
    "W tym samym momencie Selene spostrzegła, że dołączyła do nich córka."
    p2 "O miło, że jesteś - właśnie składaliśmy z ojcem pewną propozycję Raven."
    p1 "Oh, tak?"
    p2 "Tak - pomyśleliśmy, że to będzie właściwa rzecz do zrobienia..."
    # Selene obraca się z powrotem w stronę Raven
    show p2 with fc:
        xzoom 1
    p2 "Oh. Raven moja droga, widzę, że się wahasz - bez obaw."
    p2 "Nie musisz odpowiadać teraz. Najpierw odpocznij kilka dni - sporo przeszłaś."
    p2 "Tymczasem, przygotowałam Ci jakieś ubrania - są w Twoim pokoju."
    p2 "Jeśli masz ochotę to możesz od razu iść się przebrać w coś wygodnego."
    p2 "Na pewno Lia później do Ciebie dołączy i o wszystkim Ci opowie. Prawda Lia?"
    # Smile Lia ON
    show p1 lsmile with fc
    p1 "Yyy.. Tak! Oczywiście. Nie martw się Raven, wszystko Ci pokażę!"
    # Blush Raven ON
    show p4 blush with fc
    p4 "Ojej, bardzo Pani dziękuję. Tobie też, Lia. To pójdę od razu się przebrać."
    # Raven wychodzi
    show p4 -blush with fc
    show p4 with fc:
        xzoom -1
    show p4:
        linear 2.5 align (-0.4, 1.0)
    "Po wyjściu Raven nastąpiła krótka cisza, którą pierwszy przerwał ojciec."
    p3 "No dobrze, tylko pamiętaj by się tym zająć, Lia. Dziewczyna cały czas jest w szoku."
    p3 "Pokaż jej okolicę, zajmij się nią. Jest teraz Twoim obowiązkiem, przynajmniej na początku."
    p3 "Musisz nauczyć się odpowiedzialności."
    "Lia chciała odpowiedzieć, ale nie miała okazji bo ojciec kontynuował."
    p3 "Ale dziś jeszcze musisz pomóc trochę w pracy, zajmij się barem, a potem zanieś zamówienie do kuźni."
    p3 "Rozumiemy się, tak?"
    p1 "Oczywiście. A gdzie to zamówienie?"
    "Odpowiedziała Lia wiedząc, że nie ma sensu wdawać się w dyskusję."
    p3 "Będzie czekało na Ciebie przy barze. A teraz zmykaj, zajmij się pracą."
    "Lia nie spodziewała się niczego innego, znów w wir pracy. Jak zwykle."
    "Pozostało teraz jedynie zdecydować co najpierw..."
    $ paczka01 = "oczekuje"
    hide p3 with easeoutleft
    pause 0.5
    scene black

####### event P2-D01 ##########
    while _return != "go_ee001":
        call screen ee_tavern_kitchen_d01 with dissolve
        if _return == "P2-D01":
            scene room_kitchenday
            show p2:
                align (0.3, 1.0)
            show p1:
                align (0.7, 1.0)
            with dissolve
            show p2 with dissolve:
                xzoom -1
            p2 "Lia..."
            "Powiedziała Selene spokojnym głosem spoglądając na swoją córkę."
            "Mówiła dalej. W głosie słychać było matczyną troskę..."
            p2 "Jak się czujesz? Wszystko dobrze?"
            p1 "Chyba tak, dlaczego pytasz?"
            p2 "Po prostu się o Ciebie martwię. Dużo przed Tobą."
            p1 "Oj mamo, nie przesadzaj... Aż tyle przecież się nie dzieje..."
            p2 "Oh, dziecko drogie. Może jeszcze tego nie widzisz, ale życie nie będzie stało w miejscu."
            p1 "No wiem, ale..."
            p2 "Cicho. Nie przerywaj mi teraz."
            p2 "Ojciec ma rację, musisz nauczyć się odpowiedzialności oraz samodzielności."
            p2 "Pamiętaj, że nie zawsze będziemy w pobliżu, żeby Ci pomóc."
            p2 "Mam nadzieję, że w ciągu tych najbliższych dni pokażesz nam, że jesteś w stanie sobie poradzić z prostymi rzeczami."
            p1 "Czemu tak nagle Wam na tym zależy?"
            p2 "Jak mówiłam, życie nie stoi w miejscu. Prędzej czy później by Ciebie to czekało."
            p2 "Pewne wydarzenia to trochę przyspieszyły, ale wierzę, że dasz radę."
            p2 "A teraz zbieraj się, masz obowiązki. Ja muszę iść coś załatwić."
            p1 "No dobrze..."
            "Lia nie dokończyła swojej wypowiedzi i już zauważyła, że matka opuściła kuchnię."
            show p2 with fc:
                xzoom 1
            # Selene wychodzi w lewo z pomieszczenia i kuchnia jest pusta
            hide p2 with easeoutleft
            "Przez moment Lia zastanawiała się nad jej słowami."
            "Nie mogła jednak pojąć dziwnego zachowania mamy."
            "Otrząsnęła się szybko z zamyślenia i wróciła do teraźniejszości."
            hide p1 with fc
            $ p2_d01_check = True #p2 znika po tej rozmowie
    jump ee_001_intro

    ################
    #Po wyjściu z kuchni i powrocie Selene już nie będzie, Kuchnia będzie pusta. Rozmowa tylko dostępna od razu po zakończeniu wcześniejszego dialogu. Wyjście z kuchni prowadzi do Sali Głównej. Przechodzimy do EE-001

screen ee_tavern_kitchen_d01(): # /|\ do eventu P2-D01 powyżej /|\
    tag ee
    modal True
    add "room_kitchenday"
    if not p2_d01_check:
        imagebutton auto "p2_%s" focus_mask True xalign 0.3 yalign 1.0 action Return("P2-D01")
    imagebutton auto "room_lia_exit_%s" focus_mask True action Return("go_ee001")
###################
label ee_001_intro:
    scene img_tavern_mainroom
    show p1pl wink_player
    with dissolve
    $ renpy.free_memory()

    p1 "Uhh... Co teraz?"
    menu:
        "To zależy od Ciebie.":
            pass
    #sad Lia ON
    show p1pl bneutral wink_player lsad with fc
    p1 "Eh..."
    p1 "..."
    #surprised_neutral Lia ON
    show p1pl bsurprised widenedwink_player lneutral with fc
    p1 "A co gdyby to nie zależało ode mnie?"
    menu:
        "Co masz na myśli?":
            pass
    #surprised_happy Lia ON
    show p1pl bsurprised widenedwink_player lsmile with fc
    p1 "Mogłoby to na przykład zależeć od Ciebie..."
    menu:
        "Hmm. Niby w jaki sposób?":
            pass
    #smile Lia ON
    show p1pl bneutral wink_player lsmile with fc
    p1 "Po prostu powiesz co mam robić lub mówić, a ja będę to robić!"
    p1 "I tak przeważnie nie ma czasu lub możliwości dyskutować o wszystkim."
    p1 "To co, co na to powiesz?"
    menu:
        "Możemy chyba spróbować...":
            pass
    #blush Lia ON
    show p1pl blush with fc
    p1 "Super! Wiedziałam, że mogę na Ciebie liczyć!"
    #smile Lia ON
    show p1pl bneutral wink_player lsmile with fc
    #w momencie “oddaję się w Twoje ręce.” trzeba wymyślić jakiś taki mistycznie fajny dźwięk w tle co by nie był zbyt mocny, zostawiam to w takiej formie, żeby podyskutować o tym jak tu będziesz bo jeszcze nic nie wykminiłem
    p1 "To teraz wszystko zależy od Ciebie! Oddaję się w Twoje ręce."
    gr "Spokojnie spokojnie! Jeszcze musisz mi powiedzieć jedną rzecz..."
    #confused Lia ON
    show p1pl bsurprised wink_player lneutral with fc
    p1 "Jaką?"
    gr "Mniej więcej określ się jak chciałabyś pokierować Twoje życie."
    p1 "Uhh... Ciężko powiedzieć. Nie jestem pewna..."
    gr "Spokojnie. Skup się. Pomyśl co może być przed Tobą..."
    #thinking Lia ON
    show p1pl bangry closed lsad with fc
    gr "Pomyśl o tym na czym Ci najbardziej zależy. Zastanów się bardzo dobrze."
    gr "To bardzo ważna decyzja, więc spokojnie i nie śpiesz się z odpowiedzią."
    p1 "Dobrze..."
    #przy tym równo jak Lia zamyka oczy do nowej miny dodać animację zamykanych oczu tak całkiem, żeby ekran zrobił się czarny cały. I potem wskakują te decyzje w formie graficznej


    call screen chooseYourCard with dissolve

    play sound sfx_future_calls
    if c_nothing:
        show black
        show card_nothing:
            align (0.5,0.5) pos (0.25,0.45)
            ease 2 pos (0.5,0.45) zoom 1.2
        pause 1
        hide black with Dissolve(2.0)
        hide card_nothing with Dissolve(2.0)

        show p1pl bneutral wink lneutral with fc
        p1 "Wiesz co. Ja po prostu nic nie chcę."
        show p1pl bneutral wink_player lneutral with fc
        p1 "Nie potrzebuję niczego..."
        gr "Dobrze wiesz, że tak nie jest..."
        p1 "Nie. Nie chcę niczego konkretnego."
        #Lia angry ON
        show p1pl bangry narrowedwink_player lsad with fc
        p1 "To Twoja wina. Zostałam popchnięta do decyzji."
        p1 "Teraz ją zaakceptuj."
        gr "Dobrze..."
        p1 "A teraz chodźmy wypełnić obowiązki."
        p1 "I tak nic więcej na nas nie czeka w życiu."

    if c_destiny:
        show black
        show card_destiny:
            align (0.5,0.5) pos (0.5,0.45)
            ease 2 zoom 1.2
        pause 1
        hide black with Dissolve(2.0)
        hide card_destiny with Dissolve(2.0)

        show p1pl bneutral wink lneutral with fc
        p1 "Myślę, że może przede mną kryć się coś więcej."
        show p1pl bneutral wink_player lneutral with fc
        gr "Co dokładnie masz na myśli?"
        p1 "Jeszcze nie wiem, ale myślę, że wkrótce się dowiemy."
        gr "Podoba mi się to podejście."
        #Lia smile ON
        show p1pl bneutral wink_player lsmile with fc
        p1 "To co, zaczynamy?"
        gr "Prowadź."

    if c_hal:
        show black
        show card_love:
            align (0.5,0.5) pos (0.75,0.45)
            ease 2 pos (0.5,0.45) zoom 1.2
        pause 1
        hide black with Dissolve(2.0)
        hide card_love with Dissolve(2.0)

        show p1pl bneutral wink lneutral with fc
        p1 "Chciałabym być szczęśliwa. To musi być miłe."
        show p1pl bneutral wink_player lneutral with fc
        gr "Na pewno jest. Masz pomysł jak do tego doprowadzić?"
        p1 "Chyba tak. Chciałabym znaleźć kogoś z kim mogłabym być szczęśliwa."
        gr "Masz kogoś na oku?"
        p1 "Chyba tak. Myślę, że w tym Ty mi pomożesz."
        gr "W jaki sposób?"
        #Lia smile ON
        show p1pl bneutral wink_player lsmile with fc
        p1 "Przecież wiesz! W wyborach! Sama się przecież nie zdecyduję głuptasie."
        p1 "Ale najpierw zabierzmy się do pracy! Dużo obowiązków przed nami."





    hide p1pl with dissolve
    call screen podziekowanie with dissolve
    $ ee = 1
    $ zm_tutorial_jrnl_done = True
    # $ preferences.system_cursor = True
    jump ee_tavern_mainroom # przejście do normalnej EE


################################################################################


return
