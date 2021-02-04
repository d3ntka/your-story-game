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
define p8 = Character("Henrietta", color="#bb7949")
define p9 = Character("Levius", color="#465a78")
define p10 = Character("Ove", color="#646464")
define p11 = Character(_("Strażnik"), color="#60c090")
define p12 = Character(_("Strażnik"), color="#7d9999")
define p13 = Character(_("Architekt"), color="#1b7523")
define p16 = Character("Cirdan", color="#9b7e79")
define p16q = Character("???", color="#9b7e79")


#define p14 = Character(_("Babcia"), color="d0cbcb") #"Grandma" w tłumaczeniu
#define p15 = Character("Aurora", color="fbf49d")

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


######### cechy
default c_destiny = False
default c_hal = False
default c_nothing = False
default c_ciekawosc = False
default c_lenistwo = False
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


default persistent.updatetest201007_1 = True  # przy persistent zmieniać datę i if'a niżej w label splashscreen

label splashscreen:
    call screen splash
    if persistent.updatetest201007_1: #aktualizowac date przy nowym update
        call screen nowosci
        $ persistent.updatetest201007_1 = False #aktualizowac date przy nowym update
    return

# JEDZIEMY Z TYM KOKSEM
label start:
################################################################################
########################## przeskok do gry własciwej ###########################
    stop music
    if config.developer:
        jump devskroty
    else:
        jump epizod1
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
        textbutton "epizod 1" action Jump("epizod1")
        textbutton "epizod 2-poz" action [SetVariable("d_e1_senmarzen", True), Jump("epizod2")]
        textbutton "epizod 2-neutr" action [SetVariable("d_e1_senneutral", True), Jump("epizod2")]
        null

        textbutton "epizod 3-nolie" action [SetVariable("d_krotkienogiklamstwa", 0), Jump("epizod3")]
        textbutton "epizod 3-lie1" action [SetVariable("d_krotkienogiklamstwa", 1), Jump("epizod3")]
        textbutton "epizod 3-lie2" action [SetVariable("d_krotkienogiklamstwa", 1), Jump("epizod3")]
        textbutton "epizod 3b" action [SetVariable("d_koszmar", True), Jump("epizod3b")]

        textbutton "epizod 4" action [SetVariable("d_gofestiwal", True), Jump("epizod4")]
        textbutton "ep 4 piwo" action [SetVariable("d_gofestiwal", True), Jump("ep4piwo")]
        textbutton "epizod 5" action Jump("epizod5")
        textbutton "epizod 5+P5" action [SetVariable("d_gofestiwal", True), Jump("epizod5")]

        textbutton "epizod 6" action Jump("epizod6")
        null
        null
        null

        textbutton "epizod 7 P4" action Jump("epizod7p4")
        textbutton "epizod 7 P5" action Jump("epizod7p5")
        textbutton "epizod 7 N" action Jump("epizod7n")
        null

        textbutton "epizod 8" action Jump("epizod8")
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
label epizod1:

    ######################## napis demo #######################
    show screen demo
    screen demo():
        zorder 99
        if ee == 0:
            add "demo_version"
        elif ee >= 0:
            add "demo_version_ee"
    ###########################################################

    jump e1



    # Scena w tawernie, bohaterka obsluguje gosci i zastanawia sie co zrobic z reszta dnia
    # Wybor powoduje przejscie do POKOJU lub na SPACER

    # Epizod 1 Ujecie 1 Tawerna
    # Bohaterka zastanawia sie co zrobic z reszta wolnego dnia

    #scene black
    #scene anim_cg_tavern_wall1

    #scene cg_tavern_wall with Dissolve(2.0):
    #    linear 40 zoom 1.05
    #    pause 0.1
    #    linear 40 zoom 1.0
    #    repeat
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
    play sound sfx_ambient_people_doors fadein 1.0 fadeout 3.0 # TODO do poprawki mimo wszystko
    play ambient sfx_ambient_fire fadein 1.0 fadeout 3.0
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music nowhere_land fadein 5.0
    pause 1.0
    "Harmider ciągnący się za opuszczającymi powoli Tawernę gośćmi w końcu zmieniał się w utęskniony spokój."
    "Lia zamknęła drzwi za ostatnim gościem i oparła się o ścianę, zmęczona całym dniem. Ciszę zakłócał jedynie trzaskający w kominku ogień."

    #"She leaned tiredly against the wall, listening to the silence disturbed only by the crackling embers in the fireplace."
    "..."
    window hide
    pause 2.0
    window show
    stop ambient fadeout 2.0
    "Po kilku dłuższych chwilach dźwięk ustał. Martwą ciszę przerwało głośne westchnięcie."

    p1 "Ehh, mam już {b}dość{/b}. Kolejny bezsensowny dzień w tej durnej pracy..."
    p1 "Ah, zrobiłabym coś ze sobą, ale nawet nie wiem co."
    p1 "Dlaczego życie musi być takie trudne i skomplikowane?"
    p1 "Mogłabym pójść na spacer, ale z drugiej strony jutro ciężki dzień. Mam swoje obowiązki!"
    p1 "Nie dam rady wstać i znów zmuszą mnie do dodatkowej pracy. Do kitu to wszystko!"

    scene tavern_door_lia_eyesopened:
        zoom 1.05
        pause 1
        linear 40 zoom 1.0
        linear 40 zoom 1.05
        repeat
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
    with Dissolve(1.0)
    p1 "Ehh, może Ty mi powiesz co powinnam zrobić, co?"
    window hide
    menu:
        "Musisz złamać rutynę. Chodźmy na spacer!":
            stop music fadeout 3.0
            gr "Musisz złamać rutynę. Chodźmy na spacer!"
            p1 "Masz rację, chodźmy!"
            jump e1u1a

        "Lepiej idź spać.":
            gr "Lepiej idź spać. Jeśli będziesz jutro nieżywa to rodzice znów każą Ci więcej pracować i nigdzie więcej nie wyjdziesz!"
            p1 "Faktycznie, lepiej się wyspać. Idę do pokoju."
            jump e1u1b

#########################  Epizod 1 Ujecie 1B POKOJ  ###########################
label e1u1b:
    scene anim_room_lia_nightdragonlight     # TODO podmienić szkic na final
    with fade
    show p1 shadow
    $ c_lenistwo = True
    "Obrażona na cały otaczający świat, Lia ruszyła w stronę swojego pokoju."
    "Pokonała liczne (a przynajmniej tak sądziła) stopnie schodów."
    play audio sfx_drzwi
    "Dotarła do swojego pokoju i zatrzasnęła za sobą drzwi. Wydały one huk głośniejszy niż się tego spodziewała."
    "Na krótką chwilę zawładnął nią strach, że kogoś obudziła."
    "Po chwili niewzburzona niczym cisza przegoniła strach i przywróciła w jej oczach błysk nienawiści do świata."
    "Lia usiadła na łóżku, spojrzała w Twoją stronę i powiedziała:"
    show p1 lsad bangry narrowedwink_player with fc
    p1 "Nienawidzę ich wszystkich...  Wolałabym mieć inne życie..."
    p1 "Ahhh."
    show anim_room_lia_nightdragon behind p1 with dissolve
    show p1 wink_player lneutral with dissolve
    stop music fadeout 3.0
    p1 "Dobranoc."
    #hide p1
    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music [darren_curtis_the_old_pumpkin_patch, darren_curtis_the_old_pumpkin_patch, "<silence 1000.0>"] fadein 5.0
    scene black with dissolve
    pause 1

    # A1 E1 U2B Koszmar
    # Po tym ujęciu przenosimy się do E3U1B
    # old forest w nocy z tym ziomkiem i pochodnią, zoomujący się na ziomka i nagle znikający i chwilka czarnego ekranu
    $ quick_menu = False
    #scene sen_forest_night_man with fade
    play ambient sfx_hallow_wind
    call screen sen_koszmar
    image sen_forest_night_man:
        contains:
            "anim_forest_night_sen"
            #zoom 0.5 #anchor (0.0,0.0)
            #linear 5
            zoom 0.8

            ease 8 zoom 1.1 pos (-1.05,-0.4)
            #linear 3 zoom 1.4 pos (-1.02,-0.4)
        contains:
            "dreams_border"
            zoom 0.5
        time 14.0
        "black"
    screen sen_koszmar():
        image "sen_forest_night_man"
        timer 15.0 action Jump("pokoszmarze")

label pokoszmarze:
    stop ambient
    $ d_koszmar = True
    $ quick_menu = True
    jump epizod3b

#########################  Epizod 1 Ujecie 1A SPACER ###########################
label e1u1a:
    # Wybór U1A kieruje nas na spacer do pobliskiego lasu.
    window hide
    scene forest_night with Dissolve(1.0):
        pos (-1.0,-0.6) zoom 0.98
        linear 12.5 zoom 1.0
    #play music sfx_szumdrzew fadein 3.0
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music arthur_vyncke_red_forest
    play ambient sfx_windy_forest
    pause 1
    $ c_ciekawosc = True
    "Niedaleko Tawerny znajduje się las."
    "Chociaż można powiedzieć, że to Tawerna znajduje się niedaleko lasu."
    "Rośnie on tutaj od przynajmniej kilku wieków. A tak przynajmniej twierdzą najstarsze elfy."
    "Lia czasem wymyka się tutaj, aby odpocząć od torturującej codzienności."
    "Nie korzysta jednak z głównej ścieżki wydartej wiele lat temu przez ludzi (na spółkę z krasnoludami). Chodziło chyba wtedy o jakąś nową kopalnię."
    "Po pewnym czasie ktoś dokończył dzieła i połączył ścieżkę z okoliczną wsią."
    transform tr_sciezkadolas:
        pos(-1.0, -0.6)
        ease 12.5 pos (-0.1, -0.5) zoom 0.9

    scene forest_night at tr_sciezkadolas:
        ease 60.0 zoom 0.9
        ease 60.0 zoom 1.0
        repeat

    show p1 shadow at right with easeinright:
        xoffset -120
    "Lia delikatnie westchnęła nad losem zdegradowanego środowiska po czym czmychnęła w kierunku swojej własnej, sekretnej ścieżki."
    "Mijając wiekowe drzewa pomyślała, że ludzie pochopnie oceniają wszystko na pierwszy rzut oka."
    "Nie interesuje ich wnętrze."
    "Czy to istot czy chociażby tego lasu."
    "\"Chociaż może to dla Ciebie i lepiej\" - pomyślała Lia."
    "Spojrzała uważniej na korony pobliskich drzew."
    "Las odpowiedział jej tylko delikatnym podmuchem wiatru."
    "Szelest liści wyprowadził ją w idealnym momencie z głębszych zakamarków umysłu."
    "Właśnie dotarła do miejsca, w którym należało zanurzyć się w morze drzew."
    "Przeciskanie się przez leśne gęstwiny nie należało do najprzyjemniejszych rzeczy."
    "Jednak świadomość nagrody czającej się za tą niewielką trudnością była wystarczającą motywacją."
    "Po dłuższej chwili Lia przedostała się w końcu do ścieżki i westchnęła."
    scene bg forest
    show p1 shadow at right:
        xoffset -200
    with Dissolve(1.0)
    play music2 sfx_jungle_atmosphere_night
    $ renpy.music.set_volume(0.7, delay=0, channel='musictight')
    play musictight sfx_small_stream_flowing
    "Przed jej oczami malował się widok zupełnie inny niż przy wydrążonej nienaturalnie drodze do kopalni."
    "Tamtejszy mrok zastąpił blask księżyca. Odbijał się on w strumyku płynącym wzdłuż przykrytej delikatnym mchem wąskiej ścieżki."
    "Lia rozpoczęła swój rytualny spacer, który prawie natychmiast zamienił się w życiowe rozmyślania."
    "O tym, że nie wie dokąd prowadzi jej życie. O tym, że jej rodzice wymagają od niej znacznie więcej niż sam król od swoich służących."
    "O tym, że jedyne co w życiu robi to pracuje oraz podaje gościom strawę i alkohol (a w zasadzie to przede wszystkim alkohol)."
    "Na koniec jej myśli zaczęły wędrować do tej jednej pozytywnej rzeczy, która ją ostatnio spotkała. W końcu miała przyjaciela."
    "Nie była jednak pewna czy akurat teraz z nią jest."
    "Przyjazne otoczenie, cichy szum wiatru oraz delikatny dźwięk płynącego strumyka dodał jej troszkę odwagi. Postanowiła po prostu zapytać:"
    show p1 at center with ease: # TODO Lia ma patrzec na gracza
        xoffset 0
    show p1 wink_player
    p1 "Hej, nadal tu jesteś?"
    gr "Oczywiście."
    p1 "Oh, już się delikatnie bałam."
    p1 "Odkąd mi towarzyszysz to jest mi tak jakby, hmm... łatwiej."
    p1 "Ciężko mi tylko stwierdzić kiedy przy mnie jesteś."
    gr "Oh, nie musisz się o to martwić!"
    gr "Jestem z Tobą cały czas. Nigdy Cię nie opuszczę"
    gr "Sama kierujesz swoim losem, ale jeśli czegoś potrzebujesz to po prostu mnie zapytaj."
    p1 "Naprawdę? Jesteś tu zawsze? Cz.. czyli mówisz, że mój strach jest nieuzasadniony?"
    gr "Dokładnie tak. Naprawdę nie musisz się bać. Najważniejsze to poprosić o pomoc, a wtedy zawsze Ci doradzę."
    p1 "Dziękuję, to dla mnie bardzo ważne. Dobrze, że ujawniasz się coraz częściej."
    p1 "Nie wiem co bym zrobiła, gdybym dalej była sama."
    p1 "Naprawdę ciężko codziennie robić to samo i żyć tak jak żyję."
    p1 "Mama stara się być miła, ale widzę, że coś stale ją trapi - nie chcę jej stresować."
    p1 "A ojciec... jego się chyba troszkę boję, wolałabym... Zaraz, co to było? Słyszałeś to?"

label e1u2a:
    play sound sfx_szuranielisci # TODO skrocic dzwiek
    show p1 widenedwink bsurprised lopen shadow at right with easeinright
    "Dopiero co nabierający rumieńców monolog został przerwany przez nienaturalnie głośny szelest liści."
    show bg forest postac with dissolve # TODO dodac prawidlowe tlo
    "Za drzewami, jakby znikąd, nagle pojawił się ledwo widoczny kształt postaci."
    "Tajemnicza osoba była praktycznie niewidoczna, a samą twarz zasłaniał głęboki kaptur."
    "Lia delikatnie wzdrygnęła się ze strachu. Na szczęście odwaga jeszcze jej nie opuściła. Po czym wyszeptała:"
    p1 "Ooo! Ktoś tam stoi? Co robimy?"
    stop music fadeout 10.0
    menu:
        #p1 "Co robimy?"
        "Nie wygląda zbyt groźnie - podejdź i sprawdź! Poznajmy kogoś nowego!":
            p1 "Dobrze!"
            jump e1u3a

        "Lepiej nie podchodzić... ale na wszelki wypadek zawołaj. Niech wie, że go widzimy!":
            jump e1u3b

####### Epizod 1 Ujecie 3 wersja A - Tajemnicza postac ##########
label e1u3a:
    image wjazdnatajemniczapostac:
        "bg forest postac"
        zoom 1.0
        ease 4 zoom 1.2
        "bg forest" with Dissolve(1.0)
        zoom 1.2
    #    pause 2.0
    #    linear 4 zoom 1.0
    scene wjazdnatajemniczapostac

    "Lia postanowiła powoli zbliżyć się do tajemniczej postaci."
    "Nie była jednak pewna czy zakapturzony nieznajomy ją widzi."
    "Sylwetka tajemniczej postaci powoli zaczęła się ujawniać."
    "W pewnym momencie udało się dostrzec, że tajemniczy nieznajomy to tak naprawdę młoda dziewczyna!"
    "Gdy tylko zauważyła zbliżającą się Lię - niespodziewanie zniknęła wśród drzew."
    show p1 bsad lsad wink_player shadow at center
    p1 "Oh! Miałam nadzieję, że rzeczywiście uda mi się porozmawiać z kimś nowym. Szkoda, że uciekła... bo chyba była to dziewczyna, co nie?"
    gr "Tak... a przynajmniej tak mi się wydaje."
    p1 "Super byłoby mieć przyjaciółkę. Myślisz, że się jeszcze kiedyś pojawi?"
    gr "A co to za smutek w głosie? Nie trać nadziei! Na pewno się pojawi."
    gr "Jeśli nie ona to ktoś inny. Pamiętaj, jestem tutaj, żeby Ci pomóc. Teraz wszystko się zmieni. Zobaczysz."
    show p1 -lsad with fc
    p1 "No dobrze... pewnie masz rację."
    show p1 -bsad with Dissolve(.1)
    p1 "Wracajmy!"
    show p1 lsmile with Dissolve(.15)
    p1 "Jutro na pewno będzie lepsze!"
    stop music2 fadeout 2.0
    stop musictight fadeout 2.0

