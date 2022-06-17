
default LasPodejscie = False
default runFromThisLife = False
default theTruthHasBeenSpoken = False
default be01 = False
default e3a1 = False
default e3a2 = False
default e1_intro = 1


label e1:

    "Naprawdę mi jej szkoda. Dziewczyna prowadzi szare, monotonne i, w gruncie rzeczy, smutne życie."

    menu:
        "Chyba czuje się samotna.":
            "Zdaje się, że nie ma wielu przyjaciół. Po prawdzie - nie ma ich chyba wcale."
            "Oczywiście pracuje w Tawernie i z tego powodu zna sporo ludzi, często się z nimi styka."
            "Jednak takie przelotne relacje to nie to samo. Powinna znaleźć kogoś z kim mogłaby być bliżej."
            "Kogoś, kogo mogłaby nazwać przyjacielem."
            $ e1_intro = 1
        "Jej życie wydaje się bardzo monotonne.":
            "Wciąż tylko praca, po której nie ma już wiele czasu ani siły na cokolwiek innego niż sen."
            "Przydałaby jej się jakaś odmiana, jakieś nowe doświadczenie. Inaczej zatraci zupełnie jakąkolwiek radość."
            "Nie musi w końcu zupełnie zmieniać swojego życia. Wystarczy nadać mu nieco… koloru."
            $ e1_intro = 2
        "Chyba przytłaczają ją obowiązki.":
            "Być może ma zbyt wiele obowiązków. Spędza w pracy tyle czasu… w zasadzie to nawet tu mieszka!"
            "Brakuje jej choćby chwili na oddech, na wsłuchanie się w samą siebie."
            "Nic dziwnego, że czuje się tym wszystkim coraz bardziej przytłoczona."
            $ e1_intro = 3
    "Spróbuję jej pomóc. Może wcale wiele nie trzeba."

    #Na ekranie: Ciemny ekran.
    #Harmider w tle (oddalające się głosy rozmów)
    #Dźwięk zamykanych drzwi
    scene black with fade
    play sound sfx_ambient_people_doors fadein 1.0 fadeout 3.0 # TODO do poprawki mimo wszystko
    play ambient sfx_ambient_fire fadein 1.0 fadeout 3.0
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music nowhere_land fadein 5.0
    pause 1.0
    "Harmider i hałas przekrzykujących się głosów, trzask naczyń, śmiechy i śpiewy, słowem - wszystkie typowe, karczemne dźwięki, powoli milkną."
    "Coraz więcej gości opuszcza Tawernę. Miejsce każdego zajmuje cisza, utęskniony spokój. W końcu wypełnia już całą Tawernę."
    #Na ekranie: CG z Tawerny (Lia oparta o drzwi z zamkniętymi oczami)"
    transform alphawdol:
        linear 8 alpha 1.0
        linear 10 alpha 0.4
        repeat
    scene tavern_door_lia_eyesclosed:
        linear 12 zoom 1.05
    show tavern_door_lights1 at alphawdol:
        linear 50 zoom 1.2
        pause 0.3
        linear 50 zoom 1.0
        repeat
    show tavern_door_lights2:
        zoom 1.2 alpha 0.8
        block:
            linear 77 zoom 1.0 alpha 0.9
            pause 0.3
            linear 100 zoom 1.2 alpha 0.8
            repeat
    with fade
    "Gdy ostatni z gości opuszcza Tawernę, Lia zamyka za nim drzwi. Odetchnąwszy opiera się o ścianę i z prawdziwą ulgą przymyka oczy." 
    "Wsłuchuje się w utęsknioną ciszę, którą przyjemnie zakłóca jedynie delikatny trzask ognia w kominku."
    "..."
    window hide
    with fc
    pause 2.0
    window auto
    with fc
    stop ambient fadeout 3.0
    #W tle cały czas delikatny dźwięk ognia, który teraz zanika (najlepiej do 5-6sec wyciszenie)""
    "Jest zmęczona. Bardzo. Jednak zamiast iść prosto do łóżka znów na chwilę tonie we własnych myślach."
    "Z dnia na dzień czuje coraz mocniej, że coś traci. Coś bardzo ważnego."
    "{i}Nuda i monotonia. Nic więcej.{/i}"
    "{i}Wstań, pracuj, śpij, wstań, pracuj, śpij, wstań, pracuj… Polecenia. Każdy dzień, każda chwila łatwa do przewidzenia. Ciągle to samo.{/i}"
    "..."
    p1 "Powoli zaczynam mieć tego dość…"
    show tavern_door_lia_eyesopened behind tavern_door_lights1, tavern_door_lights2 with Dissolve(1.0):
        zoom 1.05
        linear 14 zoom 1.00


    stop music fadeout 3.0
    menu:
        "Przesadzasz. Wciąż jest w tobie sporo życia!":
            p1 "Może przesadzam..."
            p1 "Ale skąd mogę wiedzieć? Nic innego nie znam."
            menu:
                "Może to jest rozwiązanie?":
                    pass
            p1 "Niby co?"
            menu:
                "Cokolwiek. Po prostu coś zróbmy. Coś innego.":
                    pass
            p1 "Nie wiem. Nie jestem przekonana..."
            #przejście do tabeli niżej

        "Nic dziwnego, poza tym, że wciąż to wytrzymujesz.":
            p1 "A co mogę zrobić?"
            menu:
                "Cokolwiek. W tej sytuacji wystarczy, że będzie to coś innego niż zazwyczaj.":
                    pass
            p1 "Może."
            p1 "A może nie."
            p1 "Zresztą nawet nie wiem co można zrobić."
            menu:
                "Za dużo myślisz. Trzeba spróbować.":
                    pass
            p1 "Nie wiem. Nie jestem przekonana..."
            #przejście do tabeli niżej

        "W takim razie otwórz drzwi i uciekaj od tego życia." if not runFromThisLife:
            p1 "Co masz na myśli?"
            menu:
                "Dokładnie to. Otwórz drzwi i uciekaj!":
                    pass
            p1 "..."
            menu:
                "Szybko. Teraz.":
                    pass
            p1 "Może... W sumie czemu nie..."
            menu:
                "Biegnij!":
                    pass
            scene black with fade
            show e1c with dissolve
            #ujęcie komiks E1AC
            "I pobiegła. Może wbrew sobie, ale pobiegła."
            $ runFromThisLife = True
            #czarny ekran, napis biały na środku
            window hide
            with fc
            hide e1c with dissolve
            pause 0.2
            show text _("{color=#eee}Lia ruszyła przed siebie zostawiając obecne życie za plecami. Zniknęła dla świata, ale odrodziła się dla siebie. Pewnie nikt już ponownie jej nie zobaczył. Znalazła nową drogę, nowe życie.{/color}") with dissolve
            show text _("{color=#eee}Czy było szczęśliwsze? To pozostanie tajemnicą.{/color}") with dissolve
            pause
            window auto
            with fc
            # TODO w tle głos DUB01
            # TODO \Co to było? Cofnij. Teraz.\
            # TODO cofa grę do samego początku i usuwa tę opcję
            # TODO dostajemy achievement ACHIEV01
            $ renpy.block_rollback()
            jump e1


    # TODO w momencie pojawienia się tych opcji w tle poleci DUB02 (jednorazowo)

    if e1_intro == 1:
        p1 "Wiesz…czuję się bardzo samotna."
        p1 "Tak naprawdę nie mam nikogo. Oczywiście, mam rodziców, ale poza nimi? Kogoś z kim mogłabym oderwać się od codzienności. Kogoś takiego mi brakuje."
        p1 "Tutaj… tutaj wszyscy mnie znają, jako dziewczynę z Tawerny. Tym jestem i tym zostanę. Nic się nie zmienia…"
        p1 "Ale może Ty masz jakiś pomysł? Co mogłabym zrobić już, teraz, w tej chwili?"
    if e1_intro == 2:
        p1 "Wiesz… Mam wrażenie, że moje życie jest bardzo monotonne."
        p1 "Praktycznie nic się w nim nie dzieje. Naprawdę! Mam wrażenie, że w tej chwili mogę opowiedzieć ci ze szczegółami, co będę robić za miesiąc."
        p1 "Żadnych niespodzianek, żadnej przyjemnej niepewności. Nic."
        p1 "Może zresztą to moja wina…"
        p1 "Ale może Ty masz jakiś pomysł? Co mogłabym zrobić już, teraz, w tej chwili?"
    if e1_intro == 3:
        p1 "Wiesz… chyba przytłaczają mnie te wszystkie obowiązki."
        p1 "Mam wrażenie, jakby w moim życiu nie było nic poza pracą. Łapię się czasem na takim myśleniu… o Tawernie, rozumiesz?"
        p1 "O zamówieniach, o zapasach, o liczbie gości, tym czy wszystko jest, czy jedzenie w spiżarni się nie zepsuło, czy piwa starczy. Nie tylko w pracy. Przed snem, zaraz po obudzeniu. Ciągle."
        p1 "Nie wiem czy tak to powinno wyglądać…"
        p1 "Ale może Ty masz jakiś pomysł? Co mogłabym zrobić już, teraz, w tej chwili?"

    #TODO background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
    scene img_tavern_mainroom_night
    show p1pl wink_player shadow
    with fade
    menu:
        "Masz swoje ulubione miejsca, prawda? Może mi je pokażesz?":
            "Lia staje na równe nogi i wbija wzrok w drzwi."
            #Lia confused ON"
            show p1pl bsurprised lneutral with fc
            p1 "Masz na myśli Ogród?"
            menu:
                "Tak.":
                    pass
            p1 "Może..."
            menu:
                "Może? Na co czekamy?":
                    pass
            #Lia surprised ON"
            show p1pl bsurprised widenedwink_player lneutral with fc
            p1 "Ale teraz? Tak od razu?"
            menu:
                "A czemu nie? Chcesz przełamać rutynę?":
                    pass
            #Lia surprised ON"
            show p1pl bsurprised lsmile with fc
            p1 "Nie... tak. Tak, chcę. Zdecydowanie!"
            menu:
                "Super! No to chodźmy!":
                    pass
            #Lia happy ON"
            show p1pl bneutral wink_player lsmile with fc
            p1 "Świetnie! Chodźmy!"
            #przejście do E1A
            jump e1a

        "Po prostu nie narzekaj tyle.":
            "Lia staje na równe nogi i wbija wzrok w drzwi."
            #Lia Pose_CrossedArm
            #Lia annoyed ON
            show p1pl  with fc
            p1 "A co innego mogę zrobić?"
            #Lia angry ON"
            show p1pl bangry narrowedwink_player lsad with fc
            p1 "Zresztą, wydaje ci się, że narzekam bez powodu?"
            menu:
                "Nie.":
                    #neutral Lia ON
                    show p1pl bneutral closed lsmile with fc
                    p1 "No właśnie."
                    #Lia Pose_ToCamera
                    p1 "To powiesz mi co mam zrobić?"
                    menu:
                        "Masz swoje ulubione miejsca, prawda?":
                            pass
                    p1 "Tak. Co z nim?"
                    menu:
                        "Może byś mi je w końcu pokazała?":
                            pass
                    #Lia surprised ON                    
                    p1 "Teraz?"
                    menu:
                        "Czemu nie?":
                            pass
                    p1 "Może..."
                    menu:
                        "Super! No to chodźmy!":
                            pass
                    #Lia smile ON
                    show p1pl bneutral wink_player lsmile with fc
                    p1 "No... no dobra. Tak! Świetnie! Chodźmy!"
                    #przejście do E1A

                "Tak.":
                    #Lia angry ON
                    "Przez całe ciało Lii przebiega nieprzyjemny dreszcz. Odruchowo zaciska szczękę."
                    p1 "Po co ty tu właściwie jesteś?"
                    menu:
                        "Już tłumaczę...":
                            pass
                    #Lia annoyed ON"
                    show p1pl bangry narrowedwink_player lneutral with fc
                    p1 "Wiesz co? Nie obchodzi mnie to. Ani trochę."
                    p1 "W ogóle mnie nie obchodzisz. Po prostu się zamknij."
                    p1 "Idę spać."
                    #przejście do E1B
                    jump e1b




        "Rób co chcesz.":
            "Lia staje na równe nogi i wbija wzrok w drzwi."
            #Lia Pose_CrossedArm
            #Lia annoyed ON
            p1 "Pff. Wielkie dzięki. Naprawdę, wspaniała pomoc. Dziękuję."
            p1 "Na razie."
            #przejście do E1B
            jump e1b

################################################################################
#################################    E1A     ###################################
################################################################################

label e1a:
    # TODO w momencie przejścia w tle jest dźwięk: DUB03
    $ LovePath += 1

    p1 "Zanim pójdziemy pokażę Ci to miejsce na mapie. Spójrz." 
    #pokazuje się mapa, zoom na Tawernę 
    show mapka_fhd with dissolve:
        zoom 1.5 xalign 0.59 yalign .14
        ease 2 zoom 2.5

    p1 "W tym miejscu jest Tawerna, o tutaj. Tu jesteśmy teraz."
    #zoom utrzymany z przejściem na secret garden
    show mapka_fhd:
        ease 2 xalign 0.78 yalign .04
    p1 "A w tym miejscu jest mój Sekretny Ogród. Tam właśnie się wybieramy."
    p1 "To jak? Gotów do drogi?"
    menu: 
        "Tak!":
            #Lia happy ON
            p1 "Świetnie! No to ruszajmy."
        "Nie...":
            #Lia happy ON
            p1 "To był twój pomysł! Teraz się nie wykręcaj. Ruszamy!"


    window hide
    with fc

    #play music sfx_szumdrzew fadein 3.0
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music arthur_vyncke_red_forest
    play ambient sfx_windy_forest
    transform tr_sciezkadolas:
        pos(-1.0, -0.6)
        ease 16 pos (-0.0, -0.5) zoom 0.9

    scene forest_night at tr_sciezkadolas:
        ease 60.0 zoom 0.9
        ease 60.0 zoom 1.0
        repeat

    show p1 shadow:
        align (1.3,1.0)
        ease 1 align (0.9,1.0)
    window auto
    with fc
    "Lia, uśmiechnięta i, zdaje się, naprawdę zadowolona, opuszcza Tawernę i rusza wskazaną na mapie drogą."
    #background stary las w nocy, przejście jak wcześniej było (ruch tła na zoomie, Lia powoli idzie od prawej do lewej)
    "Spacer przebiega spokojnie. Mimo nocy okolica sprawia wrażenie przyjaznego i bezpiecznego miejsca."
    p1 "Może i dobrze, że mnie do tego namówiłeś."
    p1 "Chodźmy. To już niedaleko. Musimy przejść tylko kawałek przy lesie."
    "Kiedy Lia zbliża się do drzew widać wyraźnie ich grube, poskręcane konary. Rozłożyste gałęzie i potężne pnie świadczą o tym, że las rośnie tu od niepamiętnych czasów."
    p1 "Właściwie jesteś tu ze mną po raz pierwszy. Oto Stary Las."

    menu:
        "Powiesz mi o nim coś więcej?":
            #Lia Pose_ToCamera
            #neutral Lia ON
            p1 "Ta stara ścieżka którą mijaliśmy prowadzi do wioski, ale mało kto z niej teraz korzysta."
            p1 "Początkowo miała prowadzić do jakiejś kopalni, ale dawno już nikt się tym nie interesuje."
        "Nie traćmy czasu!":
            #Lia Pose_ToCamera
            #neutral Lia ON
            p1 "Masz rację."

    #zatrzymanie się i lekki zoom na przejście między drzewami
    p1 "O, to tutaj. Już prawie jesteśmy. Teraz tylko przecisnąć się przez las i zaraz będziemy na miejscu."
    "Lia przeciska się między splątanymi pniami. Nie ma z tym jednak najmniejszego problemu. Porusza się między drzewami z taką swobodą, jakby była we własnym domu. Widać, że choć może dawno tu nie była, to zna to miejsce."
    # TODO dźwięk przeciskania się i przejście w Sekretny Ogród, zmiana tła
    transform tr_show_garden:
        xalign 0.0
        linear 7 xalign 1.0

    $ dt = 5
    scene secretgarden_bg with fade:
        xalign 0.0
    show secretgarden_bg at tr_show_garden
    play music2 sfx_jungle_atmosphere_night
    $ renpy.music.set_volume(0.7, delay=0, channel='musictight')
    play musictight sfx_small_stream_flowing
    p1 "Jesteśmy na miejscu."
    #przejście po całym tle, takie pokazowe całego miejsca, 5-7 sec"
    p1 "I jak? Podoba ci się?"
    show secretgarden_bg with dissolve:
        xalign 1.0
    show p1 with moveinright:
        align (.8,1.0)

    menu:
        "Tak.":
            #Lia smile ON
            p1 "Świetnie!"
            #neutral Lia ON
            p1 "Tak czy inaczej."

        "Nie.":
            #Lia shock ON
            p1 "O nie!"
            #Lia sad ON
            p1 "Tak czy inaczej."

    p1 "Tak się zastanawiam…"
    #sad_smile Lia ON
    p1 "Może mogłabym tu przychodzić częściej."
    p1 "Rzadko tu bywam. Tak naprawdę nie wiem dlaczego. Chociaż…"
    #confused Lia ON
    p1 "Chociaż może jednak wiem… Powiedzieć ci?"
    #smile Lia ON 
    p1 "A zresztą, i tak Ci powiem."
    #sad_smile Lia ON
    p1 "Wydaje mi się… Sądzę, że rodzice forsują na mnie taki tryb życia. Wiesz - monotonny, jednostajny, łatwo przewidywalny."
    p1 "Wydaje mi się, że chcieliby uniknąć wszelkich… niespodzianek? Nieprzewidzianych sytuacji? Chyba tak."
    p1 "Wciąż powtarzają mi, że muszę ciężko pracować, być posłuszna. Wykonywać ich polecenia."
    p1 "Tylko jaki to ma sens? Nie mam nic konkretnego z takiego życia…"
    #Lia sad ON
    menu:
        "Tak myślisz?":
            p1 "Tak właśnie myślę."
        "Chyba masz rację.":
            p1 "Sam widzisz…"
    
    p1 "Nie mam nawet żadnych przyjaciół, wiesz? Jedyna osoba z którą byłam trochę bliżej musiała wyjechać. Do tej WIELKIEJ stolicy! Zupełnie poza moim zasięgiem…"

    menu:
        "Kto to taki?":
            p1 "Ech… nazywa się Cirdan."
            #sad_smile Lia ON
            p1 "Kiedyś, lata temu byliśmy… chyba można powiedzieć, że byliśmy przyjaciółmi."

            menu:
                "Ale wyjechał, tak?":
                    p1 "Tak, wyjechał studiować do stolicy. To duża zmiana. Straciliśmy kontakt."
                    p1 "W sumie powinnam się cieszyć. Cirdan zawsze był mądry. Powinnam się cieszyć, że może się rozwijać."
                    #Lia sad ON
                    p1 "Tylko… tak naprawdę żałuję, że odkąd wyjechał, jakby zniknął z mojego życia. Zostały tylko wspomnienia, nic więcej."
                    menu:
                        "Hej, kontakt zawsze można odnowić!":
                            #sad_smile Lia ON
                            p1 "Myślisz? Myślisz, że po tylu latach to ma jeszcze sens?"
                        "Oczywiście. Zawsze warto spróbować.":
                            p1 "Może faktycznie. Tak, myślę, że masz rację."
                        "Musisz spróbować, kiedy będzie okazja!":
                            #Lia smile ON
                            p1 "Dziękuję! Chyba tak właśnie zrobię. Wiesz, tak myślę…"
                "Rozumiem.":
                    #Lia sad ON
                    p1 "Niestety, tak już bywa."

        "To faktycznie przykre…":
            #Lia sad ON
            p1 "Też tak myślę. Ale…"
    
    p1 "Może dzięki tobie udałoby się coś zmienić. Nie oczekuję wiele, ale może coś… cokolwiek."
    #Lia smile ON
    p1 "Jak myślisz? Pomożesz mi?"

    menu:
        "Oczywiście! Zrobię co w mojej mocy.":
            pass

    # TODO dźwięk szelestu krzaczkowego w tle z 1sec opóźnienia"
    play sound sfx_szuranielisci
    p1 "Dziękuję! Może..."
    #Lia shock ON"
    show p1 bsurprised widenedwink lopen with fc
    p1 "Zaraz. Słyszałeś to?"
    show black with dissolve
    show e1b with dissolve
    # TODO komiks E1A ujęcie 1"
    p1 "Widzisz to? Ktoś tam chyba stoi?"
    p1 "Co mam zrobić?"
    hide e1b with dissolve
    hide black with dissolve
    menu:
        "Po prostu podejdź i sprawdź.":
            # +1 pkt PODEJDZLAS
            $ LasPodejscie = True
            #Lia Pose_Confused
            #confused Lia ON
            show p1 bsurprised wink lneutral with fc
            p1 "No dobrze..."
            show black with dissolve
            show e1b with dissolve
            pause 0.4
            show e1b_2 with Dissolve(1.0)
            # TODO komiks E1A ujęcie 2
            "Lia ostrożnie zbliża się do źródła hałasu. Gdy tylko jest już wystarczająca blisko ze zdziwieniem odkrywa, że tajemnicza postać…"
            "...zniknęła."
            p1 "Co? Jak to? Co się tu dzieje?"
            menu:
                "Nie wiem. Wyglądało jakby, ktokolwiek to był, zniknął na twoich oczach.":
                    pass
            p1 "Właśnie… Dziwne. Nawet bardzo. Może mi się po prostu przewidziało?"
            #powrót do normalnego ujęcia rozmowy z graczem"
            hide e1b
            hide e1b_2
            with dissolve
            hide black
            with dissolve
            menu:
                "Może masz rację.":
                    pass
            #confused Lia ON
            p1 "Może."

        "Najlepiej zawołaj. Zobaczymy kto to.":
            #Lia Pose_Confused
            #confused Lia ON
            p1 "Może i tak… no dobrze."
            p1 "HALO, JEST TAM KTO?"
            "..."
            "Nie ma odpowiedzi. Do Lii powróciło tylko ledwo uchwytne echo jej wołania."
            #komiks E1A ujęcie 3"
            show black with dissolve
            show e1b_2 with dissolve
            "Lia powoli i ostrożnie zbliża się do drzewa, które zdaje się być źródłem hałasu"
            p1 "Nikogo tu nie ma."
            #powrót do normalnego ujęcia rozmowy z graczem
            hide e1b
            hide e1b_2
            with dissolve
            hide black
            with dissolve
            p1 "Musiało mi się to przewidzieć."
            menu:
                "I przesłyszeć.":
                    pass
            #confused Lia ON
            p1 "W sumie tak. Dziwny zbieg okoliczności…" 
            #neutral Lia ON
            p1 "Ale w końcu to las, takie dźwięki to norma."
            menu:
                "Prawda. Możesz mieć rację.":
                    pass
            #confused Lia ON
            p1 "Może…"

    #Lia Pose_ToCamera
    #neutral Lia ON
    p1 "Hmm. To jak, chyba nam starczy przygód na jedną noc, co?"

    menu:
        "Tak! Wracajmy.":
            #smile Lia ON
            show p1 bneutral wink lsmile with fc
            p1 "Świetnie! No to wracamy."

        "Nie. Zostańmy jeszcze.":
            #neutral Lia ON
            p1 "A co chcesz tu jeszcze robić?"
            menu:
                "W zasadzie to nie wiem.":
                    pass
            p1 "Świetnie. Mam pomysł. Może wracajmy?"
            menu:
                "Hmm. No dobra. Chodźmy.":
                    pass
            #smile Lia ON
            show p1 bneutral wink lsmile with fc
            p1 "Świetnie! Wracamy."

    stop music2 fadeout 2.0
    stop musictight fadeout 2.0
    #background zmiana na Tawerna z zewnątrz (wersja nocna ofc)
    scene anim_tavern nighttime dragon with fade:
        pos (-0.4, -0.8) zoom 2.5
        ease 8 pos (-0.5,-0.3) zoom 1.8

    $ renpy.sound.set_volume(0.9, delay=0, channel='ambient')
    $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
    play ambient sfx_warm_evening_outdoors
    "Droga powrotna obywa się bez żadnych problemów i Lia szybko dociera do domu."
    "Po drodze sporo myśli o swoim życiu. Tak prosta rzecz jak spacer skłoniła ją do nowym przemyśleń. Wie już, że chce coś zmienić. Nie wie jeszcze tylko dokładnie co i w jaki sposób."
    #zmiana tła na pokój P1 (ciągle noc), Lia w pozycji rozmowy z graczem"
    #happy Lia ON"
    scene anim_room_lia_nightdragon
    $ renpy.music.set_volume(0.5, delay=0, channel='ambient')
    show p1pl bneutral wink_player shadow lsmile
    with fade
    p1 "Dzięki za ten spacer."
    p1 "Mam nadzieję, że teraz, z Twoją pomocą, uda się coś zmienić w moim życiu."
    p1 "Dobranoc!"
    menu:
        "Dobranoc.":
            pass
    hide p1pl with dissolve
    stop ambient fadeout 1.0
    stop music
    pause 0.3
    $ renpy.sound.set_volume(1, delay=0, channel='ambient')
    $ renpy.sound.set_pan(0, delay=0, channel='ambient')
    $ quick_menu = False
    call screen dream_good with Dissolve(2.0)
    scene black
    pause 1
    # TODO przejście w sen, taka mgiełka ładna i pojawia się CG_dream_good. Troszkę światła się majtają i efekt ekran przechodzi zoomem od dołu do góry, żeby jakoś tak zatrzymał się lekko na twarzy i potem poof budzi się
    #przejście do E2A
    jump e2a


