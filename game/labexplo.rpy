
######################   Quick Answers  #########################
default qa = [__("“Nie chcę teraz tego robić.”"),
__("“Hmm, chyba zamknięte. Spróbuję później.”"),
__("“Wolałabym tego teraz nie robić.”"),
__("“Nie ma tam nic interesującego.”"),
__("“Nie ma sensu pracować w nocy.”"),
__("“O tej godzinie nikogo nie obsłużę.”"),
"6",
"7",
"8",
"9",
"10",
"11",
"12",
"13",
"14",
"15",
"16",
"17",
"18",
"19",
__("“Hmm, jeden z założycieli Tawerny.”"),
__("“Ah, jedna z osób bez której ta Tawerna by nie powstała.”")
]





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

######################   POTĘŻNE LABELE EKSPLORACYJNE  #########################
################################## EE WIOSKA ###################################
label ee_town:
    #if config.developer:
    #    scene black
    #    show text "ee_town" at truecenter
    #    pause 0.2

    $ lok = "wios"
    scene img_festival_dn_dragon with fade:
        zoom 0.46875
    while _return != "0":
        if dt < 5:
            scene anim_festival_day_dragon with dissolve:
                zoom 0.46875
        if dt >= 5:
            scene anim_festival_night_dragon with dissolve:
                zoom 0.46875
        call screen ee_town
        if _return == "niedostepne":
            "Dostępne w pełnej wersji"



################################# EE TAWERNA ###################################

label ee_tavern_liaroom:
    #if config.developer:
    #    scene black
    #    show text "pokoj Lii" at truecenter
    #   pause 0.2

    $ lok = "taw"

    while _return != "0":

        if dt == 1:
            scene anim_room_lia_morningdragon with dissolve
        if dt == 2:
            scene anim_room_lia_noondragon with dissolve
        if dt == 3:
            scene anim_room_lia_goldenhourdragon with dissolve
        if dt == 4:
            scene anim_room_lia_eveningdragon with dissolve
        if dt == 5:
            scene anim_room_lia_nightdragonlight with dissolve
        if dt > 5:
            scene anim_room_lia_nightdragon with dissolve
        call screen ee_tavern_liaroom with fc


##################################
init:
    $ lista_ee001_p4n_odp = [
                            _("\"Nie powinnam tego robić... Raven pewnie już śpi.\""),
                            _("\"Jest środek nocy. Nie chcę obudzić Raven.\""),
                            _("\"Raven na pewno już śpi. Sprawdzimy co u niej w trakcie dnia.\""),
                            _("\"Daj z tym spokój. Zajrzymy do niej jutro.\""),
                            _("\"Czego nie rozumiesz? Nie będę wchodzić do niej po nocy.\"")
                                ]
    default x_p4n_odp = 0 # zmienna indeksowania


################################################################################
################################################################################

label ee_tavern_hall:
    $ lok = "taw"
    scene img_tavern_hall
    while _return != "0":
        call screen ee_tavern_hall with fc
        if _return == "ee_hall_guestroom":
            if dt >= 5: # "ee001_p4n"
                $ ee001_p4n_odp = lista_ee001_p4n_odp[x_p4n_odp] # zmienna pobierająca wartość string pod tłumaczenie
                p1 "[ee001_p4n_odp!t]"
                if x_p4n_odp < len(lista_ee001_p4n_odp)-1:
                    $ x_p4n_odp += 1
                else:
                    $ x_p4n_odp = 0
            else:
                jump e8_p4
        if _return == "ee_hall_liaroom":
            jump ee_tavern_liaroom
        if _return == "ee_hall_mainroom":
            jump ee_tavern_mainroom
        if _return == "ee_hall_bathroom":
            p1 "[qa[0]]"
            if config.developer:
                menu:
                    "testing":
                        jump testowanie
                    "wylyź":
                        pass
        if _return == "ee_hall_diningroom":
            p1 "[qa[2]]"
        if _return == "ee_hall_parentsroom":
            p1 "[qa[3]]"