label e1u4a:
    scene anim_tavern nighttime dragon with fade:
        pos (-0.4, -0.8) zoom 2.5
        linear 8 pos (-0.5,-0.3) zoom 1.8
    $ renpy.sound.set_volume(0.9, delay=0, channel='ambient')
    $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
    play ambient sfx_warm_evening_outdoors
    "Droga powrotna zleciała szybko i bez żadnych niespodzianek."
    "Lia całą drogę myślami była przy tajemniczej dziewczynie."
    "Zastanawiała się kim mogła być i dlaczego tak się bała."
    scene anim_room_lia_nightdragon with fade
    $ renpy.music.set_volume(0.5, delay=1, channel='ambient')
    "Po powrocie do pokoju przeszło jej przez myśl, że może wcale nie ma tak źle."
    "Przynajmniej nie musi przed czymś uciekać po nocy w lesie."
    show lia lsmile wink_player shadow with fc:
        align (0.5,0.0)
    p1 "Ahh, mimo wszystko cieszę się z tego spaceru. Dziękuję Ci za tę poradę! Teraz mogę spokojnie pójść spać."
    "W jej głosie można było usłyszeć nutkę nadziei."
    p1 "Dobranoc!"
    hide lia with dissolve
    stop ambient fadeout 1.0
    stop music
    "Zmęczenie spacerem dało się we znaki - Lia prawie natychmiast zasnęła."
    $ renpy.sound.set_volume(1, delay=0, channel='ambient')
    $ renpy.sound.set_pan(0, delay=0, channel='ambient')

    #sen z marzeniami | decyzja

    $ quick_menu = False
    $ d_e1_senmarzen = True
    play ambient sfx_birds
    image sen_forest_justforest:
        contains:
            "anim_forest_justforest"
            align (.5,.5) pos (0.25,0.2)
            zoom 0.6
            linear 15 pos (0.15,0.2)
        contains:
            "anim_dreams_border"
        time 10.0


    call screen sen_marzen with fade
    screen sen_marzen():
        image "sen_forest_justforest"
        timer 9.0 action Jump("epizod2")

######## Epizod 1 Ujecie 3 wersja B - Tajemnicza postac ##########
label e1u3b:
    "Lia postanowiła zawołać tajemniczą postać."
    "Nie czekając na dodatkową motywację do działania, krzyknęła:"
    p1 "Hej, halo! - co tu robisz tak późno?"
    "Niespodziewany krzyk musiał przerazić nieznajomego, gdyż natychmiast zniknął pośród gęstych drzew."
    show bg forest with Dissolve(0.1)
    "\"Może krzyczenie do kogoś obcego w środku nocy nie było najlepszym pomysłem\" - pomyślała Lia, po czym dodała zawiedzionym głosem:"
    show p1 lsad bsad at center with move
    p1 "No cóż, szkoda... Chyba czas wracać."
    stop music2 fadeout 2.0
    stop musictight fadeout 2.0

label e1u4b:

    # Na ekranie: Tawerna z zewnątrz (wersja nocna)
    scene anim_tavern nighttime dragon with fade:
        pos (-0.4, -0.8) zoom 2.5
        linear 8 pos (-0.5,-0.3) zoom 1.8

    $ renpy.sound.set_volume(0.9, delay=0, channel='ambient')
    $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
    play ambient sfx_warm_evening_outdoors
    "Droga powrotna zleciała szybko i bez żadnych niespodzianek."
    "Lia całą drogę myślami była przy tajemniczej postaci."
    "Zastanawiała się kto to był i czemu tak nagle zniknął."
    # Na ekranie: Pokój P1
    scene anim_room_lia_nightdragon with fade
    $ renpy.music.set_volume(0.5, delay=0, channel='ambient')
    "Po powrocie do pokoju przeszło jej przez myśl, że może wcale nie ma tak źle."
    "Przynajmniej nie jest zmuszona włóczyć się w nocy po lesie."
    "Z delikatną nutką nadziei w głosie, rzekła:"
    # Na ekranie: Na środku P1 - patrząca na gracza
    show p1 wink_player shadow with dissolve # TODO p1 patrząca na gracza
    p1 "Spacer nie był mimo wszystko taki zły. To była dobra porada. Dobranoc!"
    stop ambient fadeout 1.0
    stop music
    "Zmęczenie spacerem dało się we znaki - Lia prawie natychmiast zasnęła."
    scene black with dissolve
    pause 1
    $ renpy.sound.set_volume(1, delay=0, channel='ambient')
    $ renpy.sound.set_pan(0, delay=0, channel='ambient')


    #sen neutralny | decyzja
    #old forest tylko za dnia zoomujący na ścieżkę
    #scene black with fade
    #pause 1
    image sen_forest_day:
        contains:
            "forest_day" # przy forest_day_fog ktore tu ma byc domylsnie trzeba poprawic align
            align (0.5, 0.3) zoom .75
            linear 6 align (0.85,0.3) zoom .8
            linear 10 zoom 1.1
            linear 100 align (0.85,0.4) zoom 1.4
        contains:
            "anim_dreams_border"


    $ quick_menu = False
    $ d_e1_senneutral = True
    play ambient sfx_hallow_wind
    call screen sen_neutral with fade
    screen sen_neutral():
        add "sen_forest_day"
        timer 13.0 action Jump("epizod2")

################################################################################
#############################   EPIZOD DRUGI   #################################
label epizod2:
    scene black
    pause 0.5
    stop ambient
    $ quick_menu = True
    # Sniadanko bohaterki z rodzicami
    scene anim_room_lia_morning with fade #pokoj P1
    if d_e1_senmarzen:
        $ renpy.music.set_volume(0.5, delay=0, channel='music')
        play music [alexander_nakarada_relaxing_ballad, alexander_nakarada_relaxing_ballad, "<silence 1000.0>"] fadein 5.0
        "Lia zbudziła się o brzasku."
        show p1 with Dissolve(0.5)
        "Promienie Słońca wpadały przez okno i delikatnie muskały jej policzek."
        "Delikatne ciepło przyciągnęło miłe wspomnienie ze snu."
        show p1 lsmile with fc
        "\"Może to dobry znak\" - pomyślała Lia, po czym delikatnie się uśmiechnęła."
        "Szybko się ubrała i ruszyła w kierunku kuchni na śniadanie."
    if d_e1_senneutral: # pokoj P1
        $ renpy.music.set_volume(0.5, delay=0, channel='music')
        play music [alexander_nakarada_spring, alexander_nakarada_spring, "<silence 1000.0>"] fadein 5.0 fadeout 10
        #show p1 closed #TODO crop twarzy lol
        "W oddali niosło się pianie koguta. Lia delikatnie spróbowała otworzyć oczy."
        "Niestety promienie Słońca wpadające przez okno skutecznie zaprzepaściły kilka pierwszych prób."
        "..."
        "..."
        #show p1 narrowedwink
        "Minęła dłuższa chwila. Lia słyszała głos ojca, który wołał ją na śniadanie."
        "\"Chętnie pospałabym do wieczora\" - pomyślała, po czym zaczęła powoli wstawać."
        #hide p1 with easeoutleft # TODO with MoveTransition()
        "Ubrała się i opornie wyruszyła w kierunku kuchni."


    scene bg tavern 0:
        zoom 2.0 align (.5,.5) # TODO Dodać tło - Ciemny korytarz tawerny
        linear 15 xpos 0.0
    "Lia minęła kilka pomieszczeń. Jednym z nich była główna kuchnia połączona z jadalnią."
    "Ta do której zmierzała to w zasadzie pomieszczenie połączone z zapleczem Tawerny."
    "Z tej na górze już nie korzystają. Po co robić bałagan w dwóch miejscach?"
    "Tak przynajmniej uważają jej rodzice, ale nikt nie słucha jej porady aby nie jeść w miejscu pracy."
    "Po krótkiej wędrówce przez domowe korytarze dotarła na miejsce i otworzyła drzwi."

    if d_e1_senmarzen:
        scene room_kitchenday with dissolve

        show p1 lsmile with easeinright
        "Weszła do środka z uśmiechem na twarzy."
        show p2 with easeinright:
            align(.9,1.0)
        show p1 with fc:
            xzoom -1
        p1 "Dzień Dobry Mamo!"
        show p3 with easeinright:
            align(.6,1.0) xzoom -1
        show p1 with ease:
            align(.2,1.0)

        p1 "Dzień dobry Tato!"
        show p3 with fc:
            xzoom 1
        "Rodzice spojrzeli po sobie, delikatnie zdziwieni."
        "Rzadko widywali jak ich córka się uśmiecha. Wydało im się to aż nadto podejrzane."
        show p3 with fc:
            xzoom -1
        "Ciszę przerwał Ojciec."
        p3 "Czy coś się stało? Skąd ten uśmiech?"
        p1 "Czy od razu coś musiało się stać?"
        p2 "Dziecko, przecież Cię znamy. Powiedz czy coś się stało."
        p1 "Ehh..."

    if d_e1_senneutral:
        # Na ekranie: P2 oraz P3 po lewej stronie, P1 pojawiająca się chwilę po nich po prawej
        scene room_kitchenmealday
        show p2:
            align (.4,1.0)
        show p3:
            align (.1,1.0)
        with fade

        "Z grymasem na twarzy weszła do kuchni."
        show p1 narrowedwink with easeinright:
            align (.8,1.0)
        "Lia postanowiła tradycyjnie skupić się na znalezieniu czegoś normalnego do jedzenia."
        # Na ekranie: P3 wysuwa się mocniej do przodu i bliżej do P1 (mogą na środku być)
        show p3 at center with move
        show p2 at left with ease:
            xzoom -1
        "Nie przyszło jej to łatwo. Finalnie drogę zagrodził jej Ojciec, delikatnie się nachylił i powiedział:"
        p3 "Dzień dobry młoda damo! Cieszymy się, że zaszczyciłaś nas swoją obecnością."
        p1 "..."
        p3 "Mogłabyś wydusić chociaż proste \"Dzień dobry\"..."
        # Na ekranie: Wracamy do pierwotnego rozstawienia, tj. P2, P3 po lewej i P1 prawo
        show p3 at center with ease
        show p3 at left with move
        show p2 at center with move:
            xoffset -200

        "Powiedział Ojciec, po czym z delikatnym smutkiem usunął się z drogi i wrócił na swoje miejsce."
        "..."
        "Po krótkiej, niezręcznej ciszy - Ojciec znów zabrał głos. Tym razem głos był zimniejszy, ewidentnie domagający się odpowiedzi."
        p3 "Lia, co robiłaś wczoraj po pracy? Słyszałem, że nie weszłaś od razu na piętro. Poszłaś spać tak jak prosiłem przed zamknięciem Tawerny?"

    show p1 lneutral bsad with fc
    "Lia zaczęła się stresować. Nie wiedziała co zrobić."
    "Tętno zaczęło jej przyspieszać, a oczy krążyły jakby szukały pomocy..."

    # Wybór: Prawda czy fałsz
    menu:
        "Lepiej powiedz im prawdę.":
            jump e2u2a
        "Byłaś w pokoju. Jeśli dowiedzą się, że wyszłaś to dołożą Ci więcej pracy.":
            $ d_krotkienogiklamstwa +=1
            jump e2u2b
        "[[Nic nie mów]" if persistent.nicniemow < 2:
            jump e2u2c


# Epizod 2 Ujecie 2A
# Prawda rodzicom przekazana
label e2u2a:
    # Na ekranie bez zmian z poprzedniego ujęcia
    p1 "Ahh, wiesz Tato... byłam na spacerze w lasku, chciałam się przejść. Nic nadzwyczajnego się nie stało! Chociaż..."
    "Powiedziała jednym tchem, po czym odetchnęła z ulgą, w ciszy dziękując przyjacielowi."
    p3 "Chociaż co?"
    "Powiedział Ojciec niecierpliwym głosem."
    "Lia zrozumiała, że niepotrzebnie o tym wspomniała. Teraz nie było jednak odwrotu."

    # Jeśli \"Podejdź i sprawdź\" w E1U2A
    if d_e1_senmarzen:
        p1 "Zauważyłam kogoś w lesie i chciałam sprawdzić kto to, ale gdy podeszłam..."
        p2 "Oj, nierozsądnie kochanie..."
        p1 "No wiem, ale sądziłam, że nic mi nie grozi. Zauważyłam tylko, że to młoda dziewczyna, chyba elfka - uciekła od razu gdy tylko się zbliżyłam."
        show p2 with fc
        show p3 with fc:
            xzoom 1
        "Rodzice popatrzyli po sobie dziwnym wzrokiem. "
        "Niepokojącą ciszę przerwała Matka:"
        show p3 with fc:
            xzoom -1
        p2 "Nic się nie stało. Dobrze, że powiedziałaś nam prawdę. Bardzo nas to cieszy."
        p2 "Tylko następnym razem uważaj, a najlepiej dać znać, że wychodzisz. Nie będziemy się wtedy tak bardzo martwić."
        p1 "Oj, nie przesadzaj mamo..."
        p2 "Nie przesadzam skarbie. Bardzo Cię kochamy i nie wiem co bym zrobiła gdyby coś Ci się stało..."
        "Mimo niewielkiego pomieszczenia, czuć było gęstą atmosferę."
        "Rozmowy o uczuciach były trudne. Nie było ich dużo, ale gdy się pojawiały to zawsze ich epicentrum była troskliwa matka."
        p3 "To prawda, jesteś naszą małą księżniczką - nie pozwoliłbym, żeby coś Ci się stało."
        "Oh, strasznie dziwne uczucie - pomyślała Lia, reagując w ten sposób na słabo jej znane ciepło wewnątrz ciała."
        "Każda chwila zdawała się teraz trwać godzinami, myśli kłębiły się we wszystkie strony, w końcu Lia zdołała wydukać:"
        p1 "Ja... ja nie wiem co powiedzieć... uh.. dziękuję..."
        show p2 smile with fc
        show p3 smile with fc:
            xzoom 1
        "Rodzice niespodziewanie uśmiechnęli się, ojciec tylko kiwnął na znak akceptacji w kierunku swojej żony."
        show p3 smile with fc:
            xzoom -1
        p2 "Wystarczy, że będziesz grzeczna..."
        p2 "No, przynajmniej w miarę grzeczna."
        "Powiedziała z uśmiechem, po czym spojrzała w stronę męża. Po chwili dodała:"
        p2 "Jeśli masz ochotę, możesz dziś wcześniej skończyć pracę i przejść się na festiwal do wioski i troszkę się pobawić. Co Ty na to?"
        show p1 bsurprised with fc
        "Lia nie była niczego zbytnio pewna, teraz też nie mogła podjąć samodzielnie decyzji. Potrzebowała pomocy..."

    # Jeśli \"Zawołaj\" w E1U2A
    if d_e1_senneutral:
        p1 "Widziałam kogoś w lesie, ale zawołałam go z bezpiecznej odległości i..."
        p3 "Zrobiłaś co? Niezbyt mądre..."
        p2 "Zorn, daj jej dokończyć."
        p1 "No więc, zawołałam z daleka, ale ten ktoś od razu uciekł. Nie wiem nawet jak wyglądał."
        show p2 with fc:
            xzoom 1
        show p3 with fc:
            xzoom 1
        "Rodzice popatrzyli po sobie z lekkim niepokojem."
        "Nastała cisza, Ojciec ewidentnie się mocno zamyślił. Na jego twarzy malowało się skupienie."
        show p2 with fc:
            xzoom -1
        "W czasie gdy Ojciec się zastanawiał, ciszę przełamała Mama:"
        p2 "Nie widziałaś czegoś jeszcze nietypowego? Czy na pewno powiedziałaś nam wszystko?"
        "Zapytała spokojnym głosem, uśmiechając się nerwowo."
        p1 "Nic więcej nie widziałam, naprawdę!"
        p3 "Dobrze, dobrze."
        "Powiedział ojciec niespodziewanie."
        p3 "Wierzymy Ci, oczywiście. Pytamy na wszelki wypadek. Nie chcielibyśmy, żeby coś Ci się stało."
        p3 "Następnym razem uważaj. A jeśli wychodzisz gdzieś o tak późnych godzinach to wcześniej nas uprzedź!"
        p3 "Gdyby coś Ci się stało to nie wiemy co byśmy zrobili... Musisz uważać Lia, proszę."
        "Ojciec zakończył swój bardzo spokojny i krótki monolog. Lia była bardzo zaskoczona."
        "Rzadko kiedy widywała i jednocześnie słyszała swojego ojca, który mówi jednocześnie z takim spokojem i obawą w głosie."
        "Zastanawiała się przez moment nad tym dlaczego tak się tym przejęli - przecież to był tylko głupi spacer niedaleko domu. Co mogłoby się jej stać?"
        "W międzyczasie głos znów zabrał Ojciec:"
        p3 "We wsi nadal trwa festiwal. Jeśli chciałabyś to możesz dziś skończyć pracę trochę wcześniej, przejść się tam i może trochę rozerwać. Co Ty na to?"
        show p1 bsurprised with fc
        "Lia przed momentem nie była pewna zachowania swojego Taty, a teraz miałaby na dodatek podjąć jakąś decyzję? Praktycznie niemożliwe. Znów potrzebowała pomocy..."

    jump e2u3a # skok do menu z wyborem czy Lia pojdzie na festiwal