################################################################################
#################################    E1B     ###################################
################################################################################

label e1b:
    # TODO DUB04 - “try better next time”

    $ HatePath += 1
    #czarne tło
    scene black with fade
    "Widocznie dotknięta Lia rusza w stronę swojego pokoju. Gniew, za którym pewnie kryje się prawdziwy ból, widać w każdym jej gwałtownym kroku."
    #background pokój Lii, wersja nocna i Lia w pozycji rozmawiającej z graczem"
    play audio sfx_drzwi
    scene anim_room_lia_nightdragonlight
    show p1pl shadow
    with fade
    "Gdy tylko dociera do swojego pokoju łapie za krawędź drzwi i z rozmachem je zamyka. Huk, które wydają jest głośniejszy niż się spodziewała."
    #shock Lia ON
    "Z lekkim niepokojem zamiera w bezruchu. Nasłuchuje, czy w sąsiednich pokojach ktoś się porusza - boi się, że mogła kogoś obudzić."
    #Lia Pose_CrossedArm
    #annoyed Lia ON
    "Ma szczęście - nikt niczego nie usłyszał. Po krótkiej chwili wypuszcza powietrze i, już nieco spokojniej, siada na łóżku."
    p1 "Dalej tu jesteś?"
    stop music fadeout 3.0
    menu:
        "Tak, jestem.":
            #angry Lia ON
            p1 "To chyba tyle z łamania rutyny."
            p1 "Wielkie dzięki za pomoc."
            p1 "Dobranoc."

        "Wiesz, że teraz lepiej nie podpadać Twoim rodzicom.":
            #angry Lia ON
            p1 "Ach, teraz cię to wszystko obchodzi, tak?"
            p1 "Teraz się przejmujesz?"
            p1 "Widzę, że to tyle z łamania rutyny.”"
            p1 "Dobranoc."
        
        "...":
            #angry Lia ON
            p1 "Tak, lepiej się nie odzywaj."
            p1 "Po prostu zostaw mnie w spokoju."
            #sad Lia ON
            p1 "Dobranoc."

    hide p1pl with dissolve
    pause 0.3
    $ quick_menu = False
    call screen dream_bad with Dissolve(2.0)
    scene black
    pause 1
    # TODO

    #po “dobranoc” powolne przejście w czarny ekran jakby sen, może lekka mgiełka?
    #tutaj odpala się zły sen
    #efekt mgiełki i przejścia w sen, jako background mamy ciemny las z postacią z pochodnią, powolny zoom na nią leci (podobnie jak było obecnie), zbliżenie trwa chwilę i nagle po paru sekundach wyskakuje CG_dream_bad może z jakimś creepy dźwiękiem i po sekundzie poof znika wszystko i Lia się budzi
    #po śnie przejście do E2B
    jump e2b


################################################################################
#################################    E2A     ###################################
################################################################################


label e2a:
    #na ekranie pokój P1 o brzasku
    $ dt = 1
    $ quick_menu = True
    scene anim_room_lia_morning with fade
    play music alexander_nakarada_relaxing_ballad volume 0.5
    "Lia najpierw czuje jak pierwsze promienie słońca delikatnie muskają jej twarz. Dopiero po chwili otwiera oczy."
    "Delikatne ciepło wlewające się przez okno, oraz to, które poczuła gdzieś głęboko w środku, przekonują ją, aby wstać od razu."
    "Dopiero po chwili dziewczyna zauważa, że od samego przebudzenia ma uśmiech na twarzy."
    show p1pl bneutral wink_player lsmile with dissolve
    #Lia pojawia się na ekranie, rozmowa z graczem
    #smile Lia ON
    menu:
        "Dzień dobry!":
            pass
    #happy Lia ON
    p1 "Oh! Dzień dobry!"
    #smile Lia ON
    p1 "Dziękuję za wczoraj! Od razu czuję się lepiej."
    #happy Lia ON
    p1 "Widzisz? Wstałam od razu! Nawet nie pomyślałam, żeby zostać w łóżku do południa."
    p1 "Dobra, czas się zbierać na śniadanie."
    #korytarz jako tło, bez postaci
    "Lia opuszcza pokój i wychodzi wprost na korytarz części mieszkalnej Tawerny."
    #Lia na ekranie, rozmawia z graczem
    #Lia confused ON
    p1 "Hej, zaraz, moment…"
    #Lia smile ON
    p1 "Pokazywałam ci kiedyś co można znaleźć w Tawernie?"
    menu:
        "Nie, nigdy":
            p1 "O, to może pokażę ci wszystko teraz? Co Ty na to?"
        "Może coś wspominałaś...":
            p1 "Hm... nie sądzę, nie przypominam sobie. Pokazać ci?"

    menu:
        "Tak, chętnie posłucham.":
            #smile Lia ON
            p1 "Dobrze!"
            p1 "Zaraz obok mojego pokoju jest sypialnia rodziców. Nic ciekawego."
            p1 "O, a tam z tyłu jest łazienka."
            #smirk Lia ON
            p1 "Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada."
            menu:
                "Haha, dobrze! Masz rację. Obiecuję, że nie będę.":
                    pass
            #smile Lia ON
            p1 "Haha, świetnie! Zaraz obok jest jadalnia i kuchnia."
            p1 "Oczywiście mieliśmy jeść właśnie tam. No i oczywiście jemy gdzie indziej. Plany to jedno, życie to drugie - po co brudzić dwa miejsca, prawda?"
            p1 "W związku z tym jemy na dole."
            #confused Lia ON
            p1 "Zresztą, tata woli mieć zawsze oko na to, co dzieje się w Tawernie."
            #smile Lia ON
            p1 "No, ale jest też mniej sprzątania!"
            p1 "O, a tutaj, obok, jest jedyny w tym skrzydle pokój gościnny."
            p1 "Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty."
            p1 "No dobrze, to chyba wszystko. Możemy iść dalej."

        "Nie, nie ma takiej potrzeby.":
            #Lia confused ON
            p1 "Oh. No dobrze, to chodźmy dalej."

    #background sala główna Tawerny, pusta. Lia na środku w pozycji rozmowy z graczem
    #confused Lia ON
    scene img_tavern_mainroom
    show p1pl bsurprised wink_player lneutral
    with fade
    p1 "No dobra. Rodziców chyba jeszcze nie ma. W razie czego jesteś ze mną tak?"
    menu:
        "Oczywiście. Cały czas.":
                    pass
    #Lia smile ON"
    show p1pl bneutral wink_player lsmile with fc
    p1 "Cieszę się. Uch... dobra, wchodzę." 
    #background zmiana na kuchnię, Lia po lewej patrzy w prawo"
    #od prawej wchodzi P2"
    #Lia smile ON"
    scene room_kitchenmealday
    show p1 bneutral wink lsmile:
        align (0.1,1.0)
        xzoom -1
    with fade
    show p2 with easeinright:
        align(.7,1.0)
    p1 "Dzień dobry Mamo!"
    #od prawej wchodzi P3, P2 się lekko przesuwa w lewo, żeby zrobić miejsce"
    show p2:
        linear 0.5 align(.6,1.0)
    show p3 behind p2 with easeinright:
        align(.93,1.0) xzoom -1
    p1 "Dzień dobry Tato!"
    # TODO P2 i P3 patrzą na siebie, oboje confused ON"
    show p2 with fc:
        xzoom -1
    "Rodzice spoglądają na siebie, widocznie zaskoczeni tak dobrym humorem córki."
    "W końcu niezbyt często bywa tak uśmiechnięta od samego rana."
    "Wydaje się, że są lekko… podejrzliwi?"
    #P2 i P3 patrzą teraz na Lię, tj. w lewo"
    #neutral P2 i P3 ON"
    show p2 neutral wink with fc
    show p3 neutral wink with fc
    show p2 with fc:
        xzoom 1
    show p1 bsurprised wink lneutral with fc
    p3 "No dzień dobry, dla ciebie najwidoczniej bardzo dobry... Czy coś się stało?"
    #confused Lia ON"

    p1 "Dlaczego miało się coś stać?"
    #P2 wychodzi na pierwszy plan (coś podobnego co wcześniej było)"
    #P2 smile ON"
    show p2 smile:
        linear 0.5 xalign 0.5
    show p1 bsurprised widenedwink lsad with fc
    p2 "Dziecko... Przecież Cię znamy. Co się stało?"
    show p1 bsad closed lsad with fc
    p1 "Ehh..."
    stop music fadeout 5.0

    menu:
        "Powiedz im prawdę.":
            jump e2a1

        "Powiedz, że nic się nie stało.":
            #E2A2
            #confused Lia ON
            #P2 i P3 neutral ON
            show p1 bsurprised wink lneutral with fc
            show p2 neutral wink with fc
            show p3 neutral wink with fc
            p1 "Ale nic się nie stało. Naprawdę."
            p3 "Czyli twierdzisz, że wczoraj, jak tylko skończyłaś pracę, zamknęłaś Tawernę i grzecznie poszłaś do siebie spać. Mam rację?"
            menu:
                "Powiedz, że tak. ":
                    p1 "No tak. Dokładnie."
                    p3 "I po co kłamiesz? Czy ty nie rozumiesz…"
                    p1 "Nie kłamię…"
                    #angry Zorn ON
                    p3 "Nie! Nawet nie zaczynaj."
                    #shock Lia ON
                    p3 "Wiem, że Cię nie było w pokoju…"
                    #P3 patrzy na P2
                    p3 "Naprawdę, czasem nie mam do ciebie sił."
                    #P3 patrzy na P1
                    #sad Lia ON
                    #mała przerwa, jakieś 2-3 sec, żeby gracz poczuł tą przedłużającą się, niezręczną ciszę.
                    p3 "Czekam na Ciebie w sali. Mamy sporo pracy."
                    #P3 wychodzi z kuchni
                    show p3 with fc:
                        xzoom 1
                    show p3:
                        linear 1 xalign 1.45
                    #sad P2 ON
                    p2 "Córeczko, musisz być bardziej odpowiedzialna."
                    p2 "Nie możesz tak bez słowa wychodzić w nocy. Jeszcze do lasu!"
                    p2 "Coś mogło Ci się stać…"
                    p2 "Nigdy byśmy tego sobie nie wybaczyli."
                    p2 "Tata tak się denerwuje właśnie dlatego, że bardzo cię kocha i martwi o ciebie."
                    p2 "Postaraj się być bardziej ostrożna."
                    #P2 wychodzi z kuchni
                    #P1 do gracza, sad ON"
                    show p2 with fc:
                        xzoom -1
                    show p2:
                        linear 2 xalign 1.4
                    show p1:
                        linear 2 xalign 0.5
                    pause 1.5
                    show p1 bneutral wink_player lsad -smalltears with fc
                    p1 "Nie jestem taka pewna, czy to była dobra rada…"
                    p1 "Ale mimo wszystko dzięki."
                    #Lia wychodzi z kuchni
                    show p1:
                        linear 2 xalign 1.4
                    $ e3a2 = True
                    #przejście do E3A2
                    jump e3

                "Lepiej powiedz prawdę.":
                    p1 "Nie do końca…"
                    #angry Zorn ON"
                    show p3 angry angrywink with fc
                    p3 "Rozumiem. No to powiedz mi jak było DOKŁADNIE. I postaraj się być bardziej precyzyjna."
                    #w tym miejscu idzie to samo co w E2A1, w całości
                    jump e2a1

        # TODO "[[Nic nie mów.]" if not be01:
        #     jump be01
            #przejście do BE01

# osobno bo można tu przejść z 2 wyborów w poprzednim menu
label e2a1:
    # E2A1
    $ theTruthHasBeenSpoken = True
    #sad_smile Lia ON
    show p2 neutral
    show p1 bsad wink lsmile
    with fc
    p1 "No, więc… po prostu… Po prostu byłam się przejść. Tak."
    #angry Zorn ON"
    show p3 angry angrywink
    p3 "GDZIE?!"
    #shock Lia ON"
    show p1 bsurprised widenedwink lopen
    with fc
    #2-3 sekundy przerwy
    pause 2.0
    p3 "Lepiej nie każ mi czekać!"
    show p2 with fc:
        xzoom -1
    p2 "Zorn, bardzo cię proszę. Spokojnie. Nie denerwuj się."
    #confused Lia ON
    show p1 bsurprised wink lneutral with fc
    p2 "Pozwól, że ja się tym zajmę. Ty może zajrzysz do sali głównej? Zerknij czy Cię tam nie ma i nie masz czegoś do zrobienia, dobrze?"
    p3 "Mhm. Może tobie pójdzie sprawniej."
    show p2 with fc:
        xzoom 1
    p3 "Jak już tutaj skończycie, to czekam na ciebie w głównej sali, Lia. Mamy sporo pracy."
    #P3 wychodzi, P2 troszkę zbliża się do P1"
    show p3 with fc:
        xzoom 1
    show p3:
        linear 1 xalign 1.45
    show p2:
        linear 1 xalign 0.42
    p2 "Lia… Powiedz mi, proszę, gdzie dokładnie byłaś."
    #P1 sad ON
    p1 "W lesie… Znaczy w Ogrodzie dokładnie."
    p2 "Rozumiem. W tym Twoim Sekretnym Ogrodzie, tak?"
    #sad_smile Lia ON
    p1 "Tak… Byłam się tylko przejść, naprawdę. Nie poszłam na długo."
    p2 "Oczywiście. Czy podczas tego twojego spaceru coś się wydarzyło? Cokolwiek?"
    #sad Lia ON
    p1 "Nic szczególnego, tylko…"
    p2 "Tylko co?"
    p1 "Eh… Myślałam, że kogoś widziałam. Tylko mi się wydawało. Jestem pewna. To pewnie tylko jakieś zwierzę w krzakach, nic więcej."
    p2 "Skąd taka pewność?"

    #jeśli 1pkt PODEJDZLAS
    if LasPodejscie:
        p1 "Po prostu poszłam sprawdzić… Nikogo tam nie było."
        #shocked P2 ON
        p2 "Oh dziecko… To było bardzo nierozsądne. Bardzo. Pamiętaj, żeby więcej tak nie robić, dobrze?"
        p2 "Ale… no, najważniejsze, że nic się nie stało."

    #jeśli brak punktu PODEJDZLAS
    else:
        p1 "Zawołałam czy ktoś tam jest. Nikt nie odpowiedział, ani nawet się nie poruszył."
        #shocked P2 ON
        p2 "Oh dziecko… To było bardzo nierozsądne. Bardzo. Pamiętaj, żeby więcej tak nie robić, dobrze?"
        p2 "Ale… no, najważniejsze, że nic się nie stało."

    p2 "Lia, proszę cię. Musisz mi obiecać, że będziesz bardziej uważać w przyszłości. Wiesz ile zna… wiesz, że jesteś dla nas wszystkim, tak?"
    p1 "Tak, mamo, rozumiem…"    
    #smile P2 ON"
    show p2 smile
    p1 "No dobrze..."
    p2 "Dobrze, dobrze, córeczko. Cieszę się. Dokończ śniadanie i idź pomóż tacie, dobrze?"
    p1 "Dobrze mamo."
    #P2 wychodzi z kuchni"
    #sad_smile Lia ON, do gracza:"
    show p2 with fc:
        xzoom -1
    show p2:
        linear 2 xalign 1.4
    show p1:
        linear 2 xalign 0.5
    pause 1.5
    show p1 bsad wink_player lsmile with fc
    p1 "Dzięki za pomoc. Ciężko byłoby bez Ciebie."
    p1 "No nic, czas zabrać się do pracy."
    $ e3a1 = True
    jump e3
    #przejście do E3A1