##################################
label ee_tavern_mainroom:
    $ lok = "taw"
    #scene img_tavern_mainroom with Dissolve(0.3)
    while _return != "0":
        scene img_tavern_mainroom with Dissolve(.2)
        call screen ee_tavern_mainroom #with Dissolve(.1)
        #with Dissolve(0.5)
        if _return == "ee_tavern_hall":
            jump ee_tavern_hall
        if _return == "ee_tavern_mainroom_bar":
            if not ee001_UkonczenieEpizodow['e8_work1']:
                if not ee001_UkonczenieEpizodow['e8_p4'] or not ee001_UkonczenieEpizodow['e8_p5']:
                    if dt < 4:
                        call e8_work1
                    if dt >= 4:
                        p1 "[qa[5]]"
            else:
                if dt < 5:
                    jump ee_tavern_mainroom_bar
                if dt >= 5:
                    p1 "[qa[5]]"
        if _return == "e8_p16":
            jump e8_p16
        if _return == "paczka01":
            p1 "Hmm, muszę zanieść tę paczkę do kuźni."
            $ paczka01 = "odebrana"
        #if _return == "beer":
        #if _return == "dekoracje":
        #if _return == "żyrandole":
        #if _return == "tablemess":
        #if _return == "floorflourmess":
        #if _return == "floorwinemess":
        #if _return == "barrightmess":
        #if _return == "barleftmess":
        if _return == "ee_tavern_kitchen":
            jump ee_tavern_kitchen
        if _return == "ee_tavern_leftroom":
            jump ee_tavern_leftroom
        if _return == "ee_tavern_rightroom":
            jump ee_tavern_rightroom
        if _return == "ee_tavern_outside":
            jump ee_tavern_outside
        #if dt == 5:
        #    scene img_tavern_mainroom_day #with fade
        #if dt == 1:
        #    scene img_tavern_mainroom_night #with fade
        #hide img_tavern_mainroom

###########################
init:
    default czyjestgosc1 = 1
    default czyjestgosc2 = 1

label ee_tavern_leftroom:

    scene img_tavern_leftroom
    while _return != "0":
        call screen ee_tavern_leftroom with dissolve
        if _return == "ee_tavern_mainroom":
            jump ee_tavern_mainroom
        if _return == "P7_D01":
            call p7_d01 from _call_p7_d01
        if _return == "ee_leftroom_painting":
            p1 "[qa[20]]"
        if _return == "dt+1" or "dt=1":
            $ czyjestgosc1 = renpy.random.randint(0, 1)
            $ czyjestgosc2 = renpy.random.randint(0, 1)


###########################
label ee_tavern_rightroom:
    scene img_tavern_rightroom
    while _return != "0":
        call screen ee_tavern_rightroom with dissolve
        if _return == "ee_tavern_mainroom":
            jump ee_tavern_mainroom
        if _return == "ee_rightroom_painting":
            p1 "[qa[21]]"


##################################
label ee_tavern_mainroom_bar:
    #if config.developer:
    #    scene black
    #    show text "bar" at truecenter
    #    pause 0.2

    $ lok = "taw"
    scene tavern_main_bar_bg0_dn
    show tavern_main_bar_bar1_dn
    with dissolve
    while _return != "0":
        call screen ee_tavern_mainroom_bar with Dissolve(0.3)
        if _return == "e8_p16":
            jump e8_p16
        if _return == "ee_tavern_mainroom":
            jump ee_tavern_mainroom
    #with dissolve

##################################
label ee_tavern_kitchen:
    scene room_kitchenday with dissolve
    while _return != "0":
        call screen ee_tavern_kitchen with dissolve
        if _return == "ee_tavern_mainroom":
            jump ee_tavern_mainroom

########################## EE TAWERNA NA ZEWNĄTRZ ##############################
label ee_tavern_outside:
    default klik_tent1 = True
    $ lok = "taw"

    while _return != "0":
        if dt>=5:
            scene anim_tavern nighttime dragon with dissolve
        else:
            scene anim_tavern outside dragon with dissolve
        call screen ee_tavern_outside with fc
        with dissolve

        if _return == "namiot":
            call .e001_tent from _call_ee_tavern_outside_e001_tent
        if _return == "tawerna":
            jump ee_tavern_mainroom

    #### local_label pod ee_tavern_outside ###
    label .e001_tent:
        if c_hal:
            "Lia spojrzała na rozstawiony przed Tawerną namiot."
            "”Ojciec mówił, żeby tam nie podchodzić. Najlepiej będzie jak go posłucham” - pomyślała i wróciła do swoich zajęć."
        else:
            "Lia spojrzała na rozstawiony przed Tawerną namiot."
            "”Ciekawe co tam skrywają. Ojciec mówił, że nikt nie powinien tam podchodzić” - rozmyślała, lustrując jednocześnie wzrokiem złożoną konstrukcję."

            if c_destiny:
                if dt>=5:
                    show anim_tavern nighttime dragon:
                        linear 8 zoom 1.5 align (0.0,0.5)
                    with dissolve
                else:
                    show anim_tavern outside dragon:
                        ease 8 zoom 1.5 align (0.0,0.5)
                    with dissolve
                #Powolny zoom na namiot wraz z tekstami niżej, czas ok. 8 sekund
                "Przyglądając się postanowiła powoli się zbliżyć."
                "Zdawała sobie sprawę, że nie jest to najmądrzejsze zachowanie, ale..."
                "Nagle usłyszała donośny głos za swoimi plecami."
                #kamera się zatrzymuje, pojawia się Lia po lewej, odwracając się w prawą stronę z której wchodzi Tajemniczy Gość 2
                show p1:
                    align (0.1, 1.0)
                with dissolve
                show hidden_dude2 with moveinright:
                    align (.8,1.0)
                show p1 with fc:
                    xzoom -1
                tg2 "A co my tu mamy? Ładnie to tak się skradać do cudzej własności?"
                show p1 bsurprised widenedwink lsad
                # TODO Surprised Lia ON
                "Zaskoczona Lia nie była w stanie wykrztusić żadnego słowa."
                tg2 "Cholera by to i te dzieciaki… No już, zmykaj stąd i nie kręć się przy naszym namiocie."
                show p1 -bsurprised -widenedwink lsad
                # TODO Surprised Lia OFF
                "Długo się nie zastanawiała, spuściła wzrok i ruszyła w swoją stronę."
                "Kątem oka zauważyła tylko jak tajemniczy jegomość zniknął wewnątrz wciąż tajemniczego namiotu."


            if c_nothing:
                p1 "Ehh, pewnie nic takiego."
                "Powiedziała Lia cicho pod nosem i wróciła do swoich zajęć."
        $ klik_tent1 = False
    return

