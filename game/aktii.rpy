################################################################################
#########################   SCENA WYPCHNIECIA P4   ##########################
################################################################################
screen p4_defenestration:
    tag defenestration
    textbutton "wypchnij ją" focus_mask True action Show("p4_defenestration_anim")
screen p4_defenestration_anim:
    tag defenestration
    add "anim_e7p4_raven_ravenroom_push"

image anim_e7p4_raven_ravenroom_push:
    contains:
        "e7p4c1_raven_ravenroom_push1"
        #xalign 1.0 yalign 1.0
        xpos -0.05
        linear 0.5 xpos 0.0
        linear 2.0 xpos 0.02
    contains:
        1.0
        "e7p4c2_raven_ravenroom_push2a"
        #xalign 1.0 yalign 1.0
        ypos 0.07
        linear 0.7 ypos 0.0
        linear 0.7 ypos -0.02
    contains:
        1.0
        "e7p4c2_raven_ravenroom_push2b"
        #xalign 1.0 yalign 1.0
        ypos -0.07
        linear 0.7 ypos 0.0
        linear 0.7 ypos 0.02
    contains:
        2.0
        "black"
        alpha 0.0
        linear 0.2 alpha 1.0
    contains:
        2.0
        "e7p4c3_raven_ravenroom_push3"
        align (.5,.5) alpha 0.0
        linear 1.0 alpha 1.0 zoom 1.02
        linear 2.5 zoom 1.05


################################################################################
############################ wątek Raven #######################################
################################################################################
label e8_p4:

    #Rozpoczynamy klikając w pokój Raven na korytarzu
    #Proszę pamiętać, że nocą nie da się kliknąć, tylko mamy to -" EE001-P4N
    #Pierwsza linijka dzieje się z perspektywy korytarza, można lekki zoom zrobić na drzwi
    $ ravenDress = ""
    show img_tavern_hall:
        linear 3 align (1.0,1.0) zoom 1.2
    "Lia zapukała lekko w drzwi. Po krótkiej chwili usłyszała z wewnątrz “Proszę”."
    #Tutaj przejścia do Pokoju Raven, zacznijmy z lekkim zoomem do prawej strony jak Lia wbija
    scene room_raven_evening_empty with fade:
        zoom 1.4 align (1.0,0.3)
    show p1:
        zoom 1.3 align (1.45,0.2)
        linear 3 zoom 1.3 align (0.8,0.2)
    show p4:
        zoom 1.3 align (-0.5,0.2)
    "Otworzyła drzwi po czym powoli weszła do środka."
    #Tutaj lekkie oddalenie do pełnego obrazu i ujawnienie Raven z lewej strony.

    show room_raven_evening_empty:
        linear 2 zoom 1.0 align (1.0,0.3)
    show p1:
        linear 2 zoom 1.0 align (0.8,1.0)
    show p4:
        linear 2 zoom 1.0 align (0.0,1.0)
    "Na drugim końcu pomieszczenia dostrzegła Raven."
    "Lia zauważyła, że Raven przebrała się w nowe ubrania."
    #Podchodzą do siebie powoli, niech staną tak jakby po prostu do rozmowy.
    show p1:
        linear 2 zoom 1.0 align (0.6,1.0)
    show p4:
        linear 2 zoom 1.0 align (0.3,1.0)

    menu:
        "“Ślicznie wyglądasz w nowej sukience!”":
            "Dziewczyny powoli zbliżyły się do siebie. Pierwsza odezwała się Lia."
            #Raven blush ON
            #Lia blush ON
            show p4 blush with fc
            show p1 blush with fc
            p1 "Hej Raven! Muszę powiedzieć, że ślicznie wyglądasz w tej nowej sukience!"
            "Raven lekko się zaczerwieniła, Lia postanowiła od razu kontynuować, unikając jednocześnie niezręcznej ciszy."
            #Lia smile ON
            show p1 lsmile with fc
            p1 "Ah, no i w ogóle przyszłam sprawdzić jak się czujesz i czy wszystko dobrze."
            #smile Raven ON
            show p4 lsmile with fc
            p4 "Oj, tak! Wszystko dobrze i dziękuję! To bardzo miłe co mówisz."

        "Nie zwracaj uwagi na zmianę stroju.":
            "Dziewczyny powoli zbliżyły się do siebie. Pierwsza odezwała się Lia."
            p1 "Hej Raven! Przyszłam sprawdzić jak się czujesz i czy wszystko dobrze."
            #smile Raven ON
            show p4 lsmile with fc
            p4 "Lia! Bardzo miło z Twojej strony - dziękuję! Wszystko dobrze - dzięki Waszej pomocy."

    "Nastała krótka cisza. Obie dziewczyny ze spokojem wpatrywały się w siebie."

    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ cecha DESTINY":
                $ c_destiny = True
                pass
            "dev/ cecha HAL":
                $ c_hal = True
                pass
            "dev/ cecha NOTHING":
                $ c_nothing = True
                pass
    ########################### /devstuff #########################

    #jeśli cecha: DESTINY
    if c_destiny == True:
        "Lia przyglądała się Raven ze świeżym zainteresowaniem."
        "Była ciekawa czy pojawienie się jej tutaj - akurat teraz, było zrządzeniem losu czy może czymś więcej..."
        "”Może później się jej zapytam o szczegóły. Najpierw obowiązki” - pomyślała, po czym powiedziała:"
        #Raven smile OFF"
        show p4 -lsmile with Dissolve(0.2)
        p1 "Cieszę się, że wszystko dobrze! Moi rodzice się ucieszą."
        p4 "Tak tak, możesz im podziękować - naprawdę niezmiernie mi miło, że oni się tak martwią."
        p4 "Jakieś plany co możemy teraz porobić razem?"

    #jeśli cecha: HAL
    if c_hal == True:
        "Lia przyglądała się Raven z lekkim zauroczeniem."
        #Raven blush ON
        show p4 blush with fc
        p1 "Ale uroczy uśmiech..."
        #Lia blush ON
        show p1 blush with fc
        "Momentalnie się zaczerwieniła. Zdała sobie sprawę, że powiedziała to na głos..."
        p1 "Oj, przepraszam... Nie chciałam tego mówić głośno..."
        #happy Raven ON
        show p4 lsmile narrowedwink with fc
        p4 "Nie nie, nic się nie stało! To szalenie miłe!"
        "”I jeszcze jest taka miła...” - pomyślała tym razem Lia."
        p1 "Oh. Ale i tak przepraszam, nie chciałam, żeby wyszło tak dziwnie."
        p4 "Oj no! Naprawdę nic się nie stało!"
        #smile Raven ON
        show p4 lsmile wink with fc
        p4 "Masz jakieś plany co możemy porobić dalej?"

    #jeśli cecha: NOTHING
    if c_nothing == True:
        "Lia przyglądała się Raven. Nie była w stanie dostrzec nic nadzwyczajnego."
        "Myśli szybko uleciały w całkowicie innym kierunku."
        #smile Raven OFF
        show p4 lneutral with fc
        "Głębokie zamyślenie “o niczym” przerwał nagle głos Raven."
        p4 "Hej Lia, żyjesz?"
        #surprised Lia ON
        show p1 lneutral widenedwink bsurprised with fc
        p1 "Oh, tak tak. Wybacz, zamyśliłam się."
        #surprised Lia OFF
        show p1 lneutral -widenedwink -bsurprised with fc
        p4 "Właśnie zauważyłam, ładnie odleciałaś. Wszystko w porządku?"
        p1 "Tak, tak - tylko się zamyśliłam. Mówiłaś coś wcześniej?"
        p4 "Tak. Pytałam czy mamy jakieś plany teraz."


    menu:
        "“Myślałam, żeby pokazać Ci moje ulubione miejsce...”":
            p1 "Myślałam, żeby pokazać Ci moje ulubione miejsce..."
            #Raven smile ON
            show p4 lsmile with fc
            p4 "Ooo, brzmi interesująco - bardzo chętnie je zobaczę!"
            #Lia smile ON
            show p1 lsmile with fc
            p1 "O, to super! Możemy iść od razu jeśli chcesz..."
            p4 "Tak! Jak najbardziej - chodźmy!"
            jump e8_p4a
            #Przejście do E8-P4A


        "“Możemy przejść się do naszej wioski.”":
            p1 "Hmm, tak - moglibyśmy przejść się do wioski. Zobaczyłabyś trochę więcej naszej okolicy. Co Ty na to?"
            p4 "Brzmi ciekawie. Idziemy teraz?"
            p1 "Tak! Możemy wyruszyć od razu. Chodźmy!"
            jump e8_p4b
            #Przejście do E8-P4B

        "“Oh, nie - teraz nie mam dla Ciebie czasu.”":
            #wybranie opcji dodaje
            # +1 pkt HatePath
            # +1 pkt RavenHate
            $ HatePath += 1
            $ RavenHate += 1
            #sad Raven ON
            show p4 bsad lsad
            p1 "Oh, niestety nie mam teraz więcej czasu dla Ciebie."
            p4 "Ah, rozumiem. To co mam teraz..."
            p1 "Możesz zejść na dół i poszukać mojej mamy, na pewno znajdzie dla Ciebie jakieś zajęcie."
            p4 "No dobrze. To pójdę od razu."
            #Raven wychodzi z pokoju, Lia zostaje sama
            show p4:
                linear 4 xalign 0.0 xpos 1.0
            "Po wyjściu Raven z pokoju, Lia poczuła się strasznie dziwnie."
            "”To pewnie zmęczenie” - pomyślała po czym ruszyła w kierunku swojego pokoju."
            #zmiana Background na pokój Lii
            scene img_pokojlii_dragon
            show p1
            with dissolve
            "”Położę się na chwilę.” - pomyślała i tak zrobiła."
            hide p1
            scene black with dissolve
            call timechange from _call_timechange_1
            scene img_pokojlii_dragon with dissolve
            # TODO Upływ czasu: 1
            "Po pewnym czasie Lię obudziło pukanie do drzwi."
            #Lia z lewej strony
            #confused Lia ON
            show p1:
                align (.1, 1.0) xzoom -1
            p1 "Proszę..."
            "Odpowiedziała zaspanym głosem."
            #Selene pojawia się po prawej
            show p2:
                align (0.0,1.0) xpos 1.0
                linear 2 xpos 0.7
            "Do pokoju weszła jej mama, spojrzała na nią po czym powiedziała."
            p2 "Chyba wystarczy tego spania, nie uważasz?"
            p1 "Może... Co jest?"
            p2 "Chodź na dół. Czas trochę popracować i pokażesz Raven co i jak."
            p2 "Postanowiła trochę pomóc przy pracy."
            p1 "Ehh... No dobrze. Zaraz zejdę."
            p2 "Nie zaraz. Teraz."
            #annoyed Lia ON
            show p1 bangry narrowedwink with fc
            p1 "No dobrze dobrze, idę."
            #Selene wychodzi i przejście do E8-WORK2
            show p2 with fc:
                xzoom -1
            show p2:
                linear 2 xpos 1.0

            jump e8_work2