################################################################################
#################################    E2B     ###################################
################################################################################


label e2b:
    # bez śniadania bo koszmar
    #na ekranie pokój P1, poranek
    $ quick_menu = True
    scene anim_room_lia_morning with fade
    play sound sfx_easy_door_opening
    "..."
    #od prawej wchodzi P3 angry
    show p3 angry:
        align (1.35,1.0) xzoom -1
        linear 1 align (0.7, 1.0)
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music [alexander_nakarada_spring, alexander_nakarada_spring, "<silence 10000.0>"] fadein 5.0 fadeout 10
    "Lia budzi się gwałtownie i z prawdziwym przerażeniem zrywa z posłania. Przez chwilę jest tylko strach - echo nocnego koszmaru. Dziewczyna nie wie gdzie jest, nie wie co się wokół niej dzieje. Jest tylko przerażenie."
    "Po chwili dociera do niej, że obudziło ją trzaśnięcie drzwi towarzyszące energicznemu wtargnięciu ojca do jej pokoju."
    p3 "Nie słyszysz, że cię wołam?"
    #Lia pojawia się po lewej, angry ON
    show p1 bangry narrowedwink lsad with fc:
        align (0.1,1.0) xzoom -1
    p1 "Ej, tato! Nie możesz tak wchodzić bez pukania! Co, jakbym była rozebrana?!"
    #Suprised Lia ON
    #Confused P3 ON
    show p1
    show p3
    with fc
    p3 "No dobrze dobrze, masz rację. Przepraszam."
    p3 "Po prostu wołałem cię już dość długo. Zacząłem się martwić czy wszystko w porządku."
    p3 "Już zdążyłaś przegapić śniadanie, a trzeba jeszcze przygotować Tawernę do otwarcia."
    #sad Lia ON
    p3 "Czekam na ciebie na dole."
    p1 "Dobrze, tato. Zaraz przyjdę."
    #P3 wychodzi z pokoju, P1 mówi do gracza 
    #sad_smile Lia ON
    show p3 with fc:
        xzoom 1
    show p3:
        linear 1 xalign 1.45
    pause 1
    show p1:
        linear 0.5 xalign 0.4
    show p1 bsad wink_player lsmile with fc
    p1 "Dzień dobry."
    menu:
        "Dzień dobry.":
            pass
    p1 "Ten sen… Był dziwny. Bardzo… I naprawdę przerażający…"
    p1 "Nie rozumiem..."
    menu:
        "To tylko sen. Nie przejmuj się.":
            pass
    p1 "Może masz rację. Ale wciąż było to bardzo dziwne… Nigdy nie śniły mi się takie rzeczy."
    p1 "No nic, może jest tak jak mówisz. Zwykły sen i nic więcej. Trzeba się zbierać. Czas do pracy." 
    #sad Lia ON
    p1 "Znowu."
    "Lia wyszła ze swojego pokoju wprost na Tawerniany korytarz."
    #Lia na ekranie, rozmawia z graczem

    scene tavern_hall_bg0
    show p1pl bsurprised wink_player lneutral
    with fade
    #Lia confused ON
    p1 "Hej, zaraz, moment…"
    #Lia smile ON
    p1 "Opowiadałam ci kiedyś co można znaleźć w Tawernie?"
    menu:
        "Nie, nigdy":
            p1 "O, to może pokażę ci wszystko teraz? Co Ty na to?"
        "Może coś wspominałaś...":
            p1 "Hm... nie sądzę, nie przypominam sobie. Pokazać ci?"

    menu:
        "Tak, chętnie posłucham.":
            #smile Lia ON
            p1 "Dobrze!"
            p1 "Zaraz obok mojego pokoju jest sypialnia rodziców. Nic ciekawego."
            p1 "O, a tam z tyłu jest łazienka."
            #smirk Lia ON
            p1 "Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada."
            menu:
                "Haha, dobrze! Masz rację. Obiecuję, że nie będę.":
                    pass
            #smile Lia ON
            p1 "Haha, świetnie! Zaraz obok jest jadalnia i kuchnia."
            p1 "Oczywiście mieliśmy jeść właśnie tam. No i oczywiście jemy gdzie indziej. Plany to jedno, życie to drugie - po co brudzić dwa miejsca, prawda?"
            p1 "W związku z tym jemy na dole."
            #confused Lia ON
            p1 "Zresztą, tata woli mieć zawsze oko na to, co dzieje się w Tawernie."
            #smile Lia ON
            p1 "No, ale jest też mniej sprzątania!"
            p1 "O, a tutaj, obok, jest jedyny w tym skrzydle pokój gościnny."
            p1 "Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty."
            p1 "No dobrze, to chyba wszystko. Możemy iść dalej."

        "Nie, nie ma takiej potrzeby.":
            p1 "Oh. No dobrze, to chodźmy dalej."

    "Lia rusza na dół. W głównej sali już czeka na nią ojciec."
    #przejście do #E3A3
    jump e3 # nie potrzeba żadnych dodatkowych zmiennych


################################################################################
##################################    E3     ###################################
################################################################################

label e3:
    play music peritune_minstrel fadein 10.0 fadeout 10.0 volume 0.4
    $ dt = 1
    ################ devstuff #################
    if config.developer:
        menu:
            "dev/ e3a1":
                $ e3a1 = True
                pass
            "dev/ e3a2":
                $ e3a2 = True
                pass
            "dev/ e3a3":
                pass
    #########################################

    if e3a1:
        scene tavern_main_bar_bg0
        show p3 at zabarem:
            xalign 0.5 xzoom -1.0
        show tavern_main_bar_bar1
        show p1:
            align (0.0,1.0) xzoom -1
        with fade
        #tło bar, P1 po lewej, P3 prawo za barem

        "Po wyjściu z kuchni na Lię czekał ojciec."
        #confused Lia ON
        show p1 bsurprised wink lneutral with fc
        p3 "Poczekaj Lia."
        p3 "Rozmawiałem z Twoją matką."
        p3 "Mimo, że byłaś nieodpowiedzialna to przyznałaś się, co jest dobre."
        #surprised_neutral Lia ON"
        show p1 bsurprised widenedwink lneutral with fc
        p3 "Możliwe, że trochę zbyt mocno Cię pilnujemy, więc mamy propozycję..."
        #surprised_happy Lia ON"
        show p1 bsurprised widenedwink lsmile with fc
        p3 "Jeśli masz ochotę możesz dziś skończyć wcześniej pracę i przejść się na festiwal do wioski."
        p1 "Oh... Nie wiem co powiedzieć..."
        p3 "Po prostu powiedz czy chcesz iść."
        menu:
            "Powiedz, że chcesz.":
                # +1pkt FESTIVAL01
                $ d_gofestiwal = True
                #smile Lia ON
                show p1 bneutral wink lsmile with fc
                p1 "Chętnie pójdę. Dziękuję."
                p3 "No dobrze... To przed wieczorem Cię zastąpię."
                p3 "Tymczasem czas na pracę."

            "Powiedz, że nie chcesz.":
                #sad_smile Lia ON
                show p1 bsad wink lsmile with fc
                p1 "Dziękuję za propozycję, ale nie chcę iść."
                p3 "Oh. No dobrze. Twoja decyzja."
                p3 "No to czas na pracę."

    elif e3a2:
        scene tavern_main_bar_bg0
        show p3 angry at zabarem:
            xalign 0.5 xzoom -1.0
        show tavern_main_bar_bar1
        show p1:
            align (0.0,1.0) xzoom -1
        with fade
        #tło bar, P1 po lewej, P3 prawo za barem - P3 angry ON
        p3 "No jesteś w końcu. Zostań chwilę."
        #surprised_sad Lia ON"
        show p1 bsurprised widenedwink lsad with fc
        p3 "Mam nadzieję, że następnym razem nie będziesz próbować kłamać."
        p3 "Zacznij być bardziej odpowiedzialna."
        p3 "A teraz chodź do pracy."

    else:
        scene ep_img_tavern_mainroom_nozoom
        show p1:
            align(0.2,1.0) xzoom -1
        show p3:
            align(0.6,1.0) xzoom -1
        with dissolve
        #background sala główna, P1 lewo i P3 prawo stoją sobie
        p3 "O! Jesteś wreszcie. Chodź mi pomóc."

    scene ep_img_tavern_mainroom_nozoom
    show p1:
        align(0.2,1.0) xzoom -1
    show p3:
        align(0.6,1.0) xzoom -1
    with dissolve
    #background zmienia się na całą salę główną, P1 lewo i P3 prawo stoją sobie
    p3 "Dobra. Ja idę przygotować drugą salę. Ty zacznij od wytarcia stołów."
    p3 "Tylko dokładnie! Sprawdzę później."
    #P3 wychodzi do prawej sali. frown Lia ON, mówi do gracza:
    show p3 with fc:
        xzoom 1
    show p3:
        linear 1 xalign 1.45

    show p1:
        linear 1.3 xalign .4
    pause 1
    show p1 wink_player with fc
    p1 "Zawsze tak mówi i potem i tak nie sprawdza... No ale i tak trzeba to ogarnąć."
    # odpala się mini gra ze stoliczkiem
    jump czyszcz


################################################################################
################################    PO STOLE    ################################
################################################################################