############################### EE SECRET GARDEN ##############################
label ee_secretgarden1:
    $ lok = "secretgarden"
    scene secretgarden1_bg with dissolve
    while _return != "0":
        call screen ee_secretgarden1 with fc
        if _return == "secretgarden1_owocki":
            #p1 "secretgarden1_owocki"
            jump ee_secretgarden_whole
        if _return == "secretgarden1_tree":
            #p1 "secretgarden1_tree"
            jump ee_secretgarden2 ############### TODO chwilowe przejście na prawą stronę
        if _return == "secretgarden1_water":
            p1 "secretgarden1_water"

label ee_secretgarden2:
    $ lok = "secretgarden"
    scene secretgarden2_bg with dissolve
    while _return != "0":
        call screen ee_secretgarden2 with fc
        if _return == "secretgarden2_owocki":
            p1 "secretgarden2_owocki"
        if _return == "secretgarden2_tree":
            #p1 "secretgarden2_tree"
            jump ee_secretgarden1 ############### TODO chwilowe przejście na lewą stronę
        if _return == "secretgarden2_sus":
            p1 "secretgarden2_sus"
        if _return == "secretgarden2_terra":
            p1 "secretgarden2_terra"


init:
    default xadj = ui.adjustment()
label ee_secretgarden:
    $ lok = "secretgarden"
    scene secretgarden_bg with dissolve:
        xalign xadj.value/1920
    while _return != "0":

        call screen ee_secretgarden with Dissolve(0.2)
        scene secretgarden_bg:
            xalign xadj.value/1920
        if _return == "secretgarden_owocki":
            p1 "secretgarden_owocki"

        if _return == "secretgarden_sus":
            p1 "secretgarden_sus"

        if _return == "secretgarden_terra":
            p1 "secretgarden_terra"

        if _return == "secretgarden_tree":
            p1 "secretgarden_tree"

        if _return == "secretgarden_water":
            p1 "secretgarden_water"

        p1 "[xadj.value]"
label secretgarden_owocki:

    p1 "secretgarden_owocki"
    return
################################# EE MONUMENT ##################################
label ee_monument:
    $ lok = "mon"
    while _return != "0":
        if _return == "dt+1":
            scene img_monument_przejscie:
                zoom 0.5
        if _return == "dt=1":
            scene img_monument_przejscie:
                zoom 0.5
        scene img_monument with dissolve:
            zoom 0.5
        if dt >= 3:
            show anim_monument_fire:
                zoom 0.5
        call screen ee_monument with fc
        if _return == "guard11_talk":
            call ee_monument_guard11_talk from _call_ee_monument_guard11_talk
        if _return == "guard12_talk":
            call ee_monument_guard12_talk from _call_ee_monument_guard12_talk
        if _return == "architect_talk":
            call ee_monument_architect_talk from _call_ee_monument_architect_talk