############################ OGRÓD Z RAVEN ############################
label e8_p4a:
    #Background to las w tle, jak wcześniej w E2
    #naturalne miny wracają
    #Niech Lia i Raven poruszają się od prawej do lewej bardzo powoli, Lia przed Raven
    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ paczka odebrana":
                $ paczka01 = "odebrana"
                pass
            "dev/ paczka nieodebrana":
                pass
    ########################### /devstuff #########################
    "Dziewczyny opuściły Tawernę i ruszyły powoli w kierunku Sekretnego Ogrodu."
    scene forest_day:
        pos (-1.0,-0.6) zoom 0.98
        linear 100 pos (-0.15,-0.5) zoom 1.0
    show p1:
        align (0.0,1.0) xpos .6
    show p4:
        align (0.0,1.0) xpos .8 xzoom -1
    with Dissolve(1.0)

    p4 "To miejsce... Możesz powiedzieć o nim coś więcej?"
    #Lia smirk ON
    show p1 bangry narrowedwink lsmile with fc
    p1 "A co, nie lubisz niespodzianek?"
    p4 "W zasadzie nie wiem... Powiedz chociaż troszkę!"
    #Lia smile ON
    show p1 bneutral wink lsmile with fc
    p1 "No dobrze dobrze! Idziemy do Sekretnego Ogrodu. A przynajmniej tak go nazywam..."
    #Raven smile ON
    show p4 lsmile with fc
    p4 "Ooo, brzmi tajemniczo. Daleko to?"
    p1 "Nieee, niedługo powinniśmy widzieć przejście między drzewami - na pewno zauważysz."
    #happy Raven ON
    show p4 narrowedwink lsmile with fc
    p4 "Super! Nie mogę się doczekać!"
    p1 "Mam nadzieję, że Ci się spodoba! Tak samo jak mi się spodobało."
    #zwykłe miny ON
    show p1 bneutral wink lneutral with fc
    show p4 bneutral wink lneutral with fc
    p4 "Jak w ogóle trafiłaś na to miejsce?"
    p1 "Kiedyś go znalazłam przypadkiem, było tak jakby coś mnie wzywało..."
    p1 "W sumie nie pamiętam już dokładnie."
    p4 "Oh, chyba rozumiem."
    "Raven zamyśliła się zastanawiając się jak mogło dokładnie coś takiego wyglądać."
    "Tymczasem marsz nawiedziła krótka cisza."


    # TODO jeśli mamy PACZKA01
    if paczka01 == "odebrana":
        #dodatkowy dialog komentujący paczkę
        "Ciszę postanowiła niespodziewanie przerwać Raven."
        p4 "W ogóle jeśli mogę się zapytać... Po co Ci ta paczka?"
        #surprised Lia ON
        show p1 bneutral wink lsmile with fc
        p1 "Oj, głupia ja... Zapomniałam, że już ją wzięłam."
        p1 "Ojciec mnie poprosił, żeby ją dostarczyć do wioski..."
        #surprised Lia OFF
        show p1 bsurprised widenedwink lneutral with fc
        p1 "No trudno. Teraz chyba będę musiała z nią cały czas chodzić."
        #happy Raven ON
        show p4 narrowedwink lsmile with fc
        p4 "Haha, chyba nie masz teraz wyjścia."
        #smile Lia ON
        show p1 bneutral wink lsmile with fc
        p4 "Ale nie martw się! Pomogę Ci jej przypilnować!"
        p1 "Haha, dzięki! Tymczasem powoli docieramy do celu - chodź!"
        #emocje OFF
        show p1 bneutral wink lneutral with fc
        show p4 bneutral wink lneutral with fc

    #jeśli nie mamy paczki to nie ma dodatkowego dialogu w tym momencie


    # TODO wjazd tła nad przejście między drzewami, powolne
    show forest_day:
        pos (-0.15,-0.5) zoom 1.0
        linear 60 pos (-0.25,-0.7) zoom 1.3
    with Dissolve(1.0)
    "Na horyzoncie powoli ujawniało się przejście o którym wcześniej wspomniała Lia."
    "W końcu obie dotarły do wejścia, Lia odezwała się jako pierwsza:"
    p1 "Musimy teraz przejść kawałek przez gęsty las. Chodź za mną."
    "Raven ruszyła za Lią bez słowa, unikając jak najstaranniej wszelkich naturalnych przeszkód."
    "Po kilkunastu minutach bardzo powolnego marszu zaczął powoli ujawniać się Ogród."


    #Ogród wjeżdża, od lewej do prawej. Postacie znikają w tej chwili i jest przejazd od #lewej do prawej pokazujący całość, a następnie jesteśmy na lewej części i wraca rozmowa
    scene secretgarden_bg:
        align (1.0,1.0)
        linear 20 xalign 0.2
    #pause 20


    #Raven i Lia stoją po lewej, obie patrząc się w prawo - tak jakby na drzewo
    #Raven surprised ON
    #Lia sad ON
    show p1 bsad lsad:
        align (-1.05,1.0) xzoom -1
        linear 20 align (0.05,1.0)
    show p4 bsurprised widenedwink:
        align (-1.3,1.0)
        linear 20 align (0.3,1.0)
    with fade
    pause
    p1 "Skąd takie zdziwienie? Nie podoba Ci się???"
    "Raven nie odpowiedziała od razu, jej wzrok wędrował po wszystkich zakamarkach Ogrodu."
    #happy Raven ON
    show p4 bneutral narrowedwink lsmile with fc:
    p4 "Hmm? Nie, nie - jest tu pięknie! Przepraszam, aż nie wiem co więcej powiedzieć..."
    #smile Lia ON
    show p1 bneutral wink lsmile with fc:
    p1 "Czyli podoba Ci się tutaj, tak?"
    p4 "Tak! Jest wspaniale!"
    #normal Lia ON
    show p1 bneutral wink lneutral with fc:
    p1 "Oh, cieszę się w takim razie - nikogo wcześniej tu nie zabierałam..."
    p1 "Nie byłam pewna Twojej reakcji."
    #smile Lia ON
    show p1 lsmile with fc:
    p4 "Oj, niepotrzebnie się przejmujesz! Cieszę się, że mnie tu zabrałaś!"
    p1 "No dobrze, masz rację. Co chciałabyś porobić?"
    p4 "Nie mam pojęcia, może poróbmy przez chwilę nic?"
    p1 "Haha, podoba mi się ten pomysł."
    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ zrobione e7-p4":
                $ akt1_UkonczenieEpizodow["e7_p4"] = True
                pass
            "dev/ inny wybór":
                pass

    ########################### devstuff #########################

    #Postacie na chwilę znikają, znów powolne przejście przez cały art, lekki zoom tu i tam 6sec
    hide p1
    hide p4
    with dissolve
    show secretgarden_bg:
        linear 6 xalign 0.6
        linear 5 zoom 1.1 xalign 0.9

    "Dziewczyny spacerowały przez chwilę po wszystkich zakamarkach Ogrodu."
    "Po kilku chwilach usiadły pod drzewem, każda wpatrując się w swoim kierunku - rozmyślając nad wszystkim i niczym."
    #tutaj wraca ujęcie na postacie (po tym lataniu po obszarze, wycentrowane na drzewie)
    window hide
    show secretgarden_bg:
        linear 2.5 xalign 0.5 yalign 0.5 zoom 1.2
    #    block:
    #        linear 2 zoom 1.22
    #        linear 1 zoom 1.23
    #        linear 1 zoom 1.22
    #        linear 2 zoom 1.2
    #        linear 1 zoom 1.19
    #        linear 2 zoom 1.21
    #        repeat
    pause 3
    show p1:
        align (.8,1.8)
    show p4:
        align (.2,1.8)
    with dissolve
    window show


    ########### TODO przynajmniej 1pkt RavenLove / lub E7-P4
    if akt1_UkonczenieEpizodow['e7_p4']:
        "Po kilku minutach Lia postanowiła się odezwać:"
        p1 "Hej! Akrobatko - o czym tak myślisz?"
        p4 "Hah, akrobatko? Dziwnie..."
        p1 "Oj, przepraszam - nie chciałam, żeby tak to źle zabrzmiało..."
        #Raven blush ON
        show p4 blush with fc
        p4 "Nie nie, chciałam powiedzieć, że dziwnie zabrzmiało. Po prostu..."
        #Raven smile ON
        show p4 lsmile with fc
        p4 "Po prostu teraz nie czułam w tym nic negatywnego."
        #Lia blush ON
        show p1 blush
        p4 "Gdy Ty to powiedziałaś to było to dla mnie miłe..."
        p1 "Oh..."
        #sad smile Raven ON
        show p4 bsad lsmile with fc
        p4 "Nie zrozum mnie źle. Po prostu nie czułam się tak wcześniej."
        p4 "Opowiadałam Ci jak wyglądała moja historia..."
        #sad smile Lia ON
        show p1 bsad lsmile with fc
        p1 "To prawda... Może lepiej o tym nie myśleć tyle? Skupić się na tym co jest teraz?"
        #smile Raven ON
        show p4 -bsad with fc
        p4 "Chyba masz rację."
        #neutral Raven ON
        show p4 bneutral wink lneutral with fc
        p4 "A co do teraźniejszości... Twoja mama zaproponowała, żebym została z Wami przez jakiś czas."
        #surprised_happy Lia ON
        show p1 bsurprised widenedwink lsmile with fc
        p1 "Oh... Naprawdę? I co odpowiedziałaś?"
        p4 "Jeszcze nic. Prosiła, żebym się zastanowiła."
        #confused Raven ON
        show p4 bsurprised wink lneutral with fc
        p4 "Co powinnam zrobić Twoim zdaniem?"
        #smile Lia ON
        show p1 bneutral wink lsmile with fc
        p1 "Zostań z nami! Będzie Ci z nami dobrze!"
        #surprised_happy Raven ON
        show p4 bsurprised widenedwink lsmile with fc #Dissolve(0.1)
        "Natychmiast odpowiedziała Lia, co pozytywnie zaskoczyło Raven."
        p4 "Huh... Mówisz poważnie?"
        p1 "Jak najbardziej!"
        p4 "To w takim razie chyba zostanę..."
        p1 "Super! Na pewno tego nie pożałujesz."
        #smile Raven ON
        show p4 bneutral wink lsmile with fc
        p4 "Wiem, że nie."
        "Dziewczyny zerkały na siebie w spokojnych uśmiechach."
        "Po chwili pogrążyły się we własnych myślach."

    ########### TODO poniżej 1pkt RavenLove / lub E7-P5 E7-N
    else:
        "Lia odezwała się pierwsza:"
        p1 "O czym myślisz?"
        #surprised_sad Raven ON
        show p4 bsurprised widenedwink lsad with fc
        p4 "Hmm? Wybacz, zamyśliłam się..."
        #surprised_happy Lia ON
        show p1 bsurprised widenedwink lsmile with fc
        p1 "Hah. Właśnie o to pytałam."
        #surprised_neutral Lia ON
        show p1 lneutral with fc
        p1 "O czym tak myślisz?"
        #sad Raven ON
        show p4 bneutral wink lsad with fc
        p4 "Uh. Chyba o wszystkim. Ciężko mi to opisać."
        p4 "Strasznie dużo ostatnio się wydarzyło. To coś nowego dla mnie."
        #confused Lia ON
        show p1 bsurprised wink lneutral with fc
        p1 "W dobrym czy złym sensie?"
        p4 "Szczerze? Wydaje mi się, że w dobrym... Tylko to wciąż wszystko nowe."
        #more_sad Raven ON
        show p4 narrowedwink lsad with fc
        p4 "Wydaje mi się też, że gorzej niż wcześniej nie mogłoby być..."
        #shock Lia ON
        show p1 bsurprised widenedwink lopen with fc
        p1 "Aż tak źle było?"
        p4 "Mhm. Nie chcę zbyt dużo o tym mówić..."
        p4 "Powiem tylko, że nie było łatwo. Byłam kimś na zawołanie, musiałam robić co mi kazali..."
        #sad Lia ON
        show p1 bneutral wink lsad with fc
        p4 "Nie życzyłabym tego nikomu innemu."
        p1 "Oh. Nie wiedziałam. Przykro mi. Z nami na pewno byłoby Ci lepiej..."
        #surprised_sad Raven ON
        show p4 bsurprised widenedwink lsad with fc
        p4 "Odnośnie tego... Twoja mama zaproponowała, żebym została z Wami przez jakiś czas."
        #surprised_happy Lia ON
        show p1 bsurprised widenedwink lsmile with fc
        p1 "Oh... Naprawdę? I co odpowiedziałaś?"
        p4 "Jeszcze nic. Prosiła, żebym się zastanowiła."
        #confused Raven ON
        show p4 bsurprised wink lneutral with fc
        p4 "Myślałam co powinnam zrobić. Co byś mi doradziła?"
        #smile Lia ON
        show p1 bneutral wink lsmile with fc
        p1 "Zostań z nami! Na pewno poczujesz się w naszym gronie lepiej."
        #surprised_happy Raven ON
        show p4 bsurprised widenedwink lsmile with fc
        "Odpowiedziała Lia bardzo szybko, co pozytywnie zaskoczyło Raven."
        p4 "Poważnie? Chciałabyś, żebym została?"
        p1 "Oczywiście."
        p4 "To w takim razie chyba zostanę..."
        p1 "Super! Na pewno tego nie pożałujesz."
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        p4 "Taką właśnie mam nadzieję."
        "Dziewczyny zerkały na siebie w spokojnych uśmiechach."
        "Po chwili pogrążyły się we własnych myślach."

    #ujęcie z lekkim odjazdem od drzewa, 3-4 sec takiego spokojnego ruchu po ogrodzie
    window hide
    show secretgarden_bg:
        linear 4 xalign 0.5 yalign 0.0
    show p1:
        align (.8,1.8)
        linear 4 align (.8,3.5)
    show p4:
        align (.2,1.8)
        linear 4 align (.2,3.5)
    pause 3.9
    scene black with dissolve
    pause 1

    #powrót do ujęcia dziewczyn patrzących na siebie
    scene secretgarden_bg:
        xalign 0.5 yalign 0.5 zoom 1.2
    show p1:
        align (.8,1.8)
    show p4:
        align (.2,1.8)
    with fade
    window auto
    "Upłynęła dłuższa chwila, w której zarówno Lia jak i Raven odpłynęły ku swoim myślom."
    "W pewnym momencie Raven westchnęła."
    #thinking Raven ON
    show p4 bangry closed lsad with fc
    #surprised_neutral Lia ON
    show p1 bsurprised widenedwink lneutral with fc
    p4 "Sigh..."
    p1 "Hmm? Stało się coś?"
    #surprised_sad Raven ON
    show p4 bsurprised widenedwink lsad with fc
    p4 "Hmm? Oh, nie... Wybacz. Za dużo myślę."
    p1 "O czym?"
    p4 "Uh, o niczym takim. Po prostu za dużo myślę."
    #confused Lia ON
    show p1 bsurprised wink lneutral with fc
    p1 "..."
    p4 "Zastanawiam się po prostu nad wszystkim..."
    p1 "Nad czymś konkretnym?"
    p4 "Haha, nad życiem. Ale nie wiem czy można je nazwać konkretnym."
    p4 "To obecnie jeden wielki chaos, który ciężko pojąć."
    p4 "Zastanawiam się nad tym co teraz w ogóle zrobić."
    p4 "Zastanawiam się nad tym czy te zbiry mnie w ogóle zostawią..."
    #suprised_sad Lia ON
    show p1 bsurprised widenedwink lsad with fc
    p4 "Zastanawiam się czy nie wrócą się zemścić."
    p4 "Myślę o tym czy będę w stanie żyć z Wami..."
    #small_tears Raven ON
    show p4 smalltears with Dissolve(0.3)
    p4 "Czy będę wystarczająco dobra, czy dam radę... Nie chcę Cię..."
    p4 "Nie chcę Was teraz zawieść."
    "Lia była lekko zaskoczona nagłym wybuchem szczerości ze strony Raven."
    "Spojrzała w jej kierunku uważnie, widziała, że Raven jest bliska łez."

    menu:
    ########### E8-P4AD1 (Romans)
        "Przytul ją.":
            # +1 pkt RavenLove
            # +1 pkt LovePath
            $ RavenLove += 1
            $ LovePath += 1
            #ujęcie komiksu E8P4C1
            show black with fade
            show e8p4c1 with dissolve
            p1 "Chodź tu do mnie."
            #ujęcie komiksu E8P4C2
            show e8p4c2 with dissolve
            "Lia zbliżyła się do Raven i mocno ją przytuliła."
            p1 "Wszystko będzie dobrze."
            #ujęcie komiksu E8P4C3
            show e8p4c3 with dissolve
            "Ta lekko zaskoczona szybko odwzajemniła uścisk wtulając się w jej ramiona."
            "Trwały chwilę w tej pozie, obie czerpiąc z tego nieznajomą energię."
            p4 "Dziękuję."
            "Wyszeptała Raven po chwili."
            #powrót do standardowego ujęcia
            show p1 bneutral wink lsmile with fc
            show p4 bneutral wink lsmile -smalltears with fc

            hide e8p4c3
            hide e8p4c2
            hide e8p4c1
            with dissolve
            hide black with dissolve
            #smile Lia ON
            #smile Raven ON

            "Po chwili obie odsunęły się od siebie z uśmiechami na twarzach."
            p1 "Chyba czas już powoli wracać."
            p4 "Dobrze, chodźmy."
            "Obie ruszyły w drogę powrotną, uśmiechając się i zerkając na siebie co chwilę."
            # TODO w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_2
            #$ dt + 1
            #przejście przed drzewami obok drogi do starego lasu
            scene forest_dn:
                pos (-0.15,-0.5) zoom 0.98
                linear 60 pos (-1.0,-0.6) zoom 1.0
            #show p1:
            #    align (0.0,1.0) xpos .6
            #show p4:
            #    align (0.0,1.0) xpos .8 xzoom -1
            with Dissolve(1.0)
            "Droga powrotna była spokojna, obie spędziły ją na rozmyślaniach."
            "W Tawernie przywitał je Zorn."


    ########### E8-P4AD2 (just friends)
        "“Wszystko będzie dobrze, razem damy radę.”":
            #big_tears Raven ON
            #sad_smile Lia ON
            show p4 bigtears with fc
            show p1 bsad wink lsmile with fc
            p1 "Hej, hej! Nie myśl tyle o każdej rzeczy."
            p1 "Teraz wszystko już będzie dobrze."
            p1 "Hej, spójrz na mnie proszę."
            p1 "..."
            #small_tears Raven ON
            show p4 -bigtears with fc
            p4 "..."
            p1 "Będzie dobrze. Razem przez to przejdziemy, dasz radę?"
            p4 "Spróbuję..."
            p1 "Musisz mi obiecać, że dasz radę. Nie ma próbowania."
            #sad_smile Raven ON
            show p1 bsad wink lsmile with fc
            p4 "No dobrze. Zrobię co w mojej mocy. Możemy już wracać?"
            p1 "Oczywiście. Chodźmy."
            # TODO w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_3
            #przejście przed drzewami obok drogi do starego lasu
            scene forest_dn:
                pos (-0.15,-0.5) zoom 0.98
                linear 60 pos (-1.0,-0.6) zoom 1.0
            with fade
            "Powrót minął spokojnie, obie miały chwilę na uspokojenie emocji i pozbieranie myśli."
            "Dotarły do Tawerny, gdzie przywitał je Zorn."


    ############# E8-P4AD3 (negatywnie)
        "“Oj już tak nie płacz nad swoim losem, weź się w garść.”":
            #+1 pkt HatePath
            #+1 pkt RavenHate
            $ RavenHate += 1
            $ HatePath += 1
            #Raven suprsied_sad ON
            show p4 bsurprised widenedwink lsad with fc
            p4 "Uh..."
            #frown Lia ON
            show p1 bangry wink lneutral with fc
            p1 "Po prostu nie możesz tyle płakać nad swoim losem."
            p1 "Weź się w garść."
            p4 "Postaram się..."
            p1 "Tymczasem czas wracać. Długo już tu siedzimy. Chodź."
            #ujęcie z powolnym odjazdem od drzewa
            "Dziewczyny wstały w ciszy i ruszyły w drogę powrotną."
            # TODO w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_4
            #przejście przed drzewami obok drogi do starego lasu
            scene forest_dn:
                pos (-0.15,-0.5) zoom 0.98
                linear 60 pos (-1.0,-0.6) zoom 1.0
            with fade
            "Ta minęła w ciszy i rozmyślaniach."
            "W końcu dotarły do Tawerny, gdzie z powitaniem czekał Zorn."


    ########################### devstuff #########################
    if config.developer:
        show screen devscreen
        "oh just look at the time!"
        "1"
        "2"
        "3"
        "4"
        "5"
    ########################### /devstuff #########################

    #wejście do Tawerny ze spaceru odbywa się automatycznie
    #background sala główna, dziewczyny po lewej, Zorn po prawej


    #### TODO jeśli nie ma jeszcze pory NOC

    if dt < 5:
        scene img_tavern_mainroom
        show p1:
            align(0.0,1.0) xzoom -1
        show p4:
            align(0.2,1.0)
        show p3:
            align(.8,1.0) xzoom -1
        with fade
        p3 "Hej dziewczyny, gdzie byłyście?"
        #surprised_neutral Lia ON
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Oh, tylko krótki spacer."
        p3 "Mhm. Rozumiem. Raven... Zastanawiałaś się może już nad propozycją mojej żony?"
        #surprised_neutral Raven ON
        show p4 bsurprised widenedwink lneutral with fc
        "Raven zerknęła najpierw na Lię, potem z powrotem na Zorna."
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        p4 "Tak... Pomyślałam, że mogłabym zostać."
        p3 "Wybornie! Będzie Ci z nami dobrze. Hmm."
        p3 "To co powiecie na to, żeby trochę pomóc teraz w Tawernie? Raven od razu zobaczy co i jak."
        #frown Lia ON
        show p1 bangry wink lneutral with fc
        p1 "Ale tato..."
        "Niespodziewanie przerwała jej Raven."
        #annoyed Lia ON
        show p1 bangry narrowedwink lneutral with fc
        p4 "Myślę, że to dobry pomysł... Chciałabym pomóc i się odwdzięczyć."
        p3 "Świetnie, miło z Twojej strony Raven. Lia Ci wszystko pokaże."
        #neutral Lia ON
        show p1 bneutral wink lneutral with fc
        #confused Raven ON
        show p4 bsurprised wink lneutral with fc
        p1 "Eh... Oczywiście, chodź ze mną Raven."
        #przejście do E8-WORK2


    #### TODO jeśli jest już NOC
    if dt >= 5:
        scene img_tavern_mainroom
        show p1 shadow:
            align(0.0,1.0) xzoom -1
        show p4: # TODO shadow:
            align(0.2,1.0)
        show p3 shadow:
            align(.8,1.0) xzoom -1
        with fade
        p3 "Hej dziewczyny, gdzie byłyście tak późno?"
        #surprised_neutral Lia ON
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Oh, tylko krótki spacer."
        p3 "Mhm. Rozumiem. Raven... Zastanawiałaś się może już nad propozycją mojej żony?"
        #surprised_neutral Raven ON
        show p4 bsurprised widenedwink lneutral with fc
        "Raven zerknęła najpierw na Lię, potem z powrotem na Zorna."
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        p4 "Tak... Pomyślałam, że mogłabym zostać."
        show p3 smile with fc
        p3 "Wybornie! Będzie Ci z nami dobrze. Hmm."
        p3 "To co powiecie na to, żeby trochę pomóc w Tawernie rano? Raven od razu zobaczy co i jak."
        #frown Lia ON
        show p1 bangry wink lneutral with fc
        p1 "Ale tato..."
        "Niespodziewanie przerwała jej Raven."
        #annoyed Lia ON
        show p1 bangry narrowedwink lneutral with fc
        p4 "Myślę, że to dobry pomysł... Chciałabym pomóc i się odwdzięczyć."
        p3 "Świetnie, miło z Twojej strony Raven. Lia Ci wszystko rano pokaże."
        #neutral Lia ON
        show p1 bneutral wink lneutral with fc
        #confused Raven ON
        show p4 bsurprised wink lneutral with fc
        p1 "Eh... No dobrze. To teraz chodźmy spać i rano się widzimy, tak?"
        p3 "Mhm."
        scene black with fade
        "Dziewczyny udały się do swoich pokojów i szybko zasnęły."
        # TODO upływ czasu o 1
        call timechange from _call_timechange_5
        "Noc minęła spokojnie. Rano obie szybko się ubrały i zeszły piętro niżej."
        #przejście do E8-WORK2

    $ ee001_UkonczenieEpizodow['e8_p4'] = True
    jump e8_work2