label poczyszczeniustolu:
    #sala główna, Lia na środku, neutral ON
    scene ep_img_tavern_mainroom_nozoom
    show p1:
        align(0.5,1.0)
    if n == n_max:
        "Lia wyprostowała się, aby przyjrzeć się czy czegoś nie ominęła."
        "Wygląda na to, że wszystko dobrze!"
        "Chciała pomyśleć Lia, ale zrozumiała, że to głos ojca."
        #P3 od prawej pojawia się znienacka, Lia obraca się w jego kierunku
        show p3 behind p1 with Dissolve(1.0):
            align (0.75,1.0) xzoom -1
        show p1 with fc:
            xzoom -1
        p3 "Mówiłem, że sprawdzę. Bardzo ładnie. Teraz zajmij się resztą, a pot..."

    else:
        "Lia wyprostowała się, aby przyjrzeć się czy czegoś nie ominęła."
        "Od razu zauważyła, że ominęła jeden fragment."
        "Gdy tylko chciała zabrać się za poprawienie tego usłyszała za sobą głos."
        #P3 od prawej pojawia się znienacka, Lia obraca się w jego kierunku
        show p3 behind p1 with Dissolve(1.0):
            align (0.75,1.0) xzoom -1
        show p1 with fc:
            xzoom -1
        p3 "Ominęłaś fragment, o tam!"
        "Odezwał się ojciec wskazując palcem na niedoczyszczony fragment."
        #angry Lia ON
        show p1 bangry narrowedwink with fc
        p1 "Tak, widzę! Akurat teraz musiałeś podejść i sprawdzić?"
        "Powiedziała Lia ze złością w głosie. Natychmiast tego pożałowała widząc złość na twarzy Taty."
        #Angry Zorn ON"
        show p3 angry with fc
        p3 "Młoda Damo, proszę się zachowywać! Nastę..."

    play audio sfx_drzwi
    "Nagle z hukiem otworzyły się drzwi, Zorn zareagował pierwszy."
    #sala główna, Zorn stoi bliżej środka i patrzy w lewo, Lia za nim też patrzy w lewo"
    #angry P3 ON"
    show p1 behind p3:
        linear 0.5 xalign .74
    show p3:
        linear 0.5 xalign 0.45
    show p3 angry with fc
    pause 0.3
    show p1 with fc:
        xzoom 1
    p3 "Halo! Zamknięte jeszcze! Proszę wyp..."
    #neutral P3 ON, po lewej wchodzi P6 i patrzy w prawo"
    show p6 with easeinleft:
        align (.5,.5) pos (0.2,0.78) xzoom -1
    show p3 neutral with fc
    p3 "Aaa, HAHA - to Wy Panie Mohon. Wchodź, nie krępuj się!"
    p6 "HAHA, a czego miałbym się krępować? Zgłupiałeś Zorn?"
    p6 "Weź polej piwo bo mnie chuj strzeli zar... Oooo, panienko!"
    #P1 wychodzi przed Zorna"
    show p3 behind p1
    show p1:
        linear 0.5 xalign 0.6
    p6 "Uszanowanie, dzień dobry - prześlicznie panienka dziś wygląda!"
    #blush Lia ON"
    show p1 blush with fc
    p1 "Dzień dobry Panie Mohon!"
    show p1:
        linear 0.5 xalign 0.74
    show p1 behind p3 with fc
    #Zorn wychodzi znów przed Lię, Lia znów w prawo"
    p3 "No dobra dobra, starczy tych uprzejmości. Chodź Mohon, potrzebujesz czegoś?"
    #frown Lia ON"
    show p1 bangry wink lneutral with fc
    p6 "Hmm, ten... Mieliśmy omówić..."
    p3 "Ach, tak - pamiętam. Chodź, coś Ci naleję i pogadamy. Lia posprzątaj ostatnią salę."
    p1 "Dobrze."
    hide p1 with moveoutleft
    #przejście do lewej sali"
    #Lia mówi do gracz, sad_smile ON"
    scene img_tavern_leftroom:
        zoom 1.2 align (1.0,1.0)
    show p1pl bsad wink_player lsmile
    with dissolve
    p1 "Dobra. Daj mi chwilę, ogarnę wszystko."


    menu:
        "Kto to był?":
            #happy Lia ON
            show p1pl bneutral narrowedwink_player lsmile with fc
            p1 "Oh, to był Pan Mohon. Często tutaj przychodzi."
            p1 "Jak na pewno było widać to krasnolud."
            #confused Lia ON"
            show p1pl bsurprised wink_player lneutral with fc
            p1 "Hmm, co by jeszcze można o nim powiedzieć..."
            p1 "Eh, opowiadanie o kimś jest skomplikowane."
            #neutral Lia ON"
            show p1pl bneutral wink_player lneutral with fc
            p1 "Pracuje w kopalni z tego co mi wiadomo."
            p1 "W sumie go lubię, jest zawsze miły dla mnie."
            p1 "Może trochę wulgarny, ale nadrabia to uśmiechem."
            p1 "Często widują się z moim ojcem. Nie wiem po co."
            p1 "Hmm. To chyba wszystko."
            #sad_smile Lia ON"
            show p1pl bsad wink_player lsmile with fc
            p1 "Nigdy bardziej się nad tym nie zastanawiałam. Wybacz."
            menu:
                "Nie przejmuj się. Dziękuję.":
                    pass
            #smile Lia ON"
            show p1pl bneutral wink_player lsmile with fc
            p1 "Nie ma za co! Dobra, czas wziąć się do pracy."

        "Dobrze, poczekam w ciszy.":
            pass

    #lewa sala sama, lekki ruch kamery, zoom/przejście (2-3sec)
    hide p1pl with fc
    show img_tavern_leftroom:
        linear 3 xalign 0.0
    "Lia zabrała się za sprzątanie sali. Jak tylko skończyła to ruszyła z powrotem do głównej sali."
    #przejście do sali głównej, Zorn za barem"
    scene ep_img_tavern_mainroom
    show p3:
        zoom 0.3 xpos 0.6 yalign 0.6
        xzoom -1
    show tavern_main_bar3_dn_idle:
        zoom 1.2
        align (.5,.5)
    show tavern_main_beer4_idle:
        zoom 1.2
        align (.5,.5)
    with dissolve
    "..."
    #Lia wchodzi od lewej"
    show p1 with moveinleft:
        align (0.0,1.0) xzoom -1
    p3 "O, Lia - chodź tutaj."
    # show img_tavern_mainroom:
    #     linear 0.4 zoom 1.5 align(0.6,0.5)
    scene tavern_main_bar_bg0
    show p3 at zabarem:
        xalign 0.6 xzoom -1.0
    show tavern_main_bar_bar1
    with dissolve
    show p1 bangry wink lneutral  with easeinleft:
        align (0.0,1.0) xzoom -1
    #zoom na bar, Lia po lewej i Zorn po prawej"
    #frown Lia ON"
    p3 "Wszystko posprzątane?"
    p1 "Tak."
    p3 "Super, to przejmij bar i..."


    stop music fadeout 2

    tg1 "Ekhem."
    hide p3 with moveoutleft
    scene ep_img_tavern_mainroom
    show p3:
        align (0.68,1.0) xzoom -1
    show tg1:
        align (0.2,1.0) xzoom -1
    with dissolve
    #powrót do widoku sali głównej, Lia za barem (jeśli możliwe), po lewej TG1, Zorn staje przed nim"
    tg1 "Jeśli można."
    p3 "Oczywiście. Za Tobą."
    #wychodzą z pomieszczenia, powrót do zoomu na bar, Lia do gracza, confused ON"
    scene tavern_main_bar_bg0
    show p1 bsurprised wink_player lneutral at zabarem:
        xalign 0.6
    show tavern_main_bar_bar1
    with dissolve
    p1 "Huh. Dziwne. Znów jeden z tych zakapturzonych typów."

    menu:
        "Co to za jedni?":
            p1 "Hmm. To jest bardzo dobre pytanie."
            p1 "Nikt nie wie. Rozbili namiot przed Tawerną jakiś czas temu i tam mieszkają."
            p1 "Przychodzą czasem po prowiant. Ogólnie to się kręcą po całej okolicy."
            p1 "Może będzie kiedyś okazja dowiedzieć się coś więcej."
            p1 "Wiem tyle, że płacą dobrze, więc tata chyba nie zadaje za dużo pytań."
            p1 "Pewnie szkoda stracić klientów."
            p1 "Dobra, kiedy indziej o tym pogadamy - słyszę, że wraca."

        "Rzeczywiście dziwne.":
            p1 "Są trochę przerażający. No nic, wracam do pracy."
            "Po krótkiej chwili Zorn wrócił do pomieszczenia."


    #Lia surprised_neutral ON
    #zoom na bar, Lia po prawej, Zorn po lewej
    show p1 bsurprised widenedwink lneutral with fc
    show p3 with moveinleft:
        align (0.0,1.0)
    p3 "Dobra, wszystko ogarnięte. Jak coś to ktoś z nich przyjdzie później po paczkę z prowiantem."
    p1 "Od tych zakapturzonych?"
    p3 "Tak, od nich. Za paczkę zapłacili z góry. Idę ją przygotować."
    p3 "Później Ci ją przyniosę, po prostu im ją wydasz."
    p3 "Pilnuj Tawerny, wkrótce ludzie zaczną krążyć."
    #Zorn wychodzi z pomieszczenia"
    hide p3 with moveoutleft
    "..."
    #Lia mówiąca do gracza, neutral ON"
    show p1 bneutral wink_player lneutral with fc
    p1 "No to zaczynamy pracę."


    #tutaj skip, przejście na background zewnątrz Tawerny i upływ czas do południa, 3-4sec, +1 upływ czasu"
    window hide
    with fc
    show anim_tavern outside dragon with dissolve
    pause 4
    hide anim_tavern outside dragon
    play ambient medieval_tavern_ambience_5min fadein 1.0 fadeout 2.0 volume 0.7
    play music the_old_tower_inn fadein 5.0 volume 0.7
    #po przejściu powrót do Tawerny, zoom taki sam jak wcześniej i Lia mówiąca do gracza, Lia frown ON"
    show p1 bangry wink lneutral
    with dissolve
    window auto
    with fc
    show p1 wink_player with fc
    p1 "Oh... Jesteś tutaj dalej ze mną?"
    menu:
        "Oczywiście.":
            pass
    #sad_smile Lia ON"
    show p1 bsad wink_player lsmile with fc
    p1 "Dzięki."
    p1 "Przynajmniej rano jest mały ruch, więc można pogadać..."
    #tutaj bez imienia pierwsze powiedzenie od Ainy i bez pokazywania jej"
    p7q "Halo, słyszysz mnie?"
    #Lia wraca na pozycję, zoom na bar"
    #surprised_neutral Lia ON"
    #Aina się pojawia, neutral ON, po lewej przed barem"
    show p1 bsurprised widenedwink lneutral with fc
    show p7 with fc:
        align (0.1,1.0)
    p7 "Halo?"
    p1 "Oh. Przepraszam, zamyśliłam się. Co potrzeba?"
    #Aina smile ON"
    show p7 bneutral wink lsmile with fc
    p7 "Haha! Nie ma problemu, też czasem zdarza mi się odlecieć myślami nie wiadomo gdzie."
    #Lia smile ON"
    show p1 bneutral wink lsmile with fc
    p7 "Dla mnie to co zwykle!"
    p1 "Już podaję!"
    window hide
    with fc
    show black with dissolve
    show work3a with dissolve
    show work3b with Dissolve(1.0)
    pause 0.5
    hide work3b with Dissolve(1.0)
    hide work3a with dissolve
    hide black with dissolve
    window auto
    with fc
    #komiks z folderu work work, tak by jako animacja wyglądał work 3A i work 3B"
    #Lia blush ON"
    show p1 blush with fc
    p7 "Dzięki ślicznotko! Do zobaczenia!"
    #Aina znika z ekranu, Lia do gracza"
    hide p7 with moveoutleft
    show p1 -blush wink_player with fc
    p1 "To było lekko niespodziewane..."

    menu:
        "Oj tam! To tylko komplement.":
            p1 "Huh, niby tak. Masz rację, ale... Oh, ktoś idzie."
        "Haha! Urocza dziewczyna!":
            p1 "Mhm, masz rację. Może... Oh, ktoś idzie."

    #wracamy na standardowy zoom, pojawia się TG2 (inny niż wcześniej) i podpis go ‘???’
    #surprised_neutral Lia ON
    show p1 wink with fc
    show tg2 with moveinleft:
        align (0.1,1.0) xzoom -1
    tg2 "Witam."
    p1 "Dzień dobry. W czym mogę pomóc?"
    #confused Lia ON"
    show p1 bsurprised wink lneutral with fc
    tg2 "Ja po paczkę."
    p1 "Hmm? Ah, paczka... dziś rano zamówiona, tak?"
    tg2 "Tak."
    #sad_smile Lia ON"
    show p1 bsad wink lsmile with fc
    p1 "Um, już podaję."
    #komiks folder work work Lia podająca paczkę"
    show black with dissolve
    show work_bar_base with dissolve
    show work_bar_package with dissolve
    p1 "Proszę."
    hide work_bar_package with dissolve
    tg2 "Mhm."
    hide work_bar_base with Dissolve(0.2)
    hide black with dissolve
    hide tg2 with moveoutleft
    pause 0.2
    show p1 bangry narrowedwink_player lneutral with fc
    #annoyed Lia ON, TG2 wychodzi ze sceny od razu. Lia mówi do gracza"
    p1 "Nie dość, że nie pokazują twarzy to jeszcze są niemili. Pff."
    #levius na razie bez imienia i jego podpis jako ‘???’"
    p9q "Hej Lia!"
    #przejście do standardowej sceny, Levius po lewej, Lia wciąż za barem, Lia surprised_neutral ON,"
    show p9 with moveinleft:
        align (0.1,1.0)
    show p1 bsurprised widenedwink lneutral with fc
    p1 "Um... Cześć!"
    p9 "To ja, Levius. Pamiętasz mnie?"
    #sad_smile Lia ON, Levius smile ON"
    show p1 bsad wink lsmile
    show p9 bneutral wink lsmile
    with fc
    p1 "Oh, tak - oczywiście."
    p9 "Cieszę się! Umm... Co porabiasz?"
    p1 "Huh? Teraz jak widzisz pracuję."
    #sad_smile Levius ON"
    show p9 bsad wink lsmile with fc
    p9 "Oh, no tak. To nie przeszkadzam teraz."
    p9 "Jakbyś miała ochotę później porozmawiać to nie krępuj się proszę."
    #smile Lia ON, Levius smile ON"
    show p1 bneutral wink lsmile
    show p9 bneutral wink lsmile
    with fc
    p1 "Dobrze, będę pamiętać."
    p9 "Dziękuję! Do zobaczenia!"
    #Levius wychodzi z kadru, Lia confused ON i mówi do gracza:"
    hide p9 with moveoutleft
    show p1 bsurprised wink_player lneutral with fc
    p1 "Dziwny dzień. Dziwni ludzie. Wracam do pracy."
    # TODO Lia znika z ekranu, główna sala (ruch ludzi z cieniami może), lekki ruch out zoom z baru na całość, 2-3 sec"
    show ep_img_tavern_mainroom with dissolve
    "Lia wróciła do pracy i w pełni się na niej skupiła."
    #tutaj odpala się przejście na zewnątrz Tawerny i dwie ścieżki są:
    window hide
    with fc
    stop ambient
    stop music
    ################ devstuff #################
    if config.developer:
        menu:
            "dev/ idziemy na festiwal":
                $ d_gofestiwal = True
                pass
            "dev/ nie idziemy nigdzie":
                pass
    #########################################

    if d_gofestiwal:

        #czas upływa o jeden, do popołudnia. Wracamy do sali i ujęcie na Lię za barem i Zorn stoi po lewej też za barem
        show anim_tavern outside dragon with Dissolve(1.2)
        pause 3.5
        hide ep_img_tavern_mainroom
        show p1 wink
        hide anim_tavern outside dragon with Dissolve(1.2)
        show p3 with moveinleft:
            align (.1,1.0)
        window auto
        with fc
        p3 "Hej Lia, jak idzie praca?"
        p1 "Wszystko dobrze."
        p3 "To dobrze. Jeśli chcesz dalej iść na festiwal to mogę Cię już zastąpić."
        p3 "To jak, chcesz iść?"

        menu:
            "Chodźmy na festiwal!":
                #smile Lia ON
                show p1 bneutral wink lsmile with fc
                p1 "Tak! Z chęcią pójdę."
                p3 "No dobrze. Tylko uważaj na siebie."
                p1 "Będę na pewno!"
                p3 "Obiecaj, że będziesz."
                #frown Lia ON"
                show p1 bangry wink lneutral with fc
                p1 "Obiecuję!"
                p3 "No dobrze dobrze. Zmykaj już. Nie wracaj za późno."
                #przejście na zewnątrz Tawerny, przechodzimy do E4
                scene anim_tavern outside dragon with Dissolve(1.2)
                pause 2
            "Lepiej zostań w pracy.":
                #confused Lia ON
                show p1 bsurprised wink lneutral with fc
                p1 "Nie, nie trzeba."
                p1 "Zostanę i jeszcze popracuję."
                p3 "Oh. Hmm, no dobrze. Twoja decyzja."
                #smile Lia ON"
                show p1 bneutral wink lsmile with fc
                p3 "Dzięki, że zostałaś pomagać."
                #Zorn wychodzi, Lia do gracza"
                hide p3 with moveoutleft
                p1 "Zawsze coś w zamian. Chociaż nie jestem do końca przekonana do tej decyzji."
                #sad_smile Lia ON"
                show p1 bsad wink_player lsmile with fc
                p1 "No ale już nic nie zrobimy. Wracam do pracy."
                #efekt wyjścia z tawerny, out zoom od baru do pełnej sali i wyjście na zewnątrz Tawerny, upływ czasu do wieczora"
                #powrót do ujęcia za barem. Pojawia się Zorn po lewej za barem obok Lii"
                show anim_tavern outside dragon with Dissolve(1.2)
                pause 1.2
                show anim_tavern nighttime dragon with Dissolve(2.0)
                pause 1.0
                hide anim_tavern outside dragon
                show p1 bneutral wink lneutral
                hide anim_tavern nighttime dragon with Dissolve(1.0)
                show p3 behind tavern_main_bar_bar1 at zabarem:
                    xalign -0.3
                    linear 1 xalign .2
                pause 1
                p3 "Jak tam?"
                #frown Lia ON"
                show p1 bangry wink lneutral with fc
                p1 "Dobrze."
                p3 "Możesz iść już spać. Ja zamknę Tawernę."
                #sad_smile Lia ON"
                show p1 bsad wink lsmile with fc
                p3 "Jeszcze raz dzięki, że zostałaś pomóc. Dobranoc."
                p1 "Dobranoc."
                #przejście do pokoju Lii, Lia do gracza, relaxed ON"
                scene anim_room_lia_nightdragon
                show p1pl bneutral closed lsmile shadow
                with fade
                p1 "Uh, jestem zmęczona. Pójdę od razu spać."
                #neutral Lia ON"
                show p1pl bneutral wink_player lneutral with fc
                p1 "Dobranoc."
                menu:
                    "Dobranoc.":
                        pass
                #przejście do E5
                jump e5

    else:

        #jeśli nie ma tego punktu
        #czas upływa o dwa, do wieczora, wracamy do ujęcia za barem. Pojawia się Zorn po lewej za barem obok Lii
        show anim_tavern outside dragon with Dissolve(1.2)
        pause 1.2
        show anim_tavern nighttime dragon with Dissolve(2.0)
        pause 1.0
        hide anim_tavern outside dragon
        hide ep_img_tavern_mainroom
        show p1 bneutral wink lneutral
        hide anim_tavern nighttime dragon with Dissolve(1.0)
        show p3 behind tavern_main_bar_bar1 at zabarem:
            xalign -0.3
            linear 1 xalign .2
        pause 1
        window auto
        with fc
        p3 "Jak idzie praca?"
        #frown Lia ON"
        show p1 bangry wink lneutral with fc
        p1 "Idzie dobrze."
        p3 "Mhm. Możesz iść już spać. Ja zamknę. Dobranoc."
        p1 "Eh. Dobranoc."
        #przejście do pokoju Lii, Lia do gracza, relaxed ON"
        scene anim_room_lia_nightdragon
        show p1pl bneutral closed lsmile shadow
        with fade
        p1 "Uh, jestem zmęczona. Pójdę od razu spać."
        #neutral Lia ON"
        show p1pl bneutral wink_player lneutral with fc
        p1 "Dobranoc."
        menu:
            "Dobranoc.":
                pass
        #przejście do E5
        jump e5


################################################################################
##################################    E4     ###################################
################################################################################