# Epizod 2 Ujecie 3A
label e2u3a:
    menu:
        "Chodźmy na festiwal! Może tym razem uda się poznać kogoś fajnego!": #leci na festiwal
            show p1 lsmile bneutral with fc
            p1 "Oo, dziękuję! Chętnie się tam przejdę."
            show p2 smile with fc
            show p3 smile with fc
            "Rodzice uśmiechnęli się delikatnie i zobaczyli tylko jak Lia wychodzi z kuchni."
            $ d_gofestiwal = True
            jump epizod3
        "Lepiej zostań w pracy do końca. Powinnaś starać się zdobyć zaufanie rodziców.": #pomija festiwal
            show p1 lneutral bneutral with fc
            p1 "Myślę, że zostanę w pracy do końca. Wystarczy mi tego wychodzenia."
            if d_e1_senmarzen:
                show p2 -smile with fc:
                    xzoom 1
                show p3 -smile with fc:
                    xzoom 1
            elif d_e1_senneutral:
                show p2 -smile with fc:
                    xzoom 1
                show p3 -smile with fc:
                    xzoom 1
            "Rodzice popatrzyli po sobie lekko zdziwieni."
            if d_e1_senmarzen:
                show p3 with fc:
                    xzoom -1
            if d_e1_senneutral:
                show p2 with fc:
                    xzoom -1
            p2 "Dobrze, jak uważasz. Tymczasem starczy tego siedzenia, zaraz trzeba otwierać!"
            # d_gofestiwal się nie zmienia
            jump epizod3

# Epizod 2 Ujecie 2B
label e2u2b:
    p1 "Taak, zamknęłam drzwi za gośćmi, chwilę posiedziałam i poszłam spać..."
    "Powiedziała Lia z lekką niepewnością w głosie. Unikała jednocześnie kontaktu wzrokowego z Mamą czy Tatą"
    "Niestety nie umknęło to ich uwadzę. Nie miało to wielkiego znaczenia, gdyż Ojciec westchnął ciężko i z ledwo wyczuwalnym smutkiem w głosie, powiedział:"
    p3 "Lia, byłem w Twoim pokoju aby sprawdzić czy śpisz. Nie było Cię. Teraz powiedz mi..."
    p3 "Mam sam dedukować czy jednak się przyznasz?"
    "Lia nerwowo spuściła wzrok, nie wiedziała co powiedzieć..."
    "\"Czy będę kiedyś w stanie podejmować decyzje sama?\" - pomyślała, czekając w międzyczasie na pomoc od swojego przyjaciela."

    menu:
        "Nie ma sensu tego dłużej ciągnąć... powiedz im.":
            jump e2u2bpowiedz
        "Nie mów nic, ciągle mają tylko pretensje. Nie dawaj im kolejnych powodów.":
            $ d_krotkienogiklamstwa +=1
            jump e2u2bniemow

    label e2u2bpowiedz:
        p1 "Byłam wczoraj w lesie... Poszłam tylko na krótki spacer! Nic takiego się nie stało..."
        show p3 angry with fc
        p3 "Stało się, oj stało się! Najpierw kłamstwo, a teraz okazuje się, że włóczysz się po lesie w nocy. SAMA! Czemu postąpiłaś tak nieodpowiedzialnie? Masz jakieś wytłumaczenie?"
        p1 "Chciałam przełamać rutynę..."
        "Powiedziała smutnym głosem Lia."
        p3 "Ciesz się, że nogi Ci ktoś nie przełamał! Ja..."
        show p1 bsad with fc
        # TODO Na ekranie: p1 zmienia się na \"sad\"
        "Smutny głos córki zadziałał chyba na matkę. Chwyciła delikatnie mężą za ramię i przerywając mu, powiedziała:"
        p2 "Zorn, spokojnie. Mogła sobie coś zrobić, to prawda. Na szczęście nic się nie stało."
        show p3 with Dissolve(0.2)
        "Zaczęła swoim spokojnym głosem, po czym spojrzała na córkę i kontynuowała:"
        p2 "A Ty, młoda damo, mimo wszystko przesadziłaś. Nie mamy nic przeciwko, żebyś szła sobie na spacer."
        p2 "Tylko uprzedź nas wcześniej i proszę Cię, rób to o normalnej porze - w ciągu dnia."
        p2 "Jeśli coś takiego się powtórzy to czeka Cię poważny szlaban."
        "Spokojny głos nie zwiódł Lii. Wiedziała, że matka nie żartuje i musi teraz bardzo uważać."
        "Mimo wszystko delikatny uśmiech wrócił na jej twarz i gdzieś głęboko w środku czuła delikatną wdzięczność za ratunek przed Ojcem."
        "Z szeregu myśli wyrwał ją dalszy wywód jej Matki:"
        p2 "... w związku z czym dzisiaj zostaniesz do końca pod naszym okiem. Pracujesz do późna i kładziesz się spać. Przypilnujemy tego. A teraz zjedz śniadanie i powycieraj stoły nim przyjdą goście."
        hide p3 with easeoutleft
        pause 0.5
        hide p2 with easeoutleft
        "\"Mogło być gorzej\" - pomyślała Lia. Zwróciła uwagę, że Ojciec wyszedł z kuchni, a chwilę po nim Matka. Lia dokończyła śniadanie, po czym wstała i powiedziała:"
        hide p1
        show lia wink_player: # TODO check position + jaka mina?
            align (0.5,0.0)
        with dissolve
        p1 "Dziękuję Ci za pomoc!" # [do gracza] Lia skierowana do gracza + zoom
        jump epizod3

    label e2u2bniemow:
        "Lia nie powiedziała słowa, zajęła się śniadaniem."
        "Minęła chwila nim Lia zaczęła czuć wzbierającą w Ojcu złość"
        "..."
        "Lia próbowała zająć się śniadaniem. Napięta sytuacja powodowała, że ręka trzęsła jej się przy każdym kęsie."
        "Ciekawe co będzie teraz - pomy..."
        # TODO Ekran: Uderzenie ręki o stół, efekt trzęsącego się ekranu
        show p3 angry with fc
        with vpunch
        "Nagle Ojciec niespodziewanie uderzył ręką w stół - tak mocno, że wszystko na stole delikatnie podskoczyło."
        p3 "Długo zamierzasz mnie ignorować?"
        p3 "Co Ty sobie wyobrażasz? Że możesz tutaj siedzieć i nic nie robić?"
        p3 "Na dodatek myślisz, że możesz sobie od tak wyjść w środku nocy?"
        "Głos Ojca narastał z każdą chwilą i powoli zaczął oddziaływać na Lię."
        # TODO Na ekranie: P1 zmienia się na \"sad\""
        show p1 bsad with fc
        "Lia zaczęła się zastanawiać czy podjęła dobrą decyzję. Przez wątpliwości zrobiło jej się jeszcze bardziej smutno."
        "Przez sekundę pomyślała nawet czy nie przerwać Ojcu, lecz teraz zbyt bardzo się bała."
        p3 "Na dodatek próbowałaś nas okłamać. Przecież to jest niedopuszczalne!"
        p3 "Dziewczyno, postępuj tak dalej a nie opuścisz tego budynku przez bardzo, bardzo długi czas!"
        p3 "Mogłabyś chociaż spróbować na mnie spojrzeć gdy do Ciebie mówię!"
        show p1 narrowedwink
        "Lia próbowała spojrzeć na Ojca, lecz nie pozwalał jej strach. Kumulujący się smutek zniechęcał ją do czegokolwiek."
        p3 "Oj... myślisz, że smutne oczy teraz pomogą? Było myśleć o tym wcześniej smarkulo!"
        "Ojciec zatrzymał na moment gniewną tyradę. Próbował się uspokoić, ale chyba zdenerwowało go to jeszcze bardziej."
        p3 "KURWA... momentami nie mogę już z nią wytrzymać!"
        "Krzyknął Ojciec - bardziej w kierunku swojej żony, niż dziecka."
        show p1 lsad smalltears with fc
        "Lia mocno się przestraszyła i mimowolnie rozpłakała"
        # TODO Na ekranie: P1 zmienia się na \"cry\"
        "Ojciec najwyraźniej nie zwrócił na to uwagi i dalej kontynuował:"
        p3 "Naprawdę. Nie daję rady jej upilnować. Coś jej się w końcu stanie! Myślę, że lepiej byłoby ją wysła..."
        p2 "ZORN!"
        show p3 angry with fc:
            xzoom 1
        "Przerwała niespodziewanie Matka"
        p2 "Wystarczy tego! Lia zrozumiała. Ja też zrozumiałam. Damy radę, razem."
        show p3 with fc
        "Uspokoiła męża, po czym zwróciła się w stronę córki."
        show p3 with fc:
            xzoom -1
        p2 "A Ty, niegrzeczna istoto - na pewno w najbliższej przyszłości nie opuścisz tego budynku. Dziś pracujesz do końca i nawet nie waż się znikać nam z oczu na zbyt długo. Nie chcemy się martwić."
        p2 "A teraz skończ śniadanie i do pracy!"
        jump epizod3

# Epizod 2 Ujecie 2C CRASH
label e2u2c:

    image kuchnia_blur1 = im.Blur("places/kitchen/room_kitchenmealday.png", 2.0)
    image kuchnia_blur2 = im.Blur("places/kitchen/room_kitchenmealday.png", 4.5)
    stop music
    scene kuchnia_blur1
    show p1 bsad narrowedwink lsad
    with dissolve
    "Stres praktycznie całkowicie obezwładnił Lię."
    "Bez porady stała się bezradna i zwyczajnie..."
    scene kuchnia_blur2
    show p1 bsad narrowedwink lsad smalltears bigtears
    with dissolve
    "...momentalnie się rozpłakała."
    # Tutaj odwala się mini przebudzenie z tekstem:
    $ quick_menu = False
    scene black
    if persistent.nicniemow == 0:
        show text _("{color=#fff}{i}Co Ty robisz? Masz ją prowadzić, a nie bezczynnie obserwować. Jeszcze raz!{/i}{/color}"):
            align (0.5,0.85)
        pause
    elif persistent.nicniemow == 1:
        show text _("{color=#fff}{i}A Ty dalej swoje? Więcej tego nie zrobisz. Jeszcze raz!{/i}{/color}"):
            align (0.5,0.85)
        pause
    else:
        show text _("{color=#fff}{i}Jak to możliwe? Muszę to poprawić.{/i}{/color}")
    $ persistent.nicniemow += 1
    $ d_koszmar = False
    $ d_e1_senmarzen = False
    $ d_e1_senneutral = False
    $ d_gofestiwal = False
    $ d_krotkienogiklamstwa = 0
    scene black
    pause 2
    $ renpy.block_rollback()
    $ quick_menu = True
    jump epizod1


################################################################################
#############################   EPIZOD TRZECI   ################################
label epizod3:
    scene ep_img_tavern_mainroom
    with fade
    $ renpy.music.set_volume(0.4, delay=0, channel='music')
    play music peritune_minstrel fadein 10.0 fadeout 10.0
    ##############   jeśli Prawda w E2        ########################
    if d_krotkienogiklamstwa == 0:
        "Lia dotarła do głównej sali, a na jej twarzy malował się uśmiech. Ktoś mógłby stwierdzić, że to dość nieczęsty widok."
        show p1 with dissolve:
            align (.5,1.0) xzoom -1
        #queue music "<silence 3.0>"
        "Mógłby... gdyby tylko ktoś ją teraz widział. Rozejrzała się po Tawernie w poszukiwaniu czegoś do zrobienia."
        "W tym momencie do sali wszedł Ojciec i na nią spojrzał."
        show p3 at right with easeinright:
            xzoom -1
        p3 "To jak? Zabieramy się do pracy?"
        p1 "Pewnie, w końcu trzeba wszystko dobrze przygotować. Od czego mam zacząć?"
        p3 "Możesz zacząć od ogarnięcia stołów. Niezbyt nadają się do czegokolwiek po wczorajszym wieczorze."
        p3 "Ah, i pamiętaj. Sprawdzę jak Ci poszło!"
        p1 "Zawsze tak mówisz i nigdy nie sprawdzasz!"
        p3 "Dziś sprawdzę."
        "Powiedział spokojnie Ojciec, po czym wrócił na zaplecze."
        "Lia przewróciła tylko oczami, ale zaraz potem zabrała się do pracy"

    ###############    jeśli Kłamstwo -> Prawda     ##################
    elif d_krotkienogiklamstwa == 1:
        "Lia dotarła do głównej sali. W myślach dziękowała, że wszystko poszło w miarę sprawnie."
        #Na ekranie: P1
        show p1:
            align (.5,1.0) xzoom -1
        "Odetchnęła lekko z ulgą i ruszyła w głąb"
        "Prawie natychmiast usłyszała głos Ojca..."
        show p3 at right with easeinright:
            xzoom -1.0
        p3 "No, wreszcie jesteś! Chodź i mi pomóż."
        p1 "Przecież wszystko praktycznie gotowe. Z czym mam tu niby pomóc?"
        p3 "Eh. Widzisz te stoły? Widzisz na nich kurz? No już - bierz szmatkę i je powycieraj! Tylko dokładnie, potem sprawdzę."
        "\"Ta, jasne.\" - pomyślała Lia. \"Zawsze tak mówi i nigdy tego nie robi\""
        "Mimo wszystko Lia wzięła się do roboty... bo cóż innego miała niby zrobić?"

    ################    jeśli Kłamstwo -> Kłamstwo    ################
    elif d_krotkienogiklamstwa == 2:
        "Lia była jeszcze w głębokim szoku. Ledwo dotarła do głównej sali."
        "Zatrzymała się przed wejściem i wzięła głęboki wdech. Próbowała się uspokoić."
        #Na ekranie: P1
        show p1 with easeinleft:
                align (.5,1.0) xzoom -1
        "Weszła do sali i ruszyła w głąb. Prawie natychmiast drogę zagrodził jej Ojciec"
        show p3 at right with easeinright:
            xzoom -1.0
        p3 "No, wreszcie jesteś! Chodź i mi pomóż."
        p1 "Przecież wszystko praktycznie gotowe. Z czym mam tu niby pomóc?"
        p3 "Eh. Widzisz te stoły? Widzisz na nich kurz? No już - bierz szmatkę i je powycieraj! Tylko dokładnie, potem sprawdzę."
        "\"Ta, jasne.\" - pomyślała Lia. \"Zawsze tak mówi i nigdy tego nie robi\""
        "Mimo wszystko Lia wzięła się do roboty... bo cóż innego miała niby zrobić?"

    jump czyszcz