################################################################################
################################################################################
############################# WIOSKA Z RAVEN ###################################

label e8_p4b:

    #Background ścieżka przed Wioską
    #naturalne miny wracają
    #Niech Lia i Raven poruszają się od prawej do lewej bardzo powoli, Lia przed Raven
    scene forest_village_dragonday:
        align (1.0,1.0)
        linear 60 align (0.0,1.0)
    show p1:
        align (0.7,1.0)
    show p4 behind p1:
        align (1.02,1.0) xzoom -1
    with fade
    "Dziewczyny opuściły Tawernę i ruszyły powoli w kierunku Wioski."

    #surprised_neutral Raven ON
    #surprised_happy Lia ON
    show p1 bsurprised widenedwink lsmile
    show p4 bsurprised widenedwink lneutral
    with fc
    p4 "Co właściwie jest w tej wiosce?"
    p1 "Hmm. Byłaś w wielu wioskach wcześniej?"
    p4 "Chyba niezbyt. W kilku byłam, ale nie były zbyt duże."
    p4 "Z tego co zrozumiałam ta jest większa?"
    p1 "Hmm, można tak powiedzieć..."
    p1 "W zasadzie sama nie byłam w innych wioskach, więc w sumie nie mam porównania."
    p1 "Na pewno domów jest więcej niż kilka, w samym centrum jest ich kilkanaście."
    p1 "Mamy też doki, hmm... jest market gdzie możesz kupić różne rzeczy. No jest troszkę atrakcji chyba."
    p1 "Teraz wszystko jest też wystrojone z okazji festiwalu, więc za jakiś czas wszystko będzie wyglądało ciut inaczej."
    #sad_smile Lia ON
    #sad Raven ON
    show p1 bsad wink lsmile
    show p4 bneutral wink lsad
    with fc
    p4 "Hah, doki... W sumie nigdy nie widziałam morza."
    p1 "Poważnie?"
    p4 "Tak..."
    #smile Raven ON
    show p4 bneutral wink lsmile with fc
    p1 "Hmm. Może dziś będzie ku temu okazja!"
    p4 "Byłoby super..."
    "Dalej maszerowały chwilę w ciszy."
    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ paczka odebrana":
                $ paczka01 = "odebrana"
                pass
            "dev/ paczka nieodebrana":
                pass
    ########################### /devstuff #########################
    ###### jeśli mamy PACZKA01
    if paczka01 == "odebrana":
        #dodatkowy dialog komentujący paczkę
        "Postanowiła ją znów przerwać Raven."
        p4 "W ogóle jeśli mogę się zapytać... Po co Ci ta paczka?"
        #surprised Lia ON
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Oh, muszę dostarczyć ją do kowala."
        p1 "Pomyślałam, że wezmę ją przy okazji."
        #sad smile Lia ON
        show p1 bsad wink lsmile
        p1 "Mam nadzieję, że to dla Ciebie nie jest żaden problem..."
        #happy Raven ON
        #smile Lia ON
        show p1 bneutral wink lsmile
        show p4 bneutral narrowedwink lsmile
        with fc
        p4 "Hah, oczywiście, że nie!"
        p1 "Oh, to dobrze! W zasadzie docieramy już powoli do wioski."


    #####jeśli nie mamy PACZKA01
    else:
    #jeśli nie mamy paczki to tylko jedno zdanie dodatkowe przed zmianą ujęcia
        "Po jakimś czasie dotarły na obrzeża wioski."


    #tutaj zmiana tła w wioskę, może jakiś efekt ruchu, żeby poczuć jakby weszły? Od prawej lekki zoom i
    # powolne oddalanie widoku na całą wioskę
    #surprised_happy Raven ON
    #smile Lia ON
    scene img_festival_dn_dragon with fade:
        zoom .6 align (0.0,0.0) pos (-0.2,0.0)
        1
        linear 5 align (0.0,0.0) pos (-1.0,-0.77) zoom 1.0
    pause 6
    show p1 bneutral wink lsmile with moveinright:
        align (0.7,1.0)
    show p4 bsurprised widenedwink lsmile with moveinright:
        align (1.02,1.0) xzoom -1

    "Obie dziewczyny powoli ruszyły w głąb wioski."
    show img_festival_dn_dragon:
        linear 7 align (0.0,0.0) pos (-0.7,-0.77) zoom 1.0
    "Raven uśmiechała się pod nosem co ucieszyło Lię."
    p1 "I jak? Podoba Ci się?"
    p4 "Hmm? Ach, tak! Lepiej niż sobie wyobrażałam. Sporo tutaj wszystkiego!"
    #w tym momencie niech dziewczyny zbliżają się już do centrum, i teraz z lewej nagle wejdzie Meamir i zbliży się
    p1 "Zaraz przejdziemy dalej to zobaczy..."
    show p5 with moveinleft:
        align (0.15,1.0) xzoom -1
    "Lia nie była w stanie dokończyć swojej wypowiedzi. Przerwał jej znajomy głos."
    #smile Meamir ON
    #surprised_happy Lia ON
    #confused Raven ON
    show p1 bsurprised widenedwink lsmile
    show p4 bsurprised wink lneutral
    show p5 bneutral wink lsmile
    with fc
    p5 "Hej Lia!"
    p1 "Oh, hej Meamir!"
    show p5:
        linear 1.5 align (0.4,1.0)
    ########################### devstuff #########################
    if config.developer:
        if not akt1_UkonczenieEpizodow["e7_p5"] and not ee001_UkonczenieEpizodow["e8_p5"]:
            menu:
                "dev/ zrobione e7-p5":
                    $ akt1_UkonczenieEpizodow["e7_p5"] = True
                    pass
                "dev/ zrobione e8-p5":
                    $ ee001_UkonczenieEpizodow["e8_p5"] = True
                    pass
                "dev/ inny wybór":
                    pass

    ########################### devstuff #########################

    ########## TODO jeśli było E8-P5 lub E7-P5
    if akt1_UkonczenieEpizodow['e7_p5'] or ee001_UkonczenieEpizodow['e8_p5']:
        #surprised_neutral Meamir ON
        show p5 bsurprised widenedwink lneutral with fc
        p4 "..."
        #surprised_happy Raven ON
        show p4 bsurprised widenedwink lsmile with fc
        p1 "Oh, właśnie, Meamir poznaj Raven. Raven, to jest Meamir."
        p4 "Hej, miło Cię poznać!"
        #surprised_neutral Raven ON
        #frown Meamir ON
        show p4 bsurprised widenedwink lneutral
        show p5 bangry wink lneutral
        with fc
        p5 "Cześć... hmm, Raven. Kim jesteś? Skądś Cię kojarzę..."
        p5 "Czy to nie z tej sytuacji sprzed Tawerny?"
        #sad_smile Lia ON
        show p1 bsad wink lsmile with fc
        p1 "Oh, tak - Raven miała kłopoty. Mój tata jej pomógł i chwilowo została z nami."
        #smile Meamir ON
        #surprised_happy Raven ON
        show p5 bneutral wink lsmile
        show p4 bsurprised widenedwink lsmile
        with fc
        p5 "To bardzo miło z jego strony!"
        #annoyed Raven ON
        #smirk Meamir ON
        #shock Lia ON
        show p1 bsurprised widenedwink lopen
        show p4 bangry narrowedwink lneutral
        show p5 bangry narrowedwink lsmile
        with fc
        if ee001_UkonczenieEpizodow['e8_p5']:
            p5 "Miło też z Twojej strony, że mimo wszystko przyszłaś się później ze mną spotkać."
        else:
            p5 "Miło też z Twojej strony, że mimo wszystko przyszłaś się wtedy ze mną spotkać."
        #annoyed Meamir ON
        #smirk Raven ON
        #confused Lia ON
        show p1 bsurprised wink lneutral
        show p4 bangry narrowedwink lsmile
        show p5 bangry narrowedwink lneutral
        with fc
        if ee001_UkonczenieEpizodow['e8_p5']:
            p1 "Oh... No tak w sumie wyszło po prostu..."
        else:
            p1 "Oh... No tak bez pożegnania Cię zostawiłam, a Raven i tak musiała odpocząć..."
        #smile Meamir ON
        show p5 bneutral wink lsmile with fc
        if ee001_UkonczenieEpizodow['e8_p5']:
            p5 "Mhm. No dobrze, a jakie plany teraz? Może pójdziemy gdzieś na spacer, co?"
        else:
            p5 "Mhm. No dobrze, a jakie plany teraz? Może pójdziemy znów na spacer gdzieś, co?"
        p1 "Oh, na ten moment jestem z..."



    ########## TODO jeśli było E7-P4 lub E7-N
    else:
        #surprised_sad Meamir ON
        show p5 bsurprised widenedwink lsad with fc
        p4 "..."
        #surprised_happy Raven ON
        show p4 bsurprised widenedwink lsmile with fc
        p1 "Oh, właśnie, Meamir poznaj Raven. Raven, to jest Meamir."
        p4 "Hej, miło Cię poznać!"
        #surprised_sad Raven ON
        #frown Meamir ON
        show p4 bsurprised widenedwink lsad
        show p5 bangry wink lneutral
        with fc
        p5 "Cześć... hmm, Raven. Kim jesteś? Skądś Cię kojarzę..."
        p5 "Czy to nie z tej sytuacji sprzed Tawerny?"
        #sad_smile Lia ON
        show p1 bsad wink lsmile with fc
        p1 "Oh, tak - Raven miała kłopoty. Mój tata jej pomógł i chwilowo została z nami."
        #sad Lia ON
        show p1 bneutral wink lsad with fc
        p1 "Ah i od razu chciałabym przeprosić. W całym tym zamieszaniu zapomniałam się z Tobą pożegnać jak byłeś w Tawernie."
        #smile Lia ON
        #sad_smile Raven ON
        #smile Meamir ON
        show p1 bneutral wink lsmile
        show p4 bsad wink lsmile
        show p5 bneutral wink lsmile
        with fc
        p5 "Oh, nic się nie stało! Zdarza się. Miło, że pamiętałaś."
        #surprised_happy Lia ON
        #annoyed Raven ON
        show p1 bsurprised widenedwink lsmile
        show p4 bangry narrowedwink lneutral
        with fc
        p5 "Jak będziesz miała ochotę to będzie można przejść się na spacer..."
        #sad_smile Lia ON
        #smirk Raven ON
        #annoyed Meamir ON
        show p1 bsad wink lsmile
        show p4 bangry narrowedwink lsmile
        show p5 bangry narrowedwink lneutral
        with fc
        p1 "Oh, to miłe z Twojej strony - chwilowo jednak jestem z Raven, może później..."
        p5 "Oh... To może..."


    "Niespodziewanie przerwał im nieznajomy głos."
    #Wchodzi Ove (P10) od lewej, pozostała trójka obraca się w jego kierunku
    #confused Lia, Raven i Meamir ON
    show p10 with moveinleft:
        align (0.0,1.0)
    show p1 bsurprised wink lneutral
    show p4 bsurprised wink lneutral
    show p5 bsurprised wink lneutral
    with fc
    show p5 with fc:
        xzoom 1
    "Ten brzmiał inaczej i niekoniecznie Lia przypisałaby go do tych przyjemnych."

    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ paczka oddana":
                $ paczka01 = "oddana"
                pass
            "dev/ paczka odebrana":
                $ paczka01 = "odebrana"
                pass
            "dev/ paczka oczekuje":
                $ paczka01 = "oczekuje"
                pass
    ########################### /devstuff #########################

    ######### PACZKA01 wcześniej dostarczona
    if paczka01 == "oddana":
        #angry Ove ON
        show p10 bangry narrowedwink with fc
        p10 "Co to za zbiorowisko?"
        p5 "Tato... To Lia, przyniosła wcześniej paczkę."
        p10 "Ty jesteś Lia, tak?"
        #confused Lia ON
        show p1 bsurprised wink lneutral with fc
        p1 "Tak proszę Pana."
        #neutral Ove ON
        show p10 bneutral wink with fc
        #angry Raven ON
        show p4 bangry narrowedwink lsad with fc
        p10 "Dobrze, że sama ją przyniosłaś, a nie w jakimś dziwnym towarzystwie."
        p10 "Może nie stójcie jak takie słupy na środku przejścia. Zabralibyście się za coś sensownego."
        p10 "Młody, masz mi jeszcze pomóc coś w kuźni, rozumiemy się?"
        p5 "Tak..."
        #Ove wychodzi w lewo jak przyszedł, Meamir obraca się w kierunku dziewczyn z powrotem
        show p10 with fc:
            xzoom -1
        show p5 with fc:
            xzoom -1
        hide p10 with moveoutleft

        p5 "Ekhem... To był mój ojciec. Em, przepraszam za niego..."
        "Niespodziewanie przerwała mu Raven."
        #confused Lia ON
        #frown Raven ON
        #annoyed Meamir ON
        show p1 bsurprised wink lneutral
        show p4 bangry wink lneutral
        show p5 bangry narrowedwink lneutral
        with fc
        p4 "Wybacz, że przerywam kolego, ale Lia... Możemy wracać? Niezbyt dobrze się czuję."
        show p1 with fc:
            xzoom -1
        p1 "Oh. Oczywiście, że możemy - chcesz wrócić od razu?"
        #smirk Raven ON
        #surprised_sad Meamir ON
        show p4 bangry narrowedwink lsmile
        show p5 bsurprised widenedwink lsad
        with fc
        p4 "Tak."
        p1 "Dobrze, to chodźmy."
        #sad_smile Lia ON
        show p1 bsad wink lsmile with fc
        show p1 with fc:
            xzoom 1
        p1 "Meamir, zobaczymy się może później - papa!"
        p5 "No dobrze... Do zobaczenia."
        #Meamir wychodzi w lewo, dziewczyny w prawo. Przejście na background ścieżka przed wioską



    ######### PACZKA01 jest
    elif paczka01 == "odebrana":
        #angry Ove ON
        show p10 bangry narrowedwink with fc
        p10 "Co to za zebranie tutaj?"
        p10 "Młody, pytałeś o paczkę?"
        p5 "Jeszcze nie..."
        #shock Lia ON
        #surprised_sad Raven ON
        show p1 bsurprised widenedwink lopen
        show p4 bsurprised widenedwink lsad
        with fc
        p10 "To na co czekasz? Zresztą, widzę, że takie towarzystwo to pewnie nie dałoby rady przynieść żadnej..."
        #confused Lia ON
        #neutral Ove ON
        show p1 bsurprised wink lneutral
        show p10 bneutral wink
        with fc
        p10 "Ah, coś tam jednak widzę. Lia tak? To moja paczka?"
        #sad_smile Lia ON
        show p1 bsad wink lsmile with fc
        p1 "Tak, to ja. I tak to Pana paczka, proszę."
        #paczka znika z rączek Lii oraz z tego uniwersum
        $ paczka01 = "oddana"
        p10 "Mhm. W końcu."
        #Ove wychodzi w lewo jak przyszedł, Meamir obraca się w kierunku dziewczyn z powrotem
        show p10 with fc:
            xzoom -1
        hide p10 with moveoutleft
        show p5 with fc:
            xzoom -1
        p5 "Ekhem... To był mój ojciec. Em, przepraszam za niego..."
        "Niespodziewanie przerwała mu Raven."
        #confused Lia ON
        #frown Raven ON
        #annoyed Meamir ON
        show p1 bsurprised wink lneutral
        show p4 bangry wink lneutral
        show p5 bangry narrowedwink lneutral
        with fc
        p4 "Wybacz, że przerywam kolego, ale Lia... Możemy wracać? Niezbyt dobrze się czuję."
        show p1 with fc:
            xzoom -1
        p1 "Oh. Oczywiście, że możemy - chcesz wrócić od razu?"
        #smirk Raven ON
        #surprised_sad Meamir ON
        show p4 bangry narrowedwink lsmile
        show p5 bsurprised widenedwink lsad
        with fc
        p4 "Tak."
        p1 "Dobrze, to chodźmy."
        #sad_smile Lia ON
        show p1 bsad wink lsmile with fc
        show p1 with fc:
            xzoom 1
        p1 "Meamir, zobaczymy się może później - papa!"
        p5 "No dobrze... Do zobaczenia."
        #Meamir wychodzi w lewo, dziewczyny w prawo. Przejście na background ścieżka przed wioską


    ######### PACZKA01 nie jest obecna
    else:
        # +1 pkt PaczkaRozrabiaka
        $ PaczkaRozrabiaka += 1
        #angry Ove ON
        show p10 bangry narrowedwink with fc
        p10 "Co to za zbiorowisko tutaj?"
        p10 "Młody, pytałeś o paczkę?"
        p5 "Jeszcze nie..."
        p10 "To na co czekasz? Zresztą, przecież widzę, że jej nie ma... Eh, liczyć na kogoś."
        #shock Lia ON
        #surprised_sad Raven ON
        show p1 bsurprised widenedwink lopen
        show p4 bsurprised widenedwink lsad
        with fc
        p10 "Lia jesteś, tak? Gdzie paczka?"
        p1 "Tak, to ja... Jeszcze nie przyniosłam proszę Pana."
        p10 "Eh, to załatw to - najlepiej jak najszybciej."
        p10 "Zresztą nie dziwię się, że nic nie jest zrobione. W takim towarzystwie to ciężko coś zrobić."
        p10 "Słyszysz młody, ogarnij to - rozumiemy się?"
        p5 "Oczywiście..."


        #Ove wychodzi w lewo skąd przyszedł, Meamir odwraca się znów w kierunku dziewczyn
        show p10 with fc:
            xzoom -1
        hide p10 with moveoutleft
        show p5 with fc:
            xzoom -1
        #sad_smile Meamir ON
        show p5 bsad wink lsmile with fc
        p5 "Ekhem... To był mój ojciec. Em, przepraszam za niego..."
        p5 "To ten, gdzie jest paczka?"
        #surprised_neutral Lia ON
        #angry Raven ON
        #surprised_neutral Meamir ON
        show p1 bsurprised widenedwink lneutral
        show p4 bangry narrowedwink lsad
        show p5 bsurprised widenedwink lneutral
        with fc
        p4 "Nie tutaj jak widać. Lia, możemy wracać? Nie czuję się najlepiej."
        show p1 with fc:
            xzoom -1
        #frown Raven ON
        show p4 bangry wink lneutral with fc
        p1 "Oh... Oczywiście, że możemy."
        show p1 with fc:
            xzoom 1
        p1 "Ah, Meamir - co do paczki to przyniosę później."
        #surprised_sad Meamir ON
        show p5 bsurprised widenedwink lsad with fc
        p5 "No dobrze..."

    #Meamir wychodzi w lewo, dziewczyny w prawo. Przejście na background ścieżka przed wioską
    show p1 with fc:
        xzoom -1
    show p4 with fc:
        xzoom 1
    pause .17
    hide p4 with moveoutright
    hide p1 with moveoutright
    show p5 with fc:
        xzoom 1
    hide p5 with moveoutleft

    scene forest_village_dragonday:
        align (0.0,1.0)
        linear 13 align (0.1,1.0)
    show p1:
        align (0.35,1.0) xzoom -1
    show p4 behind p1:
        align (0.65,1.0)
    with fade
    p4 "Uh. Ojciec Meamira przypominał mi tych oprychów, z którymi Twój się rozprawił..."
    p4 "Przepraszam... Po prostu nie miałam ochoty dłużej tam być."
    p1 "Rozumiem. A jak się teraz czujesz?"
    p4 "Nie wiem... Muszę pomyśleć."
    "Przez krótką chwilę dziewczyny maszerowały w ciszy."
    "Raven jednak zaczęła mówić: niespodziewanie i intensywnie."
    show forest_village_dragonday with fc:
        align (0.1,1.0)
    #surprised_sad Lia ON
    #angry Raven ON
    show p1 bsurprised widenedwink lsad
    show p4 bangry narrowedwink lsad
    with fc
    p4 "W sumie to czuję się fatalnie... Ten cały ojciec Meamira przypomniał mi tylko o wszystkich złych rzeczach z wcześniej."
    p4 "I nie mówię, że on musi być zły czy coś. Po prostu tak się poczułam."
    show p4 with fc:
        xzoom -1
    p4 "I jeszcze to lekceważące W TAKIM TOWARZYSTWIE... Prawie jakbym wróciła do tego wszystkiego co było wcześniej."
    p1 "..."
    p1 "Nie wiem co powiedzieć... Co masz dokładnie na myśli?"
    p4 "Huh. Od czego by tu zacząć. Może od ciągłego wydawania poleceń, zabraniania czegokolwiek..."
    p4 "Trzymania mnie prawie dosłownie na smyczy."
    #sad Raven ON
    show p4 bneutral wink lsad with fc
    p4 "Nie pozwolili mi nawet nigdy z nikim się zaprzyjaźnić."
    p4 "Na nic mi nie pozwalali! Na dodatek teraz nie wiem co zrobić dalej..."
    p1 "..."
    p4 "Zastanawiam się czy w ogóle te gnoje z przeszłości mnie zostawią..."
    p4 "Zastanawiam się czy nie wrócą nagle się zemścić."
    p4 "Po prostu nie wiem co mam teraz robić!"
    "Lia była lekko zaskoczona nagłym wybuchem szczerości ze strony Raven."
    p4 "Myślę o tym czy byłabym w stanie mieszkać z Wami i Was nie zawieść..."
    #shock Lia ON
    show p1 bsurprised widenedwink lopen with fc
    p4 "Oh... No tak. Nie mówiłam. Twoja mama zaproponowała mi, żebym została z Wami na dłużej..."
    #surprised_happy Lia ON
    #small_tears Raven ON
    show p1 bsurprised widenedwink lsmile
    show p4 smalltears
    with fc
    p1 "Ooo, koniecznie musisz z nami zostać! Na pewno będzie Ci dobrze!"
    p4 "Tak sądzisz? Nie jestem pewna..."
    p1 "Tak! Będzie dobrze. Naprawdę."
    p4 "Eh.. Wciąż się waham. Przepraszam. Za dużo myślę... Po prostu nie chcę Was teraz zawieść."
    "Raven odwróciła głowę. Lia zauważyła, że może za moment zalać się łzami."



    menu:
    ######## E8-P4AD1 (Romans)
        "Przytul ją.":
            #+1 pkt RavenLove
            $ RavenLove += 1
            #komiks ujęcie E8P4C1
            p1 "Chodź tu do mnie."
            show black with dissolve
            show e8p4c1 with dissolve
            "Lia zbliżyła się do Raven i mocno ją przytuliła."
            #komiks ujęcie E8P4C2
            show e8p4c2 with dissolve
            p1 "Wszystko będzie dobrze."
            "Ta lekko zaskoczona szybko odwzajemniła uścisk wtulając się w jej ramiona."
            #komiks ujęcie E8P4C3
            show e8p4c3 with dissolve
            "Trwały chwilę w tej pozie, obie czerpiąc z tego nieznajomą energię."
            p4 "Dziękuję."
            "Wyszeptała Raven po chwili."
            #powrót do standardowego ujęcia
            hide e8p4c3
            hide e8p4c2
            hide e8p4c1
            with dissolve
            hide black with dissolve
            #smile Lia ON
            #smile Raven ON
            show p1 bneutral wink lsmile
            show p4 bneutral wink lsmile
            with fc
            "Po chwili obie odsunęły się od siebie z uśmiechami na twarzach."
            p1 "Chyba czas już powoli wracać."
            p4 "Dobrze, chodźmy."
            "Obie ruszyły w drogę powrotną, uśmiechając się i zerkając na siebie co chwilę."
            # TODO CHECK w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_6
            # przejście przed Tawerną lekki zoom na Tawernę
            "Droga powrotna była spokojna, obie spędziły ją na rozmyślaniach."
            "W Tawernie przywitał je Zorn."



    ####### E8-P4AD2 (just friends)
        "“Wszystko będzie dobrze, razem damy radę.”":
            #big_tears Raven ON
            #sad_smile Lia ON
            show p1 bsad wink lsmile
            show p4 bigtears
            with fc
            p1 "Hej, hej! Nie myśl tyle o każdej rzeczy."
            p1 "Teraz wszystko już będzie dobrze."
            p1 "Hej, spójrz na mnie proszę."
            p1 "..."
            #small_tears Raven ON
            show p4 -bigtears with fc
            p4 "..."
            p1 "Będzie dobrze. Razem przez to przejdziemy, dasz radę?"
            p4 "Spróbuję..."
            p1 "Musisz mi obiecać, że dasz radę. Nie ma próbowania."
            #sad_smile Raven ON
            show p4 bsad wink lsmile with fc
            p4 "No dobrze. Zrobię co w mojej mocy. Możemy iść dalej?"
            p1 "Oczywiście. Chodźmy."
            # TODO w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_7
            #przejście przed Tawerną lekki zoom na Tawernę
            "Powrót minął spokojnie, obie miały chwilę na uspokojenie emocji i pozbieranie myśli."
            "Dotarły do Tawerny, tam przywitał je Zorn."


    ####### E8-P4AD3 (negatywnie)
        "“Oj już tak nie płacz nad swoim losem, weź się trochę w garść.”":
            #+1 pkt HatePath
            #+1 pkt RavenHate
            $ HatePath +=1
            $ RavenHate +=1
            #Raven suprsied_sad ON
            show p4 bsurprised widenedwink lsad with fc
            p4 "Uh..."
            #frown Lia ON
            show p1 bangry wink lneutral with fc
            p1 "Po prostu nie możesz tak płakać nad swoim losem tyle."
            p1 "Weź się w garść."
            p4 "Postaram się..."
            p1 "Chodźmy dalej. Mamy kawałek do przejścia jeszcze."
            #ujęcie z powolnym ruchem na ścieżce
            "Dziewczyny ruszyły dalej w ciszy."
            # TODO w tym miejscu mamy upływ czasu o jedną porę do przodu
            call timechange from _call_timechange_8
            #przejście na zewnątrz Tawerny
            "Droga minęła głównie na rozmyślaniu."
            "W końcu dotarły do Tawerny, tam z powitaniem czekał Zorn."



    #wejście do Tawerny ze spaceru odbywa się automatycznie
    #background sala główna, dziewczyny po lewej, Zorn po prawej

    scene img_tavern_mainroom
    show p1:
        align(0.0,1.0) xzoom -1
    show p4:
        align(0.2,1.0)
    show p3:
        align(.8,1.0) xzoom -1
    with fade

    ########### jeśli nie ma jeszcze pory NOC
    if dt < 5:
        p3 "Hej dziewczyny, gdzie byłyście?"
        #surprised_neutral Lia ON
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Oh, tylko krótki spacer."
        p3 "Mhm. Rozumiem. Raven... Zastanawiałaś się może już nad propozycją mojej żony?"
        #surprised_neutral Raven ON
        show p4 bsurprised widenedwink lneutral with fc
        "Raven zerknęła najpierw na Lię, potem z powrotem na Zorna."
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        p4 "Tak... Pomyślałam, że mogłabym zostać."
        p3 "Wybornie! Będzie Ci z nami dobrze. Hmm."
        p3 "To co powiecie na to, żeby trochę pomóc teraz w Tawernie? Raven od razu zobaczy co i jak."
        #frown Lia ON
        show p1 bangry wink lneutral with fc
        p1 "Ale tato..."
        "Niespodziewanie przerwała jej Raven."
        #annoyed Lia ON
        show p1 bangry narrowedwink lneutral with fc
        p4 "Myślę, że to dobry pomysł... Chciałabym pomóc na ile mogę i się odwdzięczyć."
        p3 "Świetnie, miło z Twojej strony Raven. Lia Ci wszystko pokaże."
        #neutral Lia ON
        #confused Raven ON
        show p1 bneutral wink lneutral
        show p4 bsurprised wink lneutral
        with fc
        p1 "Eh... Oczywiście, chodź ze mną Raven."

        #przejście do E8-WORK2



    ########### jeśli jest już NOC
    if dt >= 5:
        p3 "Hej dziewczyny, gdzie tak późno byłyście?"
        #surprised_neutral Lia ON
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Oh, tylko krótki spacer."
        p3 "Mhm. Rozumiem. Raven... Zastanawiałaś się może już nad propozycją mojej żony?"
        #surprised_neutral Raven ON
        show p4 bsurprised widenedwink lneutral with fc
        "Raven zerknęła najpierw na Lię, potem z powrotem na Zorna."
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        p4 "Tak... Pomyślałam, że mogłabym zostać."
        p3 "Wybornie! Będzie Ci z nami dobrze. Hmm."
        p3 "To co powiecie na to, żeby trochę pomóc w Tawernie rano? Raven od razu zobaczy co i jak."
        #frown Lia ON
        show p1 bangry wink lneutral with fc
        p1 "Ale tato..."
        "Niespodziewanie przerwała jej Raven."
        #annoyed Lia ON
        show p1 bangry narrowedwink lneutral with fc
        p4 "Myślę, że to dobry pomysł... Chciałabym pomóc na ile mogę i się odwdzięczyć."
        p3 "Świetnie, miło z Twojej strony Raven. Lia Ci wszystko rano pokaże."
        #neutral Lia ON
        #confused Raven ON
        show p1 bneutral wink lneutral
        show p4 bsurprised wink lneutral
        with fc
        p1 "Eh... No dobrze. To teraz chodźmy spać i rano się widzimy, tak?"
        p3 "Mhm."
        "Dziewczyny udały się do swoich pokojów i szybko zasnęły."
        #upływ czasu o 1
        call timechange from _call_timechange_9
        "Noc minęła spokojnie. Rano obie szybko się ubrały i zeszły piętro niżej."

        #przejście do E8-WORK2
    jump e8_work2