label e4:
    scene anim_tavern outside dragon
    #background zewnątrz Tawerny, popołudnie, Lia do gracza, surprised_happy ON
    show p1pl bsurprised widenedwink_player lsmile
    with dissolve
    p1 "Dobra. Tak jak ostatnio, pokażę Ci w ogóle gdzie idziemy."
    show mapka_fhd with dissolve:
        zoom 1.5 xalign 0.59 yalign .14
        ease 2 zoom 2.5
        ease 4 xalign 0.82 yalign .36
        ease 2 zoom 2.3 xalign 0.85 yalign .45
    #otwiera się mapa, zoom na lokację Tawerny i przesunięcie zoomu na wioskę"
    p1 "Idziemy tutaj do wioski, pójdziemy skrótem przez las, nic się nie powinno stać."
    #mapa się zamyka, Lia do gracza, Lia happy ON"
    hide mapka_fhd with dissolve
    show p1pl bneutral narrowedwink_player lsmile with fc
    p1 "Chodźmy!"
    #przejście, upływ czasu +1, backgroung ścieżka przed wioską, Lia do gracza, surprised_neutral ON"
    scene forest_village_dragonevening with fade:
        zoom 0.8 align (0.83,0.85)
    show p1pl bneutral wink_player lneutral with fc
    p1 "Jesteśmy prawie na miejscu. W sumie jak już tu dotarliśmy to nie jestem przekonana do tego pomysłu..."
    menu:
        "Dlaczego?":
            pass
    #sad Lia ON"
    show p1pl bneutral wink_player lsad with fc
    p1 "No bo co ja tu właściwie jestem? Nikogo praktycznie nie znam, bawić też zbytnio się nie lubię..."
    menu:
        "Hmm. Na pewno nie zaszkodzi pójść i zobaczyć co i jak.":
            pass
    #sad_smile Lia ON"
    show p1pl bsad wink_player lsmile with fc
    p1 "Niby tak... To co mam zrobić?"
    menu:
        "Wejdź do wioski, znajdź jakieś piwo i zobaczymy co dalej. Na pewno nie będzie źle.":
            pass
    #relaxed Lia ON"
    show p1pl bneutral closed lsmile with fc
    p1 "Hmm."
    #smile Lia ON"
    show p1pl bneutral wink_player lsmile with fc
    p1 "No dobrze. Ufam Ci, chodźmy."
    #przejście na wioskę, bawiący się ludzie cienie, Lia od prawej do lewej bardzo powoli ‘idzie’, surprised_happy ON
    scene anim_festival_night_dragon:
        align (0.5,0.5)
        pos (-0.4,-0.14)
        zoom 0.9
    show p1 bsurprised widenedwink lsmile:
        zoom 0.8
        align (1.0,1.0)
        linear 10 xalign 0.5
    $ renpy.music.set_volume(0.3, delay=0, channel='music')
    play music peritune_market fadein 3.0
    with fade

    "Lia ruszyła przez wioskę sprawnie unikając bliższego kontaktu z ludźmi."
    "Wolała nie ryzykować potencjalnego wciągnięcia w wir tańca."
    "Wzięła piwo i przystanęła gdzieś na boku."
    #Lia do gracza, neutral ON w tle ciągle wioska"
    show p1 bneutral wink_player lneutral with fc
    p1 "Nie jest tak źle póki co..."
    #surprised_neutral Lia ON"
    show p1 bsurprised widenedwink lneutral with fc
    p1 "Wyjątkowo dobrze widać Zielonego Smoka podczas tego festiwalu."
    menu:
        "Co masz na myśli?":
            pass
    #neutral Lia ON"
    show p1 bneutral wink_player lneutral with fc
    p1 "Hmm. Przeważnie jest słabiej widoczny. Spójrz w górę."
    hide p1 with fc
    show anim_festival_night_dragon with dissolve:
        # align (0.5,0.5) zoom 0.9
        ease 4 pos (-0.4,0.45)

    #Lia znika, kamera przechodzi na niebo skupiając się na smoku (lekki ruch)"
    p1 "Na jego cześć jest cały festiwal."
    p1 "Krąży wokół niego też sporo legend."
    p1 "Chcesz usłyszeć co o tym wiem?"

    menu:
        "Bardzo chętnie!":
            # Lia wraca, jest na boku tak żeby nie zasłaniała smoka i wciąż jakby
            # bliżej ekranu rozmawiając z graczem
            # sad_smile Lia ON
            show p1 bsad wink_player lsmile with fc:
                align (1.0,-0.3) zoom 1.5
            p1 "Zaznaczę od razu, że w sumie to nie wiem za dużo."
            p1 "Pamiętam tylko tyle co opowiadała mi mama..."
            #smile Lia ON"
            show p1 bneutral wink_player lsmile with fc
            p1 "Ale... Po pierwsze smok pojawia się zawsze w różnych odstępach czasowych."
            p1 "Nikt nie wie kiedy dokładnie się pojawi i dlaczego jest to takie losowe."
            p1 "Ostatni festiwal odbywał się jakoś siedem lat temu."
            #blush Lia ON"
            show p1 blush with fc
            p1 "Wcześniejszego nie pamiętam bo byłam zbyt mała..."
            #smile Lia ON"
            show p1 bneutral wink_player lsmile -blush with fc
            p1 "Obecny trwa prawie dwa tygodnie i powoli zbliżamy się do końca."
            p1 "Wracając do samej legendy. Mówi się, że Smok pojawia się w momencie kiedy Królestwo jest zagrożone."
            p1 "Zielony Smok jest jakby strażnikiem naszej wyspy czy coś takiego."
            p1 "Hmm... Co jeszcze."
            p1 "Ah, tak. Mówi się, że jest związany z ogromną wieżą w centrum naszej wyspy. Że właśnie tam mieszka."
            p1 "Nikt jednak tego nie potwierdził bo wstęp ma tam tylko rodzina królewska."
            p1 "Właśnie! Odnośnie rodziny królewskiej!"
            p1 "Słyszałam od gości w Tawernie, że na zakończenie festiwalu księżniczka Aurora i książę Caius przyjadą świętować do naszej wioski."
            p1 "Wszyscy są tym jakoś specjalnie podekscytowani."
            #blush Lia ON"
            show p1 blush with fc
            p1 "W sumie chętnie zobaczę tę księżniczkę, ponoć jest bardzo piękna..."
            #neutral Lia ON"
            show p1 bneutral wink_player lneutral -blush with fc
            p1 "No ale nie jest to teraz ważne."
            p1 "Hmm, to chyba wszystko co wiem."
            p1 "Jak będziemy chcieli to może uda się kiedyś dowiedzieć czegoś więcej od kogoś."
            menu:
                "Dzięki za opowieść.":
                    pass
            #smile Lia ON"
            show p1 bneutral wink_player lsmile with fc
            p1 "Nie ma za co!"

        "Nie, dzięki.":
            #Lia wraca, jest na boku tak żeby nie zasłaniała smoka i wciąż jakby bliżej ekranu rozmawiając z graczem
            #frown Lia ON
            show p1 bangry wink_player lneutral with fc:
                align (1.0,-0.3) zoom 1.5
            p1 "Hmm. Jak chcesz."

    # po tekstach lekki zastój na smoku i powrót na standardowe ujęcie Lii,
    # mówi do gracza, relaxed ON
    hide p1 with fc
    show anim_festival_night_dragon with fc:
        # align (0.5,0.5) zoom 0.9
        ease 4 pos (-0.4,-0.14)
    pause 4
    show p1pl bneutral closed lsmile with fc
    p1 "Hmm. Nie jest tu tak źle..."
    with hpunch
    #efekt zatrzęsienia ekranu, Meamir w nią wpadł"
    hide p1pl with fc
    "Zamyślona Lia prawie się przewróciła po niespodziewanym zderzeniu."
    #zwykły ujęcie, wioska w tle, Lia stoi z boku i przed nią Meamir"
    #Lia shock ON"
    show p1 bsurprised widenedwink lopen:
        align (0.7,1.0)
    show p5:
        align (0.5,1.0) xzoom -1
    with dissolve
    "Odzyskała szybko równowagę i zauważyła przed sobą nieznajomego chłopaka!"
    #Meamir podpisany na początku ‘???’, Meamir surprised_happy ON"
    show p5 bsurprised widenedwink lsmile with fc
    show p5:
        linear 1.0 xalign 0.45
    show p1:
        ease 0.5 xalign 0.75
    p5q "Na Zielonego Smoka! Przepraszam! Nie zauważyłem Cię, czy wszystko w porządku?"
    #Lia surprised_neutral ON"
    show p1 bsurprised widenedwink lneutral with fc
    p1 "Oj, tak... Nic się nie stało. Tylko troszkę się przestraszyłam... i straciłam swoje piwo."
    #Meamir blush ON"
    show p5 blush with fc
    p5q "Ojej, przepraszam raz jeszcze... Rozglądałem się i nie patrzyłem przed siebie."
    "{i}Uroczy.{/i} - pomyślała Lia."
    #happy Lia ON"
    show p1 bneutral narrowedwink lsmile with fc
    p1 "Nic się nie stało! Naprawdę. Sama byłam też zamyślona... Trochę też moja wina."
    p5q "Oh, no dobrze! Ale na wszelki wypadek w ramach przeprosin może dasz się skusić na wspólne piwo?"
    p1 "Hmm... W zasadzie czemu nie. Ale pod jednym warunkiem."
    #Meamir confused ON"
    show p5 bsurprised wink lneutral -blush with fc
    p5q "Jakim?"
    #Lia smirk ON"
    show p1 bangry narrowedwink lsmirk with fc
    p1 "Musisz przynajmniej powiedzieć jak się nazywasz!"
    #Meamir surprised_happy ON"
    #Meamir dostaje normalny podpis"
    show p5 bsurprised widenedwink lsmile with fc
    p5 "Ahh, nie przedstawiłem się. Przepraszam! Jestem Meamir, a Ty?"
    p1 "No nie wiem czy jeszcze na to zasłużyłeś..."
    #Meamir blush ON"
    show p5 blush with fc
    p5 "Oh... No to..."
    #surprised_happy Lia ON"
    show p1 bsurprised widenedwink lsmile with fc
    p1 "Oj no! Żartuję tylko, jestem Lia!"
    p1 "Miło Cię poznać!"
    p5 "Oh. Ciebie też miło poznać Lia!"
    p1 "No no, nie czerwień się tak - chodźmy na to piwo!"
    #Meamir smile ON"
    show p5 -blush bneutral wink lsmile with fc
    p5 "Dobrze, dobrze - chodźmy!"
    # przejście do zoomu na skrzynkę z piwem i stoją naprzeciwko siebie,
    # both smile ON"

    scene anim_festival_night_dragon:
        align (0.5,0.5)
        pos (-0.1,-0.34)
        zoom 1.1
    show festival_skrzynka_night
    # Lia and Meamir smile ON
    show p5 bneutral wink lsmile:
        align (.2,1.0) xzoom -1
    show p1 bneutral wink lsmile:
        align (.8,1.0)
    with fade
    "Dotarli do miejsca z piwem. Meamir nalał dwa pełne kubki. Pierwszy podał Lii."
    p5 "Proszę bardzo, ten dla Ciebie."
    p1 "A dziękuję bardzo."
    #both blush ON"
    show p1 blush
    show p5 blush
    with fc
    "Przez moment wpatrywali się na siebie bez słowa, powoli sącząc swoje trunki."
    "{i}Uroczy jest.{/i} - pomyślała Lia."
    #smile Meamir ON"
    show p5 bneutral wink lsmile -blush with fc
    p5 "Hmm... Jesteś stąd w ogóle?"
    #confused Lia ON"
    show p1 bsurprised wink lneutral with fc
    "{i}Dziwne pytanie.{/i} - pomyślała Lia."
    p1 "Hmm. Nie do końca. Co prawda mieszkam niedaleko, ale nie tutaj we wiosce."
    p5 "A gdzie?"
    p1 "Um... Niedaleko. Przy Tawernie na rozdrożach. Dlaczego pytasz?"
    #surprised_happy Meamir ON"
    show p5 bsurprised widenedwink lsmile with fc
    p5 "Ah, wybacz. Pytam bo dopiero się wprowadziliśmy i poznaję okolicę."
    #smile Lia ON"
    show p1 bneutral wink lsmile with fc
    p1 "Oo, nie wiedziałem, że ktoś jeszcze ma się wprowadzić. Słyszałam tylko o nowym kowalu..."
    #smile Meamir ON"
    show p5 bneutral wink lsmile with fc
    p5 "Hah, to właśnie my. Znaczy dokładnie to mój ojciec."
    #sad_smile Meamir ON"
    show p5 bsad wink lsmile with fc
    p5 "O mnie pewnie nikt nie wspominał, nie jestem na tyle interesujący."
    #smirk Lia ON"
    show p1 bangry narrowedwink lsmirk with fc
    p1 "Oj, nie przesadzaj. Na pewno nie jest tak źle! Zresztą kowal bez swojego pomocnika niewiele zrobi!"
    #blush Meamir ON"
    show p5 blush with fc
    p5 "Oh, pewnie masz rację!"
    #sad_smile Meamir ON"
    show p5 bsad wink lsmile -blush with fc
    p5 "No ale to właśnie stąd moje dziwne pytanie! Ciekaw jestem co jest w okolicy."
    #happy Lia ON"
    show p1 bneutral narrowedwink lsmile with fc
    p1 "Rozumiem! Po prostu byłam lekko zaskoczona takim pytanie."
    p1 "Więc jak na ten moment podoba Ci się to nasze otoczenie?"
    #blush Meamir ON"
    show p5 blush with fc
    p5 "Umm. Na pewno po dzisiejszym wieczorze znacznie bardziej niż wczoraj."
    #blush Lia ON"
    show p1 blush with fc
    p1 "Oh... A to dlaczego? Stało się coś ciekawego?"
    #smirk Meamir ON"
    show p5 bangry narrowedwink lsmile -blush with fc
    p5 "Można tak powiedzieć."
    #confused Lia ON"
    show p1 bsurprised wink lneutral -blush with fc
    p1 "Co masz dokładnie na myśli?"
    #blush Lia ON"
    show p1 blush with fc
    p5 "To że na siebie wpadliśmy!"
    #blush Meamir ON"
    show p5 blush with fc
    p5 "Wiem, że nie brzmi to dobrze... Ale cieszę się z tego naszego zderzenia."
    p5 "Nie wiem co bym tu sam robił, a w takim towarzystwie od razu milej..."
    #smile Lia ON"
    show p1 bneutral wink lsmile -blush with fc
    p1 "Hah, też się cieszę. Sama w sumie też byłam tutaj lekko zagubiona."
    #smile Meamir ON"
    show p5 bneutral wink lsmile -blush with fc
    p5 "No widzisz! Hmm, to może chciałabyś się jeszcze gdzieś przejść?"
    #sad_smile Lia ON"
    show p1 bsad wink lsmile with fc
    p1 "Hmm, wiesz co... Bardzo chętnie, ale robi się już trochę późno. Powinnam wracać"
    #sad Meamir ON"
    show p5 bneutral wink lsad with fc
    p5 "Oj no! Już chcesz uciekać? Przecież jeszcze nie jest tak późno. Zostań jeszcze trochę!"
    p1 "Chciałabym, ale jeszcze muszę wrócić do domu - nie chcę, żeby rodzice się martwili!"
    #sad_smile Meamir ON"
    show p5 bsad wink lsmile with fc
    p5 "Ah, no dobrze - rozumiem... To ostatnie pytanie tylko, co porabiasz na co dzień, pomagasz w tej Tawernie?"
    #surprised_happy Lia ON"
    show p1 bsurprised widenedwink lsmile with fc
    p1 "Hah, tak. A czemu pytasz?"
    #smile Meamir ON"
    show p5 bneutral wink lsmile with fc
    p5 "To w takim razie się może jutro zobaczymy! Mam coś odebrać."
    #smile Lia ON"
    show p1 bneutral wink lsmile with fc
    p1 "Oo, to bardzo fajnie, więc nie ma co się przejmować skoro jutro się zobaczymy!"
    p5 "Może znajdziesz wtedy chwilkę na rozmowę, co?"
    #smirk Lia ON"
    #sad_smile Meamir ON"
    show p1 bangry narrowedwink smirk
    show p5 bsad wink lsmile
    with fc
    p1 "Może może, kto wie. Zobaczymy jutro!"
    p1 "A teraz muszę naprawdę uciekać, papa!"
    #smile Meamir ON"
    show p5 bneutral wink lsmile with fc
    p5 "Dobrze, do zobaczenia!"
    #znikają i out zoom wioski by całość bardziej widać"
    hide p1
    hide p5
    hide festival_skrzynka_night
    with dissolve
    show anim_festival_night_dragon:
        align (0.5,0.5)
        pos (-0.1,-0.34) zoom 1.1
        linear 10 pos (0.1,0.3) zoom 0.65
    with dissolve
    "Lia od razu opuściła wioskę i ruszyła w kierunku Tawerny."
    stop music
    #background Tawerna noc"
    scene img_tavern_mainroom_night with fade
    "W Tawernie nie było słychać już żadnych głosów. Po cichu ruszyła do swojego pokoju, żeby nikogo nie obudzić."
    #background pokój, Lia mówi do gracza, smile ON"
    scene anim_room_lia_nightdragonlight
    show p1pl bneutral wink_player lsmile shadow
    with dissolve
    p1 "Nie sądziłam, że ten dzień będzie w miarę interesujący."
    p1 "Dziękuję za porady! Ciekawa jestem co czeka nas jutro."
    p1 "A teraz do spania! Dobranoc!"
    menu:
        "Dobranoc!":
            pass
    #przejście do E5

################################################################################
##################################    E5     ###################################
################################################################################


label e5:
    #animacja przejścia z nocy w dzień, zewnątrz Tawerny
    #background pokój Lii, rano
    ################ devstuff #################
    if config.developer:
        menu:
            "dev/ bylismy na festiwalu":
                $ d_gofestiwal = True
                pass
            "dev/ nie bylismy na festiwalu":
                $ d_gofestiwal = False
                pass
    #########################################

    scene anim_tavern nighttoday dragon with dissolve
    $ renpy.sound.set_volume(0.5, delay=0, channel='ambient')
    $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
    play ambient sfx_morning_ambience
    pause 6
    $ renpy.music.set_volume(0.5, delay=0, channel='musictight')
    play musictight the_old_tower_inn fadein 1.0
    if d_gofestiwal:
        scene anim_room_lia_noondragon with fade
        "Lia powoli otworzyła oczy i rozejrzała się po pokoju."
        "Zauważyła, że słońce było już wyżej niż zazwyczaj."
        "Szybko się ubrała i wstała."
        #Lia pojawia się na ekranie, do gracza, confused ON"

        show p1pl bsurprised wink_player lneutral with fc
        p1 "Dzień dobry... huh, dziwne..."
        menu:
            "Dzień dobry. Co takiego?":
                pass
        p1 "Zaspałam i nikt nie przyszedł mnie obudzić..."
        p1 "Hmm. No nic. Idę na śniadanie."
        stop ambient
        $ renpy.sound.set_volume(1, delay=0, channel='ambient')
        $ renpy.sound.set_pan(0, delay=0, channel='ambient')
        #bg kuchnia, P1 wchodzi od prawej, mówi do gracza"
        #surprised_sad Lia ON"
        scene room_kitchenmealday with fade
        show p1 with moveinright:
            align (.7,1.0)
        show p1 bsurprised widenedwink_player lsad with fc
        p1 "Oh, widzę, że już po śniadaniu..."
        #smile Lia ON"
        show p1 bneutral wink_player lsmile with fc
        p1 "A nie, jednak coś mi zostawili. Zjem i czas do pracy."
        #przejście do sali, zoom na bar, P1 lewo, P3 prawo"
        scene tavern_main_bar_bg0
        show p3 at zabarem:
            xalign 0.5 xzoom -1
        show tavern_main_bar_bar1
        with fade
        show p1 at zabarem behind tavern_main_bar_bar1 with moveinleft:
            xzoom -1
        p3 "A kto to wstał w końcu."
        #frown Lia ON"
        show p1 bangry wink lneutral with fc
        p1 "Czemu mnie nikt nie obudził..."
        p3 "Pomyśleliśmy, że możesz chcieć odpocząć po wczoraj."
        #blush Lia ON"
        show p1 blush with fc
        p1 "Oh. Dziękuję."
        p3 "Nie ma za co. A teraz możesz pomóc. Stań za barem i przypilnuj Tawerny."
        #sad_smile ON"
        show p1 bsad wink lsmile -blush with fc
        p1 "Dobrze tato."
        show p3 at zabarem:
            linear 1 xalign -0.45
        show p1 at zabarem:
            linear 1 xalign 0.5
        pause 1
        show p1 at zabarem with fc:
            xzoom 1
        pause 0.3
        #Zorn wychodzi, Lia za barem
        hide p3

    else:
        scene anim_room_lia_morningdragon with fade
        "Lię zbudził dźwięk otwieranych drzwi. Otworzyła oczy."
        #od prawej wchodzi Selene"
        show p2 with moveinright:
            align (.7,1.0)
        p2 "Dzień dobry Lia, wstawaj już. Zaraz śniadanie i trzeba tacie pomóc w Tawernie."
        p1 "Uhh... Jeszcze pięć minut..."
        p2 "Wstawaj wstawaj. Śniadanie czeka na Ciebie."
        #P2 wychodzi w prawo"
        show p2 with fc:
            xzoom -1
        pause 0.2
        hide p2 with moveoutright
        "Lia przeciągnęła się ze zmęczeniem, westchnęła i w końcu wstała."
        #Lia na środku, mówi do gracza, frown ON"
        show p1pl bangry wink_player lneutral with fc
        p1 "Dzień dobry... Uh, kolejny dzień przed nami - hurra..."
        menu:
            "Dzień dobry...":
                pass
        p1 "Dobra, idę do kuchni coś zjeść."
        stop ambient
        $ renpy.sound.set_volume(1, delay=0, channel='ambient')
        $ renpy.sound.set_pan(0, delay=0, channel='ambient')

        ##################### Kuchnia ########################
        #bg kuchnia, P2 po lewej, P1 wchodzi od prawej
        #P2 smile ON, P1 neutral
        scene room_kitchenmealday
        show p2 smile:
            align (.3,1.0) xzoom -1
        with fade
        show p1 with moveinright:
            align (.75,1.0)
        p2 "Dzień dobry Lia, jak Ci minęła noc?"
        p1 "Normalnie. Jak miała niby minąć?"
        #sad Selene ON, surprised_sad Lia ON"
        show p2 sad
        show p1 bsurprised widenedwink lsad
        with fc
        p2 "No dobrze, już o nic nie pytam."
        #neutral Selene ON"
        show p2 neutral with fc
        p2 "Zjedz śniadanie i idź pomóż tacie."
        #sad_smile Lia ON"
        show p1 bsad wink lsmile with fc
        p1 "Dobrze..."
        hide p2 with moveoutright
        #Selene wychodzi z kuchni, Lia do gracza"
        show p1 wink_player with fc
        p1 "No dobra. Zjem i idę pracować."
        ######################### bar ###############################

        #przejście do sali, zoom na bar, P1 lewo, P3 prawo"
        scene tavern_main_bar_bg0
        show p3 at zabarem:
            xalign .65 xzoom -1
        show tavern_main_bar_bar1
        with fade
        show p1 behind tavern_main_bar_bar1 at zabarem:
            xalign -0.3 xzoom -1
            linear 1.5 xalign 0.25
        #frown Lia ON"
        show p1 bangry wink lneutral with fc
        p3 "Miło, że w końcu dołączyłaś."
        p1 "Ale..."
        p3 "Dobra, nieważne. Sporo pracy przede mną."
        p3 "Zostań za barem i pilnuj Tawerny, nie powinno być zbyt dużo gości."
        hide p3 with moveoutleft
        pause 1
        #Zorn wychodzi, Lia za barem

    #Lia do gracza, sad_smile ON\
    hide p1
    show p1pl bsad wink_player lsmile
    with fc
    p1 "Czasem przed południem nie jest tak źle... Ruch przeważnie niewielki."
    p1 "Zobaczymy co dzień przyniesie."
    #przejście na zewnątrz Tawerny, przejście czasowe (ptaszki, ruch słońca) i upływ czasu +1, powrót do środka"
    #po wejściu do Tawerny od razu odpala się komiks z kuflami, jest zoom na barze"
    scene anim_tavern outside dragon with fade
    pause 7
    play ambient medieval_tavern_ambience_5min fadein 1.0 fadeout 2.0 volume 0.7
    scene tavern_main_bar_bg0
    show p1 at zabarem:
        xalign .5
    show tavern_main_bar_bar1
    show black with fc
    with fade
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


    p1 "Zamówienie nr. 66 gotowe!"
    hide piwo_1
    hide piwo_2
    hide piwo_3
    with dissolve
    hide black with dissolve
    #pojawia się guest 1, ten elf co ostatnio, podpis Gość po prostu"
    show elf1:
        align (-0.1,-0.5)
        zoom 0.68
    with dissolve
    p1 "Tylko proszę nie wylać jak ostatnio..."
    r1 "Dobrze! Tak się stanie moja Pani!"
    #gość znika,
    hide elf1 with dissolve
    #pojawia się Henrietta"
    show p8 with moveinleft:
        align (0.1,1.0)
    p8 "Cześć Lia. Co tam ciekawego?"
    p1 "Oh, hej Henrietta. Nic szczególnego. Coś podać?"
    p8 "Mhm. Daj butelkę czegoś mocnego, długi dzień przede mną."
    p1 "Hmm."
    # TODO komiks jak będzie work z podaniem butelki jakiejś"
    p1 "To powinno być w porządku, proszę."
    #Henrietta smile ON, Lia blush ON"
    show p8 bneutral wink lsmile
    show p1 blush
    with fc
    p8 "Dzięki Lia. Do zobaczenia później."
    #Lia smile ON"
    show p1 bneutral wink lsmile with fc
    p1 "Do zobaczenia."
    #Hen wychodzi, ujęcie na całą salę, Lia za barem + cienie przechodzących ludzi, ze 2-3 tu i tam"
    hide p8 with moveoutleft
    show p1 -blush with fc
    pause 1
    scene ep_img_tavern_mainroom_nozoom:
        align (0.5,0.5) zoom 1.3
    show p1:
        zoom 0.4 xpos 0.6 yalign 0.65
    show tavern_main_bar3_dn_idle:
        align (0.5,0.5) zoom 1.3
    show anim_festival_walking_shadows:
        zoom .95 ypos 0.3
    with dissolve
    "Goście powoli przewijali się przez Tawernę zajmując całkowicie myśli Lii."

    if d_gofestiwal:
        scene tavern_main_bar_bg0
        show p1 at zabarem:
            xalign .5
        show tavern_main_bar_bar1
        "Lia stała akurat plecami do baru gdy nagle usłyszała znajomy głos."
        p5 "Hej Lia! Dzień dobry!"
        #pojawia się Meamir, smile ON, Lia smile ON"
        show p5 bneutral wink lsmile with moveinright:
            align (1.0,1.0)
        show p1 at zabarem with fc:
            xzoom -1
        show p1 bneutral wink lsmile with fc
        p1 "O, hej Meamir! Dzień dobry!"
        p5 "Jak tam Twój dzień mija?"
        p1 "Standardowo, nic ciekawego się nie dzieje, a Twój?"
        p5 "To samo, nic ciekawego..."
        #blush Lia ON"
        #smirk Meamir ON"
        show p1 blush with fc
        show p5 bangry narrowedwink lsmile with fc
        p5 "Chociaż teraz już jest ciekawiej..."
        p1 "Znów się wygłupiasz!"
        #smile Meamir ON, Lia smile ON"
        show p5 bneutral wink lsmile
        show p1 bneutral wink lsmile
        with fc
        p5 "No dobrze dobrze... Przyszedłem po zamówienie..."

    else:
        scene tavern_main_bar_bg0
        show tavern_main_bar_bar1
        show p1 behind tavern_main_bar_bar1 at zabarem:
            xalign 0.5
        with fade
        "Lia stała akurat plecami do baru gdy usłyszała przyjemny i interesujący głos."
        #podpis Meamira na początek ‘???’"
        #Meamir smile ON, Lia surprised_happy smile ON"

        show p1 bsurprised widenedwink lsmile with fc
        p5q "Dzień dobry! Hej!"
        show p5 bneutral wink lsmile with moveinright:
            align (0.8,1.0)
        #pojawia się Meamir po lewej, Lia wciąż za barem"
        show p1 at zabarem:
            xzoom -1
        p1 "Dzień dobry..."
        #pojawia się imię Meamira w podpisie"
        p5 "Nazywam się Meamir. Przyszedłem po zamówienie mojego taty, znaczy kowala..."
        #Lia smile ON"
        show p1 bneutral wink lsmile with fc
        p1 "Oh, musisz chyba chwilkę poczekać, mój tata spodziewał się Ciebie później..."
        #sad_smile Meamir ON"
        show p5 bsad wink lsmile with fc
        p5 "Ah, rozumiem..."
        #confused Lia ON"
        show p1 bsurprised wink lneutral with fc
        p1 "..."
        p5 "..."
        p5 "Przepraszam, że pytam... Ale czy mógłbym poznać Twoje imię?"
        #sad_smile Lia ON"
        show p1 bsad wink lsmile with fc
        p1 "Oh, przepraszam - nazywam się Lia. Powinnam się przedstawić od razu..."
        #smile Meamir ON"
        show p5 bneutral wink lsmile with fc
        p5 "Nie nie, nic się nie stało! Bardzo miło Cię poznać, śliczne imię!"
        #blush Lia ON"
        show p1 blush with fc
        p1 "Dziękuję!"
        p5 "Przyjemność po..."


    #bar zoom, P1 za barem, P5 przed barem po prawej, P3 za barem bardziej po lewej stronie
    #Lia confused ON, Meamir sad_smile ON
    show p3 behind tavern_main_bar_bar1 at zabarem with moveinleft:
        align (0.1,1.0)
    show p1 bsurprised wink lneutral -blush with fc
    show p5 bsad wink lsmile with fc
    p3 "A co tu się dzieje młodzieży? Co to za rozmowy w pracy Lia?"
    show p1 at zabarem with fc:
        xzoom 1
    p1 "Um..."
    p3 "Ty jesteś Meamir, tak?"
    p5 "Tak, to ja..."
    p3 "Miałeś być później."
    #Meamir confused ON"
    show p5 bsurprised wink lneutral with fc
    p5 "Ah, tak to prawda. Ale udało mi się wcześniej wyrobić z obowiązkami..."
    p3 "Hmm, no dobrze. Zaraz przygotuję wszystko. Poczekaj chwilę..."
    #tutaj taki efekt zrobić, że Zorn się odwraca od nich, ale od razu zawraca"
    show p3 at zabarem:
        linear 0.1 xzoom -1
        linear 2 xalign 0.0
        linear 0.1 xzoom 1
    p3 "Tylko grzecznie mi tutaj. Zaraz wrócę."
    show p3 at zabarem:
        linear 3 xalign -0.4
    pause 2
    show p1 at zabarem with fc:
        xzoom -1
    show p1 bsurprised widenedwink lneutral with fc
    show p5 blush with fc
    #surprised_neutral Lia ON, Meamir blush ON
    #Zorn wychodzi w lewo


    if d_gofestiwal:
        #sad_smile Lia ON, smile Meamir ON
        show p1 bsad wink lsmile with fc
        show p5 bneutral wink lsmile with fc
        p5 "Hmm..."
        p5 "Wczoraj było bardzo przyjemnie na festiwalu!"
        #blush Lia ON"
        show p1 blush with fc
        p1 "To prawda!"
        p5 "Może dziś też chciałabyś gdzieś wyjść? Na przykład na spacer wieczorem?"
        p1 "Oh, właściwie czemu..."


    else:
        #confused Lia ON, Meamir blush ON
        show p1 bsurprised wink lneutral with fc
        show p5 blush with fc
        p5 "Um... Pomagasz codziennie w Tawernie?"
        #smile Lia ON"
        show p1 bneutral wink lsmile with fc
        "{i}Całkiem uroczy.{/i} - pomyślała Lia."
        p1 "Tak, pomagam tutaj - w zasadzie to moje główne zajęcie."
        #smile Meamir ON"
        show p5 bneutral wink lsmile with fc
        p5 "Od dawna tu mieszkasz?"
        #surprised_neutral Lia ON"
        show p1 bsurprised widenedwink lneutral with fc
        p1 "Całe życie w zasadzie... Dlaczego pytasz?"
        #sad_smile Meamir ON"
        show p5 bsad wink lsmile with fc
        p5 "Ah, wybacz. Wprowadziliśmy się dopiero, więc chciałbym się zorientować w nowej okolicy."
        p5 "Mam nadzieję, że nie zabrzmiało to strasznie źle..."
        #Lia smile ON, Meamir smile ON"
        show p1 bneutral wink lsmile with fc
        show p5 bneutral wink lsmile with fc
        p1 "Nie! Bez obaw, tak tylko zapytałam."
        p5 "Ah, to dobrze. A coś jeszcze robisz na co dzień?"
        #sad_smile Lia ON"
        show p1 bsad wink lsmile with fc
        p1 "Huh. Nie, niezbyt. Głównie pracuję, muszę pomagać rodzicom przy Tawernie."
        #surprised_happy Lia ON"
        show p1 bsurprised widenedwink lsmile with fc
        p5 "Hmm, to tak sobie myślę. Może zechciałabyś wyjść ze mną na spacer? Pokazać okolicę czy coś..."
        #surprised_happy Meamir ON"
        show p5 bsurprised widenedwink lsmile with fc
        p1 "Oj, hmm, teraz ciężko mi powiedzieć, ale w sumie czemu..."

    #dźwięk przerażającego KRZYKU
    #równo z krzykiem pojawia się Zorn i jego dialog
    hide p3
    stop musictight
    stop ambient
    $ renpy.music.set_volume(0.1, delay=0, channel='audio')
    $ renpy.music.set_pan(0.8, delay=0, channel='audio')
    play audio sfx_female_scream
    show p3 with moveinleft:
        align (0.1,1.0)
    show p1 -blush widenedwink bsurprised lneutral with fc
    show p5 -blush widenedwink bsurprised lneutral with fc
    p3 "Co tam się dzieje na zewnątrz?!"
    #angry Zorn activated
    show p3 angry with fc
    p3 "Muszę to sprawdzić."
    $ renpy.music.set_pan(0.5, delay=0, channel='audio')
    #przejście do E6