########## alternatywne wejście z E1U1B #############
label epizod3b:

    # TODO Na ekranie: Pokój P1
    scene anim_room_lia_morning
    show p3 angry at center with easeinright:
        xzoom -1
    show p3 with fc:
        xzoom 1
    "Nagłe wejście Ojca do pokoju Lii gwałtownie wybudziło ją z koszmarnego snu."
    p3 "Nie słyszysz jak Cię wołam?"
    "Lia nie była jeszcze całkiem przytomna. Przez zmrużone oczy dostrzegła, że Słońce już dawno wstało."
    "Gwałtownie się rozejrzała, w międzyczasie zakrywając się kołdrą."
    p1 "Tato! Nie jestem jeszcze ubrana!"
    "Wyrzuciła z siebie, lecz szybko zauważyła że Ojciec wcale na nią nie patrzył. Jego wzrok skierowany był na zewnątrz."
    #hide p3 angry
    show p3 at center with Dissolve(.15)
    p3 "Spokojnie, przecież nie patrzę. Jest późno, a ja wołałem Cię już kilkukrotnie - wstawaj!"
    hide p3 with easeoutright
    "Powiedział w miarę spokojnie po czym ruszył z powrotem, zamykając za sobą drzwi."
    "Lia została sama w pokoju, ziewnęła głośno i szybko się ubrała."
    "Gdy tylko się ogarnęła to ruszyła do Głównej Sali. Domyśliła się, że śniadanie pewnie ją ominęło, więc skierowała się od razu do swojego miejsca pracy."
    # TODO Na ekranie: Korytarz
    scene bg tavern 0:
        zoom 2.0 align (.5,.5) # TODO Dodać tło - Ciemny korytarz tawerny
        linear 8 xpos 0.0
    "Nie miała także zbyt wiele czasu aby zastanowić się nad swoim snem..."
    stop music fadeout 5.0
    "Przemknęła szybko przez korytarz i wręcz zbiegła do głównej sali."
    # TODO Na ekranie: Główna Sala lub Bar (jeśli tego pierwszego nie ma, a jeszcze nie ma)
    scene tavern_main_bar_bg0
    show p3 at zabarem:
        xalign 0.5 xzoom -1.0
    show tavern_main_bar_bar1
    with fade
    "Zauważyła ojca, który praktycznie zakończył już przygotowania do otwarcia Tawerny."
    show p1 at left with easeinleft:
        xzoom -1.0
    p3 "No, wreszcie jesteś! Chodź i mi pomóż."
    show p1 bsad with fc
    p1 "Przecież wszystko praktycznie gotowe. Z czym mam tu niby pomóc?"
    p3 "Eh. Widzisz te stoły? Widzisz na nich kurz? No już - bierz szmatkę i je powycieraj! Tylko dokładnie, potem sprawdzę."
    show p1 bangry with fc
    "\"Ta, jasne.\" - pomyślała Lia. \"Zawsze tak mówi i nigdy tego nie robi\""
    show p1 -bangry with fc
    "Mimo wszystko Lia wzięła się do roboty... bo cóż innego miała niby zrobić?"
    jump czyszcz

#### Na ekranie: Minigra z wycieraniem stołu ########
label poczyszczeniustolu_old:
    scene tavern_main_bar_bg0
    show p1 at zabarem:
        xalign .5 xzoom -1
    show tavern_main_bar_bar1

    if n == n_max:
        "Lia wyprostowała się, aby przyjrzeć się czy czegoś nie ominęła."
        "Wygląda na to, że wszystko zrobione!"
        show p1 lsmile wink at zabarem with fc:
            xalign .5
        "Chciała pomyśleć Lia. Zrozumiała, że to głos Ojca zza jej ramienia."
        show p3 behind tavern_main_bar_bar1, p1 at zabarem with dissolve:
            xalign 0.2
        show p1 at zabarem with dissolve:
            xalign .5 xzoom 1
        p3 "Mówiłem, że sprawdzę. Bardzo ładnie. Teraz zajmij się resztą, a pot..."
    else:
        "Lia wyprostowała się, aby przyjrzeć się czy coś jej nie umknęło."
        "Od razu zauważyła, że pominęła jeden fragment."
        "Gdy tylko chciała zabrać się za poprawki, usłyszała za sobą głos."
        show p3 behind tavern_main_bar_bar1 at zabarem with dissolve:
            xalign (0.2)
        p3 "Ominęłaś fragment, o tam!"
        "Odezwał się Ojciec wskazując palcem na niedoczyszczony fragment."
        #Na ekranie: Angry Lia ON
        show p1 bangry narrowedwink with fc
        p1 "Tak, widzę! Musiałeś akurat podejść i sprawdzić?"
        "Powiedziała Lia ze złością w głosie. Natychmiast tego pożałowała widząc złość na twarzy Taty."
        #Na ekranie: Angry Zorn ON
        show p3 angry at zabarem with Dissolve(.2):
            xalign 0.2
        p3 "Młoda Damo, proszę się zachowywać! Nastę..."

    scene ep_img_tavern_mainroom
    show p3 at center
    with dissolve
    # TODO Na ekranie: Główna Sala lub Bar
    play audio sfx_drzwi
    "Nagle w Tawernie rozległ się huk otwieranych drzwi. Zorn zareagował pierwszy i od razu zawołał:"
    p3 "Halo, jeszcze zamknięte! Proszę wy.. Aaa, to Ty Mohon! Właź właź, nie krępuj się."
    # Na ekranie: P3 + P6 na bokach
    if d_koszmar:
        $ renpy.music.set_volume(0.7, delay=0, channel='music')
        play music the_old_tower_inn fadein 5.0 fadeout 5.0
    show p6 with easeinright:
        align (.5,.5) pos (0.8,0.78)
    p6 "HAHA, a czego miałbym się krępować? Zgłupiałeś Zorn?"
    show p1 with easeinleft:
        align (.1,1.0) xzoom -1
    p6 "Weź polej piwo bo mnie chuj strzeli zar... Oooo, panienko!"
    # Na ekranie: Wjeżdża z lewej P1
    show p6 blush with fc
    p6 "Uszanowanie, Dzień dobry - prześlicznie panienka dziś wygląda!"
    show p1 lsmile blush with fc
    p1 "Dzień dobry Panie Mohon!"
    hide p1 with easeoutleft
    show p6 -blush with fc
    "Odpowiedziała lekko zarumieniona Lia i wróciła do pracy."
    # TODO Na ekranie: Główna Sala lub Bar - P3 + P6
    "Bardzo lubiła swojskiego krasnoluda, który nie przejmował się zbytnio konwenansami."
    "Pracował w kopalni i często tu przychodził. Czy to sam, czy ze swoimi kompanami."
    "Zawsze głośni, zawsze wulgarni - oczywiście gdy tylko nie było jej w pobliżu."
    "Lia kątem oka zauważyła, że jej Ojciec wymienia kilka zdań z Mohonem."
    "Krasnolud po chwili wstał, pomachał do niej i wyszedł z Tawerny tak samo głośno jak do niej wszedł."
    hide p6 with easeoutright
    "Gdy spojrzała w kierunku drzwi, zauważyła zmierzającego do niej Ojca."
    # TODO Na ekranie: Jakaś lekka zmiana ujęcia wewnątrz Tawerny, odbicie lustrzane, P1 + P3
    scene tavern_main_bar_bg0
    show tavern_main_bar_bar1
    show p1 at center:
        xzoom -1
    with dissolve
    show p3 at right with moveinright:
        xzoom -1
    p3 "Jak tam, posprzątane?"
    p1 "Tak, wszystko już skończone!"
    p3 "Cieszę się! Teraz możesz chwilę odpocząć. Zaraz otwieramy."
    #hide p3 with easeoutleft
    #Na ekranie: P1 za barem
    scene tavern_main_bar_bg0
    show p1 at zabarem:
        xalign .5
    show tavern_main_bar_bar1
    with fade
    stop music fadeout 5.0
    "Powiedział Ojciec, po czym zniknął na zapleczu. Lia przystanęła za barem czekając na pierwszych gości..."
    #jump e3u2


# Epizod 3 Ujecie 2
label e3u2:
    # Na ekranie: Tawerna z zewnątrz (animacja z ptaszkami i dymem, zostaje dzień)
    scene anim_tavern outside dragon with fade:
        align (0.6,0.5)
        linear 6 zoom 2.0
    # TODO jakieś pojedyncze głosy zaczyna być słychać, następnie otwarcie drzwi i przejście wewnątrz
    $ renpy.music.set_volume(0.7, delay=0, channel='ambient')
    play ambient medieval_tavern_ambience_5min fadein 1.0 fadeout 2.0
    if not d_koszmar:
        $ renpy.music.set_volume(0.7, delay=0, channel='music')
        play music the_old_tower_inn fadein 5.0
    "Ruch przy Tawernie powoli narastał, więc na pierwszych gości nie trzeba było długo czekać."
    # Na ekranie: P1 za barem
    scene tavern_main_bar_bg0
    show p1 at zabarem:
        xalign .5
    show tavern_main_bar_bar1
    with fade
    "W pierwszej kolejności pojawiły się grupy robotników."
    "Teoretycznie przed pracą nie wypada spożywać alkoholu, ale tak już mają. Lubią uraczyć się zimnym kuflem nim zabiorą się do swoich obowiązków."
    "Większość z nich to osoby, które nie są zbyt rozmowne - część z nich Lia rozpoznaje po twarzy i wie co im podać."
    "Niektórzy co jakiś czas uraczą Lię uśmiechem przy odbieraniu zamówień."
    "Lia jednak woli nie zastanawiać się nad powodem ich uśmiechu."
    "Mimo wszystko Ci, na pierwszy rzut oka prości ludzie, są przyjaźnie nastawieni. Starają się nigdy nie szukać kłopotów, ani nawet okazji do rozróby."
    "Wiedzą, że nie jest to jakaś pierwsza lepsza Tawerna. Często pojawiają się tutaj ważni goście, gwardia czy chociażby strażnicy."
    "Łatwo dostać zakaz wstępu. Pojawiali się tutaj nie tylko ważni emisariusze, ale i enigmatyczni goście - chociażby grupa z namiotu obok."
    "Nikt do końca nie wiedział kto to jest, jaki jest ich cel. Przychodzili do Tawerny po zapasy, a poza tym czasem można było ich gdzieś dostrzec w okolicy."
    "\"Tajemniczy ludzie można by rzec\" - pomyślała Lia próbując skupić się na pracy."

    # TODO Na ekranie: Animacja Tawerny z dnia na noc przejście + jakieś tam dźwięki wewnątrz ludzi
    scene anim_tavern outside dragon with Dissolve(1.2)
    pause 1.2
    show anim_tavern nighttime dragon with Dissolve(2.0)
    pause 1.0
    "Czas powoli płynął do przodu. Przez Tawernę przewijali się goście, a Lia wskoczyła w wir pracy."
    # TODO Na ekranie: Przejście do środka, look na bar + P1
    scene tavern_main_bar_bg0
    show p1 at zabarem:
        xalign .5
    show tavern_main_bar_bar1
    with fade
    "Lia wykonywała dziś swoje obowiązki wyjątkowo sprawnie."
    # TODO Na ekranie: ‘animacja’ z kuflami piwa

    ####################
    #hide p1
    #$ quick_menu = False
    #window hide
    #pause 2

    ###############
    window hide
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
    #############
    #pause 0.5
    #hide piwo_1 with dissolve
    #pause 0.5
    #hide piwo_2 with dissolve
    #pause 0.5
    #hide piwo_3 with dissolve
    #pause
    ############

    pause 1
    p1 "Zamówienie nr 66 gotowe!"
    hide piwo_1
    hide piwo_2
    hide piwo_3
    # show p1 behind tavern_main_bar_bar1
    show elf1:
        align (-0.1,-0.5)
        zoom 0.68
    with dissolve
    p1 "Tylko ostrożnie! Proszę tego nie rozlać."
    # Na ekranie: Random Elf_1 w tle

    r1 "Tak się stanie moja Pani!"
    show p1 lsmile with fc
    "Lia uśmiechnęła się lekko i zabrała za obsługiwanie pozostałych gości."
    show p1 -lsmile with fc
    hide elf1 with dissolve
    stop music fadeout 15.0

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
        show p3 at right with moveinright:
            xzoom -1
        show p1 at zabarem with fc:
            xalign .5 xzoom -1
        "Zaraz po zrealizowaniu ostatniego zamówienia do Lii podszedł Ojciec."
        p3 "Za oknem robi się już ciemno. Jeśli nie zmieniłaś zdania to możesz już zmykać! Przejmę teraz bar."
        show p1 lsmile with fc
        "Lia uśmiechnęła się, podziękowała Ojcu i ruszyła do wyjścia."
        hide p1 with moveoutleft
        stop ambient fadeout 3.0
        p3 "Tylko nie wracaj za późno!"

        jump epizod4
    else:
        "Minęła dłuższa chwila nim Lia mogła odsapnąć."
        "O tej godzinie ruch był naprawdę spory. Ludzie wchodzili i wychodzili."
        "Niektórzy siedzieli jednak dłużej. Głównie osoby podróżujące z lub do stolicy."
        "\"Stolica\" - Lia pomyślała o mieście którym wszyscy się zachwycają."
        "Na moment jej myśli skupiły się na tym czy kiedyś będzie jej dane zachwycić się tym widokiem."
        "Szybko jednak wybiła sobie ten pomysł z głowy. Dotarło do niej, że całe życie spędzi tutaj. Nie ma pojęcia co mogłoby ją tam zaprowadzić..."
        "Jakby zahipnotyzowana, znów skupiła się na pracy. Czas mijał jej coraz szybciej."
        show p3 behind tavern_main_bar_bar1 at zabarem:
            xalign -0.3
            linear 1 xalign .2
        pause 1
        "Wieczór w miarę zleciał, a ostatni goście zbierali się do wyjścia. Lia kątem oka zauważyła podchodzącego Ojca."
        p3 "Możesz iść spać. Prawie wszyscy już poszli, więc zaraz zamykamy. Dobranoc."
        show p3 at zabarem:
            linear 2 xalign -0.4
        "Powiedział bez emocji Ojciec, po czym ruszył w kierunku drzwi."
        stop ambient fadeout 3.0
        "Lia nie miała siły na jakąkolwiek reakcję, więc ruszyła po prostu do swojego pokoju."
        # TODO Na ekranie: Pokój P1 + P1 na środku
        scene anim_room_lia_nightdragon
        show p1 shadow
        with fade
        $ renpy.sound.set_volume(0.9, delay=0, channel='ambient')
        $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
        play ambient sfx_warm_evening_outdoors
        "Po krótkim, acz powolnym marszu dotarła do swojego pokoju i usiadła na chwilę na łóżku."
        show p1 bsad with fc
        "Miała ochotę zapłakać. Nie była jednak do końca pewna dlaczego..."
        "Czuła się tak, jakby była tylko narzędziem w rękach rodziców."
        "Wstań. Pracuj. Idź spać. Wstań. Pracuj. Idź spać. Tak właśnie wyglądało jej życie..."
        "Pomyślała przez moment czy mogłaby to zmienić. Czy w ogóle wiedziałaby jak zacząć."
        "\"Pewnie nie...\" - pomyślała. Przebrana w ciuchy do spania położyła się, a potem przykryła kołdrą."
        "Chciała zasnąć jak najszybciej. Czym prędzej zaśnie, tym prędzej przestanie myśleć o swoim życiu."
        stop ambient fadeout 2.0
        $ renpy.sound.set_volume(1, delay=0, channel='ambient')
        $ renpy.sound.set_pan(0, delay=0, channel='ambient')
        "..."
        jump epizod5