################################################################################
################################################################################
######################### E8-P5 - wątek Meamira ################################

#w momencie kliknięcia na Meamira we wsi sprawdzamy:
##### jeśli nie było E8-P4B przechodzimy do E8-P5A
##### jeśli było E8-P4B w wersji wioskowej przechodzimy do E8-P5B

################################################################################
######################### E8-P5A - paczka w drodze #############################


#Aktywuje się poprzez kliknięcie Meamira stojącego przy Kuźni we Wsi


label e8_p5:
    if ee001_UkonczenieEpizodow["e8_p5"]:
        jump e8_p5b
    else:
        pass

    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ zrobione e7-p5":
                $ akt1_UkonczenieEpizodow["e7_p5"] = True
                pass
            "dev/ inny wybór":
                pass

    ########################### devstuff #########################


    ##############################   E8-P5A    #################################

    ###jeśli E7-P5
    if akt1_UkonczenieEpizodow["e7_p5"]:
        "Lia ruszyła powolnym krokiem w kierunku Meamira."
        #zoom na Kuźnię, Meamir po lewej, Lia po prawej
        #Meamir smile ON
        "Gdy tylko ją dostrzegł na jego twarzy od razu zagościł uśmiech."
        p4 "Lia! Hej! Miło Cię znów widzieć!"
        #surprised_happy Lia ON
        p1 "Hej Meamir!"
        p4 "Co Cię sprowadza?"
        p1 "Ah, chciałam..."
        "Wypowiedź nagle przerwał nieznajomy głos."
        #Wchodzi Ove (P10) od lewej, pozostała dwójka obraca się w jego kierunku
        #confused Lia i Meamir ON
        "Brzmiał on nietypowo. Lia niekoniecznie przypisałaby go do tych przyjemnych."

    ###jeśli E7-P4 lub E7-N
    else:
        "Lia ruszyła powolnym krokiem w kierunku Meamira."
        #zoom na Kuźnię, Meamir po lewej, Lia po prawej
        #surprised_happy Meamir ON
        "Gdy tylko ją dostrzegł na jego twarzy powoli zagościł uśmiech."
        #sad_smile Lia ON
        p4 "O, hej Lia! Miło Cię zobaczyć."
        p1 "Hej Meamir..."
        p4 "Co Cię sprowadza?"
        p1 "Oh, właśnie. Chciałam Cię przeprosić, że tak bez słowa Cię zostawiłam wtedy."
        p4 "Oj, nic się chyba nie stało. Widziałem, że było tam jakieś zamieszanie."
        p4 "Nie chciałem się wtrącać, zwiększyłbym tylko chaos."
        p1 "Oh, dzięki za zrozumienie. No trochę dziwna sytuacja była..."
        p1 "Mam teraz nadzieję, że..."
        "Wypowiedź nagle przerwał nieznajomy głos."
        #Wchodzi Ove (P10) od lewej, pozostała dwójka obraca się w jego kierunku
        #confused Lia i Meamir ON
        "Brzmiał on nietypowo. Lia niekoniecznie przypisałaby go do tych przyjemnych."

    ###jeśli mamy PACZKA01
    if paczka01 == "odebrana":
        #angry Ove ON
        p10 "Co robisz młody? Kto to?"
        p5 "Ah, to jest Lia..."
        #surprised_sad Lia ON
        p10 "Ha, Lia od Zorna? Masz moją paczkę?"
        #neutral Ove ON
        p10 "Ah, widzę, że coś tam masz - to moja?"
        #paczka znika
        p1 "T-tak... Proszę."
        p10 "Mhm. Następnym razem szybciej z zamówieniami, nie mogę wiecznie czekać."
        #Ove wychodzi w lewo, Meamir obraca się do Lii
        #surprised_neutral Lia ON
        p5 "Eh... Przepraszam za mojego tatę..."
        p5 "Nie wiem czemu jest taki... Ciężko mi czasem go zrozumieć. Nie mniej jednak, przepraszam."
        #sad_smile Lia ON
        p1 "Oh, no cóż. Rozumiem. Nic się nie stało - zdarza się."
        #sad_smile Meamir ON
        p5 "Dzięki za zrozumienie... Tak się zastanawiałem..."
        #surprised_neutral Lia ON
        p5 "Miałabyś ochotę może pójść na spacer?"

    ###jeśli nie mamy PACZKA01
    else:
        #angry Ove ON
        p10 "Co robisz młody? Kto to?"
        p5 "Ah, to jest Lia..."
        #shock Lia ON
        p10 "Ha, Lia od Zorna? Masz moją paczkę?"
        p1 "..."
        p10 "Masz ją czy nie? Bo nic nie widzę..."
        p1 "N-nie... Nie mam proszę Pana."
        #surprised_sad Meamir ON
        p10 "No kurwa... Na nikim nie można polegać!"
        p10 "Ile muszę czekać na głupią paczkę?"
        p10 "Młody, idź z nią i ogarnijcie to od razu."
        p10 "Teraz."
        #Ove wychodzi w lewo, Meamir obraca się do Lii
        #surprised_neutral Lia ON
        p5 "Eh... Przepraszam za mojego tatę..."
        p5 "Nie wiem czemu jest taki... Ciężko mi czasem go zrozumieć. Nie mniej jednak, przepraszam."
        #sad_smile Lia ON
        p1 "Oh, no cóż. Rozumiem. Nic się nie stało - zdarza się."
        #sad_smile Meamir ON
        p5 "Dzięki za zrozumienie... To przejdźmy się może po tę paczkę teraz..."
        p1 "Eh, no dobrze... Lepiej ogarnąć to od razu."
        "Dwójka ruszyła powoli poza wioskę."
        #przejście do E8-P5C
        jump e8_p5c


    menu:
        "“Jasne, z chęcią się przejdę.”":
            #happy Lia ON
            #surprised_happy Meamir ON
            p5 "Super! A gdzie chciałabyś pójść?"
            p1 "Hmm? Myślałam, że coś zaproponujesz!"
            #confused Meamir ON
            p5 "Oj... Nie pamiętasz? Dopiero się wprowadziłem, wciąż nie znam okolicy na tyle dobrze..."
            #smirk Lia ON
            p1 "No niech Ci będzie. Ale coś musisz zasugerować."
            #smile Meamir ON
            p5 "Może pokażesz swoje ulubione miejsce?"
            #smile Lia ON
            p1 "Hmm. Niech będzie. Chodźmy!"
            p5 "Oh, ok. A gdzie?"
            p1 "Zobaczysz, chodź!"
            jump e8_p5d
            #przejście do E8-P5D

        "“Dzięki, ale teraz jestem zbyt zmęczona. Innym razem.”":
            #surprised_sad Lia ON
            #surprised_sad Meamir ON
            p5 "Oh... Myślałem, że gdzieś się przejdziemy..."
            p1 "Wybacz. Po prostu nie mam teraz siły."
            p1 "Dużo się ostatnio działo. Innym razem możemy się przejść."
            #sad_smile Lia ON
            p5 "No dobrze... Oczywiście nie będę namawiał na siłę."
            p1 "Dzięki za zrozumienie. To będę uciekała."
            #sad_smile Meamir ON
            p5 "Dobrze... Do zobaczenia!"
            p1 "Papa!"
            #powrót do widoku wioski, Meamir chwilowo znika i wraca na swoje miejsce dopiero po upływie 5 pór z dostępnym kolejnym epizodem
            #neutral mina wraca Lii
            #ekran wraca do widoku wioski i do wolnej gry
            jump ee_town

        "“Nie mam ochoty z Tobą teraz nigdzie chodzić.”":
            #+1pkt HatePath
            #+1pkt MeamirHate
            $ HatePath += 1
            $ MeamirHate += 1
            #annoyed Lia ON
            #more_sad Meamir ON
            p5 "Oh... Myślałem..."
            p1 "Źle myślałeś. Nie mam ochoty nigdzie teraz iść po prostu."
            p5 "No dobrze..."
            p1 "Muszę iść. Na razie."
            p5 "Ok... Pa..."
            #powrót do widoku wioski, Meamir chwilowo znika i wraca na swoje miejsce dopiero po upływie 5 pór z dostępnym kolejnym epizodem
            #neutral mina wraca Lii
            #ekran wraca do widoku wioski i do wolnej gry
            jump ee_town