################################################################################
##################################    E6     ###################################
################################################################################


label e6:
    scene anim_tavern outside dragon
    show angry_man1:
        align (.01,1.0) xzoom -1
    show angry_man2:
        align (.25,1.0) xzoom -1
    show p4 bsurprised widenedwink lsad:
        align (.6,1.0)
        xzoom -1.0
    with fade
    #zewnątrz Tawerny, południe, 2 bandziorów po lewej, P4 po prawej, surprised_sad Raven ON
    play music alexander_nakarada_the_great_battle fadein 3.0 fadeout 10.0 volume 0.5
    "Wyglądało na to, że jacyś mężczyźni próbowali osaczyć bezbronną dziewczynę."
    #od prawej wjeżdża Zorn, angry ON"
    show p3 angry:
        xzoom -1.0
        align (1.4,1.0)
    show p3:
        linear 1.1 align (.9,1.0)
    p3 "Halo, co tu się dzieje? Co to ma znaczyć!?"
    "Na widok Zorna nieznajomi odruchowo spojrzeli się po sobie."
    "Nie wyglądali jednak na takich co dobrowolnie będą się tłumaczyć."
    b1 "Nie Twój interes elfie, wracaj do swoich spraw. Ta dziewczyna należy do nas!"
    p3 "Należy do Was?! Ganiając za tą biedną dziewczyną musieliście chyba mocno przemęczyć Wasze móżdżki."
    p3 "Osoba nie może być Waszą własnością, radzę..."
    b2 "Ja radzę zamknąć ten Twój niewyparzony ryj i nie wtrącać się do nie swoich spraw kolego."
    b1 "Dokładnie, siedź tam cicho, a my zabieramy dziewczynę..."
    "Jeden z nich ruszył powoli w kierunku dziewczyny wyciągając rękę by ją złapać."
    "Nagle czas jakby się dla niego zatrzymał..."
    #tutaj zaczynamy schemat bójki, elementy różne bez zmian"
    with vpunch
    scene zorntheangel 1 at tr_beatupbyzorn
    show anim_beatupblink
    with dissolve
    "Obcy nie był w stanie w pierwszej chwili zrozumieć co się stało."
    "Czuł ogromny ból głowy oraz pleców, przez lekko otwarte powieki widział promienie słoneczne..."
    "Dosłownie jakby leżał... W uszach strasznie mu dzwoniło. Po paru sekundach usłyszał tylko przerażający krzyk swojego kompana."
    show zorntheangel 2 at tr_beatupbyzorn
    with dissolve
    b2 "Kurwwaaaaa, mój noooos... zabijęęęę Cięęę! Auaaaaa....."
    "Krzyk zagłuszył od razu dźwięk upadającego worka ziemniaków o ziemię... A może to wcale nie był worek..."
    show zorntheangel 3 at tr_beatupbyzorn
    with dissolve
    #bez podpisu Zorna tekst Zorna jedna linijka niżej"
    p3 "Powoli bo się bardziej połamiesz."
    "Wstawał bardzo powoli. Dokładnie tak jak zasugerował głos."
    "Zresztą nie miał innego wyboru. Miał chyba złamane ze dwa żebra, nie... trzy."
    "Wstał."
    scene black
    pause 0.5
    #jeden bandyta na nogach, drugi leży, Zorn stoi blisko tego stojącego, Raven z tyłu"
    scene anim_tavern outside dragon
    show p3:
        xzoom -1
        align (.37,1.0)
    show p4 bsurprised widenedwink lsad:
        xzoom -1
        align (.7,1.0)
    with dissolve
    show angry_man2 with zoomin:
        align (.1,1.0)
    show angry_man2:
        linear .3 align (.01,1.0)
    p3 "A teraz słuchaj bardzo uważnie. Nie będę się powtarzał."
    p3 "Istnieje duża szansa, że nie wiesz, iż w naszym królestwie nie możesz kogoś sobie sobie posiadać."
    p3 "Nie możesz ot tak powiedzieć, że ktoś jest Twoją własnością!"
    p3 "A już w ogóle nie możesz tego robić przy mojej Tawernie!"
    stop music fadeout 15.0
    #Zorn obraca się w prawo"
    show p3 with fc:
        xzoom 1.0
    p3 "Lia!"
    #Lia pojawia się od prawej, shock Lia ON"
    show p1 bsurprised widenedwink lopen behind p4:
        align (1.3,1.0)
        ease 1 align (.85,1.0)
    p3 "Zabierz ją do środka - zaraz przyjdę."
    #Zorn obraca się do bandziorów, Lia i Raven wychodzą na prawo"
    show p3 with fc:
        xzoom -1.0
    show p1:
        linear .03 xzoom -1.0
        linear 1 align (1.35,1.0)
    show p4:
        linear .03 xzoom 1.0
        linear 1.2 align (1.35,1.0)
    p3 "A Was jeśli tutaj zobaczę raz jeszcze to skończycie znacznie gorzej."
    p3 "Radzę teraz się zebrać, przemyśleć swoje życie i najlepiej zacząć od nowa."
    p3 "A teraz bierz swojego kolegę i won mi stąd."

    #ładne przejście do kuchni, Raven po lewej, Lia po prawej, Raven confused ON, Lia confused ON"
    scene room_kitchenday with fade
    show p1 bsurprised wink lneutral with moveinleft:
        align (.4,1.0)
    show p4 bsurprised wink lneutral with moveinleft:
        align (0.01,1.0)
    $ renpy.music.set_volume(0.5, delay=2, channel='music')
    play music [alexander_nakarada_emotionalism, alexander_nakarada_emotionalism, "<silence 1000.0>"] fadein 10.0
    p1 "Hej... Jak masz na imię?"
    #sad_smile Lia ON"
    show p1 bsad wink lsmile with fc
    p1 "Wszystko w porządku?"
    #blush Raven ON"
    show p4 blush with fc
    p4 "Nazywam się Raven... I tak, wszystko dobrze. Dziękuję..."
    #blush Lia ON"
    show p1 blush with fc
    p4 "Um, a Ty jak się nazywasz?"
    #Lia smile ON, Raven sad_smile ON"
    show p1 bneutral wink lsmile
    show p4 bsad wink lsmile
    with fc
    p1 "Mam na imię Lia, miło Cię poznać Raven!"
    show p1 -blush
    show p4 -blush
    with fc
    p1 "Co się stało? Jak tu trafiłaś?"
    #Raven sad ON"
    show p4 bneutral wink lsad with fc
    p4 "Ja.. Ja nie wiem, uciekałam i..."
    #Zorn wchodzi po prawej, both girls confused ON"
    show p3 with moveinright:
        align (1.0,1.0) xzoom -1
    show p1 bsurprised wink lneutral
    show p4 bsurprised wink lneutral
    with fc
    p3 "Załatwione. Tamtymi nie musisz się już martwić, więcej nie powinniśmy ich zobaczyć."
    p3 "W ogóle wszystko dobrze? Nie jesteś ranna czy coś? Hmm, dziewczyno?"
    p3 "Halo, dziewczyno.. Mówię do..."
    #P2 wchodzi od prawej, Lia niech dołączy po lewej do Raven 2on2, Selene smile ON"
    show p2 with moveinright:
        align (.7,1.0)
    show p3 with move:
        xalign .99
    show p1 with move:
        xalign .3
    p2 "Zorn! Nie widzisz, że jest wystraszona?"
    show p2 smile with fc
    p2 "Ja się tym zajmę. Idź proszę sprawdzić czy nie ma Cię w głównej sali."
    #P3 wychodzi w prawo"
    hide p3 with moveoutright
    "Zorn popatrzył się na żonę, ale się nie sprzeciwił tylko grzecznie wyszedł sprawdzić czy na pewno nie ma go w tej sali."
    p2 "Podejdź tu i pokaż mi się, zranili Cię gdzieś?"
    #Raven sad ON + zbliża się do Selene jakoś na środku się ogarniają"
    show p1 with move:
        xalign .02
    show p4 bneutral wink lsad with move:
        xalign .35
    show p1 with fc:
        xzoom -1
    p4 "Niee proszę Pani... Nie zdążyli..."
    p2 "Już wszystko dobrze, nie smuć się. Nazywam się Selene, a Ty?"
    p4 "Ra... Raven."
    #Raven blush ON"
    show p4 blush with fc
    p2 "Piękne imię! Widzę, że wszystko rzeczywiście jest w porządku."
    p2 "No już, nic Ci już nie grozi - widzę, że jesteś wykończona. Chciałabyś odpocząć?"
    #surprised_happy Raven ON"
    show p4 -blush bsurprised widenedwink lsmile with fc
    "Raven nie wiedziała za bardzo co powiedzieć, pierwszy raz spotykała się z takim podejściem do niej."
    p2 "Dobrze, zakładam, że tak."
    p2 "Lia, weź ją proszę do pokoju gościnnego. Pokaż jej co i gdzie i daj jej odpocząć, dobrze?"
    p1 "Dobrze mamo. Chodź Raven."
    "Obie dziewczyny ruszyły na górę, Raven podążała spokojnie za Lią"


    #Pokój Raven, P1 wchodzi pierwsza od prawej do lewej, P4 za nią"
    #sad_smile Lia ON, confused Raven ON"
    scene room_raven_evening_empty with fade
    show p1 bsad wink lsmile with moveinright:
        align (.3, 1.0) xzoom -1
    show p4 bsurprised wink lneutral with moveinright:
        align (.7, 1.0) xzoom -1
    p1 "To jest ten pokój. Możesz tutaj sobie spokojnie odpocząć. Potrzebujesz jeszcze czegoś?"
    p4 "Nie, dziękuję. Jeśli mogę to bym się chyba zdrzemnęła..."
    p1 "Ah, oczywiście - już nie przeszkadzam. Jakbyś czegoś potrzebowała to wołaj, mam pokój naprzeciwko."
    #blush Raven ON, Lia smile ON"
    show p1 bneutral wink lsmile
    show p4 blush
    with fc
    p4 "Dziękuję."
    #Pokój P1, Zorn po lewej, Lia wchodzi od prawej, Lia confused ON"
    scene anim_room_lia_eveningdragon
    show p3:
        align (.3, 1.0)
    with fade
    show p1 with moveinright:
        align (.7, 1.0)
    p1 "Hej tato, o co chodzi?"
    p3 "Hmm? O nic! Chciałem tylko przyjść i sprawdzić czy wszystko dobrze."
    p1 "Tak, wszystko w porządku - Raven poszła się zdrzemnąć..."
    #surprised_happy Lia ON"
    show p1 bsurprised widenedwink lsmile with fc
    p3 "Pytałem bardziej o Ciebie."
    p1 "Oh... Wszystko dobrze, czemu miałoby coś być?"
    p3 "Widziałaś przecież co zrobiłem tym bandytom..."
    #smile Lia ON"
    show p1 bneutral wink lsmile with fc
    p1 "Oni sobie zasłużyli! Poza tym nie byłam zaskoczona - nie wyglądali na zbyt godnych przeciwników..."
    p3 "Hę? Widzę Wam kobietkom dziś w humorze dokuczanie mi... No nic, ważne, że wszystko dobrze."
    #Zorn wychodzi powoli na prawo, Lia przechodzi na lewo"
    show p3 with move:
        xalign 1.0
    show p1 with move:
        xalign .4
    show p1 with fc:
        xzoom -1
    p3 "Mało godni przeciwnicy? To jacy byliby godni?"
    hide p3 with easeoutright
    "Powiedział pod nosem tata po czym wyszedł z pokoju. Lia została chwilowo sama."