################################################################################
#############################   EPIZOD CZWARTY   ###############################
label epizod4:
    #if config.developer:
    #    scene black
    #    show text "epizod4" at truecenter
    #    pause
    # Na ekranie: Las (szereg drzew) + P1
    scene forest_day:
        align (0.1,0.4)
        zoom 0.8
    show p1
    with fade
    $ renpy.music.set_volume(0.3, delay=0, channel='music')
    "Po wyjściu z domu, Lia skierowała się od razu w kierunku wioski."
    "Wybrała ścieżkę przez las. Trasa nie należy może do najprzyjemniejszych, głównie przez mroczny klimat, ale na pewno do bezpiecznych i szybkich."
    # Na ekranie: Wioska w oddali
    scene forest_village_dragonevening with fade:
        zoom 0.5
    "Po niecałej godzinie Lia dotarła na miejsce. W oddali słychać było bawiących się ludzi."
    "Gdy powoli zbliżała się do wioski, poczuła delikatne ukłucie niepewności."
    # Na ekranie: Dodajemy P1 (sad) zwracającą się do gracza
    show p1 bsad wink_player with Dissolve(.2)
    p1 "Eh, nie wiem czy to jednak dobry pomysł... Co mam tutaj w zasadzie robić?"
    p1 "Nie potrafię się bawić. Może lepiej wróćmy do domu?"

    menu:
        "Nieee! Chodźmy zobaczyć ludzi!":
            gr "Nie wygłupiaj się. Już tu jesteśmy. Chodźmy zobaczyć ludzi!"
            # NE: TODO Wioska, zoom na rynek + P1 smile
            scene anim_festival_night_dragon:
                align (-3.0,-1.6)
                zoom 0.8
            show anim_festival_walking_shadows
            show p1 lsmile:
                align (.3,1.0)
            with fade

            $ renpy.music.set_volume(0.3, delay=0, channel='music')
            play music peritune_market fadein 3.0
            "Lia ruszyła powolnym krokiem w stronę bawiących się ludzi."
            "Starała się do nikogo nie zbliżać... jeszcze ktoś wziąłby ją do tańca."
            "Wolała o tym nie myśleć. Skoro już tu była to wolała nie przeżywać żadnego większego stresu."
            "Skupiła się bardziej na obserwacji wszystkiego wokół, w końcu niezbyt często opuszczała okolicę Tawerny."

            # Na ekranie: Tutaj skupmy się na obserwacji samego Festiwalu, bez Lii
            hide anim_festival_walking_shadows
            hide p1 with dissolve
            "Minęła dłuższa chwila. Lia wciąż obserwowała wystrojoną wioskę, namioty z atrakcjami."
            show anim_festival_night_dragon with dissolve:
                # align (-3.0,-1.6) zoom 0.8
                ease 5 yalign -0.1
            "A co najważniejsze, spoglądała w górę, na mieniące się zielenią niebo."
            "Przypomniała jej się matczyna opowieść o Festiwalu Smoka."
            "Raz na parę lat na niebie pojawia się ogromny Zielony Smok. Do dzisiaj nie wiadomo skąd!"
            "Nikt też nie wie kiedy pojawi się ponownie. Raz pojawia się co roku, a czasem co pięć lat."
            "Wszyscy są jednak zgodni, że jest to wspaniałe zjawisko."
            "Lia zastanawiała się czy legenda o Zielonym Smoku jest prawdziwa."
            "Słyszała już tyle różnych wersji, że nie wiedziała co o tym sądzić."
            "Jedno było pewne - Zielony Smok łączy się w jakiś sposób z ogromną wieżą stojącą w samym centrum królestwa."
            "Ludzie mówią, że to jego dom i właśnie stamtąd wyrusza zwalczać wszelkie zagrożenia dla mieszkańców wyspy."
            "Jednak nikt nie jest w stanie tego potwierdzić. Poza rodziną królewską nikt nigdy tam nie był."
            "Zresztą nawet oni niezbyt często się tam wybierają. Nie wiadomo kto i kiedy ją zbudował."
            "Wiadomo jednak tyle, że chroni ona w jakiś sposób naszą wyspę. To dzięki niej nic z zewnątrz nie zagraża mieszkańcom."
            "Dlatego nie ma zbyt wielu chętnych do kwestionowania tych opowieści. Zamiast tego wszyscy wolą się bawić podczas Festiwalu Zielonego Smoka."
            "Jest on tak istotny dla naszej kultury, że nawet księżniczka Aurora i jej brat, książę Caius odwiedzają wtedy wszystkie miasteczka i wioski."
            "A przynajmniej tak usłyszała od kilku gości w Tawernie."
            show anim_festival_night_dragon with dissolve:
                ease 4 yalign -2.0
            "Nie mogła doczekać się tej wizyty. Słyszała, że księżniczka jest bardzo piękna..."
            "Lia zaczęła wolno spacerować i jednocześnie próbowała ją sobie wyobrazić..."

            # Na ekranie: P1
            show anim_festival_walking_shadows
            show p1
            with dissolve
            "Tak się zamyśliła, że nie zauważyła idącego chłopaka, który niespodziewanie w nią uderzył!"
            # Na ekranie: P1 + niespodzianie wbija P5, # Meamir suprised ON # Lia suprised ON
            show p5 bsurprised at right with moveinright:
                xoffset -400
                #align (.6,.5)  #dopasować Lię
            with hpunch
            show p1 bsurprised with move:
                xoffset -100
                #align (.5,.5)
            "Lia prawie się przewróciła. Szybko złapała równowagę i spojrzała, że sprawcą był nieznajomy chłopak."
            show p1 with fc:
                xzoom -1.0
            # Meamir podpisany tutaj \"???\"
            p5q "Na Zielonego Smoka, przepraszam! Nie zauważyłem Cię. Wszystko w porządku?"
            #Lia normal ON
            show p1 -bsurprised
            p1 "Oj, tak... Nic się nie stało. Tylko troszkę się przestraszyłam..."
            # Meamir blush ON
            show p5 blush with fc
            p5q "Ojej, przepraszam raz jeszcze... Rozglądałem się i nie patrzyłem przed siebie."
            "\"Uroczy\" - Pomyślała Lia, ale odpowiedziała nie dając po sobie poznać zainteresowania:"
            p1 "Nic się nie stało. Naprawdę! Sama byłam zamyślona... to trochę też moja wina."
            # Meamir normal ON
            show p5 -blush with fc
            p5q "Oh, no dobrze! Ale na wszelki wypadek w ramach przeprosin może dasz się skusić na wspólne piwo?"
            "Lia i tak nie miała nic konkretnego do roboty, więc czemu nie."
            p1 "W zasadzie czemu nie, aleeeee... pod jednym warunkiem."
            p5q "Tak? Jakim?"
            # Lia smile ON
            show p1 lsmile with fc
            p1 "Musisz przynajmniej powiedzieć jak się nazywasz!"
            # Meamir smile ON
            show p5 lsmile with fc
            # Meamir dostaje podpis normalny już tutaj"
            p5q "Ahh, nie przedstawiłem się. Przepraszam!"
            p5 "Jestem Meamir, a Ty?"
            # Lia smirk ON
            show p1 bangry narrowedwink lsmile with fc
            p1 "No nie wiem czy zasłużyłeś... "
            # Meamir blush ON
            show p5 blush lsad with fc
            p5 "Oj... No to..."
            # Lia smile ON
            show p1 lsmile -bangry -narrowedwink with fc
            p1 "Oj no! Żartuję... jestem Lia!"
            p1 "Miło Cię poznać!"
            p5 "Heh, Ciebie też..."
            show p5 -lsad with fc
            "Odpowiedział Meamir lekko jeszcze zawstydzony. Delikatna pewność siebie wprawiła Lię w dobry nastrój."
            p1 "No no, nie czerwień się tak - chodźmy na to piwo!"
            # Meamir smile ON
            p5 lsmile "Dobrze, dobrze - chodźmy!"
            jump ep4piwo

        ##################### drugi wybor ###########################
        "Uspokój się. Chodź się napić!":
            gr "Uspokój się dziewczyno. Dopiero przyszliśmy. Chodźmy się napić!"
            # Na ekranie: Wioska, zoom na rynek + P1 smile
            scene anim_festival_night_dragon:
                align (0.5,0.5)
                pos (-0.1,-0.14)
                zoom 0.7
            show p1 lsmile:
                zoom 0.8
                xzoom -1
                align (.2,1.0)
            with fade
            $ renpy.music.set_volume(0.3, delay=0, channel='music')
            play music peritune_market fadein 3.0
            "Lia zauważyła skrzynię na której znajdowało się darmowe piwo."
            "Od zawsze wiadomo, że darmowe najlepsze! Pewnie ruszyła w zadanym kierunku."
            "Wzięła kufel z jakimś słabszym piwem i na chwilę przystanęła na boku, obserwując otoczenie."

            # Na ekranie: Tutaj skupmy się na obserwacji samego Festiwalu, bez Lii
            "Minęła dłuższa chwila. Lia wciąż obserwowała wystrojoną wioskę i namioty z atrakcjami."
            hide p1 with dissolve
            show anim_festival_night_dragon with dissolve:
                ease 6 ypos 0.35
            "A co najważniejsze, spoglądała w górę, na mieniące się zielenią niebo."
            "Przypomniała jej się matczyna opowieść o Festiwalu Smoka."
            "Raz na parę lat na niebie pojawia się ogromny Zielony Smok. Do dzisiaj nie wiadomo skąd!"
            "Nikt też nie wie kiedy pojawi się ponownie. Raz pojawia się co roku, a czasem co pięć lat."
            "Wszyscy są jednak zgodni, że jest to wspaniałe zjawisko."
            "Lia zastanawiała się czy legenda o Zielonym Smoku jest prawdziwa."
            "Słyszała już tyle różnych wersji, że nie wiedziała co o tym sądzić."
            "Jedno było pewne - Zielony Smok łączy się w jakiś sposób z ogromną wieżą stojącą w samym centrum królestwa."
            "Ludzie mówią, że to jego dom i właśnie stamtąd wyrusza zwalczać wszelkie zagrożenia dla mieszkańców wyspy."
            "Jednak nikt nie jest w stanie tego potwierdzić. Poza rodziną królewską nikt nigdy tam nie był."
            "Zresztą nawet oni niezbyt często się tam wybierają. Nie wiadomo kto i kiedy ją zbudował."
            "Wiadomo jednak tyle, że chroni ona w jakiś sposób naszą wyspę. To dzięki niej nic z zewnątrz nie zagraża mieszkańcom."
            "Dlatego nie ma zbyt wielu chętnych do kwestionowania tych opowieści. Zamiast tego wszyscy wolą się bawić podczas Festiwalu Zielonego Smoka."
            "Jest on tak istotny dla naszej kultury, że nawet księżniczka Aurora i jej brat, książę Caius odwiedzają wtedy wszystkie miasteczka i wioski."
            "A przynajmniej tak usłyszała od kilku gości w Tawernie."
            show anim_festival_night_dragon with dissolve:
                ease 6 ypos 0.1
            "Nie mogła doczekać się tej wizyty. Słyszała, że księżniczka jest bardzo piękna..."
            "Lia zaczęła wolno spacerować i jednocześnie próbowała ją sobie wyobrazić..."

            # Na ekranie: P1
            show p1 at center with dissolve:
                xzoom -1
            "Tak się zamyśliła, że w pewnym momencie na coś wpadła. Wylała przez to cały swój trunek!"
            # Na ekranie: P1 + niespodzianie wbija P5  # Meamir suprised ON  # Lia suprised ON
            show p1 bsurprised widenedwink with fc:
                align (.5,1.0)  #dopasować Lię
            with hpunch
            show p5 bsurprised behind p1 with dissolve:
                align (.7,1.0)
            "Mocno zaskoczona Lia spostrzegła, że uderzyła w jakiegoś chłopaka!"
            show p1 bsad wink with fc
            show p1 with move:
                align (.38,1.0)
            p1 "Ojej, przepraszam! Zamyśliłam się..."
            # Meamir podpisany tutaj \"???\"
            # Meamir smile ON
            show p5 bneutral lsmile with fc
            p5q "Hah, nic się nie stało! Sam byłem trochę nieuważny!"
            # Lia normal ON
            show p1 bneutral with fc
            "Zaskoczenie minęło, lecz mimo wszystko nie wiedziała co mu odpowiedzieć."
            show p1 blush with fc
            "Nieznajomy cały czas się uśmiechał. \"Uroczy uśmiech\" - pomyślała Lia"
            show p1 -blush with fc
            p5q "Także nie przejmuj się! Nie ma co płakać nad rozlanym piwem. Powiedziałbym nawet, że chyba jestem Ci jedno winny!"
            "Lia nie była do końca pewna co powiedzieć, ale w jakiś sposób nieznajomy ją zainteresował."
            p1 "Oh, no nie wiem... Przecież nawet nie wiem jak się nazywasz!"
            p5q "Oj, mój błąd! Przepraszam, nazywam się Meamir!"
            # Meamir dostaje podpis normalny już tutaj
            p5 "A Ty jak? Zdradzisz mi swoje imię?"
            p1 "Hah, a zdradzę - nazywam się Lia"
            p5 "Ślicznie! Nie znałem wcześniej nikogo o takim imieniu!"
            p5 "To co, piwo?"
            "Lia stwierdziła, że w sumie czemu nie. I tak nie miała nic konkretnego do roboty."
            p1 "No dobrze. Chodźmy!"
            jump ep4piwo

    label ep4piwo:
        # Na ekranie: jako BG zoom na skrzynkę z piwem, żeby na środku była, lewo P1 i prawo P5
        #scene anim_festival_night_dragon:
        #    align (0.5,1.0) zoom 0.8
        #    pos (-0.44,-0.36)
        scene anim_festival_night_dragon:
            align (0.5,0.5)
            pos (-0.1,-0.14)
            zoom 0.7
        show festival_skrzynka_night
        # Lia and Meamir smile ON
        show p1 lsmile:
            align (.2,1.0) xzoom -1
        show p5 lsmile:
            align (.8,1.0)
        with fade
        "Lia i Meamir dotarli do miejsca, w którym można było poczęstować się piwem."
        "W zasadzie było całkowicie darmowe, więc bardziej odebrała to jako miły gest."
        "Meamir nalał do pełna dwa kubki. Pierwszy podał Lii."
        p5 "Proszę bardzo, ten dla Ciebie."
        p1 "A dziękuję bardzo."
        "Dwójka wpatrywała się w siebie bez słowa, sącząc powoli swoje napoje."
        "\"Uroczy jest\" - Pomyślała Lia."
        "\"Śliczna jest\" - Pomyślał Meamir i jako pierwszy postanowił przerwać krótką ciszę."
        p5 "Hmm... jesteś stąd?"
        # Lia neutral ON
        show p1 -lsmile with fc
        "\"Dziwne pytanie\" - pomyślała Lia - \"Mógł się bardziej postarać, no ale dobra.\""
        p1 "Hmm, nie do końca. Mieszkam co prawda niedaleko, ale nie dokładnie tutaj."
        p5 "A gdzie?"
        p1 "Eee, niedaleko - przy Tawernie na rozdrożach. Dlaczego pytasz?"
        # Meamir neutral ON
        show p5 -lsmile with fc
        p5 "Ah, wybacz, że tak dopytuję. Dopiero się wprowadziliśmy i poznaję okolicę."
        p1 "Oo, nie wiedziałam, że ktoś się ma wprowadzić. Słyszałam, że nowy kowal ma być..."
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Hah, to właśnie my. Znaczy bardziej mój Ojciec."
        # Meamir neutral ON
        show p5 -lsmile with fc
        p5 "O mnie zapewne nikt nie wspominał. Nie jestem zbytnio interesujący."
        p1 "Oj, nie przesadzaj. Na pewno nie jest tak źle! Zresztą kowal to istotne stanowisko!"
        p1 "Kilka osób nie mogło się już doczekać nowego, po tym jak poprzedni zniknął."
        p5 "Hmm, pewnie masz rację. No ale przynajmniej wiesz dlaczego zadaję tyle pytań."
        p5 "Nie chciałem wyjść na wścibskiego. Po prostu jestem ciekaw co skrywa przede mną okolica."
        p1 "Rozumiem. Byłam po prostu lekko zaskoczona! Więc... jak Ci się podoba nasza okolica?"
        p5 "Po dzisiejszym wieczorze na pewno znacznie bardziej!"
        # Lia blush ON
        show p1 blush with fc
        p1 "O, a to dlaczego? Stało się coś ciekawego?"
        # Meamir smirk ON
        show p5 bangry narrowedwink lsmile with fc
        p5 "A nie wiem, całkiem możliwe. Wiesz, każdy dzień może przynieść coś nowego... coś bardzo interesującego."
        # Meamir smile ON # Lia smile ON
        show p1 lsmile with fc
        show p5 -bangry -narrowedwink lsmile with fc
        p1 "I mówisz, że ten właśnie coś takiego przyniósł?"
        p5 "Dokładnie to mam na myśli."
        p1 "Czyli co dokładnie?"
        p5 "Oj no, przecież wiesz."
        # Lia neutral ON
        show p1 -lsmile -blush with fc
        p1 "Właśnie chyba nie do końca..."
        p5 "Oj no! Nie bądź już taka skromna!"
        # Lia blush ON
        show p1 blush with fc
        p5 "Cieszę się, że dzisiaj na siebie \"wpadliśmy\"! W innym wypadku nie miałbym chyba tutaj nic do roboty."
        # Lia smile ON
        show p1 lsmile with fc
        p1 "Oh, to bardzo miłe. W sumie też się cieszę."
        p1 "Sama nie miałam pojęcia co będę tutaj robić..."
        p5 "No widzisz! Hmm, chciałabyś może się jeszcze gdzieś przejść?"
        # Lia neutral ON
        show p1 -lsmile -blush with fc
        p1 "Hmm, wiesz co... Bardzo chętnie, ale robi się już trochę późno. Powinnam wracać."
        # Meamir sad ON
        show p5 bsad lsad with fc
        p5 "Oj no! Chcesz już uciekać? Przecież jeszcze nie jest tak późno! Zostań jeszcze trochę!"
        # Meamir neutral ON
        show p5 -bsad -lsad with fc
        p1 "Chciałabym, ale jeszcze muszę dotrzeć do domu - nie chcę, żeby rodzice się martwili!"
        p5 "Ah, no dobrze - rozumiem... To ostatnie pytanie - co porabiasz na co dzień, pomagasz w Tawernie?"
        p1 "Hah, tak. A czemu pytasz?"
        p5 "To w takim razie może się jutro zobaczymy. Ojciec wysyła mnie po jakieś rzeczy."
        p1 "Oo, to bardzo fajnie! Nie ma w takim razie czym się przejmować skoro jutro się zobaczymy."
        p5 "Może znajdziesz wtedy chwilkę na rozmowę, co?"
        # Lia smile ON
        show p1 lsmile with fc
        p1 "A może, może... zobaczymy. A teraz uciekam, papa!"
        p5 "Dobrze, do zobaczenia!"
        stop music fadeout 10.0
        "Lia uśmiechnęła się, pomachała i ruszyła w kierunku domu."
        scene anim_tavern nighttime dragon with fade
        "W drodze powrotnej myślała o tym dniu. Nie sądziła, że tak nagle może wydarzyć się tyle interesujących rzeczy. Była ciekawa co przyniosą jej kolejne dni."
        # Przejście do E5
        jump epizod5