################################################################################
##################################   eventy  ###################################
label p7_d01:
    scene img_tavern_leftroom
    show tavern_leftroom_bottle2_dn_idle
    show tavern_leftroom_aina3_dn_idle
    "Lia podeszła powolnym krokiem do stolika przy którym drzemała Aina."
    show img_tavern_leftroom:
        linear 8 zoom 1.2 align (1.0,1.0)
    show tavern_leftroom_bottle2_dn_idle:
        linear 8 zoom 1.2 align (1.0,1.0)
    show tavern_leftroom_aina3_dn_idle:
        linear 8 zoom 1.2 align (1.0,1.0)
    #with dissolve
    #Tu można lekki zoom zapoczątkować na Ainę, ale leciutki i bardzo powolny np. na 7sec
    "”Aina” - pomyślała Lia analizując wzrokiem ludzką kobietę o jasnych włosach."
    "Słyszała, że to była agentka Króla. Ale to ponoć tylko plotki tawernianych gości - tak przynajmniej twierdzi jej ojciec."
    "Lia zastanawiała się co teraz, z jednej strony była jej ciekawa, a z drugie nie była pewna..."
    menu:
        "Nie krępuj się. Podejdź i porozmawiaj.":
            #Lia z lewej patrząc w prawo, Aina z prawej patrząc w lewo - Aina confused ON
            show p1 with dissolve:
                align (0.3, 1.0)
                xzoom -1
            hide tavern_leftroom_aina3_dn_idle with dissolve
            show p7 bsurprised with dissolve:
                align (0.7, 1.0)
                xzoom -1
            "Gdy tylko Lia podeszła bliżej to Aina zerwała się jak poparzona z krzesła."
            #angry Aina ON
            #scary Lia ON
            show p7 bangry widenedwink lsad with fc
            show p1 bsad widenedwink lsad with fc # TODO upewnic sie ze tak ma byc
            p7 "Co? Co jest? Oh… Co to za budzenie co?"
            p1 "Oj, przepraszam Panią, nie chciałam Pani obudzić…"
            #happy Aina ON
            #confused Lia ON
            show p7 bneutral narrowedwink lsmile with fc
            show p1 bsurprised with fc
            p7 "Haha, słodka jesteś! Aina jestem! Nie tam żadna Pani, tylko się z Tobą droczę!"

        "Może lepiej ją zostaw, chyba śpi.":
            #Lia z lewej obrócona w lewo, Aina po prawej patrząca na Lię
            show p1 with dissolve:
                align (0.3, 1.0)
            hide tavern_leftroom_aina3_dn_idle with dissolve
            show p7 with dissolve:
                align (0.7, 1.0)
                xzoom -1
            "Zaraz gdy Lia się odwróciła plecami do śpiącej Ainy to usłyszała za sobą głos: "
            #smirk Aina ON
            show p7 bangry narrowedwink lsmile with fc
            #Lia obraca się w prawo + scary Lia ON
            show p1 bsad widenedwink lsad with fc:
                xzoom -1
            p7 "Hola hola, co to za skradanie co?"
            p1 "Oh? Przepraszam Panią, ale nie skradałam się..."
            #happy Aina ON
            #confused Lia ON
            show p7 bangry narrowedwink lsmile with fc
            show p1 bsurprised with fc
            p7 "Haha, słodka jesteś! Aina jestem! Nie tam żadna Pani, tylko się z Tobą droczę!"

    #blush Lia ON
    show p1 blush with fc
    p1 "Oh..."
    p7 "Oj no! Wygłupiam się tylko - nie przejmuj się tak. Co potrzebujesz?"
    #normal Lia ON
    #normal Aina ON
    show p1 bneutral wink lneutral -blush with fc
    show p7 bneutral wink lneutral with fc
    p1 "Nic! Tak tylko z ciekawości podeszłam…"
    p7 "Ha! Mówisz? I jak? Ciekawość zaspokojona?"
    p1 "Oh, nie wiem…"
    #smile Aina ON
    show p7 lsmile with fc
    p7 "Zawsze możemy sobie z tym pomóc! Jesteś Lia tak?"
    #confused Lia ON
    show p1 bsurprised with fc
    p1 "To moje imię... Znaczy tak, to ja! A Ty Aina tak?"
    #smile Lia ON
    show p1 bneutral lsmile with fc
    p7 "Tak, to ja. Miło Cię w końcu poznać oficjalnie Lia."
    #normal Lia ON
    #normal Aina ON
    show p1 bneutral wink lneutral with fc
    show p7 bneutral wink lneutral with fc
    p7 "Jeśli mogę zadać pytanie: stało się coś?"
    p1 "Huh? Dlaczego miałoby się coś stać?"
    p7 "No słuchaj, przychodzę tutaj już od jakiegoś czasu."
    p7 "Zdarzyło Ci się mnie obsługiwać już wiele razy."
    p1 "To prawda… I co z tym?"
    #Lia blush ON
    #smile Aina ON
    show p1 blush with fc
    show p7 lsmile with fc
    p7 "To z tym, że pierwszy raz wymieniamy więcej niż pięć wyrazów."
    p1 "Oh, rzeczywiście może tak być…"
    p7 "Haha, no widzisz! To teraz opowiadaj co się stało."
    p1 "Oh, nic konkretnego…"
    p1 "Po prostu, hmm - postanowiłam chociaż lekko się otworzyć na innych."
    #smile Lia ON
    show p1 lsmile with fc
    p1 "Tak przynajmniej podpowiada mi sumienie."
    p7 "Ha! Rozumiem, rozumiem. Sumienie dobrze Ci podpowiedziało!"
    #normal Lia ON
    show p1 lneutral -blush with fc
    p1 "Lubię tak właśnie myśleć."
    p7 "I bardzo dobrze! Co Ci podpowiada teraz?"
    menu:
        "Powiedz, że chętnie byś poznała ją bliżej.":
            $ AinaLove +=1
            #smirk Lia ON
            show p1 bangry narrowedwink lsmile with fc
            p1 "Podpowiada, że chyba warto poznać Cię bliżej."
            p7 "Haha, znów ma rację! Powiem nawet, że bardzo chętnie też posłuchałabym Twojego sumienia."
            #SURPRISED_HAPPY Lia ON
            show p1 bsurprised widenedwink lsmile with fc
            #smirk Aina ON
            show p7 bangry narrowedwink lsmile with fc
            p1 "Oh, mówisz?"
            p7 "Mówię! Powiem Ci tak: dziś muszę już uciekać, ale chętnie spotkam się z Tobą wkrótce. "
            p7 "Możemy wtedy porobić coś fajnego! Zgoda?"
            #smile Lia ON
            show p1 bneutral wink lsmile with fc
            p1 "Zgoda! To co, do zobaczenia?"
            #smile Aina ON
            show p7 bneutral wink lsmile with fc
            p7 "Pewnie! Widzimy się wkrótce!"
            "Powiedziała Aina po czym zniknęła za drzwiami."
            "Lia była lekko zaskoczona, umówiła się z osobą, którą kojarzy tylko z widzenia."
            "”No nic, to chyba nic nowego ostatnio.” - pomyślała po czym wróciła do swoich zajęć."
            #Aina znika z fotelika
        "Powiedz, że chwilowo nic.":
            #confused Lia ON
            #normal Aina ON
            show p1 bsurprised with fc
            show p7 bneutral wink lneutral with fc
            p1 "Oh, w tym momencie nic konkretnego..."
            #sad Lia ON
            show p1 bsad lsad with fc
            p7 "Huh, trochę rozczarowujące."
            p7 "No nic, może podpowie Ci coś następnym razem."
            p7 "Ja niestety muszę teraz uciekać, sprawy do załatwienia. Do zobaczenia!"
            "Powiedziała praktycznie jednym ciągiem Aina po czym zwinnym krokiem ruszyła w stronę wyjścia."
            "”To było dziwne.” - pomyślała Lia i wróciła do swoich zajęć."
            #Aina znika z fotelika

    scene img_tavern_leftroom
    return