######################## E6A

    #Lia na ekranie, mówi do gracza, thinking ON
    hide p1
    show p1pl bangry closed lneutral
    with fc
    p1 "Huh... Co teraz..."
    menu:
        "Już myślałem, że nie zapytasz.":
            pass
    #surprised_neutral Lia ON"
    show p1pl bsurprised widenedwink_player lneutral with fc
    p1 "Hmm? Oh! To Ty... Przepraszam, zamyśliłam się i zapomniałam o Tobie troszkę..."
    menu:
        "Auć. Czyli nie potrzebujesz porady?":
            pass
    #sad_smile Lia ON"
    show p1pl bsad wink_player lsmile with fc
    p1 "Wybacz! Dużo się właśnie wydarzyło... I właściwie to tak! Przydałaby mi się porada."
    menu:
        "Nie ma problemu! Po to tu jestem! Co potrzebujesz?":
            pass
    p1 "Ojeju... Tyle się dzisiaj działo, że ciężko wszystko sobie poukładać..."
    menu:
        "Spróbuj! Na pewno dasz radę.":
            pass
    #smile Lia ON"
    show p1pl bneutral wink_player lsmile with fc
    p1 "Mam pomysł! Daj mi chwilkę."
    hide p1pl
    #Lia znika na sekundę, pojawia się komiks z Lią przy biurku piszącą (folder Others E6A comics)"
    show black
    with fc
    show e6a with dissolve
    "Lia usiadła na moment przy swoim biurku i otworzyła dziennik."
    "..."

    p1 "Dobra, gotowe! Zobacz."

    #otwiera się dziennik i rozpoczynamy mini poradnik"
    $ jrnl_aina_about = jrnl_aina_about_n01
    $ jrnl_henrietta_about = jrnl_henrietta_about_n01
    $ jrnl_levius_about = jrnl_levius_about_n01
    if d_gofestiwal:
        $ jrnl_meamir_about = jrnl_meamir_about_n01_fest
    else:
        $ jrnl_meamir_about = jrnl_meamir_about_n01_nofest
    $ jrnl_raven_about = jrnl_raven_about_n01

    $ jrnl_aina_todo_1 = jrnl_aina_todo_n01
    $ jrnl_henrietta_todo_1 = jrnl_henrietta_todo_n01
    $ jrnl_levius_todo_1 = jrnl_levius_todo_n01
    $ jrnl_meamir_todo_1 = jrnl_meamir_todo_n01
    $ jrnl_raven_todo_1 = jrnl_raven_todo_n01

    $ jrnl_important_1 = jrnl_important_n01

    show tutorial_base with dissolve
    hide e6a
    hide black
    p1 "Zrobiłam taki dziennik. Mogę tutaj wszystko zapisywać i dać go Tobie do przejrzenia."
    p1 "Teraz samodzielnie możesz sprawdzić co i jak i pomóc mi podjąć decyzję."
    p1 "Przeprowadzić Cię dokładnie po wszystkim?"

    menu:
        "Koniecznie! Pokaż co i jak.":
            p1 "No dobrze! No to po kolei."

            #tutaj zrobimy taki obrazkowy poradnik, z podświetleniami fragmentów i podpisami co jest co"
            #podświetlenie imion"
            show tutorial_bookmarks with fc
            p1 "Tutaj mamy imiona osób, które znam i ostatnie rzeczy z nimi związane."
            #podświetlenie lewej strony notatek"
            hide tutorial_bookmarks
            show tutorial_notes
            with fc
            p1 "W tym miejscu znajdziesz właśnie te ostatnie informacje i moje notatki."
            #podświetlenie najważniejszych celów"
            hide tutorial_notes
            show tutorial_important
            with fc
            p1 "O, a tutaj będę zaznaczać najważniejsze rzeczy do zrobienia - żeby nie zapomnieć."
            #podświetlenie opcjonalnych celów"
            hide tutorial_important
            show tutorial_optional
            with fc
            p1 "Takie mniej ważne będę wpisywać w tym miejscu."
            #standardowa ikona wyłączenia dziennika"
            hide tutorial_optional

            # show tutorial_help
            # with fc
            # p1 "Jeśli będziesz chciał, żeby wszystko Ci przypomnieć to kliknij tutaj."
            # #podświetlenie znaku zapytania
            # hide tutorial_help

            show tutorial_exit
            with fc
            p1 "Jak skończysz to tutaj możesz zamknąć dziennik."
            hide tutorial_exit
            with fc
            #cały dziennik otwarty"
            p1 "No dobra. To chyba wszystko. Sprawdź co i jak i daj mi znać jak skończysz."
            hide tutorial_base
            show screen journal_bookmark6
            with Dissolve(0.1)
            #kontrola nad dziennikiem witam, DZIENNIK N01
            #zwykła opcja wyłączenia dziennika teraz jest OFF


        "Nie trzeba, jakoś się zorientuję - daj mi chwilkę.":
            show tutorial_exit
            with fc
            p1 "Tylko zaznaczę, że tutaj możesz zamknąć dziennik."
            hide tutorial_exit
            with fc
            p1 "No dobrze, to zobacz co i jak i daj znać jak skończysz."
            hide tutorial_base
            show screen journal_bookmark6
            with Dissolve(0.1)
            #kontrola nad dziennikiem witam, DZIENNIK N01
            #zwykła opcja wyłączenia dziennika teraz jest OFF
            #w tej wersji trzeba dodać, że jak się kliknie ikonę rozmowy to wyskoczy ostrzeżenie pt. ‘Na pewno to już wszystko?’ i to wyjątek z takim ostrzeżeniem tylko do tej decyzji


    #po kliknięciu w ikonę rozmowy zamyka się dziennik i Lia pojawia się z nami rozmawiając, smile Lia ON
    show p1pl wink_player
    p1 "I jak? Co byś mi doradził teraz?"


    stop music
    menu:
        "Myślę, że warto sprawdzić co u Raven.":
            #surprised_happy Lia ON
            show p1pl bsurprised widenedwink_player lsmile with fc
            p1 "Możesz mieć rację..."
            #sad_smile Lia ON"
            show p1pl bsad wink_player lsmile with fc
            p1 "Wydawała się dość przybita."
            p1 "Poczekam chwilę. Niech się zdrzemnie i odpocznie."
            p1 "Później do niej pójdę."
            #Lia znika, sam pokój"
            hide p1pl with dissolve
            pause .2
            show anim_room_lia_goldenhourdragon with Dissolve(1.5)
            # TODO upływ czasu +1"
            #Lia wraca i do gracza, Lia smile ON"
            pause .7
            show p1pl bneutral wink_player lsmile with fc
            p1 "No dobra, już czas."
            #przejście do E7-P4
            jump epizod7p4

        "Może pójdź do wioski spotkać się z Meamirem.":
            #surprised_happy Lia ON
            show p1pl bsurprised widenedwink_player lsmile with fc
            p1 "Możesz mieć rację..."
            #sad Lia ON"
            show p1pl bneutral wink_player lsad with fc
            p1 "Trochę bez słowa go zostawiłam..."
            #thinking Lia ON"
            show p1pl bangry closed lneutral with fc
            p1 "Poza tym zapraszał na spacer. Może z nim pójdę w ramach przeprosin."
            #smile Lia ON"
            show p1pl bneutral wink_player lsmile with fc
            p1 "Dobra, zrobię tak. Pójdę od razu."
            "Jak powiedziała tak zrobiła. Wyszła z Tawerny i ruszyła w kierunku wioski."
            #przejście do E7-P5
            jump epizod7p5

        "Dużo się dziś wydarzyło. Może po prostu połóż się wcześniej spać.":
            #surprised_sad Lia ON
            show p1pl bsurprised widenedwink_player lsad with fc
            p1 "Możesz mieć rację..."
            #more_sad Lia ON"
            show p1pl bneutral narrowedwink_player lsad with fc
            p1 "W sumie rzeczywiście jestem zmęczona."
            #disappointed Lia ON"
            show p1pl bsad closed lsad with fc
            p1 "Dobra, ogarnę się i idę spać. Dobranoc."
            hide p1pl with fc
            #Lia znika, taki efekt upływającego czasu za oknem, aż do rana
            #przejście do E7-N
            jump epizod7n


################################################################################
#############################   EPIZOD 7-P4   ##################################
label epizod7p4:
    if config.developer:
        scene black
        show text "epizod7p4" at truecenter
        pause
    # Na ekranie: Pokój Raven, z lewej Raven
    $ akt1_UkonczenieEpizodow["e7_p4"] = True
    $ RavenLove += 1
    $ LovePath += 1
    scene room_raven_evening_empty
    show p4:
        align (.3, 1.0)
    with fade
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music alexander_nakarada_adventure fadein 7.0
    "Lia zapukała lekko w drzwi. Po krótkiej ciszy usłyszała spokojny głos:"
    p4 "Proszę, otwarte!"
    # Na ekranie: P1 wchodzi od prawej, powolutku się przesuwa bardzooo
    show p1:
        align (1.3, 1.0)
        ease 6 xalign .84
    "Stawiając powolne i niepewne kroki, Lia weszła do pokoju."
    p1 "Heej! Pomyślałam, że może nie chcesz być teraz sama..."
    "Powiedziała to prawie łamiącym się głosem. Liczyła na jakąś reakcję ze strony Raven."
    "Ta jednak się nie pojawiła. Na twarzy Raven pojawił się za to lekki uśmiech."
    # Raven smile ON
    show p4 lsmile with fc
    "Lia się lekko zawahała."
    p1 "Oczywiście jeśli nie chcesz to mogę sobie pójść..."
    p4 "Nie, nie! Zostań, proszę."
    # Lia smile ON
    show p4 lsmile with fc
    "Powiedziała szybko Raven."
    p4 "Przepraszam, że tak wyszło tak oschle. To wszystko jest dla mnie trochę nowe..."
    p1 "Co dokładnie?"
    p4 "To..."
    "Powiedziała Raven rozglądając się najpierw po pomieszczeniu, na końcu skupiając wzrok na Lii."
    # Lia neutral ON
    show p1 -lsmile with fc
    "Lia nie do końca zrozumiała. Jej mina mówiła chyba wystarczająco, gdyż Raven zaczęła od razu tłumaczyć."
    p4 "Ah. Bo wiesz... nie przywykłam do osób, które w pierwszej kolejności są pomocne i miłe..."
    p4 "Dla mnie to coś naprawdę nowego. Trochę ciężko mi to wyjaśnić... ale, jeśli chcesz..."
    p1 "Poproszę. Opowiedz mi."
    "Odpowiedziała Lia, sama zaskoczona dawką pewności we własnym głosie."
    "Ciekawość była jednak znacznie większa. Miała wrażenie, że mogła w końcu spotkać kogoś z kim dzieli ją znacznie więcej niż na pierwszy rzut oka może się wydawać."
    # Raven neutral ON
    show p4 -lsmile with fc
    p4 "Dobrze. To może usiądź... nie wiadomo ile to potrwa."
    "Lia wiedziała, że nie ma w pokoju dodatkowych krzeseł. Raven była tego świadoma i od razu zrobiła jej miejsce na łóżku."
    p4 "No dobrze... od czego by tu zacząć? Pomyślmy."
    "Raven zamyślona spoglądała w dal."
    "Lia wykorzystała ten moment, żeby się jej przyjrzeć..."
    "Pomyślała, że wygląda naprawdę uroczo i... i atrakcyjnie."
    "Lia poczuła coś czego jeszcze nigdy chyba nie czuła. Nie była w stanie dokładnie określić co to za uczucie..."
    "Z myśli wyrwała ją Raven - najwidoczniej zebrała już własne."
    p4 "To może od początku - gdy miałam kilka lat, nie pamiętam już dokładnie ile, przygarnęła mnie grupa cyrkowców..."
    p1 "Jak to przygarnęła?"
    p4 "Moi rodzice... w zasadzie nie wiem kim dokładnie byli. Nawet ich nie pamiętam."
    p4 "No zresztą nieważne. Byłam mała. Trochę się błąkałam i mnie przygarnęli."
    p4 "Niewiele pamiętam. Kazali mi początkowo występować w jakichś prostych numerach... musiałam zapracować na jedzenie i dach nad głową."
    p4 "Czasem zrobiłam coś źle i musiałam spać na zewnątrz. Dlatego też dużo ćwiczyłam."
    p4 "Głównie akrobacje... jeśli to też Cię interesuje. I tak mijały lata."
    p4 "Raz było lepiej, raz było gorzej. Czym dalej jednak, tym gorzej."
    "Raven westchnęła lekko wstając z łóżka."
    "Przystanęła na moment, wciągnęła powietrze i znów zaczęła:"
    p4 "Zdarzyło się nawet, że podnosili na mnie rękę jak coś im nie pasowało."
    p4 "W zasadzie nawet jak wszystko było ok to potrzebowali się wyżyć."
    p4 "Wystarczyło, że biznes szedł trochę gorzej... zawsze byłam pierwszą do ukarania."
    p4 "Ciężko się dziwić, że szło słabo. Coraz bardziej skupiali się na wyciąganiu złota od biednych, a nie na występach."
    p4 "Żeby uniknąć kar jeździliśmy głównie po mniejszych wioskach, z dala od jakiejkolwiek straży czy rycerzy."
    p4 "No ale w końcu chciwość zwyciężyła i ruszyliśmy w bardziej zaludnione miejsca."
    p4 "Pomyślałam, że to idealny i zapewne ostatni moment na ucieczkę. "
    p4 "Więc uciekłam... trzęsąc się ze strachu, że tym razem może nie skończyć się tylko na kilku ciosach..."
    "Powiedziała, po czym lekko złapała się za ramiona niechcący przywołując niechciane wspomnienia."
    p1 "Przykro mi to słyszeć... naprawdę przykro..."
    "Powiedziała smutnym głosem Lia i obserwowała jak Raven zmierza powoli w kierunku okna."
    p4 "Na szczęście się udało. Twój tata uratował mi życie. Wolę nie myśleć co by się stało gdyby nie jego reakcja... inni bali się mi pomóc..."
    # Na ekranie: CG Raven otwierająca okno pyk
    scene black with fade
    "Otworzyła szeroko okno i głęboko wciągnęła potwierze."
    scene raven_window_clear with Dissolve(2.0)
    p4 "Ale wracając... na szczęście się udało. I przepraszam, że opowiadam w tak wielkim skrócie, ale... ale niekoniecznie chcę wracać do szczegółów..."
    p1 "Nie ma problemu, rozumiem. Nie musisz opowiadać nic więcej jeśli nie chcesz..."
    "Powiedziała Lia jednocześnie podchodząc powoli do Raven."
    p4 "Dzięki za zrozumienie... ehh, nawet nie wiem co będzie ze mną dalej..."
    # TODO Na ekranie: CG Raven siedząca na parapecie (sama)
    "Powiedziała, po czym nakładając jednocześnie pelerynkę usiadła na parapecie."
    "Lia chwilę zastanawiała się co powiedzieć, po czym podeszła i usiadła obok Raven."
    # TODO Na ekranie: CG Raven i Lia na parapecie razem siedzące
    p1 "Na początek możesz zostać tutaj. Będziesz tu bezpieczna!"
    p4 "Eh, i co dalej? Jak długo mam tu zostać? Co potem? Nic teraz nie wiem..."
    p4 "Zresztą to chyba zależy przede wszystkim od Twoich rodziców. Skąd wiesz, że pozwolą mi zostać dłużej?"
    p1 "Nie zostawią Cię bez pomocy. Będzie dobrze, zobaczysz!"
    p4 "A Ty?"
    p1 "Ja? Nie mam tu zbyt wiele do powiedzenia..."
    p4 "Nie... chodzi mi o to czy Ty też... w sensie.. czy Ty też mnie nie zostawisz?"
    "Lia wyczuła lekkie napięcie w powietrzu oraz drżenie w głosie Raven. Nie była pewna odpowiedzi:"
    p1 "Oczywiście, że nie! Bardzo chciałabym, żebyś została - na pewno powiem o tym rodzicom!"
    p1 "To przykre, że spotkały Cię takie rzeczy... spróbuję zrobić co w moich siłach, żeby było Ci tu dobrze."
    "Raven spojrzała Lii prosto w oczy, przysuwając powoli dłoń w kierunku jej dłoni"
    # TODO Na ekranie: CG Raven i Lia na parapecie razem siedzące i dłońmi się łączące
    "Zmrużyła lekko oczy. Położyła lekko swoją dłoń na dłoni Lii i powiedziała bardzo cichym i spokojnym głosem:"
    p4 "Dziękuję. Przy Tobie czuję się jakoś lepiej... zupełnie jakbym..."
    p1 "Jakbyś co?"
    # TODO Raven smile ON
    p4 "Jakbym miała nadzieję. Dziękuję Ci za to..."
    p1 "Cieszę się, że moja obecność nie jest całkiem bezwartościowa..."
    p4 "Oczywiście, że nie jest głuptasie! Czemu tak mówisz?"
    "Lia lekko się zawahała. Zaczęła po drobnej pauzie:"
    p1 "Oh, po prostu nikt mi tak jeszcze nie powiedział..."
    p1 "To dla mnie coś całkowicie nowego. Przepraszam jeśli to źle zabrzmiało..."
    p4 "Nie, nie - przecież nic się nie stało. Może teraz Ty opowiesz coś o sobie?"
    p1 "Myślę, że mogę... Od czego by tu zaczą..."
    "Nagle zza drzwi rozległ się dźwięk pukania i głos Selene:"
    p2 "Hej, Dziewczyny - można wejść?"
    p1 "Jasne Mamo!"
    # Na ekranie: Ujęcie na pokój, Lia i Raven po lewej, po prawej wchodzi (powoli w miarę) P2
    scene room_raven_evening_empty
    show p1:
        align (.3, 1.0)
    show p4:
        align (.05, 1.0)
    with fade
    show p2 with moveinright:
        align (.85, 1.0)
    "Dziewczyny szybko zeskoczyły z parapetu."
    show p1:
        xzoom -1.0
    p2 "Robi się już późno, a po dzisiejszych \"atrakcjach\" Raven na pewno chciałaby odpocząć."
    p2 "No już, chodź Lia! Porozmawiamy wszyscy przy śniadaniu i zobaczymy co dalej. Może być?"
    show p1 with fc:
        xzoom 1.0
    p1 "No dobrze... dobranoc Raven!"
    p4 "Dobranoc Lia i... i dziękuję."
    # Na ekranie: Lia wychodzi, Raven lewo i Selene po prawej
    show p1 with fc:
        xzoom -1
    hide p1 with easeoutright
    p2 "Potrzebujesz czegoś jeszcze czy wszystko w porządku?"
    p4 "Tak, wszystko dobrze - bardzo Pani dziękuję."
    p2 "Oj, nie musisz - tutaj nic Ci nie grozi. Możesz spokojnie iść spać i zobaczymy się rano na śniadaniu, dobrze?"
    p4 "Oczywiście, dziękuję jeszcze raz..."
    p2 "Przyjemność po naszej stronie! A teraz dobranoc, śpij dobrze!"
    p4 "Dobranoc!"
    # Na ekranie: Korytarz, po prawej Lia, po lewej pojawia się Selene"
    scene bg tavern 0:
        zoom 1.5
    show p1:
        align (.85, 1.0)
    with fade
    show p2 with moveinleft:
        align (.25, 1.0) xzoom -1
    p2 "Ładnie to tak podsłuchiwać, co?"
    #Lia blush ON
    show p1 blush with fc
    p1 "Ja.. Ja tylko bardzo powoli wracałam do pokoju!"
    p2 "Haha, tak tak. No dobrze, nic się przecież nie stało. No już, marsz do pokoju! Zobaczymy się rano, dobranoc!"
    p1 "Dobranoc Mamo!"
    hide p1 with moveoutright
    # Na ekranie: Pokój P1, Lia na środku
    scene anim_room_lia_goldenhour
    show p1
    with fade
    "Lia weszła na swojego pokoju, zamknęła drzwi i przystanęła na środku jakby niespodziewanie nawiedziła ją jakaś myśl."
    # Na ekranie: Pokój P1, Lia na środku - zoom zwraca się do gracza
    hide p1
    show lia wink_player:
        align (0.5,0.0)
    with fc
    p1 "Oh, przepraszam, że rozmawialiśmy dziś tak mało. Strasznie pokręcony dzień..."
    menu:
        "Nic się nie stało. Bardzo dobrze sobie poradziłaś!":
            pass
    p1 "Dziękuję! Za radę także... myślę, że wybrałam bardzo dobrze!"
    menu:
        "Dobrze, że się zapytałaś i co najważniejsze... że udało się pomóc!":
            pass
    p1 "Oh, nie czuję zmęczenia. Chyba teraz w ogóle nie zasnę."
    menu:
        "Bez przesady, trochę dziś się nabiegałaś! Położysz się i wkrótce zaśniesz, zobaczysz...":
            pass
    p1 "Ah, pewnie masz rację. Zresztą, jak zwykle! To się kładę, dobranoc!"
    menu:
        "Dobranoc, śpij dobrze.":
            pass
    "Lia nie tylko zasnęła bardzo szybko, ale także z uśmiechem na twarzy."
    "Nie zdarzyło się to od bardzo dawna..."
    # Na ekranie: jakoś przejście, że noc mija - może Tawerna od zewnątrz, może coś w pokoju?
    scene anim_room_lia_goldenhour with dissolve
    pause 1
    show anim_room_lia_nightdragonlight with Dissolve(2.0)
    pause 1
    show anim_room_lia_nightdragon with Dissolve(2.0)
    pause 2
    show anim_room_lia_morning with Dissolve(2.0)
    "Lia obudziła się jeszcze nim promienie słoneczne dosięgły jej okna. Była pełna energii."
    "Pierwszy raz od dawna nie mogła doczekać się śniadania i zbliżającej się rozmowy."
    jump ee000