################################################################################
#############################   EPIZOD PIATY   #################################
label epizod5:

    #if config.developer:
    #    scene black
    #    show text "epizod5" at truecenter
    #    pause

    $ renpy.music.set_volume(0.5, delay=0, channel='musictight')
    play musictight the_old_tower_inn fadein 1.0
    ################## jesli BYLISMY na festiwalu [ep4] ##################
    if d_gofestiwal:
        # Na ekranie: animacja noc - dzień, zewn
        scene anim_tavern nighttoday dragon with dissolve
        pause 6
        # Na ekranie: Pokój P1 - słońce wyżej niż niżej
        scene anim_room_lia_noondragon with fade
        $ renpy.sound.set_volume(0.5, delay=0, channel='ambient')
        $ renpy.sound.set_pan(-0.4, delay=0, channel='ambient')
        play ambient sfx_morning_ambience
        "Gdy Lia otworzyła oczy, Słońce powoli podbijało niebo."
        "Była wypoczęta, mimo że poszła spać dość późno jak na jej standardy."
        "Nie usłyszała, żeby ktokolwiek ją budził lub wołał, ale mimo wszystko ubrała się i ruszyła w stronę kuchni."
        # Na ekranie: Kuchnia, Lia wchodzi od prawej. Nikogo więcej nie ma
        stop ambient
        $ renpy.sound.set_volume(1, delay=0, channel='ambient')
        $ renpy.sound.set_pan(0, delay=0, channel='ambient')
        scene room_kitchenday with fade
        show p1 with moveinright:
            align (.7,1.0)
        "Lia weszła do kuchni. Zauważyła, że już dawno po śniadaniu."
        "Czekała na nią tylko mała przekąska dla spóźnialskich. Zjadła ją i ruszyła w kierunku Głównej Sali."
        # Na ekranie: Bar, P3 już jest + wchodzi P1
        scene tavern_main_bar_bg0
        show p3 at zabarem:
            xalign 0.5 xzoom -1
        show tavern_main_bar_bar1
        with fade
        show p1 at zabarem behind tavern_main_bar_bar1 with moveinleft:
            xzoom -1
        "Gdy tam dotarła - zauważyła, że Ojciec już na nią czekał."
        p3 "Wreszcie jesteś. Muszę dziś zająć się kilkoma sprawami, więc będę później."
        p1 "No dobrze."
        "Powiedziała Lia bez większego zdziwienia. Nie było to nic nadzwyczajnego."
        show p3 at zabarem:
            linear 1 xalign -0.15
        show p1 at zabarem with move:
            xalign 0.5
        "Ojciec już wychodził, ale szybko się cofnął i powiedział jeszcze przed wyjściem:"
        show p3 at zabarem with fc:
            xzoom 1
            linear .5 xalign 0.0
        show p1 at zabarem with fc:
            xzoom 1
        p3 "Aha, Lia - ktoś z namiotu przyjdzie po prowiant. Już zapłacili, więc po prostu wydaj im tę paczkę."
        # Na ekranie: P3 wychodzi
        show p3 at zabarem with fc:
            xzoom -1
            linear 1 xalign -0.45
        "Powiedział Ojciec, po czym ruszył w swoim kierunku. Lia lekko się zamyśliła."
        "Kilkukrotnie widziała już tajemnicze osoby z namiotu, jednak do dzisiaj nie dowiedziała się kim oni są."
        "Przybyli kilka dni temu i rozstawili się obok Tawerny. Nie było w tym nic nadzwyczajnego - podróżnicy często tak robili."
        "Tutaj kwestia dotyczyła bardziej aury, którą emanował ich namiot."
        "Wiecznie się czają. Czasem ktoś przyuważy jednego z nich w Wiosce."
        "Czasami po prostu spacerują wzdłuż okolicznych dróg."
        "W Tawernie pojawiali się tylko po prowiant. Lia nigdy nie była w stanie przyjrzeć się ich twarzom. To wszystko przez te ich wielkie kaptury."
        "Lia nie wiedziała do końca co o nich sądzić. W pewien sposób ją przerażali."
        "Mimo wszystko Tata powiedział jej, że nie ma się czym martwić. Wkrótce pewnie znikną."
        "\"Płacą dobrze to nie wypada ich niepokoić\" - mówił ucinając jednocześnie temat."
        "Lia mogła jedynie rozmyślać, lecz dźwięk zbliżających się gości zmusił ją do odłożenia tego na później."
        "Pierwsi goście powoli zaczęli napływać przez drzwi. Dzień w Tawernie oficjalnie się rozpoczął."
        # Na ekranie: Tawerna z zewnątrz, minie kilka godzin
        scene anim_tavern outside dragon with fade
        pause 7
        # Na ekranie: Bar + P1
        scene tavern_main_bar_bg0
        show p1 at zabarem:
            xalign 0.5 xzoom -1
        show tavern_main_bar_bar1
        with fade
        "Minęło kilka godzin, gdy nagle spomiędzy gości wyłoniła się tajemnicza postać. Zbliżyła się ona do baru."
        # TODO Na ekranie: Od prawej TajemniczyGosc1
        show hidden_dude with moveinright:
            align (.8,1.0)
        show p1 at zabarem with fc:
            xzoom -1
        tg1 "Ja po prowiant."
        "Lia odruchowo skierowała wzrok w stronę paczki, chcąc podać ją mężczyźnie w kapturze."
        "Nie zdążyła się nawet schylić, gdyż enigmatyczny jegomość sam zdążył się obsłużyć kierując się jej wzrokiem."
        # TODO Na ekranie: tajemniczy gość wychodzi
        hide hidden_dude with moveoutright
        "Chwycił zgrabnie zamówione przedmioty i wyszedł tak samo powoli jak wcześniej wszedł."
        "Lia lekko westchnęła, po czym wróciła do swojej pracy."
        # Na ekranie: Tawerna z zewnątrz, mija parę godzin
        scene anim_tavern outside dragon with fade
        pause 7
        # Na ekranie: Lia za barem
        scene tavern_main_bar_bg0
        show p1 at zabarem:
            xalign .3
        show tavern_main_bar_bar1
        with fade
        "Lia stała tyłem do baru, gdy nagle zza pleców usłyszała znajomy głos."
        p5 "Hej Lia! Dzień dobry!"
        # Na ekranie: Wjeżdża P5
        show p5 with moveinright:
            align (.8,1.0)
        show p1 at zabarem with fc:
            xzoom -1
        p1 "O, hej Meamir! Dzień dobry!"
        p5 "Jak Ci mija dzień?"
        p1 "Standardowo, nic ciekawego. A Tobie?"
        p5 "To samo, nic ciekawego."
        # Meamir smile ON
        # Lia blush ON
        show p1 blush with fc
        show p5 with move:
            xalign .6
        show p5 lsmile with fc
        p5 "Robi się jednak coraz ciekawiej..."
        p1 "Znów się wygłupiasz!"
        # Lia smile ON
        show p1 lsmile with fc
        p5 "No dobrze, dobrze... To ten, przyszedłem po zamówienie..."
        "Meamir jednak nie otrzymał szansy na zakończenie swojej wypowiedzi, gdyż za barem pojawił się ojciec Lii."

        ######################## mid #################
        # Na ekranie: P1 za barem, P5 przed barem po prawej, P3 za barem bardziej po prawej stronie
        # Emocje: neutral
        show p3 behind tavern_main_bar_bar1,p1 at zabarem with dissolve:
            xalign .0
        show p1 -lsmile -blush with fc
        show p5 -lsmile with fc
        "Spojrzał na młodego chłopaka, zlustrował go dokładnie wzrokiem, po czym powiedział:"
        p3 "Meamir, tak? Miałeś być później."
        show p1 at zabarem with fc:
            xzoom 1
        p5 "Ah, tak to prawda. Udało mi się wyrobić trochę wcześniej..."
        p3 "Ha, no ładnie. No nic, zaraz wszystko przygotuję. Poczekaj chwilę."
        show p3 at zabarem:
            linear 3 xalign -0.45
        pause 3
        # Na ekranie: P3 wychodzi w lewo
        "Młodzieńcom nie pozostało nic innego jak poczekać. Meamir postanowił wykorzystać ten moment na rozmowę."
        show p5 with fc
        show p1 at zabarem with fc:
            xzoom -1
        hide p3
        ######################## /mid ################

        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Wczoraj było bardzo przyjemnie... może dziś też chciałabyś gdzieś wyjść?"
        p5 "Może spacer pod wieczór? Co myślisz?"
        "Lia w duchu ucieszyła się z tej propozycji."
        "Chyba wiedziała co chce odpowiedzieć."
        p1 "Oh, właściwie czemu n..."
        show p1 widenedwink bsurprised with fc
        show p5 -lsmile widenedwink bsurprised with fc
        stop musictight
        $ renpy.music.set_volume(0.1, delay=0, channel='audio')
        $ renpy.music.set_pan(0.8, delay=0, channel='audio')
        play audio sfx_female_scream
        "Nagle przerwała, gdyż usłyszała przerażający krzyk z zewnątrz. Nie była pewna co lub kto to był."
        "Usłyszała zza pleców głos Ojca:"

    ######################## jesli nie bylismy na festiwalu [ep4] #########################
    else:

        # Na ekranie: Animacja noc - dzień, Tawerna zewnątrz
        scene anim_tavern nighttoday dragon with dissolve
        pause 6
        # Na ekranie: Pokój P1 - słońce niżej niż wyżej
        scene anim_room_lia_morning with fade
        "Gdy Lia otworzyła oczy, promienie Słońca powoli rozbijały zasłonę nocy."
        "Wciąż lekko zaspana, zaczęła się ogarniać."
        "Zdążyła w tym czasie usłyszeć od mamy:"
        p2 "No Lia! Szybko, szybko - śniadanie i do pracy!"
        "\"A co niby robię?\" - pomyślała Lia i po chwili ruszyła w kierunku kuchni."
        # Na ekranie: Kuchnia, Lia wchodzi od prawej. P2 + P3 już po lewej sobie stoją
        scene room_kitchenmealday
        show p3:
            align (.05,1.0)
        show p2:
            align (.3,1.0)
        with fade
        show p1 with moveinright:
            align (.75,1.0)
        "Gdy Lia dotarła wreszcie do kuchni - rodzice kończyli już przygotowania do śniadania."
        p1 "Dzień dobry."
        "Powiedziała wchodząc. Ojciec tylko zerknął, a odpowiedziała Matka:"
        show p2 with fc:
            xzoom -1
        p2 "Dzień dobry Córko. Jak Ci minęła noc?"
        p1 "A jak miała minąć? Normalnie."
        show p2 with dissolve:
            xzoom 1
        "Matka widząc, że próba rozpoczęcia rozmowy spełza na niczym - nie podejmowała dalszych starań. Przynajmniej chwilowo..."
        "Rodzina jadła przez chwilę w całkowitej ciszy. Ojciec skończył pierwszy."
        p3 "Dziękuję."
        "Powiedział, po czym wyszedł z kuchni zająć się swoimi sprawami."
        hide p3 with moveoutleft
        "Lia została sama z Mamą. Ta z kolei znów spróbowała zacząć rozmowę:"
        show p2 with fc:
            xzoom -1
        p2 "Słyszałam, że nowy kowal ma całkiem przystojnego syna."
        p1 "Hmm? I co w związku z tym?"
        "Powiedziała Lia, nie skupiając się zbytnio na tym co powiedziała Matka. Ciągle była gdzieś w swoim świecie - zamyślona."
        p2 "Może dziś go poznasz. Jego ojciec zamawiał jakieś rzeczy. Zakładam, że przyśle go aby to wszystko odebrał."
        p1 "Skoro trzeba to się z nim poznam."
        "Selene poddała się. Czuła w głosie swojej córki niechęć do jakiejkolwiek rozmowy."
        "Dokończyła swoje jedzenie i ruszyła ku wyjściu."
        p2 "Kończ jedzenie i do pracy Młoda Damo!"
        # Na ekranie: P2 wychodzi
        hide p2 with moveoutleft
        "Lia odprowadziła wzrokiem Matkę, po czym skupiła się na dokończeniu swojej porcji."
        "Zrobiła to w kompletnej i uwielbianej przez nią ciszy, a następnie ruszyła w stronę Głównej Sali."
        # Na ekranie: Bar, P3 już jest + wchodzi P1
        scene tavern_main_bar_bg0
        show p3 at zabarem:
            xalign .65 xzoom -1
        show tavern_main_bar_bar1
        with fade
        show p1 behind tavern_main_bar_bar1 at zabarem:
            xalign -0.3 xzoom -1
            linear 1.5 xalign 0.25
        "Po wejściu od razu zauważyła czekającego na nią Ojca. Bez dłuższej zwłoki powiedział:"
        p3 "Lia - dziś przez chwilę muszę się czymś zająć, więc dołączę do Ciebie później."
        p1 "No dobrze."
        "Powiedziała Lia bez większego zdziwienia. Nie było to nic nadzwyczajnego."
        show p3 at zabarem:
            linear 1 xalign -0.15
        show p1 at zabarem:
            linear 0.5 xalign 0.55
        "Ojciec już wychodził, ale szybko się cofnął i powiedział jeszcze przed wyjściem:"
        show p3 at zabarem with fc:
            xzoom 1
            linear .5 xalign 0.0
        show p1 at zabarem with fc:
            xzoom 1
        p3 "Aha, Lia - ktoś z namiotu przyjdzie po prowiant. Już zapłacili, więc po prostu wydaj im tę paczkę."
        # Na ekranie: P3 wychodzi
        show p3 at zabarem with fc:
            xzoom -1
            linear 1 xalign -0.45
        "Powiedział Ojciec, po czym ruszył w swoim kierunku. Lia lekko się zamyśliła."
        "Kilkukrotnie widziała już tajemnicze osoby z namiotu, jednak do dzisiaj nie dowiedziała się kim oni są."
        "Przybyli kilka dni temu i rozstawili się obok Tawerny. Nie było w tym nic nadzwyczajnego - podróżnicy często tak robili."
        "Tutaj kwestia dotyczyła bardziej aury, którą emanował ich namiot."
        "Wiecznie się czają. Czasem ktoś przyuważy jednego z nich w Wiosce."
        "Czasami po prostu spacerują wzdłuż okolicznych dróg."
        "W Tawernie pojawiali się tylko po prowiant. Lia nigdy nie była w stanie przyjrzeć się ich twarzom. To wszystko przez te ich wielkie kaptury."
        "Lia nie wiedziała do końca co o nich sądzić. W pewien sposób ją przerażali."
        "Mimo wszystko Tata powiedział jej, że nie ma się czym martwić. Wkrótce pewnie znikną."
        "\"Płacą dobrze to nie wypada ich niepokoić\" - mówił ucinając jednocześnie temat."
        "Lia mogła jedynie rozmyślać, lecz dźwięk zbliżających się gości zmusił ją do odłożenia tego na później."
        "Pierwsi goście powoli zaczęli napływać przez drzwi. Dzień w Tawernie oficjalnie się rozpoczął."
        # Na ekranie: Tawerna z zewnątrz, minie kilka godzin
        scene anim_tavern outside dragon with fade
        pause 7
        # Na ekranie: Bar + P1
        scene tavern_main_bar_bg0
        show p1 at zabarem:
            xalign .5 xzoom -1
        show tavern_main_bar_bar1
        with fade
        "Minęło kilka godzin gdy nagle spomiędzy gości wyłoniła się tajemnicza postać. Zbliżyła się ona do baru."
        # Na ekranie: Od prawej TajemniczyGosc1, jakiś kolor trzeba wykminić + podpis \"???\"
        # TODO TAJEMNICZY GOSC
        show hidden_dude with moveinright:
            align (.8,1.0)
        tg1 "Ja po prowiant."
        "Lia odruchowo skierowała wzrok w stronę paczki, chcąc podać ją mężczyźnie w kapturze."
        "Nie zdążyła się nawet schylić, gdyż enigmatyczny jegomość sam zdążył się obsłużyć kierując się jej wzrokiem."
        # Na ekranie: tajemniczy gość wychodzi
        hide hidden_dude with moveoutright
        "Chwycił zgrabnie zamówione przedmioty i wyszedł tak samo powoli jak wcześniej wszedł."
        "Lia lekko westchnęła, po czym z powrotem wróciła do swojej pracy."
        # Na ekranie: Tawerna z zewnątrz, mija parę godzin
        scene anim_tavern outside dragon with fade
        pause 7

        scene tavern_main_bar_bg0
        show tavern_main_bar_bar1
        show p1 behind tavern_main_bar_bar1 at zabarem:
            xalign 0.2
        with fade
        "Lia stała tyłem do baru, gdy nagle zza pleców usłyszała przyjemny i interesujący głos:"
        # Tutaj Meamir będzie mówił, ale się dopiero poznają, więc na razie podpis \"???\" jego kolorem
        p5q "Dzień dobry! Hej!"
        show p1 at zabarem with dissolve:
            xzoom -1.0
        p1 "Dzień dobry."
        "Odpowiedziała Lia, lekko zdziwiona entuzjazmem nieznajomego."
        # Na ekranie: pojawia się oficjalnie P5 od prawej wchodzi
        show p5 with moveinright:
            align (.7,1.0)
        # Na ekranie: Lia za barem
        show p1 at zabarem:
            linear 1 xalign .4
        "Odwróciła się i zobaczyła młodego, dość przystojnego chłopaka. Ten od razu kontynuował:"
        #Tu można podpisać Meamira już
        p5 "Nazywam się Meamir! Przyszedłem po zamówienie mojego taty, znaczy się... Kowala."
        p1 "Oh, musisz chyba chwilkę poczekać. Mój tata spodziewał się Ciebie trochę później."
        p5 "Ah, rozumiem..."
        "Nastała chwila niezręcznej ciszy, którą spróbował przełamać Meamir"
        # Lia blush ON
        show p1 blush with fc
        # Meamir smile ON
        show p5 lsmile with fc
        p5 "Przepraszam, że pytam... Ale czy mógłbym poznać Twoje imię?"
        p1 "Oh, przepraszam - nazywam się Lia. Powinnam się przedstawić..."
        p5 "Nic się nie stało! Bardzo miło Cię poznać, śliczne imię!"
        p1 "Dziękuję!"
        # Na ekranie: P3 wchodzi na rejon
        show p3 behind p1,tavern_main_bar_bar1 at zabarem with moveinleft:
            xalign .0
        "W trakcie wymieniania tych uprzejmości do pomieszczenia wszedł Zorn."
        # Meamir neutral ON        # Lia neutral ON
        show p1 -blush with fc
        show p5 -lsmile with fc
        "Jego widok ostudził delikatnie gotujące się w pomieszczeniu emocje..."

        ######################## mid ##################
        # Na ekranie: P1 za barem, P5 przed barem po prawej, P3 za barem bardziej po prawej stronie
        # Emocje: neutral
        show p1 at zabarem with fc:
            xzoom 1
        "Spojrzał na młodego chłopaka, zlustrował go dokładnie wzrokiem, po czym powiedział:"
        p3 "Meamir, tak? Miałeś być później."
        p5 "Ah, tak to prawda. Udało mi się wyrobić trochę wcześniej..."
        p3 "Ha, no ładnie. No nic, zaraz wszystko przygotuję. Poczekaj chwilę."
        show p3 at zabarem:
            linear 3 xalign -0.35
        pause 3
        # Na ekranie: P3 wychodzi w lewo
        "Młodzieńcom nie pozostało nic innego jak poczekać. Meamir postanowił wykorzystać ten moment na rozmowę."
        hide p3

        ####################### /mid ###################
        # Meamir smile ON
        show p5 with fc:
            xzoom 1
        show p5 lsmile with fc
        p5 "Pomagasz codziennie w Tawernie?"
        show p1 at zabarem with fc:
            xzoom -1
        "Lia zerknęła na Meamira. Pomyślała, że miał całkiem uroczy uśmiech."
        p1 "Tak. Pomagam, pracuję - w zasadzie głównie to robię."
        "Rozejrzała się, ale nie zauważyła żadnych potencjalnych gości. Mogła na chwilę oddać się rozmowie."
        p5 "Od dawna tu mieszkasz?"
        p1 "Całe życie w zasadzie... Dlaczego pytasz?"
        # Meamir neutral ON
        show p5 -lsmile with fc
        p5 "Ah, wybacz. Dopiero się wprowadziliśmy, więc chciałbym zorientować się w nowej okolicy."
        p5 "Mam nadzieję, że nie masz mi tego za złe..."
        # Meamir smile ON
        show p5 lsmile with fc
        # Lia smile ON
        show p1 lsmile with fc
        p1 "Nie! Bez obaw, tak tylko zapytałam... Nie pomyślałam w sumie, że możesz być ciekaw nowej okolicy - wybacz!"
        p5 "Ah, to dobrze. Robisz coś jeszcze na co dzień?"
        p1 "Hmm. W zasadzie to niezbyt. Nie miewam za wiele konkretnych planów."
        p5 "Hmm, to tak sobie myślę. Może zechciałabyś wyjść ze mną na spacer? Pokazać okolicę czy coś..."
        "Lię zaskoczyła ta propozycja. Nigdy wcześniej takiej nie usłyszała."
        "Początkowo nie była pewna co odpowiedzieć."
        p1 "Oj, hmm. Ciężko mi powiedzieć, w sumie czemu..."
        show p1 -lsmile widenedwink bsurprised with fc
        show p5 -lsmile widenedwink bsurprised with fc
        stop musictight fadeout 1.0
        $ renpy.music.set_volume(0.1, delay=0, channel='audio')
        $ renpy.music.set_pan(0.8, delay=0, channel='audio')
        play audio sfx_female_scream
        "Nagle przerwała, gdyż usłyszała przerażający krzyk z zewnątrz. Nie była pewna co lub kto to był."
        "Usłyszała zza pleców głos Ojca:"

    ########################### end #############################################
    # Na ekranie: Wchodzi P3
    show p3 with moveinleft:
        align (.05,1.0)
    show p5 with fc:
        xzoom -1
    $ renpy.music.set_volume(0.5, delay=3, channel='music')
    play music [alexander_nakarada_the_great_battle, alexander_nakarada_the_great_battle, "<silence 1000.0>"] fadein 15.0 fadeout 10.0
    p3 "Co tam się dzieje?"
    "Powiedział Ojciec wychodząc nagle z zaplecza. Przeraźliwy krzyk musiał dotrzeć nawet i tam."
    p3 "Idę to sprawdzić."
    hide p3 with moveoutright
    hide p5 with moveoutright
    "Ojciec wartko wyruszył w kierunku drzwi. Za nim ruszyło kilku innych gości Tawerny oraz Meamir."
    "Lia po kilku sekundach wahania pomknęła na zewnątrz. Ciekawość zwyciężyła..."
    #hide p1 with moveoutright
    # Przejście do E6 (tutaj płynnie wszystko)