################################################################################
###############################   mini epizody  ################################



########################   ROZMOWY   ###############################
init:
    default z_EE001_P11_ODP1 = True
    default z_EE001_P12_ODP1 = True
    default z_EE001_P13_ODP1 = True
    default z_EE001_P13_ODP2 = True
    default z_EE001_P13_ODP3 = True
    default z_EE001_P13_ODP4 = True
    default architect_talk_odp2_a = True
    default architect_talk_odp2_b = True
    default guard11_talk = [__("Dzień dobry Obywatelko!"),
                            __("Dzień dobry!"),
                            __("Witamy przy Monumencie Legend!")]
    default guard11_talk_rand = ""

    default guard12_talk = [__("Tak?"),
                            __("Hmm?"),
                            __("Czego potrzeba?")]
    default guard12_talk_rand = ""

    default guard12_talk_2 = [__("Nie. Nie mam ochoty rozmawiać. Tam się pali ogień, idź sobie na niego popatrz."),
                            __("Nie."),
                            __("Nie rób tak. Zostaw mnie w spokoju.")]
    default guard12_talk_2_rand = ""

    default arch_talk = [__("Tak? Słucham?"),
                        __("Mhm?"),
                        __("Co potrzeba?")]
    default arch_talk_rand = ""

    default arch_talk_end = [__("Nie teraz."),
                            __("Później porozmawiamy."),
                            __("Porozmawiamy przy innej okazji.")]
    default arch_talk_rand_end = ""

    default arch_talk_odp4 = [__("Przesadziłaś ostatnio. Nie mam ochoty z Tobą rozmawiać."),
                            __("Wybacz. Powiedziałam coś wcześniej."),
                            __("Nie.")]
    default arch_talk_rand_odp4 = ""