#################################################
    ########################## E8-P5B - paczka oddana ##########################
label e8_p5b:
    #Jeśli byliśmy już we Wsi i rozmawialiśmy z Meamirem. Paczka oddana.
    #jeśli było już E8-P4B to mamy TEN (E8-P5B) początek dla wątku E8-P5:
    "Lia ruszyła powolnym krokiem w kierunku Meamira."
    #zoom na Kuźnię, Meamir po lewej, Lia po prawej
    #surprised_happy Meamir ON
    "Gdy tylko ją dostrzegł na jego twarzy zagościł uśmiech."
    p5 "Hej Lia! Miło Cię znów widzieć, co u Ciebie?"
    p1 "Hej Meamir! Ah, jestem trochę zmęczona - musiałyśmy z Raven trochę popracować."
    p5 "Oh, rozumiem. Przynajmniej udało się załatwić temat tej paczki..."
    #sad_smile Lia ON
    p1 "Hah, masz rację. Chociaż tyle..."
    #surprised_neutral Lia ON
    #blush Meamir ON
    p5 "Słuchaj... Myślałem sobie czy nie chciałabyś może przejść się na spacer?"





    menu:
        "“Jasne, z chęcią się przejdę.”":
            #happy Lia ON
            #surprised_happy Meamir ON
            p5 "Super! A gdzie chciałabyś pójść?"
            p1 "Hmm? Myślałam, że coś zaproponujesz!"
            #confused Meamir ON
            p5 "Oj... Nie pamiętasz? Dopiero się wprowadziłem, wciąż nie znam okolicy na tyle dobrze..."
            #smirk Lia ON
            p1 "No niech Ci będzie. Ale coś musisz zasugerować."
            #smile Meamir ON
            p5 "Może pokażesz swoje ulubione miejsce?"
            #smile Lia ON
            p1 "Hmm. Niech będzie. Chodźmy!"
            p5 "Oh, ok. A gdzie?"
            p1 "Zobaczysz, chodź!"
            #przejście do E8-P5D
            jump e8_p5d


        "“Dzięki, ale teraz jestem wykończona. Innym razem.”":
            #surprised_sad Lia ON
            #surprised_sad Meamir ON
            p5 "Oh... Myślałem, że gdzieś się przejdziemy..."
            p1 "Wybacz. Po prostu nie mam teraz siły."
            p1 "Dużo się ostatnio działo. Innym razem możemy się przejść."
            #sad_smile Lia ON
            p5 "No dobrze... Oczywiście nie będę namawiał na siłę."
            p1 "Dzięki za zrozumienie. To będę uciekała."
            #sad_smile Meamir ON
            p5 "Dobrze... Do zobaczenia!"
            p1 "Papa!"
            #powrót do widoku wioski, Meamir chwilowo znika i wraca na swoje miejsce dopiero po upływie 5 pór z dostępnym kolejnym epizodem
            #neutral mina wraca Lii
            #ekran wraca do widoku wioski i do wolnej gry


        "“Nie mam ochoty z Tobą teraz nigdzie chodzić.”":
            #+1pkt HatePath
            #+1pkt MeamirHate
            $ HatePath += 1
            $ MeamirHate += 1
            #annoyed Lia ON
            #more_sad Meamir ON
            p5 "Oh... Myślałem..."
            p1 "Źle myślałeś. Nie mam ochoty nigdzie teraz iść po prostu."
            p5 "No dobrze..."
            p1 "Muszę iść. Na razie."
            p5 "Ok... Pa..."
            #powrót do widoku wioski, Meamir chwilowo znika i wraca na swoje miejsce dopiero po upływie 5 pór z dostępnym kolejnym epizodem
            #neutral mina wraca Lii
            #ekran wraca do widoku wioski i do wolnej gry