################################################################################
#############################   EPIZOD SZOSTY   ################################
label epizod6:
    if config.developer:
        scene black
        show text "epizod6" at truecenter
        pause

    scene anim_tavern outside dragon
    # Na ekranie Tawerna (dzień) - po lewej 2 bandytów + p4 też po lewej obrócona do obwiesia
    show angry_man1:
        align (.01,1.0) xzoom -1
    show angry_man2:
        align (.25,1.0) xzoom -1
    show p4 bsurprised widenedwink lsad:
        align (.6,1.0)
        xzoom -1.0
    with fade
    "Wyglądało na to, że jacyś mężczyźni próbowali osaczyć dziewczynę."
    # Na ekranie wchodzi od prawej p3
    show p3:
        xzoom -1.0
        align (1.4,1.0)
    show p3:
        linear 1.1 align (.9,1.0)
    p3 "Halo, co tu się dzieje? Co to ma znaczyć? "
    "Nieznajomi odruchowo zerknęli po sobie. Nie wyglądali jednak na takich, co mają ochotę tłumaczyć się komuś obcemu."
    b1 "Nie Twój interes Elfie, wracaj do swoich spraw. Ta dziewczyna należy do nas!"
    p3 "Należy do Was? Ganiając za tą biedną dziewczyną musieliście chyba mocno uderzyć się w głowę."
    p3 "Osoba nie może być Waszą własnością, radzę..."
    b2 "Ja radzę Ci zamknąć ten niewyparzony ryj i nie wtrącać się w nie swoje sprawy kumplu."
    b1 "Dokładnie! Siedź tam cicho, a my zabieramy dziewczynę..."
    "Jeden z nich ruszył w kierunku nieznajomej dziewczyny, ale gdy wyciągnął po nią rękę - czas jakby niespodziewanie się zatrzymał."
    # TODO Na ekranie tutaj chciałby przedstawić jakoś kuku w główkę, może zamglony obraz \"od dołu\"
    with vpunch
    #hide angry_man1 with zoomout
    #hide angry_man2 with zoomout
    scene zorntheangel 1 at tr_beatupbyzorn
    show anim_beatupblink
    with dissolve
    "Obcy nie był w stanie w pierwszej chwili zrozumieć co się stało. Czuł ogromny ból głowy oraz pleców, a przez lekko otwarte powieki widział promienie Słońca. Prawie jakby leżał na ziemi."
    "W uszach nadal strasznie mu dzwoniło. Po paru sekundach usłyszał kolejne uderzenie."
    "Przeanalizował szybko czy to znów jakaś nieznana siła zaatakowała jego ciało, ale nie poczuł nic nowego. Usłyszał tylko przeraźliwy krzyk."
    show zorntheangel 2 at tr_beatupbyzorn
    with dissolve
    b2 "Kurwwaaaaa, mój noooos... zabijęęęę Cięęę! Auaaaaa....."
    "Domyślił się, że to jego kompan. Mimo ogromnego bólu spróbował wstać..."
    p3 "Powoli, bo się jeszcze bardziej połamiesz."
    show zorntheangel 3 at tr_beatupbyzorn
    with dissolve
    "Wstawał bardzo powoli. Głos brzmiał tak władczo, że nie sposób było się przeciwstawić."
    "Zresztą nie miał innego wyboru. Miał chyba złamane ze dwa żebra... a może jednak trzy."
    "Wstał."
    scene black
    pause 0.5
    # Na ekranie Tawerna, jeden bandyta leży na ziemi, drugi wstał, Zorn przy nim całkiem, Raven trochę odsunięta do tyłu
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
    p3 "A teraz słuchaj bardzo uważnie. Nie będę tego powtarzał:"
    p3 "Może i tego nie wiesz, ale w naszym Królestwie nie można być właścicielem drugiej osoby."
    p3 "Nie możesz ot tak powiedzieć, że ktoś jest Twoją własnością."
    p3 "Tym bardziej nie możesz tego robić przy mojej Tawernie."
    stop music fadeout 15.0
    # Na ekranie Zorn obraca się na prawo i mówi
    show p3 with fc:
        xzoom 1.0
    p3 "Lia!"
    # Na ekranie wchodzi Lia od prawej, stoi za Raven
    #show p1 with moveinright:
    show p1 behind p4:
        align (1.3,1.0)
        ease 1 align (.85,1.0)
    p3 "Zabierz ją do środka, a najlepiej na zaplecze! - zaraz tam przyjdę."
    # Na ekranie Zorn obraca się do bandziorów, Lia i Raven wychodzą na prawo
    show p3 with fc:
        xzoom -1.0
    show p1:
        linear .03 xzoom -1.0
        linear 1 align (1.35,1.0)
    show p4:
        linear .03 xzoom 1.0
        linear 1.2 align (1.35,1.0)
    p3 "A Wy... jeśli zobaczę was tutaj jeszcze raz to skończy się to znacznie gorzej."
    p3 "Radzę teraz się zebrać, przemyśleć swoje życie i najlepiej zacząć od nowa."
    p3 "A teraz bierz swojego kolegę, bo sam się nie ruszy i won mi stąd."
    # Na ekranie ładne przejście do kuchni, Raven po lewej, Lia po prawej

    scene room_kitchenday with fade
    show p1 with moveinleft:
        align (.4,1.0)
    show p4 with moveinleft:
        align (0.01,1.0)
    $ renpy.music.set_volume(0.5, delay=2, channel='music')
    play music [alexander_nakarada_emotionalism, alexander_nakarada_emotionalism, "<silence 1000.0>"] fadein 10.0
    "Obie dziewczyny stały obok siebie. Ani jedna, ani druga nie były w stanie nic powiedzieć."
    "Nieznajoma była w zbyt dużym szoku, a Lii brakowało pewności siebie."
    "Pomyślała jednak, że może warto spróbować..."
    p1 "Jak... Jak masz na imię? Czy wszystko dobrze?"
    "Nieznajoma spojrzała prosto na Lię. Wpatrywała się w nią z taką ciekawością, że aż lekko się zaczerwieniła."
    # Lia blush ON
    show p1 blush with fc
    "Zauważyła, że jej rozmówczyni lekko się zawstydziła. To równocześnie zawstydziło i ją samą."
    # Raven blush ON
    show p4 blush with fc
    "Jednocześnie dodało jej to także trochę pewności siebie."
    p4 "Nazywam się Raven... I taak, wszystkoo dobrze. Dziękuję..."
    p4 "A Ty jak się nazywasz?"
    # Lia smile ON
    show p1 lsmile -blush with fc
    p1 "Mam na imię Lia, miło Cię poznać!"
    "Powiedziała trochę formalnie Lia, po czym szybko dodała:"
    p1 "Co się stało? Jak tu trafiłaś?"
    # Raven surprised sad ON
    show p4 bsurprised lsad -blush with fc
    p4 "Ja.. Ja nie wiem, uciekałam i..."
    # Na ekranie p3 pojawia się po prawej
    show p3 with moveinright:
        align (.9,1.0) xzoom -1
    "Nagle do pomieszczenia wszedł Zorn."

    p3 "Załatwione! Tamtymi nie musisz się już martwić. Więcej nie powinniśmy ich zobaczyć."
    p3 "W ogóle, wszystko dobrze dziewczyno? Nie jesteś ranna czy coś?"
    "Raven nadal była lekko wystraszona. Powrót myślami do ucieczki sprowadzał dreszcze na całe ciało."
    p3 "Halo, Dziewczyno! Mówię do..."
    # Na ekranie p2 wchodzi od prawej, Lia niech dołączy po lewej do Raven 2on2
    show p2 with moveinright:
        align (.7,1.0)
    show p3 with move:
        xalign .99
    show p1 with move:
        xalign .3
    p2 "Zorn! Nie widzisz, że jest wystraszona?"
    p2 "Ja się tym zajmę. Idź proszę sprawdzić czy nie ma Cię w Głównej Sali."
    # Na ekranie p3 wychodzi w prawo spokojnym kroczkiem
    "Zorn popatrzył na żonę, lecz się jej nie sprzeciwił. Grzecznie wyszedł sprawdzić czy na pewno nie ma go w Głównej Sali."
    hide p3 with moveoutright
    p2 "Podejdź tu i mi się pokaż. Gdzieś Cię zranili?"
    # Raven sad ON + zbliża się do Selene jakoś na środku się ogarniają
    show p1 with move:
        xalign .02
    show p4 with move:
        xalign .35
    show p1 with fc:
        xzoom -1
    p4 "Niee, proszę Pani... Nie zdążyli..."
    p2 "Już wszystko dobrze, nie smuć się. Nazywam się Selene, a Ty? "
    p4 "Ra... Raven. "
    p2 "Piękne imię! Widzę, że wszystko rzeczywiście jest w porządku. "
    p2 "No już, nic Ci już nie grozi - widzę, że jesteś wykończona. Chciałabyś odpocząć? "
    "Raven nie wiedziała za bardzo co powiedzieć. Pierwszy raz spotkała się z takim podejściem."
    p2 "Dobrze... zakładam, że tak."
    p2 "Lia, weź ją proszę do pokoju gościnnego - tego na naszym piętrze. Pokaż jej co i jak oraz daj trochę odpocząć, dobrze?"
    p1 "Tak mamo. Chodź, Raven!"
    "Obie dziewczyny ruszyły na górę, Raven podążała spokojnie za Lią."
    "Po krótkiej wyprawie w głąb Tawerny dotarły do celu."
    # Na ekranie Pokój Raven, p1 wchodzi pierwsza od prawej do lewej, p4 za nią
    scene room_raven_evening_empty with fade
    show p1 with moveinright:
        align (.3, 1.0) xzoom -1
    show p4 with moveinright:
        align (.7, 1.0) xzoom -1
    "Lia weszła do pokoju pierwsza - Raven tuż za nią."
    p1 "No to ten pokój... Jakieś ubrania w razie czego masz w szafce, yyy... no i ten. To chyba wszystko. Potrzebujesz czegoś?"
    p4 "Nie, dziękuję. Jeśli mogę to chciałabym odpocząć..."
    p1 "Ah, oczywiście - już nie przeszkadzam. Jakbyś czegoś potrzebowała to wołaj, mam pokój prawie obok."
    p4 "Dziękuję."
    show p1 lsmile with fc
    "Lia tylko się uśmiechnęła, po czym wyszła i ruszyła w kierunku własnego pokoju."
    hide p1 with moveoutright
    # Na ekranie Pokój p1, Zorn po lewej, Lia wchodzi od prawej
    scene anim_room_lia_evening
    show p3:
        align (.3, 1.0)
    with fade
    show p1 with moveinright:
        align (.7, 1.0)
    "Weszła do środka - tam czekał na nią Ojciec."
    p1 "He-ej, o co chodzi?"
    p3 "Hmm? O nic! Chciałem tylko przyjść i sprawdzić czy wszystko dobrze."
    p1 "Tak, wszystko ok - Raven poszła się zdrzemnąć..."
    p3 "Pytałem bardziej o Ciebie."
    show p1 bsurprised with fc
    "Lia ledwo ukryła zdziwienie. Po chwili odpowiedziała:"
    show p1 -bsurprised with fc
    p1 "Yyy... wszystko dobrze... czemu miałoby coś być?"
    p3 "Noo... widziałaś co zrobiłem tym bandytom przed Tawerną."
    # Lia smile ON
    show p1 lsmile with fc
    p1 "Zasłużyli sobie! Poza tym nie byłam specjalnie zaskoczona - nie wyglądali na zbyt godnych przeciwników."
    "Lia, choć lekko zaskoczona swoją własną bezczelnością, nie pozwoliła aby z jej twarzy zszedł szeroki uśmiech."
    p3 "Hę? Widzę macie dzisiaj z matką nastrój na dokuczanie mi. No nic... grunt, że wszystko dobrze."
    "Powiedział Ojciec, po czym ruszył do wyjścia."
    # Na ekranie Zorn wychodzi powoli na prawo, Lia przechodzi na lewo
    show p3 with move:
        xalign .8
    show p1 with move:
        xalign .4
    show p1 with fc:
        xzoom -1
    p3 "Ci niby nie byli godni?! To jacy byliby???"
    hide p3 with easeoutright
    "Burknął jeszcze pod nosem Ojciec, po czym wyszedł z pokoju."
    "Lia została sama. Usiadła na łóżku i zaczęła myśleć."
    "Ledwo wieczór, a dzień przynióśł już tyle interesujących wydarzeń."
    "Może był to nawet najbardziej interesujący dzień w jej życiu... któż wie?"
    "Chwilowa pewność siebie nagle minęła, a negatywne myśli dały o sobie ponownie znać."
    "\"Co teraz?\" - pomyślała Lia, po czym powtórzyła to na głos jakby mogło to coś zmienić."
    p1 "Co teraz? Co tu zrobić... "
    gr "Powoli zaczęło mi się wydawać, że już nigdy nie zapytasz."
    # Na ekranie Lia na środek, zoom do rozmowy z graczem"
    hide p1
    show lia wink_player:
        align (0.5,0.0)
    with dissolve
    p1 "Oh? To Ty... W zasadzie to zapomniałam o Tobie... Przepraszam."
    gr "Zapomniałaś? Auć. Czyli to nie prośba o radę..."
    p1 "Przepraszam! W zasadzie to potrzebuję rady... Wybacz, dziś taki dzień - sporo się dzieje."
    gr "Wiem wiem, zgrywam się lekko. Rzeczywiście dzisiaj sporo się działo."
    gr "To jakie mamy opcje? Hmm?"
    p1 "Nie mam pojęcia, tyle się działo... z jednej strony mam ochotę schować się pod kołdrę i iść spać."
    p1 "Z drugiej jednak chętnie przeszłabym się za jakiś czas do Raven... wydaje się bardzo interesująca..."
    p1 "Na dodatek Meamir zapraszał mnie na wyjście. Przez to całe zamieszanie nawet się z nim nie pożegnałam..."
    p1 "Teoretycznie nie potwierdziłam, że pójdę... no ale... ahhh, co zrobić? Powiedz mi, proszę!"
    menu:
        "Wiesz co? Można by zerknąć co u Raven. Może nie teraz, ale za jakiś moment.":
            gr "Sporo przeszła. Było widać, że przy Tobie jej lepiej - sprawdź co u niej!"
            gr "Na pewno tego teraz potrzebuje."
            p1 "Oh, masz rację. Poczekam chwilę i do niej pójdę. Jeśli będzie spała to po prostu wrócę."
            jump epizod7p4
        "Zostawiłaś tego chłopaka bez słowa... Może warto się do niego przejść?":
            gr "Wiesz, możesz przeprosić i pójść na ten spacer - na pewno będzie miło!"
            p1 "Ah, możesz mieć rację! To chyba najlepsze wyjście skoro Raven i tak chciała odpocząć..."
            p1 "Tylko się ogarnę i idziemy!"
            jump epizod7p5
        "Powiem tak: kołdra i sen brzmi jak plan idealny!":
            gr "Najlepiej będzie się położyć i przemyśleć wszystko na spokojnie rano."
            p1 "Ah, pewnie masz rację - dziś sporo się działo. Tak będzie chyba najlepiej."
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
    scene room_raven_evening_empty with fade
    show p4:
        align (.3, 1.0)
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music [alexander_nakarada_adventure, alexander_nakarada_adventure, "<silence 1000.0>"] fadein 7.0
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
    gr "Nic się nie stało. Bardzo dobrze sobie poradziłaś!"
    p1 "Dziękuję! Za radę także... myślę, że wybrałam bardzo dobrze!"
    gr "Dobrze, że się zapytałaś i co najważniejsze... że udało się pomóc!"
    p1 "Oh, nie czuję zmęczenia. Chyba teraz w ogóle nie zasnę."
    gr "Bez przesady, trochę dziś się nabiegałaś! Położysz się i wkrótce zaśniesz, zobaczysz..."
    p1 "Ah, pewnie masz rację. Zresztą, jak zwykle! To się kładę, dobranoc!"
    gr "Dobranoc, śpij dobrze."
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
    $ renpy.music.set_volume(0.5, delay=0, channel='music')
    play music alexander_nakarada_now_we_ride fadein 7.0
    queue music alexander_nakarada_now_we_ride
    queue music "<silence 3.0>"

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
    p1 "To do zobaczenia, papa i dziękuję za spacer!"
    p5 "Ja też dziękuję - do zobaczenia! Dobranoc!"
    p1 "Dobranoc!"
    "Lia pomachała jeszcze na pożegnanie Meamirowi, po czym ruszyła w kierunku swojego pokoju."
    # Na ekranie: Pokój P1, Lia (neutral) na środku
    scene anim_room_lia_evening
    show lia:
        align (0.45,0.2) ypos .3 zoom 0.65
    with fade
    "Lia weszła do swojego pokoju, zamknęła drzwi i przystanęła na środku jakby niespodziewanie nawiedziła ją jakaś myśl."
    # Na ekranie: Pokój P1, Lia (sad) na środku - zoom zwraca się do gracza
    show lia lsad wink_player:
        linear .6 zoom 1.0
    p1 "Oh, przepraszam, że rozmawialiśmy dziś tak mało. Strasznie pokręcony dzień..."
    gr "Nic się nie stało. Bardzo dobrze sobie poradziłaś!"
    # Lia smile ON
    show lia lsmile with fc
    p1 "Dziękuję! Za radę także... myślę, że wybrałam bardzo dobrze!"
    gr "Dobrze, że się zapytałaś i co najważniejsze... że udało się pomóc!"
    p1 "Oh, nie czuję zmęczenia. Chyba teraz w ogóle nie zasnę."
    gr "Bez przesady, trochę dziś się nabiegałaś! Położysz się i wkrótce zaśniesz, zobaczysz..."
    p1 "Ah, pewnie masz rację. Zresztą, jak zwykle! To się kładę, dobranoc!"
    gr "Dobranoc, śpij dobrze."
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