label ee_monument_guard11_talk: #p11
    show img_monument_extras:
        zoom 0.5
    #if dt >= 3:
    #    show anim_monument_fire:
    #        zoom 0.5
    with None
    show p1:
        align (0.2,1.0)
        xzoom -1
    show p11:
        align (0.7,1.0)
    with dissolve
    $ guard11_talk_rand = renpy.random.choice(guard11_talk)
    p11 "[guard11_talk_rand]"
    if z_EE001_P11_ODP1:
        menu EE001_P11_ODP1:
            "“Co Pan tutaj robi?”":
                #DISAPPOINTED Lia ON
                show p1 bsad lsad narrowedwink with fc
                p11 "A na co to wygląda?"
                p11 "Oh, przepraszam Panienkę. Nie każdy musi to wiedzieć."
                #smile Lia ON
                show p1 lsmile bneutral wink with fc
                p11 "Jestem Strażnikiem Królewskim, mam wartę przy Monumencie."
                p11 "To bardzo ważny obiekt dla naszego królestwa, dlatego jako Straż z dumą pełnimy tego obowiązku."
                menu EE001_P11_ODP1_A:
                    "“Bardzo dziękuję za wyjaśnienie!”":
                        p11 "Jesteśmy by pomagać. Przyjemność po mojej stronie."
                        p11 "Jeśli jesteś ciekawa szczegółów na temat monumentu to porozmawiaj z Panią Architekt."
                        p1 "Tak zrobię! Dziękuję i miłego dnia!"
                        #powrót do widoku lokacji"
                        $ StrazWiedza +=1
                        $ z_EE001_P11_ODP1 = False
                        return

                    "“Dlaczego to bardzo ważny obiekt?”":
                        p11 "Hmm. Monument symbolizuje Wieżę, która chroni naszą wyspę."
                        p1 "A coś więcej o wieży jest Pan w stanie powiedzieć?"
                        p11 "Hmm. Panienka porozmawia z Panią Architekt, na pewno będzie w stanie powiedzieć coś więcej."
                        p1 "Tak zrobię. Dziękuję!"
                        #powrót do widoku lokacji
                        $ StrazWiedza +=1
                        $ z_EE001_P11_ODP1 = False
                        return

                    ">Odejdź.":
                        return
            ">Odejdź.":
                return

    if not z_EE001_P11_ODP1:
        menu EE001_P11_ODP2:
            "“Dzień dobry! Jak sytuacja?”":
                show p1 lsmile
                p11 "Wszystko w porządku! Dziękuję za troskę w imieniu swoim i reszty oddziału."
                return
            ">Odejdź.":
                return
        return

label ee_monument_guard12_talk: #p12
    #rozmowa z drugim strażnikiem, dostępny tylko: wieczorem i w nocy
    #po kliknięciu szereg losowych pierwszych odpowiedzi:

    show img_monument_extras:
        zoom 0.5
    with None
    show p1:
        align (0.2,1.0)
        xzoom -1
    show p12:
        align (0.7,1.0)
    with dissolve
    $ guard12_talk_rand = renpy.random.choice(guard12_talk)

    if z_EE001_P12_ODP1:
        p12 "[guard12_talk_rand]"
        menu EE001_P12_ODP1:
            "“Co Pan tutaj robi?”":
                p12 "A na co to wygląda?"
                #SHOCK Lia ON
                show p1 bsurprised widenedwink lopen
                p12 "Stoję sobie z nudów i patrzę na drzewa."
                p12 "Zmykaj stąd i nie przeszkadzaj. Późno jest."
                $ StrazWiedza +=1
                menu:
                    "“Nie musi być Pan taki niemiły od razu.”":

                        p12 "Proszę proszę, jaka wygadana!"
                        p12 "Powiem tak, jak taka ciekawska jesteś to przyjdź tutaj na przykład powiedzmy hmm..."
                        p12 "ZA DNIA! A nie o takich dziwnych porach."
                        p1 "Ale przecież…"
                        p12 "ŻADNEGO ALE, nie przeszkadzaj mi."
                        #powrót do widoki lokacji, zakończenie rozmowy
                        $ z_EE001_P12_ODP1 = False
                        return
                    ">Odejdź":
                        return
            ">Odejdź":
                return

    $ guard12_talk_2_rand = renpy.random.choice(guard12_talk_2)
    p12 "[guard12_talk_2_rand]"
    return