#################################
    ############### E8-P5C - wspólnie po paczkę
label e8_p5c:
    #tutaj możemy przejść tylko z E8-P5A jeśli nie mieliśmy ze sobą paczki
    # TODO upływ czasu +1
    #background Tawerna z zewnątrz
    "Droga chwilę im zajęła, oboje szli w milczeniu myśląc nad tym co zaszło."
    #tutaj pojawiają się po prawej, oboje patrząc w lewo jakby na Tawernę
    #neutral Lia i Meamir ON
    "W końcu dotarli do Tawerny, Lia odezwała się pierwsza."
    p1 "Dobrze... Możesz poczekać moment, skoczę do środka po tę paczkę."
    #surprised_neutral Meamir ON
    p5 "Oh, no dobrze."
    #Lia znika z ekranu
    p5 "..."
    #Lia pojawia się na ekranie z powrotem z paczką
    #frown Lia ON
    #sad_smile Meamir ON
    p1 "Dobra. Tu masz tę paczkę, mam nadzieję, że Twój ojciec będzie zadowolony."
    #neutral Lia ON
    p5 "Dzięki... Też mam taką nadzieję..."
    #confused Lia ON
    p5 "Wiesz... Myślałem czy nie chciałabyś mimo wszystko przejść się ze mną na spacer..."
    #confused Meamir ON
    p1 "Teraz?"
    p5 "Uh... Tak, myślałem, że można iść teraz..."
    #sad Meamir ON
    p1 "Słuchaj... Może innym razem. Teraz powinieneś ogarnąć tę paczkę."
    p1 "Zanieś ją swojemu ojcu i niech będzie to z głowy. Tak będzie lepiej."
    p5 "Pewnie masz rację..."
    #sad_smile Lia ON
    p1 "Ogólnie nie jestem zbyt pewna decyzji... Ale tym razem mam przeczucie, że lepiej będzie zrobić to w ten sposób."
    p5 "No dobrze... To pójdę to zanieść od razu."
    #paczka znika
    p1 "Cieszę się... Proszę, tutaj jest paczka. Do zobaczenia później."
    p5 "Do zobaczenia, pa!"
    #Meamir wychodzi, ekran wraca do widoki wolnej gry i tuptania po świecie
    jump ee_tavern_mainroom




    ################# E8-P5D - spacer

    #tutaj spacer do którego można dotrzeć z E8-P5A i E8-P5B
    #tło drzewa przy starym lesie, obie postacie powoli idą od prawej do lewej na tle lasku
    #happy Lia ON
    "Prawie całą drogę szli w ciszy rozmyślając nad tym co się stało."
    #confused Meamir ON
    "Gdy szli chwilę wzdłuż gęstego lasu ciszę postanowił przerwać Meamir."
    #smirk Lia ON
    p5 "To gdzie właściwie idziemy?"
    p1 "Haha, a coś taki ciekaw?"
    p5 "Oj no... Tak tylko pytam."
    p1 "No wiem wiem, tylko się droczę."
    #smile Lia ON
    p1 "Idziemy do mojego ulubionego miejsca. Dokładnie tak jak chciałeś."
    #surprised_happy Meamir ON
    p1 "Nazywam je Sekretnym Ogrodem. Może być?"
    p5 "Haha, tak tak - wybacz, że tak dopytuję. Po prostu jestem ciekaw."
    p1 "Wiem wiem. Chodź. Prawie jesteśmy, tutaj przez tę wyrwę."
    "Meamir ruszył za Lią. Po chwili udało im się przejść przez gęsty fragment lasu."
    #zmiana backgroundu na Sekretny Ogród, lekki przejście od lewej do prawej - prezentacja całości
    "Weszli powoli na polankę. Lia lekko zerkała na Meamira, ten obserwował uważnie cały Ogród."
    #ustawienie kadru mniej więcej na środku, Meamir i Lia po lewej patrząc na środek, Lia bliżej środka
    #surprised_happy Meamir ON
    #smile Lia ON
    p1 "I jak? Co sądzisz?"
    p5 "Huh. Szczerze nie wiem co powiedzieć..."
    #smirk Lia ON
    p1 "Tobie zabrakło słów? No proszę, proszę."
    #Lia obraca się w stronę Meamira
    #blush Lia ON
    #smile Meamir ON
    "Meamir spojrzał uważnie na Lię."
    "Wpatrywał się w nią przez dłuższy moment."
    p5 "Huh, masz rację - trochę mi zabrakło słów. Po prostu nie spodziewałem się jak tu pięknie."
    p1 "Oh, cieszę się, że Ci się podoba."
    p1 "Możemy sobie usiąść chwilę pod drzewem jak masz ochotę..."
    #smile Lia ON
    #surprised_happy Meamir ON
    p5 "Oczywiście! Możemy sobie przysiąść."
    #takie ujęcie z przejściem po całym ogrodzie, bez postaci
    "Siedzieli przez chwilę w ciszy obserwując cały okolicę, delektując się jej pięknym widokiem."
    #pierwsze ujęcie komiksu E8-P5
    "..."
    #drugie ujęcie komiksu E8-P5
    "Lia kątem oka zauważyła, że Meamir próbuje ją prawdopodobnie przytulić!"
    #tutaj pojawia się decyzja

    menu:
        "Przytul go.":
            #ujęcie komiksu nr.
            #+1pkt MeamirLove
            #+1pkt LovePath
            $ MeamirLove += 1
            $ LovePath += 1
            p1 "No chodź tutaj."
            "Lia odwzajemniła uścisk Meamira."
            "..."
            "Minęła chwila nim odsunęli się od Ciebie."
            #powrót do normalnego ujęcia, Lia lewo i Meamir prawo
            #blush Meamir ON
            #blush Lia ON
            p1 "To było słodkie... i miłe."
            p5 "Ojej, podobało Ci się?"
            p1 "Haha, tak - było przyjemnie. A Ty zadowolony?"
            p5 "Oj tak... To było naprawdę miłe."
            p1 "To prawda."
            p1 "Chyba czas jednak wracać, co myślisz?"
            p5 "Oh, jeśli masz ochotę to można wrócić."
            p5 "Mogę Cię odprowadzić?"
            p1 "Oczywiście. Chodźmy."
            "Dwójka ruszyła w drogę i w końcu dotarła do Tawerny."
            # TODO upływ czasu +1
            #zmiana tła na zewnątrz Tawerny
            "Zatrzymali się przed budynkiem."
            #Lia lewo, Meamir prawo
            #smile Lia ON
            #smile Meamir ON
            p1 "Dzięki za odprowadzenie."
            #blush Lia ON
            p5 "Nie ma za co, przyjemność po mojej stronie."
            #surprised_happy Lia ON
            p1 "Cieszę się. Mam nadzieję, że do zobaczenia wkrótce."
            p1 "Tymczasem muszę już uciekać, do zobaczenia!"
            #surprised_happy Meamir ON
            p5 "Też mam taką nadzieję! Do zobaczenia!"
            # Meamir znika, Lia wchodzi do Tawerny i wolna gierka wraca
            # TODO Meamir pojawi się ponownie przy kuźni z E9 po 5 porach

        "“Halo, nie przysypiaj mi tu.”":
            #ujęcie komiksu nr.
            p5 "Uh... Znaczy... Nie przysypiam..."
            p5 "Tak tylko się przeciągałem..."
            p1 "Dobrze dobrze, to co - wstajemy?"
            p5 "T-tak... Możemy..."
            #powrót do normalnego ujęcia, Lia lewo i Meamir prawo
            #confused Meamir ON
            #smirk Lia ON
            p1 "To co, wracamy powoli?"
            #sad Meamir ON
            p5 "Chyba tak..."
            p1 "To chodźmy, później będą jeszcze okazje żeby tu wpaść."
            p5 "No dobrze dobrze."
            #surprised_happy Meamir ON
            p1 "Rozchmurz się trochę i jak chcesz to możesz mnie odprowadzić."
            #smile Lia ON
            p5 "Oczywiście, że chcę! Znaczy... Chętnie Cię odprowadzę."
            p1 "To chodźmy!"
            "Dwójka ruszyła w drogę i po krótkim marszu końcu dotarła do Tawerny."
            # TODO upływ czasu +1
            #zmiana tła na zewnątrz Tawerny
            "Zatrzymali się przed budynkiem."
            #Lia lewo, Meamir prawo
            #smile Lia ON
            #smile Meamir ON
            p1 "Dzięki za odprowadzenie."
            #blush Lia ON
            p5 "Nie ma za co, przyjemność po mojej stronie."
            #surprised_happy Lia ON
            p1 "Cieszę się. Mam nadzieję, że do zobaczenia wkrótce."
            p1 "Tymczasem muszę już uciekać, do zobaczenia!"
            #surprised_happy Meamir ON
            p5 "Też mam taką nadzieję! Do zobaczenia!"
            #Meamir znika, Lia wchodzi do Tawerny i wolna gierka wraca
            #Meamir pojawi się ponownie przy kuźni z E9 po 5 porach

        "“A co Ty przepraszam robisz?”":
            #ujęcie komiksu nr.
            #+1pkt HatePath
            #+1pkt MeamirHate
            $ HatePath += 1
            $ MeamirHate += 1
            p5 "Oh... Ja? Ja nic nie robię..."
            p1 "Tak? A co to za wyciąganie rąk co?"
            p5 "Oh, tylko tak się przeciągałem..."
            p1 "Mhm. Chodź, wstajemy."
            #powrót do normalnego ujęcia, Lia lewo i Meamir prawo"
            #blush Meamir ON
            #annoyed Lia ON
            p5 "No dobrze..."
            p1 "I tak długo zabawiliśmy tutaj. Czas wracać."
            #confused Meamir ON
            p5 "To chodźmy."
            "Ruszyli powoli do poza las. Szli w ciszy."
            #tło przed lasem, tak jakby po środku
            #sad Meamir ON
            #frown Lia ON
            p1 "No dobrze. Dzięki za spacer, było znośnie."
            p5 "Oh, chociaż coś..."
            p1 "Do zobaczenia, muszę już uciekać."
            p5 "Do zobaczenia..."
            # TODO upływ czasu +1
            #przejście do głównej sali Tawerny
            "Lia po krótkim spacerze dotarła do Tawerny. Mogła wrócić w końcu do swoich zajęć."
            #wraca wolna gra
            # TODO Meamir pojawi się ponownie przy kuźni z E9 po 5 porach
    jump ee_tavern_mainroom