################################################################################
###############################   EE-000  ######################################
label ee000:
    if config.developer:
        scene black
        show text "ee000" at truecenter
        pause
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
    show p1 lsmile
    p1 "Yyy.. Tak! Oczywiście. Nie martw się Raven, wszystko Ci pokażę!"
    # Blush Raven ON
    show p4 blush
    p4 "Ojej, bardzo Pani dziękuję. Tobie też, Lia. To pójdę od razu się przebrać."
    # Raven wychodzi
    show p4 -blush
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
    show lia wink_player:
        align (0.5,0.0)
    $ renpy.free_memory()
    p1 "Uff, co teraz..."
    gr "To zależy od Ciebie."
    p1 "Co dokładnie masz na myśli?"
    gr "Słyszałaś co powiedział Twój ojciec."
    gr "Musisz być bardziej odpowiedzialna. Sytuacja tego wymaga. Rodzice tego wymagają."
    p1 "Tylko jak? Jak mam... Eh, nie wiem..."
    gr "Czego nie wiesz?"
    p1 "Wszystkiego... W jednym momencie nic się nie dzieje. A teraz nagle tyle rzeczy..."
    gr "Myślałaś, że tak będzie całe życie?"
    p1 "Nie... Znaczy nie wiem..."
    gr "Lia. Rozumiem Twoje zmieszanie, ale posłuchaj mnie..."
    if d_koszmar:
        gr "Nie możesz ciągle odpuszczać. Wiem, że to trudne, ale musisz się postarać."
        gr "Już raz postąpiłaś leniwie. Niekoniecznie wyszło Ci to dobrze."
        gr "Pamiętasz?"
        p1 "Ten sen to był przypadek..."
        gr "Skąd możesz wiedzieć? "
        p1 "Bo..."
        gr "Nie, to nie był przypadek."
        p1 "Może i masz rację..."
        gr "Wiesz, że mam. Pamiętaj, że znam Cię bardzo dobrze. "
        gr "Czuję to samo co Ty, wiem co przeżywasz. Pozwól mi sobie pomóc."
    else:
        gr "Ostatnio udało Ci się przełamać rutynę. "
        gr "Może i nie wszystko poszło tak jak byśmy chcieli, ale czy nie czułaś się po wszystkim znacznie lepiej? "
        p1 "No chyba tak... Ale..."
        gr "Nie ma żadnego ALE. Było lepiej, wiem o tym. Przecież wiesz, że czuję wszystko tak samo jak Ty. "
        gr "Wiesz, że zależy mi na tym byś dobrze się czuła."
        p1 "No wiem... "
        gr "Więc nie masz się co martwić. Wszystko będzie dobrze!"
        gr "Razem damy radę, będę zawsze przy Tobie."

    p1 "No dobrze... To w sumie co mam zrobić? "
    gr "Wracamy do tego samego, musisz podjąć decyzję czego chcesz. Konkretnie. "
    # TODO Lia angry ON
    show lia lsad bangry narrowedwink_player with fc
    p1 "No ale skąd mam wiedzieć czego chcę! Przecież..."
    gr "Hej hej, spokojnie! Weź głęboki oddech. "
    # TODO Lia angry OFF
    show lia -lsad -bangry wink_player with Dissolve(0.5)
    gr "Dobrze. Teraz skup się, zajrzyj w głąb siebie. "
    gr "Wiem, że znajdziesz odpowiedź. "

    menu:
        "Mam przeczucie, że czeka na mnie coś więcej...":
            $ c_destiny = True
            p1 "Myślę, że może przede mną kryć się coś więcej."
            gr "Coś dokładnego masz na myśli?"
            p1 "Jeszcze nie wiem, ale myślę, że wkrótce się dowiemy."
            gr "Podoba mi się to podejście."
            # TODO Lia smile ON
            show lia lsmile with fc
            p1 "To co, zaczynamy?"
            gr "Prowadź."


        "Chciałabym być szczęśliwa i znaleźć kogoś...":
            $ c_hal = True
            p1 "Chciałabym być szczęśliwa. To musi być miłe."
            gr "Na pewno jest. Masz pomysł jak do tego doprowadzić?"
            p1 "Chyba tak. Chciałabym znaleźć kogoś z kim mogłabym być szczęśliwa."
            gr "Masz kogoś na oku?"
            p1 "Chyba tak. Myślę, że w tym Ty mi pomożesz."
            gr "W jaki sposób?"
            # TODO Lia smile ON
            show lia lsmile with fc
            p1 "Przecież wiesz! W wyborach! Sama się przecież nie zdecyduję głuptasie."
            p1 "Ale najpierw zabierzmy się do pracy! Dużo obowiązków przed nami."

        "Nie chcę niczego.":
            $ c_nothing = True
            p1 "Wiesz co. Ja po prostu nic nie chcę."
            p1 "Nie potrzebuję niczego..."
            gr "Dobrze wiesz, że tak nie jest..."
            p1 "Nie. Nie chcę niczego konkretnego."
            # TODO Lia angry ON
            show lia lsad bangry narrowedwink_player with fc
            p1 "To Twoja wina. Zostałam popchnięta do decyzji."
            p1 "Teraz ją zaakceptuj."
            gr "Dobrze..."
            p1 "A teraz chodźmy wypełnić obowiązki."
            p1 "I tak nic więcej na nas nie czeka w życiu."


    $ ee = 1
    hide lia with dissolve
    call screen podziekowanie with dissolve
    jump ee_tavern_mainroom # przejście do normalnej EE


################################################################################


return