label ee_monument_architect_talk: #p13
    show img_monument_extras:
        zoom 0.5
    with None
    show p1:
        align (0.2,1.0)
        xzoom -1
    show p13:
        align (0.7,1.0)
    with dissolve
    if z_EE001_P13_ODP4:
        if z_EE001_P13_ODP1 or z_EE001_P13_ODP2 or z_EE001_P13_ODP3:
            $ arch_talk_rand = renpy.random.choice(arch_talk)
            p13 "[arch_talk_rand]"
            menu architect_talk_podst:
                "“Kim Pani jest?”" if z_EE001_P13_ODP1:
                    p13 "Nazywam się Athena. Należę do nadwornego cechu Architektów."
                    # TODO wpis do dziennika P13-A
                    menu:
                        "“Czym jest cech Architektów?”":
                            p13 "Hmm, co ja w ogóle mogę powiedzieć… Hmm."
                            p13 "Jako architekci zajmujemy się sprawami związanymi z kreacją istotnych dla królestwa elementów."
                            p13 "Na przykład projektem oraz nadzorem budowy tutejszego Monumentu."
                            $ ArchitektWiedza +=1
                            menu:
                                "“Jakie elementy są istotne dla królestwa?”":
                                    #angry Architect ON
                                    show p13 angry
                                    p13 "Ehh. Tak jak wspomniałam. Na przykład ten Monument."
                                    p13 "Na przykład latarnia w Waszej wiosce."
                                    p13 "Most na rzece czy chociażby badania nad… Uhm, nieważne zresztą."
                                    "Athena urwała nagle rozglądając się nerwowo. Nie umknęło to Twojej uwadze."
                                    menu:
                                        "“Jakie badania? Co miała Pani na myśli?”":
                                            #SHOCK Lia ON
                                            show p1 bsurprised widenedwink lopen
                                            p13 "Zadajesz strasznie dużo pytań, wiesz o tym?"
                                            p13 "Pomyśl o tym rozmawiając z kimś innym następnym razem."
                                            p13 "Tymczasem proszę zostaw mnie w spokoju."
                                            show p1 bneutral lneutral wink
                                            $ ArchitektWiedza +=1
                                            $ z_EE001_P13_ODP4 = False
                                            return
                                            #architekt się na nas wkurza i kończy rozmowę, następne rozpoczęcie rozmowy to ODP4

                                        ">Lepiej zapytaj o coś innego.":
                                            $ z_EE001_P13_ODP1 = False
                                            call architect_talk_podst from _call_architect_talk_podst
                                        ">Odejdź.":
                                            $ z_EE001_P13_ODP1 = False
                                            return
                                ">Zapytaj o coś innego.":
                                    $ z_EE001_P13_ODP1 = False
                                    call architect_talk_podst from _call_architect_talk_podst_1
                                ">Odejdź.":
                                    $ z_EE001_P13_ODP1 = False
                                    return
                        ">Zapytaj o coś innego.":
                            $ z_EE001_P13_ODP1 = False
                            call architect_talk_podst from _call_architect_talk_podst_2
                        ">Odejdź.":
                            $ z_EE001_P13_ODP1 = False
                            return
                "“Może Pani opowiedzieć więcej o Monumencie?”" if z_EE001_P13_ODP2:
                    p13 "Monument powstał na wzór Wieży znajdującej się w centrum naszej wyspy."
                    p13 "Chcieliśmy, żeby więcej osób mogło podziwiać jej blask, nawet jeśli sam Monument w pełni go nie odzwierciedla."
                    p13 "Wieża chroni naszą krainę i jest zbyt ważnym symbolem dla całego Królestwa."
                    p13 "Dlatego tutaj jest jej odzwierciedlenie, żeby więcej osób mogło podziwiać ją chociaż w minimalnym stopniu."
                    menu architect_talk_odp2:

                        "“Czemu jest ważnym symbolem?”" if architect_talk_odp2_a:
                            p13 "Hmm. Dobre pytanie. Myślę, że jest kilka powodów."
                            p13 "Jednym z nich na pewno jest fakt, że prawdopodobnie to tam mieszka Zielony Smok gdy odpoczywa od podróżowania po niebie."
                            p13 "To z tego miejsca wyrusza unicestwiać niebezpieczeństwa z zewnątrz i dzięki temu możemy żyć w spokoju."
                            p13 "Właśnie dlatego Wieża jest symbolem jedności i fundamentem dobrobytu tego królestwa."
                            $ architect_talk_odp2_a = False
                            call architect_talk_odp2 from _call_architect_talk_odp2
                            #po tym usuwa to pytanie i zostajemy w tym samym oknie (wyjątek stanowi brak dodatkowych pytań) wtedy pojawia się nowe

                        "“Przed czym dokładnie chroni wieża?”" if architect_talk_odp2_b:
                            p13 "Przed wszelkim złem jakie czyha na zewnątrz."
                            p13 "Wieża tworzy wielką barierę dzięki której zewnętrzne niebezpieczeństwa nie mają wstępu do naszej krainy."
                            $ architect_talk_odp2_b = False
                            call architect_talk_odp2 from _call_architect_talk_odp2_1
                            #jak to klikniemy to zostajemy w tym samym oknie, mamy pytanie to obok (chyba, że już je kliknęliśmy). Żeby odblokować poniższe pytanie trzeba przeklikać te dwa co są tutaj

                        "“Co Pani o tym sądzi?”" if not architect_talk_odp2_a and not architect_talk_odp2_b:
                            p13 "Sądzę, że mamy pokój i dobrobyt w Królestwie właśnie z tego powodu, że nic z zewnątrz się do nas nie dostaje."
                            p13 "Na pewno czyha tam czyste zło. Wszyscy to wiedzą."
                            "W jej głosie czuć było, że nie ma ochoty kontynuować tego tematu."

                            #zakończenie tego dialogu i powrót do bazowego schematu
                            # TODO wpis do dziennika
                            $ z_EE001_P13_ODP2 = False
                            call architect_talk_podst from _call_architect_talk_podst_3
                        ">Odejdź.":
                            return



                "“Kim są ludzie wypisani na Monumencie?”" if z_EE001_P13_ODP3:
                    p13 "To grupa osób, która przyczyniła się do zjednoczenia Królestwa."
                    p13 "Nie zawsze było tak spokojnie jak teraz, potrzeba było heroicznych czynów."
                    p13 "To właśnie ta grupa osób zasłużyła na upamiętnienie na tej tablicy w zamian za poświęcenie się dla nas."
                    menu:
                        "“Co znaczy poświęcili się?”":
                            #Lia shock ON
                            show p1 bsurprised widenedwink lopen
                            p13 "Oddali własne życia za to, żebyśmy my mogli żyć w pokoju."
                            #przy przejściu od razu Lia normal ON
                            show p1 bneutral lneutral wink
                            $ z_EE001_P13_ODP3 = False
                            call architect_talk_podst from _call_architect_talk_podst_4
                        ">Odejdź.":
                            return
                ">Odejdź.":
                    return



        else:
            $ arch_talk_rand_end = renpy.random.choice(arch_talk_end)
            p13 "[arch_talk_rand_end]"
            return
    if not z_EE001_P13_ODP4:
        $ arch_talk_rand_odp4 = renpy.random.choice(arch_talk_odp4)
        p13 "[arch_talk_rand_odp4]"
        return
    return