################################################################################
label e8_p16: # TODO dodać wywołanie po skończeniu wątków E8-P4 i E8-P5
    #Zorn stojący za barem, kliknięcie go aktywuje ten motyw
    #Lia pojawia się z lewej (też za barem), a Zorn z prawej i rozmowa jest jakby za barem
    $ ee001_UkonczenieEpizodow['e8_p16'] = True
    scene tavern_main_bar_bg0_dn
    show tavern_main_bar_bar1_dn
    show p3 at zabarem behind tavern_main_bar_bar1_dn:
        xalign 0.5 xzoom -1.0
    show p1 at zabarem behind tavern_main_bar_bar1_dn:
        xalign -0.3 xzoom -1.0
    show p1 at zabarem behind tavern_main_bar_bar1_dn:
        linear 1.5 xalign 0.1
    with dissolve
    p3 "Lia. Poczekaj. Przez to całe zamieszanie zapomniałem wspomnieć Ci o pewnej rzeczy..."
    p1 "Tak? Jakiej?"
    p3 "Wkrótce powinien wrócić..."
    "Wypowiedź nagle przerwało głośne pukanie do drzwi."
    p3 "Tak? Kto tam? Zamknięte jeszcze!"
    "Po krótkiej chwili, z zewnątrz odezwał się spokojny, wręcz kojący głos, należący z pewnością do mężczyzny."
    #postać na razie podpisana: “???”
    p16q "To ja!"
    p3 "Jaki znów JA? Imię podaj."
    p16q "A niech mnie. To ja, Cirdan."
    #tutaj P16 dostaje już podpis imienny “Cirdan”
    p3 "Ha! Cirdan! Drogi chłopcze, śmiało wchodź do środka."

    #pause
    #hide e8p16c1
    #hide black with dissolve

    #pojawia się pierwsze ujęcie komiksu z Cirdanem w drzwiach
    window hide
    show black with Dissolve(.3)
    show e8p16c1 with Dissolve(.3)
    pause
    p3 "Haha, ależ wyrosłeś!"
    p3 "Lia! Spójrz, Cirdan wrócił! Właśnie o tym chciałem Ci teraz powiedzieć."
    p3 "Chodź tu, przywitaj się."
    #drugie ujęcie komiksu jak na siebie patrzą Lia i Cirdan
    window hide
    show e8p16c2 with dissolve
    p16 "Haha, witajcie! Hej Lia, wspaniale Cię w końcu zobaczyć!"
    "Lia wpatrywała się w młodego mężczyznę. Pamiętała tę twarz."
    #ujęcie komiksowe z flashbackiem na Cirdana, zastanawiam się tu nad jakimś efektem lekko ruszającej się mgiełki, żeby jasno zakomunikować, że to jest flashback
    hide e8p16c1
    hide e8p16c2
    #with dissolve
    show e8p16c3
    with dissolve
    "Wspomnienia sprzed wielu lat nagle wróciły."
    "”Cirdan.” - pomyślała Lia. Towarzysz z jej młodości."
    "Był dla niej jak starszy brat, zawsze uśmiechnięty - zawsze pomocny."
    "Pomagał w Tawernie. W zasadzie żył tutaj i praktycznie mieszkał z nimi."
    #tutaj tak lekko jakby zaczęło zanikać to ujęcie, jakby wracała do teraźniejszości
    show e8p16c2 behind e8p16c3 #with dissolve
    hide e8p16c3 with dissolve

    "Jednak wiele lat temu wyjechał. Nie pamiętała już nawet czemu. Pamiętała, że została sama."
    #tutaj powrót już do tego ujęcia jak na siebie się wpatrują i od razu boom licznik i decyzja:
    $ timeout = 6.0
    $ timeout_label = "e8_p16_timeout"
    menu:
        "Przytul go na powitanie.":
            show e8p16c4a with dissolve
            p1 "Heeej Cirdan! Cieszę się, że wróciłeś!"
            p16 "Hah, ja też się cieszę kluseczko."
            #pojawia się ujęcie, Lia i Zorn (Zorn lekko za nią) po lewej i Cirdan po prawej. Lia blush ON, Zorn neutral i Cirdan smile ON
            show tavern_main_bar_bar1_dn behind p3, p1
            show p3:
                align (0.1,1.0) xzoom 1.0
            show p1 blush:
                align (0.37,1.0) xzoom -1.0
            show p16 lsmile:
                xalign 0.8 #xzoom -1.0
            hide black
            hide e8p16c2
            hide e8p16c4a
            with dissolve
            p1 "Kluseczko?"
            p16 "Haha, dalej drażni Cię ten pseudonim?"
            p1 "Powiedzmy..."
            p3 "No dobrze dobrze, później będziecie się droczyć."
            #Zorn lekko podchodzi w kierunku Cirdana + może warstwę wyżej wskoczyć, jak stał przed Lią
            show p1 behind p3 with fc
            show p3:
                linear 2 xalign 0.4
            show p1:
                linear 3 xalign 0.2
            "Przerwał niespodziewanie Zorn i podszedł w kierunku Cirdana."
            #Lia smile ON
            show p1 lsmile with fc
            p3 "Na pewno przywiozłeś ze sobą sporo opowieści."
            p16 "Oczywiście! Z chęcią Was nimi uraczę - trochę ich się uzbierało."
            p16 "Ale teraz muszę przeprosić, czeka mnie jeszcze organizacja po podróży - gdy tylko wszystkim się zajmę to z pewnością wrócę."
            p3 "Drzwi będą stały dla Ciebie otworem!"
            p16 "Cieszy mnie to. W takim razie na ten moment się żegnam i do zobaczenia wkrótce!"
            p16 "Miło było Cię zobaczyć Lia! Do zobaczenia!"
            p1 "Do zobaczenia Cirdan!"
            p3 "Do zobaczenia drogi chłopcze."
            #Cirdan wychodzi w prawo
            show p16 with fc:
                xzoom -1.0
            show p16:
                linear 1.5 xalign 1.4
            p3 "No. To było ciekawe. Tymczasem wracajmy do naszych zajęć."
            #pyk, koniec - Lia jest w sali głównej, a Zorn zniknął ze swojego miejsca

        "“Cześć Cirdan. Fajnie, że wróciłeś.”":
            #ujęcie z nie przytuleniem wskakuje
            show e8p16c4b with dissolve
            p16 "Masz rację! Wróciłem. Mam nadzieję, że na dobre."
            "Nastąpiła krótka, niezręczna cisza, którą szybko przerwał Zorn."
            #pojawiają się postacie, Lia i Zorn (on lekko za Lią jakby) po lewej i Cirdan po prawej. Lia blush ON, Zorn neutral ON i Cirdan smile ON
            show tavern_main_bar_bar1_dn behind p3, p1
            show p3:
                align (0.1,1.0) xzoom 1.0
            show p1 blush:
                align (0.37,1.0) xzoom -1.0
            show p16 lsmile:
                xalign 0.8 #xzoom -1.0
            hide black
            hide e8p16c4b
            hide e8p16c2
            with dissolve

            p3 "No no, w końcu jesteś! Będziemy musieli porozmawiać - na pewno masz sporo do opowiedzenia!"
            #Cirdan neutral ON
            show p16 -lsmile with Dissolve(0.2)
            p16 "Naturalnie. Chętnie Wam opowiem o stolicy i moich przygodach."
            p3 "Fantastycznie! Hmm..."
            "Zorn zerknął na Lię, widział, że ta wciąż jest lekko zmieszana całą sytuacją."
            p3 "Miło, że wpadłeś nam powiedzieć. Teraz mamy trochę pracy, więc..."
            p16 "Oh, oczywiście. Chciałem po prostu się przywitać. Porozmawiamy kiedy indziej."
            p16 "I tak muszę jeszcze zorganizować się po podróży. Odwiedzę Was wkrótce, jeśli to nie problem."
            p3 "Oczywiście, że to nie problem! Dla Ciebie drzwi stoją zawsze otwarte."
            p16 "Cieszę się, to w takim razie chwilowo Was zostawiam i do zobaczenia wkrótce."
            p16 "Miło było Cię zobaczyć Lia."
            #tutaj Cirdan wychodzi w prawo
            show p16 with fc:
                xzoom -1.0
            show p16:
                linear 1.5 xalign 1.4
            "Powiedział Cirdan na pożegnanie, po czym opuścił Tawernę."
            #Zorn trochę bliżej środka, niech odwróci się w stronę Lii, jakby stali na przeciwko siebie
            show p3:
                linear 1 xalign 0.5
                linear 0.1 xzoom -1.0
            show p1:
                linear 2 xalign 0.2
            pause 2.5
            p3 "Mogłaś powiedzieć coś więcej..."
            p1 "Nie wiedziałam co..."
            p3 "Ah, no dobrze dobrze. Będzie jeszcze okazja. Na pewno. Teraz wracaj do swoich zajęć."
            #pyk, koniec - Lia jest w sali głównej, a Zorn zniknął ze swojego miejsca
    jump ee_tavern_mainroom
    #return
label e8_p16_timeout:
    #jeśli nie wybierzemy nic w trakcie odliczania to pojawia się ta wersja:
    "Wszyscy wpatrywali się przez dłuższą chwilę w siebie."
    p1 "..."
    p3 "..."
    p16 "..."
    #tutaj pojawia się ujęcie standardowe, tło główna sala tawerny, po lewej Lia i Zorn, po prawej Cirdan
    #Lia confused ON / Zorn neutral ON / Cirdan confused ON
    show tavern_main_bar_bar1_dn behind p3, p1
    show p3:
        align (0.1,1.0) xzoom 1.0
    show p1 bsurprised:
        align (0.37,1.0) xzoom -1.0
    show p16 bsurprised:
        xalign 0.8 #xzoom -1.0
    hide black
    hide e8p16c2
    with dissolve
    p3 "Ekhem... Cirdan! Na pewno masz sporo do zrobienia po przyjeździe..."
    p16 "Hmm? Ah, tak - to prawda..."
    p3 "Proponuję w takim razie spotkanie jak tylko ogarniesz wszystko, może być?"
    p16 "Ahh, naturalnie. W takim razie do zobaczenia."
    #Cirdan wychodzi
    show p16 with fc:
        xzoom -1.0
    show p16:
        linear 1 xalign 1.4
    "Cirdan opuścił budynek w dość szybkim tempie."
    #Zorn powoli przesuwa się w prawo (2-3sec) i obraca się w kierunku Lii stojąc w okolicach środka
    #Zorn angry ON
    show p3 angry angrywink:
        linear 1 xalign 0.5
        linear 0.1 xzoom -1.0
    show p1:
        linear 2 xalign 0.2
    pause 2.5
    "W pomieszczeniu unosiła się jeszcze niezręczna atmosfera, którą spróbował rozwiać Zorn."
    p3 "Mogłaś chociaż coś powiedzieć, to było niemiłe."
    show p3:
        linear 1 xalign -0.4
    "Po czym natychmiast opuścił Lię i wrócił do swoich obowiązków."
    "Przez moment Lia dalej stała szukając wzrokiem wsparcia, którego przed chwilą jej zabrakło."
    "Po chwili wróciła do swoich zajęć."

    #Zorn znika ze swojego miejsca po tym epizodzie, następne informacje o jego stałym pobycie w EE002
    jump ee_tavern_mainroom
    #return