################################################################################
#############################   EPIZOD 7-P5   ##################################
label epizod7p5:
    #if config.developer:
    #    scene black
    #    show text "epizod7p5" at truecenter
    #    pause
    # Na ekranie: Las, przed wieczorkiem - ścieżka
    $ akt1_UkonczenieEpizodow["e7_p5"] = True
    scene forest_day:
        align (.5,.5) zoom .5
    with fade
    "Lia obeszła Tawernę i ruszyła w kierunku ścieżki."
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music alexander_nakarada_now_we_ride fadein 5.0
    "Po drodze zastanawiała się nad tym, co właściwie będą robić."
    "Wchodząc do lasu stwierdziła jednak, że nie ma to znaczenia - czas coś po prostu zrobić."
    # Na ekranie: Wioska - szerokie ujęcie bez postaci
    scene anim_festival_day_dragon with fade:
        align (0.0,0.0) zoom .5
    show p5 at left:
        zoom 0.5
        xzoom -1
    "Lia dotarła do Wioski. Pamiętała, że Meamir mieszka razem z ojcem przy kuźni."
    show anim_festival_day_dragon:
        linear 2 zoom 1.0 pos (0.0,-0.8)
    show p5 at left:
        linear 2 zoom 1.0
    "Poprawiła lekko włosy i ruszyła w odpowiednim kierunku."


    # Na ekranie: Wioska - Zoom na kuźnię, Meamir stoi po lewej i Lia tak jakby wchodzi od prawej


    $ MeamirLove +=1

    "Gdy dotarła pod kuźnię to zauważyła, że Meamir już na nią czekał. \"Ciekawe jak długo?\" - pomyślała."
    show p1 with moveinright:
        align (.7,1.0)
    # Meamir smile ON
    show p5 lsmile with fc:
        zoom 1.0
    p5 "Cześć Lia!"
    p1 "Hej Meamir!"
    show p5 with move:
        align (.3,1.0)
    p5 "Ciekaw byłem czy przyjdziesz. Cieszę się, że jesteś!"
    # Lia smile ON
    show p1 lsmile with fc
    p1 "Jestem jestem! Mam nadzieję, że Twoja ciekawość została zaspokojona..."
    p5 "No powiedzmy... tak na dobry początek."
    # Lia smirk ON
    show p1 bangry narrowedwink lsmile with fc
    p1 "Oho, a czego chciałbyś się jeszcze dowiedzieć?"
    # Meamir smirk ON
    show p5 bangry narrowedwink lsmile with fc
    p5 "Ah, wiesz - trochę tego i tamtego. Na pewno kryje się w Tobie jeszcze wiele interesujących rzeczy!"
    # Lia blush ON
    show p1 blush with fc
    p1 "No nie wiem... chyba nie ma we mnie nic ciekawego."
    # Meamir smile ON
    show p5 bneutral wink lsmile with fc
    p5 "Coś na pewno znajdziemy, jeszcze zobaczysz!"
    # Lia smile ON
    show p1 -bangry wink lsmile -blush with fc
    p5 "No ale to później, teraz powiedz co chciałabyś porobić!"
    p1 "Myślałam, że masz jakiś fajny plan!"
    p5 "Haha, to prawda - jakiś plan mam. Ale czy fajny to się jeszcze okaże!"
    # Lia smirk ON
    show p1 bangry narrowedwink lsmile with fc
    p1 "To zdradź mi szczegóły i zobaczmy!"
    # Meamir neutral ON
    show p5 bneutral lneutral with fc
    p5 "No dobrze... pomyślałem, że moglibyśmy pójść na spacer. Widziałem ładną ścieżkę niedaleko głównej drogi..."
    # Lia smile ON
    show p1 -bangry wink lsmile with fc
    p1 "Ah, masz pewnie na myśli polanę Ivana. W sumie dawno tam nie byłam..."
    # Meamir smile ON
    show p5 lsmile with fc
    p5 "Hah, możliwe, że właśnie tak się nazywa. To co o tym myślisz?"
    p1 "Bardzo dobry pomysł! Możesz w takim razie prowadzić - zobaczymy czy znasz już trochę okolicę!"
    p5 "No dobrze, to chodźmy!"
    # Na ekranie: Łąka Ivana
    # Opis ekranu: Tu mogą postacie zniknąć powoli, odjechać może widok powoli na całą wioskę i przejście w las Ivanowy wskoczyć,
    # a następnie oni sobie mogą wejść z jednej strony razem i stanąć na środku na normalną rozmowę.
    # W miarę możliwości może lekko niech się przesuwa ten las, tzn od lewej do prawej w trakcie rozmowy, żeby na zoomie było wszystko
    hide p1 with moveoutright
    hide p5 with moveoutright
    show anim_festival_day_dragon:
        linear 5 align (0.0,0.0) zoom .5
    pause 5
    # Na ekranie: Łąka Ivana
    scene anim_forest_justforest2 with fade:
        align (0.0,1.0) pos (0.0, 0.0)
        linear 120 xpos -1.0
    show p5 with moveinleft:
        align (.7,1.0)
    show p1 with moveinleft:
        align (.4,1.0) xzoom -1

    p1 "No, dotarliśmy. Tu jest początek - chciałeś iść w jakieś konkretne miejsce?"
    p5 "Hmm, myślałem żeby po prostu się przejść i porozmawiać. Tak wiesz, przed siebie!"
    p1 "Oh. W zasadzie, czemu nie..."
    # Lia neutral ON
    show p1 lneutral wink bneutral with fc
    # Meamir neutral ON
    show p5 bneutral wink lneutral with fc
    "Ruszyli przed siebie. Na początku w lekko niezręcznej ciszy, którą pierwszy postanowił przerwać Meamir."
    p5 "W zasadzie skąd wzięła się nazwa tego miejsca?"
    p1 "Ah, nie jestem dokładnie pewna. Nigdy nie zwracałam uwagi na takie historie."
    # Meamir sad ON
    show p5 lsad with fc
    p5 "Oh..."
    # Meamir smile ON
    show p5 lsmile with fc
    p1 "Ale! Wiem tyle, że Ivan był ponoć bardzo dobrym krasnoludem."
    # Meamir neutral ON
    show p5 bneutral wink lneutral with fc
    p5 "W jakim sensie dobrym?"
    p1 "W takim, że pomagał innym. Jeśli coś komuś się zepsuło to szedł i naprawił. Jeśli ktoś potrzebował pomocy w naprawie dachu to szedł i to zrobił."
    p1 "Nigdy nie chciał niczego w zamian. Dlatego po jego śmierci nazwano to miejsce na jego cześć."
    p5 "Ojej, to w sumie piękne - chciałbym żeby kiedyś ktoś tak mnie wspominał..."
    # Meamir blush ON
    show p5 blush with fc
    # Lia smile ON
    show p1 lsmile with fc
    p1 "Oho, no proszę - ładne marzenie!"
    p5 "Oj, tak tylko mi się powiedziało! Byłoby po prostu miło..."
    # Meamir smirk ON
    show p5 bangry narrowedwink lsmile with fc
    # Lia blush ON
    show p1 blush with fc
    p5 "Poza tym mówiłaś, że nie zwracasz uwagi na takie historie... a tutaj w zasadzie wiem już prawie wszystko!"
    p1 "Jakie wszystko? Zapamiętałam tylko kilka szczegółów!"
    p5 "I przekazałaś te najważniejsze! Chyba jednak zwróciłaś trochę uwagę na tę historię!"
    p1 "Może ciut..."
    # Lia smirk ON
    show p1 -blush bangry narrowedwink lsmile with fc
    p1 "Poza tym skąd wiesz, że najważniejsze... hmm?"
    # Meamir smile ON
    show p5 bneutral wink lsmile with fc
    p5 "Zwróć uwagę, że wskazałaś na najistotniejsze elementy."
    # Lia smile ON
    show p1 -bangry wink lsmile with fc
    p1 "Czyli jakie dokładnie?"
    p5 "Powiedziałaś, że był dobry. Po prostu... był dobrą osobą - czy to nie jest najistotniejsze?"
    "Lia na chwilę się zamyśliła. Spojrzała na Meamira z zaciekawieniem i pewną fascynacją."
    p1 "Chyba masz rację. Nie pomyślałam, że to może być najistotniejsze."
    p5 "Czasem najbardziej oczywiste rzeczy są tymi, które najczęściej omijamy."
    p5 "Nie ma czym się przejmować. Idziemy dalej?"
    p1 "Tak, chodźmy!"
    "Lia wskazała ścieżkę idącą w kierunku niewielkiego lasu przy drodze."
    "Przez chwilę szli w ciszy, obserwując uważnie każdy otaczający ich szczegół."
    "Tym razem ciszę postanowiła przerwać Lia."


    ########################### devstuff #########################
    if config.developer:
        menu:
            "dev/ bylismy na festiwalu":
                $ d_gofestiwal = True
                pass
            "dev/ nie bylismy na festiwalu":
                pass

    ########################### devstuff #########################


    ############################ [ if d_gofestiwal ##############################
    if d_gofestiwal:
        p1 "W ogóle... jak Ci się podobało na festiwalu?"
        # Meamir neutral ON
        show p5 bneutral wink lneutral with fc
        p5 "Hmm? Słucham?"
        "Zapytał lekko wybity ze swoich myśli Meamir."
        p1 "Pytałam jak Ci się podobał festiwal. W zasadzie jak się podoba, bo pewnie jeszcze chwilę potrwa."
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Ah, przepraszam - zamyśliłem się. Co do festiwalu... "
        p5 "Tak szczerze takie imprezy nie są zbytnio w moim stylu, ale finalnie całość muszę ocenić bardzo pozytywnie."
        p1 "A to dlaczego?"
        # Meamir blush ON
        show p5 blush with fc
        # Lia blush ON
        show p1 blush -lsmile with fc
        p5 "No jak to dlaczego? Spotkaliśmy się! Dzięki temu cały festiwal w moich oczach stał się wyśmienitym wydarzeniem!"
        p1 "Oj, nie wygłupiaj się. Na pewno byłby wyśmienity i beze mnie..."
        # Meamir smirk ON
        show p5 bangry narrowedwink lsmile with fc
        p5 "No nie wiem... myślę, że to jednak Twoja zasługa!"
        # Meamir neutral ON
        show p5 bneutral wink lneutral with fc
        # Lia smile ON
        show p1 -blush with fc
        p1 "Oh, no dobrze... a co myślisz o samym festiwalu?"
        p5 "W jakim sensie?"
        p1 "W takim ogólnym, co myślisz. Mówisz, że takie imprezy nie są dla Ciebie, ale jednak jest to duża część naszej kultury..."
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Ah, no tak. Hmm. Na pewno jest w tym czasie ślicznie. Nieczęsto całe niebo jest takie zielone."
        p5 "I tak sobie myślę, że w sumie chyba nawet polubiłem ten Festiwal."
        p1 "Dlaczego? "
        # Lia blush ON
        show p1 bneutral wink blush with fc
        p5 "Hmm... można na przykład poznać tam urocze osoby!"
        # Lia smirk ON
        show p1 bangry narrowedwink lsmile with fc
        p1 "Tak? Pierwsze słyszę. Chyba byliśmy na różnych festiwalach..."
        # Meamir sad ON
        show p5 lsad with fc
        p5 "Oh... Bo..."
    ############################ /if d_gofestiwal ] #############################

    ############################ bez festiwalu #############################
    else:
        p1 "Byłeś na festiwalu?"
        # Meamir neutral ON
        show p5 bneutral wink lneutral with fc
        p5 "Hmm? Słucham?"
        "Wyglądał na wybitego ze swoich myśli."
        p1 "Pytałam czy byłeś już na festiwalu."
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Ah, przepraszam - zamyśliłem się."
        p5 "Co do festiwalu... To tak, byłem."
        p5 "Ale powiem Ci szczerze, nie jest to chyba rodzaj wydarzenia dla mnie."
        p5 "Nie miałbym tam co robić..."
        # Meamir blush ON
        show p5 blush with fc
        p5 "Chyba, że..."
        #Lia smirk ON
        show p1 bangry narrowedwink lsmile with fc
        p1 "Chyba, że co?"
        # Lia blush ON
        show p1 blush with fc
        p5 "Chyba, że też byś tam była!"
        p1 "Oj, nie wygłupiaj się! Nie mogło być aż tak źle..."
        # Meamir smirk ON
        show p5 bneutral narrowedwink lsmile with fc
        p5 "Jednak myślę, że z Tobą byłoby znacznie ciekawiej!"
        # Meamir neutral ON
        show p5 bneutral wink lneutral with fc
        # Lia smile ON
        show p1 lsmile with fc
        p1 "Oh, no dobrze... A co myślisz o samym festiwalu?"
        p5 "W jakim sensie?"
        p1 "Mówisz, że takie imprezy nie dla Ciebie, ale no jednak jest to duża część naszej kultury..."
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Ah, no tak. Hmm. Na pewno jest w tym czasie ślicznie, nieczęsto całe niebo jest takie zielone."
        p5 "No ale mimo wszystko, żeby w pełni się tym nacieszyć potrzeba czegoś więcej..."
        p1 "Na przykład czego?"
        # Meamir blush ON
        show p5 blush with fc
        p5 "Nie czego, a kogo..."
        # Meamir sad ON
        show p5 lsad -blush with fc
        # Lia smirk ON
        show p1 bangry narrowedwink lsmile with fc
        p1 "Hmm, nie mam pojęcia o co może Ci chodzić..."
        p1 "Dziwne rzeczy opowiadasz!"
        p5 "Oh... Bo myślałem..."

    # Meamir smile ON
    show p5 lsmile with fc
    p1 "Oj no, przecież żartuję. Miałeś przestać się wygłupiać! Teraz musisz mnie odprowadzić - aż do domu!"
    p5 "Ahh... trochę się przez Ciebie zmieszałem..."
    # Lia smile ON
    show p1 bneutral wink lsmile with fc
    p1 "Haha, taki był cel! Chodźmy powoli w drugą stronę... nie chcemy po nocy tułać się po lasku."
    p5 "No dobrze, dobrze. Idziemy do Tawerny?"
    p1 "Dokładnie tak, chodź - nie stój jak słup!"
    "Meamir od razu ruszył w kierunku wskazanym przez Lię."
    # TODO Na ekranie: Tu by się przydało takie ujęcie na łąkę Ivana, żeby nie było widać lasu
    # lub jakaś ścieżka po prostu by się przydała. Pomyśleć trzeba
    "Wracali głównie w ciszy, czasem wymieniając spostrzeżenia na temat mijanych obiektów."
    "Lia była radosna. Nie czuła takiej swobody od dawna i bardzo ją to cieszyło."
    "Ale teraz skupiła się na drodze - powoli zbliżali się do Tawerny."
    # Na ekranie: Tawerna wieczór, P1 lewo i P5 prawo
    scene anim_tavern nighttime dragon
    show p5 lsmile with moveinleft:
        align (.7,1.0)
    show p1 lsmile with moveinleft:
        align (.4,1.0) xzoom -1
    "Gdy dotarli, z wewnątrz usłyszeli odgłosy przekrzykujących się gości."
    # Meamir blush ON
    show p5 blush with fc
    p1 "No dobrze, jesteśmy. Dziękuję za spacer i za odprowadzenie. Było naprawdę miło!"
    p5 "Ja też dziękuję! Cieszę się, że przyszłaś i że udało nam się miło spędzić czas."
    p5 "Hmm... a czy zasłużyłem może na przytulasa na pożegnanie?"
    # Lia blush ON
    show p1 blush with fc

    menu:
        "Przytul go!":
            p1 "No powiedzmy... powiedzmy, że zasłużyłeś."
            # TODO Na ekranie: Hug, jeśli nie będzie CG no to trudno
            show black
            show e7p5c1 with dissolve
            pause 1
            show e7p5c2 with dissolve
            "Lia z lekkim stresem postanowiła lekko przytulić Meamira na pożegnanie."
            "\"To całkiem przyjemne!\" - pomyślała Lia i wzmocniła lekko swój uścisk."
            "Meamir odwzajemnił się z podobnym zaangażowaniem."
            "Po chwili odsunęli się od siebie. Lia pożegnała się pierwsza:"
            hide black
            hide e7p5c1
            hide e7p5c2
            with dissolve
            show p5 blush
            p1 "To do zobaczenia, papa i dziękuję za spacer!"
            p5 "Ja też dziękuję - do zobaczenia! Dobranoc!"
            p1 "Dobranoc!"

        "Za wcześnie na takie rzeczy.":
            #confused Lia ON
            #sad Meamir ON
            show p1 bsurprised wink lneutral
            show p5 bneutral wink lsad
            with fc
            p1 "No nie wiem… Może następnym razem."
            p5 "Oh, no dobrze..."
            #sad_smile Lia ON
            show p1 bsad wink lsmile -blush with fc
            p1 "Ale i tak dziękuję za spacer. Było naprawdę miło!"
            #sad_smile Meamir ON
            show p5 bsad wink lsmile with fc
            p5 "Oh… Cieszę się!"
            #smile Meamir ON
            show p5 bneutral wink lsmile with fc
            p5 "I też dziękuję!"
            #happy Lia ON
            show p1 bneutral narrowedwink lsmile with fc
            p1 "Muszę już uciekać, do zobaczenia później! Dobranoc!  "
            p5 "Dobranoc!"






    "Lia pomachała jeszcze na pożegnanie Meamirowi, po czym ruszyła w kierunku swojego pokoju."
    # Na ekranie: Pokój P1, Lia (neutral) na środku
    scene anim_room_lia_evening
    show p1pl
    with fade
    "Lia weszła do swojego pokoju, zamknęła drzwi i przystanęła na środku jakby niespodziewanie nawiedziła ją jakaś myśl."
    # Na ekranie: Pokój P1, Lia (sad) na środku - zoom zwraca się do gracza
    show p1pl lsad wink_player with fc
    p1 "Oh, przepraszam, że rozmawialiśmy dziś tak mało. Strasznie pokręcony dzień..."
    menu:
        "Nic się nie stało. Bardzo dobrze sobie poradziłaś!":
            pass
    # Lia smile ON
    show p1pl lsmile with fc
    p1 "Dziękuję! Za radę także... myślę, że wybrałam bardzo dobrze!"
    menu:
        "Dobrze, że się zapytałaś i co najważniejsze... że udało się pomóc!":
            pass
    p1 "Oh, nie czuję zmęczenia. Chyba teraz w ogóle nie zasnę."
    menu:
        "Bez przesady, trochę dziś się nabiegałaś! Położysz się i wkrótce zaśniesz, zobaczysz...":
            pass
    p1 "Ah, pewnie masz rację. Zresztą, jak zwykle! To się kładę, dobranoc!"
    menu:
        "Dobranoc, śpij dobrze.":
            pass
    "Lia nie tylko zasnęła bardzo szybko, ale także z uśmiechem na twarzy."
    "Nie zdarzyło się to od bardzo dawna..."
    # Na ekranie: jakoś przejście, że noc mija - może Tawerna od zewnątrz, może coś w pokoju?
    hide p1pl with fc
    scene anim_room_lia_goldenhour with dissolve
    pause 1
    show anim_room_lia_nightdragonlight with Dissolve(2.0)
    pause 1
    show anim_room_lia_nightdragon with Dissolve(2.0)
    pause 2
    show anim_room_lia_morning with Dissolve(2.0)
    "Lia obudziła się jeszcze nim promienie słoneczne dosięgły jej okna. Była pełna energii."
    "Pierwszy raz od dawna nie mogła doczekać się śniadania i zbliżającej się rozmowy."
    jump ee000

################################################################################
#############################   EPIZOD 7-N   ###################################
label epizod7n:
    if config.developer:
        scene black
        show text "epizod7n" at truecenter
        pause
    # Na ekranie: zewnątrz Tawerny, noc w dzień pyk animowane takie ładne
    $ akt1_UkonczenieEpizodow["e7_n"] = True
    scene anim_room_lia_goldenhour with dissolve
    pause 1
    show anim_room_lia_nightdragonlight with Dissolve(2.0)
    pause 1
    show anim_room_lia_nightdragon with Dissolve(2.0)
    pause 2
    show anim_room_lia_morning with Dissolve(2.0)
    # Na ekranie: Pokój P1
    scene anim_room_lia_morning
    "Lia przebudziła się dość wcześnie, wyjątkowo wypoczęta."
    "Wczorajsza decyzja o wczesnym pójściu spać najwidoczniej już się opłaciła."
    "Usiadła na łóżku. Przeciągając się bezgłośnie, była ciekawa zbliżającego się śniadania."
    jump ee000













################################################################################
#################################    BE01     ##################################
################################################################################

label be01:
    "bado endingo"
    "zawroc wedrowcze"