################################################################################
#################################   EE000   ####################################
################################################################################

label ee000_tavern_liaroom:
    scene anim_room_lia_morning
    while _return != "0":
        call screen ee000_tavern_liaroom with dissolve
        if _return == "ee000_tavern_hall":
            jump ee000_tavern_hall

##########################
label ee000_tavern_hall:
    scene img_tavern_hall
    while _return != "0":
        call screen ee000_tavern_hall with dissolve

        if _return == "ee000_hall_bathroom":
            p1 "Nie mam czego tu szukać."
        if _return == "ee000_hall_diningroom":
            p1 "Gdybyśmy jedli w jadalni to miałabym bliżej na śniadanie… No cóż. "
        if _return == "ee000_hall_guestroom":
            p1 "W środku chyba nikogo nie ma. Raven pewnie zeszła już na śniadanie."
        if _return == "ee000_hall_parentsroom":
            p1 "Wolę tu nie zaglądać. Rodzice zresztą na pewno są już na dole."
        if _return == "ee000_hall_liaroom":
            jump ee000_tavern_liaroom
        if _return == "ee000_hall_mainroom":
            jump ee000_tavern_mainroom


###########################
label ee000_tavern_mainroom:
    scene img_tavern_mainroom
    while _return != "0":
        call screen ee000_tavern_mainroom with dissolve

        if _return == "ee000_tavern_main_bar":
            p1 "Dziś pewnie i tak czeka mnie praca… Najpierw jednak śniadanie i rozmowa."
        if _return == "ee000_tavern_hall":
            jump ee000_tavern_hall
        if _return == "ee000_tavern_leftroom":
            jump ee000_tavern_leftroom
        if _return == "ee000_tavern_rightroom":
            jump ee000_tavern_rightroom
        if _return == "ee000ep8":
            jump epizod8


###########################
label ee000_tavern_leftroom:
    scene img_tavern_leftroom
    while _return != "0":
        call screen ee000_tavern_leftroom with dissolve
        if _return == "ee000_tavern_mainroom":
            jump ee000_tavern_mainroom


###########################
label ee000_tavern_rightroom:
    scene img_tavern_rightroom
    while _return != "0":
        call screen ee000_tavern_rightroom with dissolve
        if _return == "ee000_tavern_mainroom":
            jump ee000_tavern_mainroom



return