label e8_work1:
    # TODO Możliwość kliknięcia na bar z mainroom tylko: rano, przed południem i w południe
    # TODO ta wersja działa tylko i wyłącznie przed rozpoczęciem wątków E8-P4 i E8-P5
    # w momencie kliknięcia pojawia się pytanie dialogowe:
    "Czy chcesz rozpocząć pracę?"
    menu:
        "Zacznij pracę.":
            "Lia stanęła spokojnie za barem."
            "Stwierdziła, że lepiej teraz chwilę popracować."
            "”Może chociaż tata nie będzie się czepiał, że za mało pracuje.” - pomyślała, po czym skupiła się na pracy."
            "O tej porze goście kręcili się w różnych ilościach, czasem wpadała jakaś znajoma twarz."
            "Czasem Lia po prostu nie zwracała na to uwagi. Wolała uciekać w swoje myśli."
            # TODO komiks przejściowy o tym jak sobie Lia ładnie pracuje
            # TODO upływ czasu o 1 porę do przodu
            "Tak też zrobiła i tym razem. Nawet nie zauważyła kiedy minęło tyle czasu, pracowała już kilka dobrych godzin."
            "Akurat pojawił się ojciec i poinformował, że może teraz stanąć za barem."
            "Lia zbytnio się nie zastanawiała i wróciła po prostu do swoich zajęć."
            # TODO powrót do wolnej gry i możliwość rozpoczęcia pracy/kliknięcia na bar znika
            $ ee001_UkonczenieEpizodow['e8_work1'] = True
            return
        "Później popracujesz.":
            return


label e8_work2:
    #WORK2 aktywuje się tylko i wyłącznie poprzez E8-P4 jako wymuszona kontynuacja
    #background kuchnia, dziewczyny stoją naprzeciwko siebie
    scene room_kitchenday
    #neutral Lia ON
    #confused Raven ON
    show p1:
        align (.6,1.0)
    show p4 bsurprised wink lneutral:
        align (.2,1.0)
    with fade
    p1 "No dobrze... To po kolei."
    p1 "Większość rzeczy przygotowujemy tutaj na zapleczu"
    p1 "Na ogół moja rola jest taka, że pomagam za barem."
    p1 "Nalewanie trunków, podawanie jedzenie, wiesz o co chodzi - standardowe sprawy tawerniane."
    p4 "W sumie to nie wiem..."
    p1 "Eee? Na pewno sobie jakoś dasz radę. Wracając..."
    p1 "Na początku myślę, że możesz mi pomóc po prostu."
    p1 "W ten sposób poznasz podstawy. Może nawet wpadną jakieś znajome twarze."
    p1 "To co, gotowa? "
    p4 "No... Chyba tak."
    p1 "Super, chodźmy na bar."
    #przejście do sali głównej za bar, obie dziewczyny po prawej stronie stoją, Raven bardziej po prawej - jakby stała za Lią i zerkała na to co robi, niczym uczeń
    #tutaj komiks ujęcie nr. E8P4WC1
    scene tavern_main_bar_bg0_dn
    show p1 at zabarem:
        align (.6,1.0)
    show p4 behind p1 at zabarem:
        align (.8,1.0) xzoom -1
    show tavern_main_bar_bar1_dn
    with fade
    "Lia stanęła za barem i rozpoczęła pracę."
    show black with dissolve
    show e8p4wc1 with dissolve

    "Starała się wykonywać wszystkie czynności w taki sposób, żeby Raven wszystko widziała."
    "Po chwili uważnej obserwacji postanowiła wyjść z inicjatywą i dołączyć do pracy."
    "Skupiała się na tych czynnościach, które według niej wymagały dodatkowej pomocy."
    "Lia zauważyła, że Raven szybko się odnajduje ze wszystkim."
    #tutaj komiks ujęcie nr. E8P4WC2
    show e8p4wc2 with dissolve
    "Obie dziewczyny skupiły się na pracy. Czas powoli mijał."
    "Goście wchodzili i wychodzili. Raven już po kilkudziesięciu minutach czuła się dość swobodnie."
    "Wyglądała nawet na zadowoloną. Praca bez stresu przeszłości musiała pozytywnie na nią wpływać."
    if PaczkaRozrabiaka == 1:
        "W pewnym momencie wśród gości pojawiła się znajoma twarz."
        show p5 blush behind black:
            xzoom -1 align(0.0,1.0)
        hide e8p4wc1
        hide e8p4wc2
        with dissolve
        hide black with dissolve
        #powrót do ujęcia zza baru, Lia i Raven za barem po prawej, Meamir stoi po lewej
        #surprised_happy Lia ON
        #blush Meamir ON
        #annoyed Raven ON
        show p1 bsurprised widenedwink lsmile with fc
        show p4 bangry narrowedwink lneutral with fc
        p5 "Hej Lia!"
        p1 "Cześć Meamir, co tu robisz?"
        p5 "Ah, przyszedłem po tę paczkę..."
        #smirk Raven ON
        show p4 bangry narrowedwink lsmile with fc
        #confused Meamir ON
        show p5 bsurprised wink lneutral with fc
        p4 "No hej Meamir."
        p5 "Oh, h-hej Raven. Odnośnie tej paczki..."
        #annoyed Raven ON
        #smile Lia ON
        show p4 bangry narrowedwink lneutral with fc
        show p1 bneutral wink lsmile with fc
        p1 "Tak tak, tu jest. Proszę."
        #smile Meamir ON
        show p5 bneutral wink lsmile with fc
        p5 "Dzięki Lia!"
        p4 "..."
        p5 "Nie chciałabyś może przejść się gdzieś?"
        #sad Meamir ON
        #sad_smile Lia ON
        show p5 bneutral wink lsad with fc
        show p1 bsad wink lsmile with fc
        p1 "Oh, teraz nie mogę... Musimy jeszcze trochę popracować."
        p1 "Może innym razem."
        #smile Raven ON
        show p4 bneutral wink lsmile with fc
        p5 "Mhm, no dobrze. To nie będę przeszkadzał, miłej pracy."
        p5 "Do zobaczenia!"
        p1 "Do zobaczenia Meamir!"
        $ paczka01 = "oddana"
        hide p5 with moveoutleft
        #Meamir wychodzi i lecimy dalej to co niżej

    #upływ czasu +1
    call timechange from _call_timechange_10

    scene tavern_main_bar_bg0_dn
    show p1 at zabarem:
        align (.5,1.0)
    show p4 behind p1 at zabarem:
        align (.8,1.0) xzoom -1
    show tavern_main_bar_bar1_dn
    with fade
    show p3 with moveinleft:
        align (0.1,1.0)
    #powrót do ujęcia zza baru, Lia i Raven tam są. Od lewej podchodzi Zorn
    #neutral emocje ON
    "Dziewczyny cały czas pracowały. W pewnym momencie pojawił się Zorn."
    p3 "Jak tam, wszystko dobrze? "
    #frown Lia ON
    show p1 bangry wink lneutral with fc
    p1 "Mhm."
    #blush Raven ON
    show p4 blush with fc
    p3 "A Ty Raven, co sądzisz o takiej pracy? "
    p4 "Bardzo przyjemna! Dziękuję za taką możliwość."
    p3 "Przyjemność po naszej stronie! "
    #smile Lia ON
    show p1 bneutral wink lsmile with fc
    #smile Raven ON
    show p4 bneutral wink lsmile with fc

    if dt<5:
        p3 "Ogarnijcie jeszcze tylko te naczynia. Zanieście je do kuchni, a ja przejmę teraz bar."
        p3 "Jak skończycie to możecie iść odpocząć."

    else:
        p3 "Ogarnijcie jeszcze tylko te naczynia. Zanieście je do kuchni, a ja posprzątam tutaj i zamknę Tawernę."
        p3 "Jak skończycie to do spania!"

    p1 "Dobrze! Dzięki."
    p4 "Dziękuję Panu!"
    p3 "Oj no, żadne Panu - Zorn jestem."
    p3 "Przyzwyczaisz się! No zmykajcie już."

    #przejście do kuchni, Lia po lewej i Raven po prawej. Patrzą na siebie
    scene room_kitchenday
    show p1:
        align (.3,1.0) xzoom -1
    show p4 bsurprised wink lneutral:
        align (.7,1.0) xzoom -1
    with fade
    "Dziewczyny szybko posprzątały i stanęły na moment, żeby chwilkę odsapnąć."

    if RavenHate >=1:
        #jeśli mamy przynajmniej 1pkt RavenHate
        #sad Raven ON
        #annoyed Lia ON
        show p4 lsad bsad with fc
        show p1 bangry narrowedwink with fc
        "Raven odezwała się pierwsza."
        p4 "Lia?"
        p1 "Mhm?"
        p4 "Nie zrozum mnie teraz źle..."
        #disappointed Raven ON
        #sad Lia ON
        show p4 bsad closed lsad with fc
        show p1 bneutral wink lsad with fc
        p4 "Chciałam Ci tylko powiedzieć, że nie musiałaś być wcześniej dla mnie niemiła."
        p4 "Rozumiem, że jestem tutaj nowa i w ogóle..."
        #sad Raven ON
        show p4 bneutral wink lsad with fc
        p4 "Ale Twoi rodzice zaoferowali mi tu miejsce i chciałabym skorzystać z tej szansy."
        p4 "Mam nadzieję, że miałaś po prostu gorszą chwilę i z czasem będzie między nami lepiej."
        #sad_smile Raven ON
        #neutral Lia ON
        show p4 bsad wink lsmile with fc
        show p1 bneutral wink lneutral with fc
        p4 "Uh... Tylko tyle chciałam powiedzieć na tę chwilę."
        "Lia przetrawiła w ciszy wszystkie słowa."
        "Dziewczyny przez krótki moment wpatrywały się w siebie bez słowa."

    else:
        #jeśli mamy poniżej 1pkt RavenHate
        #smile Raven ON
        #surprised_happy Lia ON
        show p4 bneutral wink lsmile with fc
        show p1 bsurprised widenedwink lsmile with fc
        "Raven odezwała się jako pierwsza: "
        p4 "Huh, nie było tak źle. Bałam się, że nie dam rady."
        #blush Raven ON
        show p4 blush with fc
        p1 "Poszło Ci bardzo dobrze!"
        #blush Lia ON
        show p1 blush with fc
        p4 "Dziękuję... To dla mnie wiele znaczy."
        #smile Raven ON
        #smile Lia ON
        show p1 bneutral wink lsmile with fc
        show p4 bneutral wink lsmile with fc
        p1 "Nie ma za co, na pewno będzie tylko lepiej!"
        show p1 -blush with fc
        show p4 -blush with fc
        "Dziewczyny przez krótki moment wpatrywały się w siebie bez słowa."

    if RavenLove >=2:
        #jeśli mamy przynajmniej 2pkt RavenLove
        #Raven blush ON
        #surprised_neutral Lia ON
        show p4 blush with fc
        show p1 bsurprised widenedwink lneutral with fc
        p4 "Lia..."
        p1 "Hmm? "
        #surprised_happy Lia ON
        show p1 bsurprised widenedwink lsmile with fc
        p4 "Chciałam tylko powiedzieć, że naprawdę doceniam to co dla mnie robisz..."
        #ujęcie komiksu EE001C1
        show black with dissolve
        show ee001c1 with dissolve
        "Lia zawstydziła się lekko."
        p4 "Myślałam sobie... Hmm..."
        p4 "Chciałam po prostu w jakiś sposób podziękować."
        #ujęcie komiksu EE001C2
        show ee001c2 with dissolve
        "Niespodziewanie Raven zbliżyła się do Lii i pocałowała ją w policzek."
        "Lia była lekko zaskoczona, przez co Raven lekko się cofnęła."
        #powrót do normalnego ujęcia, Lia confused, Raven blush
        show p1 bsurprised wink lneutral with fc
        show p4 bneutral wink lneutral blush with fc
        hide ee001c1
        hide ee001c2
        with dissolve
        hide black with dissolve
        p4 "Oj... Przepraszam, myślałam..."
        #blush Lia ON
        show p1 blush with fc
        p1 "Nie! Nie przepraszaj... To było bardzo miłe."
        p1 "Po prostu lekko mnie to zaskoczyło. Ale naprawdę to miłe."
        #surprised_happy Raven ON
        #smile Lia ON
        show p4 bsurprised widenedwink lsmile -blush with fc
        show p1 bneutral wink lsmile -blush with fc
        p4 "Naprawdę?"
        p1 "Naprawdę."
        #blush Raven ON
        show p4 blush with fc
        p4 "Cieszy mnie to... Mam nadzieję, że jeszcze uda nam się gdzieś razem przejść..."
        #smile Raven ON
        show p4 bneutral wink lsmile with fc
        p1 "Też mam taką nadzieję."
        p4 "To co... Idziemy odpocząć? Nie chciałabym podpaść nikomu teraz..."
        p1 "Aww, miło z Twojej strony. Wszystko będzie dobrze, ale chodźmy odpocząć - na pewno nie zaszkodzi."
        "Dziewczyny wspólnie opuściły kuchnię i ruszyły do swoich pokoi."

    if RavenLove <2:
        #jeśli mamy poniżej 2 pkt RavenLove
        #sad_smile Raven ON
        #frown Lia ON
        show p4 bsad wink lsmile with fc
        show p1 bangry wink lneutral with fc
        p4 "Coś jeszcze mamy zrobić?"
        #surprised_neutral Lia ON
        #confused Raven ON
        show p4 bsurprised wink lneutral with fc
        show p1 bsurprised wink lneutral with fc
        p1 "Hmm, myślę, że to wszystko. Jesteś aż tak chętna do pracy?"
        #sad_smile Lia ON
        #sad_smile Raven ON
        show p4 bsad wink lsmile with fc
        show p1 bsad wink lsmile with fc
        p4 "Znaczy... Nie chciałabym nikogo zawieść po prostu..."
        #confused Lia ON
        show p1 bsurprised wink lneutral with fc
        p1 "Huh, no rozumiem. Bez obaw, było dobrze - możemy iść odpocząć."
        #smile Raven ON
        #smile Lia ON
        show p4 bneutral wink lsmile with fc
        show p1 bneutral wink lsmile with fc
        p4 "Dobrze! To chodźmy."
        "Dziewczyny wspólnie opuściły kuchnię i ruszyły do swoich pokoi."
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
    "Lia zaraz po wejściu przebrała się do spania i wskoczyła pod kołdrę oczekując na szybki sen."
    #jeśli jest wieczór to upływ czasu +2 (tak żeby Lia obudziła się rano, a nie w nocy)
    #upływ czasu +1
    #wolne granie, background pokój Lii
    $ ee001_UkonczenieEpizodow['e8_work2'] = True
    $ ee001_UkonczenieEpizodow['e8_work1'] = True
    if dt == 4:
        call timechange from _call_timechange_11
        scene anim_room_lia_nightdragonlight with Dissolve(1.0)
        pause 1
    call timechange from _call_timechange_12
    scene img_pokojlii_dragon with Dissolve(1.0)
    jump ee_tavern_liaroom
