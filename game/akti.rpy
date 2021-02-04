
default pojscieDoLasu = False


label e1:

    ##jakby tu dodać jakąś krótką rozmowę, a może monolog nawet ‘gracza’ //
    ##przykład: Szkoda mi jej… Rzeczywiście strasznie monotonne życie. Dziewczyna mocno walczy ze swoimi emocjami i jest więźniem własnej rutyny. Może postaram się jej pomóc. Spróbuję dziś. //

    #Na ekranie: Ciemny ekran.
    #Harmider w tle (oddalające się głosy rozmów)
    #Dźwięk zamykanych drzwi
    "Harmider ciągnący się za opuszczającymi powoli Tawernę gośćmi w końcu zmieniał się w utęskniony spokój."
    #Na ekranie: CG z Tawerny (Lia oparta o drzwi z zamkniętymi oczami)"
    "Lia zamknęła drzwi za ostatnim gościem i ze zmęczeniem oparła się o ścianę wsłuchując się w ciszę, którą zakłócał jedynie trzaskający ogień w kominku."
    "..."
    #W tle cały czas delikatny dźwięk ognia, który teraz zanika (najlepiej do 5-6sec wyciszenie)""
    "Pomimo ogromnego zmęczenia znów utknęła na chwilę w swoich myślach."
    "Z dnia na dzień miała coraz bardziej dość tego życia."
    "”Wszystko jest tak monotonne i nudne.”"
    "”Wstań. Pracuj. Wykonuj polecenia. Idź spać. Wstań i znów pracuj. Ciągle to samo.”"
    "..."
    "”Uhhh… Mam dość tego wszystkiego powoli…”"

    menu:
        "gd Przesadzasz. Widać przecież, że jest w Tobie trochę życia.":
            p1 "Może i przesadzam."
            p1 "Może i jest trochę życia."
            p1 "Ale jak mam to stwierdzić jak nie znam nic innego."
            gd "To może czas coś poznać?"
            p1 "Niby co?"
            gd "Cokolwiek. Zróbmy coś po prostu."
            p1 "Nie wiem. Nie jestem przekonana..."

            #przejście do tabeli niżej

        "gd Nic nowego. Dziwne, że jeszcze to wytrzymujesz.":
            p1 "A co mam innego zrobić?"
            gd "Chwilowo wygląda na to, że nieważne co zrobisz to będzie już pójściem do przodu."
            p1 "Może."
            p1 "A może nie."
            p1 "Zresztą nawet nie wiem co można zrobić."
            gd " Coś wymyślimy. Warto spróbować."
            p1 "Nie wiem. Nie jestem przekonana..."

            #przejście do tabeli niżej

        "gd W takim razie otwórz drzwi i uciekaj od tego życia.":
            p1 "Co masz na myśli?"
            G: Zostaw to wszystko. Otwórz drzwi i uciekaj."
            p1 "…"
            G: Szybko. Teraz."
            p1 "Eh… W sumie czemu nie…"
            G: Biegnij!"
            #ujęcie komiks E1AC
            "I pobiegła."
            #czarny ekran, napis biały na środku
            "I tak Lia ruszyła przed siebie opuszczając obecne życie. Prawdopodobnie nikt już jej nigdy nie widział."
            # TODO w tle głos DUB01
            # TODO \Co to było? Cofnij. Teraz.\
            # TODO cofa grę do samego początku i usuwa tę opcję
            # TODO dostajemy achievement ACHIEV01

    # TODO w momencie pojawienia się tych opcji w tle poleci DUB02 (jednorazowo)
    menu:
        "gd Może pokazałabyś mi w końcu Twoje ulubione miejsce.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
            "Lia wstała i stanęła na równe nowi wpatrując się w drzwi."
            #Lia confused ON"
            p1 "Masz na myśli Ogród?"
            gd "Tak."
            p1 "No może…"
            gd "To na co czekamy?"
            #Lia surprised_neutral ON"
            p1 "Ale tak od razu? Teraz?"
            gd "Pewnie. Trzeba jakoś przełamać rutynę."
            #Lia surprised_happy ON"
            p1 "W sumie czemu nie…"
            gd "Super! No to chodźmy!"
            #Lia smile ON"
            p1 "Niech tak będzie!"

            #przejście do E1A

        "gd Nie ma sensu ciągle narzekać.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
            "Lia wstała i stanęła na równe nowi wpatrując się w drzwi."
            #Lia frown ON"
            p1 "No tak, a co mam niby robić?"
            #Lia angry ON"
            p1 "Zresztą myślisz, że narzekam bez powodu?"
            menu:
                "gd Nie.":
                    #relaxed Lia ON
                    p1 "No właśnie."
                    #Lia surprised_neutral ON"
                    p1 "To powiesz mi co mam zrobić?"
                    gd "A co z tym Twoim ulubionym miejscem?"
                    p1 "Co z nim?"
                    gd "Może byś mi je w końcu pokazała?"
                    p1 "Teraz?"
                    gd "Tak."
                    #Lia surprised_happy ON"
                    p1 "W sumie czemu nie…"
                    gd "Super! No to chodźmy!"
                    #Lia smile ON"
                    p1 "Niech tak będzie!"
                    #przejście do E1A

                "gd Tak.":
                    #disappointed Lia ON
                    p1 "Eh. Po co tu właściwie jesteś?"
                    gd "Już tłumaczę..."
                    #Lia annoyed ON"
                    p1 "Wiesz co. Nawet nic nie mów."
                    p1 "Średnio mnie to teraz interesuje."
                    p1 "Idę spać."

                    #przejście do E1B




        "gd To rób jak chcesz.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem"
            "Lia wstała i stanęła na równe nowi wpatrując się w drzwi."
            #Lia annoyed ON"
            p1 "Pff. Super pomoc."
            p1 "Dobra. To na razie."
            #przejście do E1B



label e1a:
    #w momencie przejścia w tle jest dźwięk: DUB03
    $ LovePath += 1

    p1 "Nim pójdziemy pokażę Ci to miejsce na mapie. Spójrz."
    #pokazuje się mapa, zoom na Tawernę"
    p1 "W tym miejscu jest Tawerna, tu jesteśmy."
    #zoom utrzymany z przejściem na secret garden"
    p1 "A tutaj mamy Sekretny Ogród do którego zaraz idziemy."
    #background stary las w nocy, przejście jak wcześniej było (ruch tła na zoomie, Lia powoli idzie od prawej do lewej)"
    p1 "Może i dobrze, że mnie do tego namówiłeś."
    p1 "Chodźmy. To niedaleko. Musimy przejść tylko kawałek przy lesie."
"
    p1 "W sumie jesteś tu ze mną pierwszy raz. To Stary Las."
    p1 "Ścieżka którą mijaliśmy prowadzi do wioski, ale mało kto z niej korzysta."
    p1 "Początkowo miała prowadzić do jakiejś kopalni, ale dawno już nikt się tym nie interesuje."
    #zatrzymanie się i lekki zoom na przejście między drzewami"
    p1 "O, to tutaj. Teraz tylko przecisnąć się przez las i zaraz jesteśmy na miejscu."
    #dźwięk przeciskania się i przejście w Sekretny Ogród, zmiana tła"
    p1 "Jesteśmy na miejscu."
    #przejście po całym tle, takie pokazowe całego miejsca, 5-7 sec"
    p1 "I jak? Podoba się?"

    menu:
        "gd Tak.":
            p1 "To fajnie."
            #neutral Lia ON"
            p1 "Tak czy inaczej."

        "gd Nie.":
            p1 "O nie!"
            #neutral Lia ON"
            p1 "Tak czy inaczej."

    #Lia thinking ON
    p1 "Tak się zastanawiam…"
    #sad_smile Lia ON"
    p1 "Może mogłabym tu przychodzić częściej."
    p1 "Nie wiem w sumie do końca czemu tego nie robiłam od dawna. Chociaż…"
    #surprised_neutral Lia ON"
    p1 "Chociaż może wiem… Chcesz też wiedzieć?"
    #smile Lia ON"
    p1 "A zresztą i tak Ci powiem."
    #sad_smile Lia ON"
    p1 "Myślę, że zaczynam wpadać w ten monotonny tryb życia, który forsują na mnie rodzice."
    p1 "Rodzice ciągle powtarzają mi, że mam ciężko pracować i być posłuszna."
    p1 "Tylko jaki to ma sens? Nie mam nic konkretnego z tego życia…"
    p1 "Nawet nie mam żadnych przyjaciół. Jedyna mi bliska osoba musiała wyjechać do WIELKIEJ stolicy… Eh."
    p1 "Może z Twoją pomocą spróbowałabym coś zmienić."
    p1 "Co myślisz? Pomożesz mi?"
    gd "Oczywiście! Zrobię co w mojej mocy."
    #dźwięk szelestu krzaczkowego w tle z 1sec opóźnienia"
    p1 "Dziękuję! Może…"
    #Lia shock ON"
    p1 "Zaraz. Słyszałeś to?"
    #komiks E1A ujęcie 1"
    p1 "Widzisz to? Ktoś tam chyba stoi?"
    p1 "Co mam zrobić?"

    menu:
        "gd Podejdź i sprawdź kto to.":
            # TODO +1 pkt PODEJDZLAS
            $ pojscieDoLasu = True
            #confused Lia ON
            p1 "No dobrze…
            #komiks E1A ujęcie 2
            "Gdy tylko Lia się zbliżyła to zauważyła, że postać zniknęła."
            p1 "Huh. Gdzie podziała się ta osoba?"
            gd "Nie wiem. Wyglądało jakby zniknęła na Twoich oczach."
            p1 "To prawda… Dziwne. Może mi się przewidziało."
            #powrót do normalnego ujęcia rozmowy z graczem"
            gd "Możesz mieć rację."
            #surprised_happy Lia ON"
            p1 "Dzięki."

        "gd Zawołaj. Zobaczymy kto to.":
            #confused Lia ON
            p1 "Hmm… No dobrze…"
            p1 "HALO, JEST TAM KTO?"
            "..."
            "W odpowiedzi jednak powróciła tylko cisza."
            #komiks E1A ujęcie 3"
            "Lia zbliżyła się lekko do drzewa."
            p1 "Huh. Nikogo tu nie ma."
            #powrót do normalnego ujęcia rozmowy z graczem"
            p1 "Musiało mi się to przewidzieć."
            gd "I przesłyszeć w sumie."
            p1 "W sumie tak."
            p1 "Ale w końcu to las, takie dźwięki to norma."
            gd "Prawda. Możesz mieć rację."
            #surprised_happy Lia ON"
            p1 "Dzięki."

    #neutral Lia ON
    p1 "Hmm. To jak, starczy przygód na jedną noc?"

    menu:
        "gd Tak! Wracajmy.":
            #smile Lia ON
            p1 "Świetnie! No to wracamy."

        "gd Nie. Zostańmy jeszcze.":
            p1 "Ehh… Co chcesz jeszcze tu robić?"
            #frown Lia ON"
            gd "W zasadzie to nie wiem."
            p1 "Świetnie. Mam pomysł. Może wracajmy?"
            #relaxed Lia ON"
            gd "Hmm. No dobra. Chodźmy."
            #smile Lia ON"
            p1 "Świetnie! Wracamy."


    #background zmiana na Tawerna z zewnątrz (wersja nocna ofc)
    "Lia wróciła do Tawerny szybko i bez żadnych problemów."
    "Myślała o tym, że czas ruszyć trochę swoje życie. Nie wiedziała jeszcze dokładnie jak."
    #zmiana tła na pokój P1 (ciągle noc), Lia w pozycji rozmowy z graczem"
    #happy Lia ON"
    p1 "Dzięki za ten spacer."
    p1 "Mam nadzieję, że teraz z Twoją pomocą uda się coś zmienić w moim życiu."
    p1 "Dobranoc!"
    gd "Dobranoc."
    #przejście w sen, taka mgiełka ładna i pojawia się CG_dream_good. Troszkę światła się majtają i efekt ekran przechodzi zoomem od dołu do góry, żeby jakoś tak zatrzymał się lekko na twarzy i potem poof budzi się
    #przejście do E2A

label e1b:
    #DUB04 - “try better next time”

    $ HatePath += 1
    #czarne tło
    "Obrażona na cały świat Lia ruszyła w stronę swojego pokoju."
    #background pokój Lii, wersja nocna i Lia w pozycji rozmawiającej z graczem"
    "Dotarła dość szybko do swojego pokoju i zatrzasnęła drzwi, które wydały głośniejszy huk niż się spodziewała."
    #shock Lia ON"
    "Przez moment nasłuchiwała z lekkim strachem czy nikogo nie obudziła."
    #annoyed Lia ON"
    "Po krótkiej chwili jednak odetchnęła i usiadła na łóżku."
    p1 "Dalej tu jesteś?"

    menu:
        "gd Tak.":
            #angry Lia ON
            p1 "To chyba tyle z łamania rutyny."
            p1 "Wielkie dzięki za pomoc."
            p1 "Dobranoc."

        "gd Wiesz, że teraz lepiej nie podpadać Twoim rodzicom.":
            #angry Lia ON
            p1 "Pff."
            p1 "Nagle tak się przejmujesz?"
            p1 "Widzę, że to tyle z łamania rutyny."
            p1 "Dobranoc."

        "gd ...":
            #angry Lia ON
            p1 "Racja. Lepiej nic nie mów."
            #very_sad Lia ON
            p1 "Najlepiej zostaw mnie samą sobie."
            #angry Lia ON
            p1 "Dobranoc."

    #po “dobranoc” powolne przejście w czarny ekran jakby sen, może lekka mgiełka?
    #tutaj odpala się zły sen
    #efekt mgiełki i przejścia w sen, jako background mamy ciemny las z postacią z pochodnią, powolny zoom na nią leci (podobnie jak było obecnie), zbliżenie trwa chwilę i nagle po paru sekundach wyskakuje CG_dream_bad może z jakimś creepy dźwiękiem i po sekundzie poof znika wszystko i Lia się budzi
    #po śnie przejście do E2B

label e2a:
    #na ekranie pokój P1 o brzasku
    "Lia otworzyła oczy wraz z pierwszymi promieniami słońca, które muskały jej twarz zza okna."
    "Delikatne ciepło, które poczuła zmotywowało ją od razu do wstania."
    "Uśmiechnęła się niespodziewanie do zbliżającego się dnia."
    #Lia pojawia się na ekranie, rozmowa z graczem"
    #smile Lia ON"
    gd "Dzień dobry!"
    #surprised_happy Lia ON"
    p1 "Oh! Dzień dobry!"
    #smile Lia ON"
    p1 "Dziękuję za wczoraj! Od razu jakoś lepiej się czuję."
    #happy Lia ON"
    p1 "Nawet nie mam chęci spać do południa!"
    p1 "Dobra, czas się ogarnąć. Widzimy się na śniadaniu."
    #korytarz jako tło, bez postaci"
    "Lia wyszła ze swojego pokoju wprost na Tawerniany korytarz."
    #Lia na ekranie, rozmawia z graczem"
    #Lia confused ON"
    p1 "Chyba nigdy nie mówiłam Ci nawet o tym co jest w samej Tawernie…"
    #Lia surprised_neutral ON"
    p1 "Powiedzieć Ci teraz?"
    menu:
        "gd Tak, chętnie posłucham.":
            #smile Lia ON
            p1 "Dobrze!"
            p1 "Zaraz obok mojego pokoju jest sypialnia rodziców. Czyli nic ciekawego."
            p1 "Tam z tyłu jest łazienka."
            #smirk Lia ON"
            p1 "Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada."
            gd "Haha, dobrze! Masz rację. Obiecuję, że nie będę."
            #smile Lia ON"
            p1 "Haha, no i super! Zaraz obok jest nasza jadalnia i kuchnia."
            p1 "Teoretycznie mieliśmy tam jeść, ale po co brudzić dwa miejsca."
            p1 "W związku z tym jemy na dole."
            #confused Lia ON"
            p1 "Tata chyba woli mieć zawsze oko na Tawernę."
            #smile Lia ON"
            p1 "No i jest mniej sprzątania!"
            p1 "Obok jest jedyny w naszym skrzydle pokój gościnny."
            p1 "Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty."
            p1 "No dobrze, to możemy iść dalej."

        "gd Nie, nie ma takiej potrzeby.":
            p1 "Oh. No dobrze, to chodźmy dalej."

    #background sala główna Tawerny, pusta. Lia na środku w pozycji rozmowy z graczem
    #confused Lia ON
    p1 "No dobra. Rodziców chyba jeszcze nie ma. W razie czego jesteś ze mną tak?"
    gd "Oczywiście. Cały czas."
    #Lia smile ON"
    p1 "Cieszę się. Dobra, wchodzę."
    #background zmiana na kuchnię, Lia po lewej patrzy w prawo"
    #od prawej wchodzi P2"
    #Lia smile ON"
    p1 "Dzień dobry Mamo!"
    #od prawej wchodzi P3, P2 się lekko przesuwa w lewo, żeby zrobić miejsce"
    p1 "Dzień dobry Tato!"
    #P2 i P3 patrzą na siebie, oboje confused ON"
    "Rodzice spojrzeli po sobie lekko zaskoczeni."
    "Nieczęsto ich córka była tak uśmiechnięta."
    "Zrodziło to lekkie podejrzenia."
    #P2 i P3 patrzą teraz na Lię, tj. w lewo"
    #neutral P2 i P3 ON"
    #confused Lia ON"
    p3 "Dzień dobry… Czy coś się stało?"
    p1 "Dlaczego miało się coś stać?"
    #P2 wychodzi na pierwszy plan (coś podobnego co wcześniej było)"
    #P2 smile ON"
    #surprised_sad Lia ON"
    p2 "Dziecko… Przecież Cię znamy. Co się stało?"
    #disappointed Lia ON"
    p1 "Ehh…"

    menu:
        "gd Powiedz im prawdę.":
            jump e2a1

        "gd Powiedz, że nic się nie stało.":
            #E2A2
            #confused Lia ON
            #P2 i P3 neutral ON
            p1 "Nic się nie stało. Naprawdę."
            p3 "Czyli mówisz, że jak tylko zamknęłaś Tawernę to poszłaś spać?"
            menu:
                "gd Powiedz, że tak. ":
                    p1 "Tak."
                    p3 "I po co kłamiesz?"
                    p1 "Nie kłamię…"
                    #angry Zorn ON"
                    p3 "Nawet nie zaczynaj."
                    #shock Lia ON"
                    p3 "Wiem, że Cię nie było w pokoju…"
                    #P3 patrzy na P2"
                    p3 "Nie mam do niej czasem siły."
                    #P3 patrzy na P1"
                    #small tears Lia ON"
                    p3 "Czekam na Ciebie w sali. Mamy sporo pracy."
                    #P3 wychodzi z kuchni"
                    p2 "Musisz być bardziej odpowiedzialna."
                    p2 "Nie możesz wychodzić nigdzie po nocy."
                    p2 "Coś mogło Ci się stać…"
                    p2 "Nie wybaczylibyśmy sobie tego."
                    #sad P2 ON"
                    p2 "Postaraj się być bardziej ostrożna."
                    #P2 wychodzi z kuchni"
                    #P1 do gracza, sad ON"
                    p1 "Nie wiem czy to była dobra rada…"
                    p1 "Ale mimo wszystko dzięki."
                    #Lia wychodzi z kuchni
                    $ e3a2 = True
                    #przejście do E3A2
                    jump e3

                "gd Lepiej powiedz prawdę.":
                    p1 "Nie…"
                    #angry Zorn ON"
                    p3 "Czyli co robiłaś?!"
                    #w tym miejscu idzie to samo co w E2A1, w całości

                    jump e2a1

        "gd [Nic nie mów.]":
            # TODO jump be01
            #przejście do BE01





label e2a1:
    # E2A1
    #sad_smile Lia ON
    p1 "Uhm. Po prostu byłam się przejść."
    #angry Zorn ON"
    #shock Lia ON"
    p3 "GDZIE?!"
    p3 "Nie każ mi czekać!"
    p2 "Zorn. Nie denerwuj się proszę."
    #confused Lia ON"
    p2 "Ja się tym zajmę. Ty może przejdź się do sali głównej i sprawdź czy Cię tam nie ma."
    p3 "Mhm. Może Tobie pójdzie sprawniej."
    p3 "Czekam na Ciebie Lia w sali. Mamy sporo pracy."
    #P3 wychodzi, P2 troszkę zbliża się do P1"
    p2 "Lia… Powiedz gdzie dokładnie byłaś."
    #P1 sad ON"
    p1 "W lesie… Znaczy w Ogrodzie dokładnie."
    p2 "Hmm. W tym Twoim Sekretnym Ogrodzie tak?"
    #sad_smile Lia ON"
    p1 "Tak… Byłam się tylko przejść."
    p2 "No rozumiem. Czy coś się stało jeszcze?"
    #sad Lia ON"
    p1 "Nic szczególnego, tylko…"
    p2 "Tylko co?"
    p1 "Eh… Myślałam, że kogoś widziałam. Ale jestem pewna, że mi się przewidziało."
    p2 "Hmm. Skąd pewność?"

    #jeśli 1pkt PODEJDZLAS
    if pojscieDoLasu:
        p1 "Poszłam sprawdzić… Nikogo nie było."
        p2 "Oh dziecko… Bardzo nierozsądnie."
        p2 "Najważniejsze, że nic się nie stało."

    #jeśli brak punktu PODEJDZLAS
    if not pojscieDoLasu:
        p1 "Zawołałam czy ktoś tam jest. Nikogo nie było."
        p2 "Nierozsądnie dziecko."
        p2 "Dobrze, że nic się nie stało."


    p2 "Musisz mi obiecać, że będziesz bardziej uważać w przyszłości."
    #smile P2 ON"
    p1 "No dobrze…"
    p2 "Cieszę się. Dokończ śniadanie i idź pomóż potem tacie."
    p1 "Dobrze mamo."
    #P2 wychodzi z kuchni"
    #sad_smile Lia ON, do gracza:"
    p1 "Dzięki za pomoc. Ciężko byłoby bez Ciebie."
    p1 "No nic, czas zabrać się do pracy."
    $ e3a1 = True
    jump e3
    #przejście do E3A1

label e2b
    # bez śniadania bo koszmar
    #na ekranie pokój P1, poranek
    "..."
    #od prawej wchodzi P3 angry
    "Lia gwałtownie wybudziła się z przerażającego snu gwałtownym wejściem ojca do pokoju."
    p3 "Nie słyszysz jak Cię wołam?"
    #Lia pojawia się po lewej, angry ON"
    p1 "Tato! Nie możesz tak wchodzić bez pukania. Co jakbym była rozebrana?!"
    #surprised_happy Lia ON"
    #neutral P3 ON"
    p3 "No dobrze dobrze, przepraszam - masz rację."
    p3 "Po prostu wołałem Cię całą chwilę i martwiłem się, że coś się stało."
    p3 "Ominęło Cię już śniadanie. Trzeba jeszcze przygotować Tawernę na otwarcie."
    #surprised_sad Lia ON"
    p3 "Czekam na Ciebie na dole."
    p1 "No dobrze dobrze, zaraz przyjdę."
    #P3 wychodzi z pokoju, P1 mówi do gracza"
    #sad_smile Lia ON"
    p1 "Dzień dobry."
    gd "Dzień dobry."
    p1 "Ten sen… Był dziwny. Był przerażający…"
    p1 "Nie rozumiem go."
    gd "To tylko sen. Nie przejmuj się."
    p1 "Może masz rację. Ale wciąż było to bardzo dziwne…"
    p1 "No nic. Trzeba się ogarnąć i czas do pracy. Znowu."
    "Lia wyszła ze swojego pokoju wprost na Tawerniany korytarz."
    #Lia na ekranie, rozmawia z graczem"
    #Lia confused ON"
    p1 "Chyba nigdy nie mówiłam Ci nawet o tym co jest w samej Tawernie…"
    #Lia surprised_neutral ON"
    p1 "Powiedzieć Ci teraz?"
    menu:
        "gd Tak, chętnie posłucham.":
            #smile Lia ON
            p1 "Dobrze!"
            p1 "Zaraz obok mojego pokoju jest sypialnia rodziców. Czyli nic ciekawego."
            p1 "Tam z tyłu jest łazienka."
            #smirk Lia ON"
            p1 "Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada."
            gd "Haha, dobrze! Masz rację. Obiecuję, że nie będę."
            #smile Lia ON"
            p1 "Haha, no i super! Zaraz obok jest nasza jadalnia i kuchnia."
            p1 "Teoretycznie mieliśmy tam jeść, ale po co brudzić dwa miejsca."
            p1 "W związku z tym jemy na dole."
            #confused Lia ON"
            p1 "Tata chyba woli mieć zawsze oko na Tawernę."
            #smile Lia ON"
            p1 "No i jest mniej sprzątania!"
            p1 "Obok jest jedyny w naszym skrzydle pokój gościnny."
            p1 "Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty."
            p1 "No dobrze, to możemy iść dalej."
        "gd Nie, nie ma takiej potrzeby.":
            p1 "Oh. No dobrze, to chodźmy dalej."

    "Lia dotarła do sali głównej gdzie czekał na nią ojciec."

    #przejście do #E3A3





label e3:

    if e3a1:
        #tło bar, P1 po lewej, P3 prawo za barem
        "Po wyjściu z kuchni na Lię czekał ojciec."
        #confused Lia ON
        p3 "Poczekaj moment Lia."
        p3 "Rozmawiałem moment z Twoją matką."
        p3 "Mimo, że byłaś nieodpowiedzialna to przyznałaś się co jest dobre."
        #surprised_neutral Lia ON"
        p3 "Możliwe, że trochę zbyt mocno Cię pilnujemy, więc mamy propozycję…"
        #surprised_happy Lia ON"
        p3 "Jeśli masz ochotę możesz dziś skończyć wcześniej pracę i przejść się na festiwal do wioski."
        p1 "Oh… Nie wiem co powiedzieć…"
        p3 "Po prostu powiedz czy chcesz iść."
        menu:
            "gd Powiedz, że chcesz.":
                # +1pkt FESTIVAL01
                $ d_gofestiwal = True
                #smile Lia ON
                p1 "Chętnie pójdę. Dziękuję."
                p3 "No dobrze… To przed wieczorem Cię zastąpię."
                p3 "Tymczasem czas na pracę."

            "gd Powiedz, że nie chcesz.":
                #sad_smile Lia ON
                p1 "Dziękuję za propozycję, ale nie chcę iść."
                p3 "Oh. No dobrze. Twoja decyzja."
                p3 "No to czas na pracę."

    elif e3a2:
        #tło bar, P1 po lewej, P3 prawo za barem - P3 angry ON
        p3 "No jesteś w końcu. Zostań chwilę."
        #surprised_sad Lia ON"
        p3 "Mam nadzieję, że następnym razem nie będziesz próbować kłamać."
        p3 "Zacznij być bardziej odpowiedzialna."
        p3 "A teraz chodź do pracy."
        #przechodzimy niżej


    else e3a3:
        #background sala główna, P1 lewo i P3 prawo stoją sobie
        p3 "O! Jesteś wreszcie. Chodź mi pomóc."
        #przechodzimy od razu niżej



    #background zmienia się na całą salę główną, P1 lewo i P3 prawo stoją sobie
    p3 "Dobra. Ja idę przygotować drugą salę. Ty zacznij od wytarcia stołów."
    p3 "Tylko dokładnie! Sprawdzę później."
    #P3 wychodzi do prawej sali. frown Lia ON, mówi do gracza:
    p1 "Zawsze tak mówi i potem i tak nie sprawdza... No ale i tak trzeba to ogarnąć."
    # odpala się mini gra ze stoliczkiem
    jump czyszcz

    #### Na ekranie: Minigra z wycieraniem stołu ########
label poczyszczeniustolu:

    if n == n_max:
        "Lia wyprostowała się, aby przyjrzeć się czy czegoś nie ominęła."
        "Wygląda na to, że wszystko zrobione!"
        show p1 lsmile wink at zabarem with fc:
            xalign .5"
        "Chciała pomyśleć Lia. Zrozumiała, że to głos Ojca zza jej ramienia."
        show p3 behind tavern_main_bar_bar1, p1 at zabarem with dissolve:
            xalign 0.2"
        show p1 at zabarem with dissolve:
            xalign .5 xzoom 1"
        p3 "Mówiłem, że sprawdzę. Bardzo ładnie. Teraz zajmij się resztą, a pot..."
    else:
        "Lia wyprostowała się, aby przyjrzeć się czy coś jej nie umknęło."
        "Od razu zauważyła, że pominęła jeden fragment."
        "Gdy tylko chciała zabrać się za poprawki, usłyszała za sobą głos."
        show p3 behind tavern_main_bar_bar1 at zabarem with dissolve:
            xalign (0.2)"
        p3 "Ominęłaś fragment, o tam!"
        "Odezwał się Ojciec wskazując palcem na niedoczyszczony fragment."
        #Na ekranie: Angry Lia ON"
        show p1 bangry narrowedwink with fc
        p1 "Tak, widzę! Musiałeś akurat podejść i sprawdzić?"
        "Powiedziała Lia ze złością w głosie. Natychmiast tego pożałowała widząc złość na twarzy Taty."
        #Na ekranie: Angry Zorn ON"
        show p3 angry at zabarem with Dissolve(.2):
            xalign 0.2"
        p3 "Młoda Damo, proszę się zachowywać! Nastę..."


    "Nagle z hukiem otworzyły się drzwi, Zorn zareagował pierwszy."
    #sala główna, Zorn stoi bliżej środka i patrzy w lewo, Lia za nim też patrzy w lewo"
    #angry P3 ON"
    p3 "Halo! Zamknięte jeszcze! Proszę wyp…"
    #neutral P3 ON, po lewej wchodzi P6 i patrzy w prawo"
    p3 "Aaa, HAHA - to Wy Panie Mohon. Wchodź, nie krępuj się!"
    p6 "HAHA, a czego miałbym się krępować? Zgłupiałeś Zorn?"
    p6 "Weź polej piwo bo mnie chuj strzeli zar… Oooo, panienko!"
    #P1 wychodzi przed Zorna"
    p6 "Uszanowanie, dzień dobry - prześlicznie panienka dziś wygląda!"
    #blush Lia ON"
    p1 "Dzień dobry Panie Mohon!"
    #Zorn wychodzi znów przed Lię, Lia znów w prawo"
    p3 "No dobra dobra, starczy tych uprzejmości. Chodź Mohon, potrzebujesz czegoś?"
    #frown Lia ON"
    p6 "Hmm, ten… Mieliśmy omówić…"
    p3 "Ach, tak - pamiętam. Chodź, coś Ci naleję i pogadamy. Lia posprzątaj ostatnią salę."
    p1 "Dobrze."
    #przejście do lewej sali"
    #Lia mówi do gracz, sad_smile ON"
    p1 "Dobra. Daj mi chwilę, ogarnę wszystko."


    menu:
        "gd Kto to był?":
            #happy Lia ON
            p1 "Oh, to był Pan Mohon. Często tutaj przychodzi."
            p1 "Jak na pewno było widać to krasnolud."
            #confused Lia ON"
            p1 "Hmm, co by jeszcze można o nim powiedzieć…"
            p1 "Eh, opowiadanie o kimś jest skomplikowane."
            #neutral Lia ON"
            p1 "Pracuje w kopalni z tego co mi wiadomo."
            p1 "W sumie go lubię, jest zawsze miły dla mnie."
            p1 "Może trochę wulgarny, ale nadrabia to uśmiechem."
            p1 "Często widują się z moim ojcem. Nie wiem po co."
            p1 "Hmm. To chyba wszystko."
            #sad_smile Lia ON"
            p1 "Nigdy bardziej się nad tym nie zastanawiałam. Wybacz."
            gd "Nie przejmuj się. Dziękuję."
            #smile Lia ON"
            p1 "Nie ma za co! Dobra, czas wziąć się do pracy."

        "gd Dobrze, poczekam w ciszy.":
            pass

    #lewa sala sama, lekki ruch kamery, zoom/przejście (2-3sec)
    "Lia zabrała się za sprzątanie sali. Jak tylko skończyła to ruszyła z powrotem do głównej sali."
    #przejście do sali głównej, Zorn za barem"
    "..."
    #Lia wchodzi od lewej"
    p3 "O, Lia - chodź tutaj."
    #zoom na bar, Lia po lewej i Zorn po prawej"
    #frown Lia ON"
    p3 "Wszystko posprzątane?"
    p1 "Tak."
    p3 "Super, to przejmij bar i..."
    tg1 "Ekhem."
    #powrót do widoku sali głównej, Lia za barem (jeśli możliwe), po lewej TG1, Zorn staje przed nim"
    tg1 "Jeśli można."
    p3 "Oczywiście. Za Tobą."
    #wychodzą z pomieszczenia, powrót do zoomu na bar, Lia do gracza, confused ON"
    p1 "Huh. Dziwne. Znów jeden z tych zakapturzonych typów."

    menu:
        "gd Co to za jedni?":
            p1 "Hmm. To jest bardzo dobre pytanie."
            p1 "Nikt nie wie. Rozbili namiot przed Tawerną jakiś czas temu i tam mieszkają."
            p1 "Przychodzą czasem po prowiant. Ogólnie to się kręcą po całej okolicy."
            p1 "Może będzie kiedyś okazja dowiedzieć się coś więcej."
            p1 "Wiem tyle, że płacą dobrze, więc tata chyba nie zadaje za dużo pytań."
            p1 "Pewnie szkoda stracić klientów."
            p1 "Dobra, kiedy indziej o tym pogadamy - słyszę, że wraca."

        "gd Rzeczywiście dziwne.":
            p1 "Przerażający są trochę. No nic, wracam do pracy."
            "Po krótkiej chwili Zorn wrócił do pomieszczenia."


    #Lia surprised_neutral ON
    #zoom na bar, Lia po prawej, Zorn po lewej
    p3 "Dobra, wszystko ogarnięte. Jak coś to ktoś z nich przyjdzie później po paczkę z prowiantem."
    p1 "Od tych zakapturzonych?"
    p3 "Tak, od nich. Za paczkę zapłacili z góry. Idę ją przygotować."
    p3 "Później Ci ją przyniosę, po prostu im ją wydasz."
    p3 "Pilnuj Tawerny, wkrótce ludzie zaczną krążyć."
    #Zorn wychodzi z pomieszczenia"
    "..."
    #Lia mówiąca do gracza, neutral ON"
    p1 "No to zaczynamy pracę."
    #tutaj skip, przejście na background zewnątrz Tawerny i upływ czas do południa, 3-4sec, +1 upływ czasu"
    #po przejściu powrót do Tawerny, zoom taki sam jak wcześniej i Lia mówiąca do gracza, Lia frown ON"
    p1 "Oh… Jesteś tutaj dalej ze mną?"
    gd "Oczywiście."
    #sad_smile Lia ON"
    p1 "Dzięki."
    p1 "Przynajmniej rano jest mały ruch, więc można pogadać…"
    #tutaj bez imienia pierwsze powiedzenie od Ainy i bez pokazywania jej"
    p7 "Halo, słyszysz mnie?"
    #Lia wraca na pozycję, zoom na bar"
    #surprised_neutral Lia ON"
    #Aina się pojawia, neutral ON, po lewej przed barem"
    p7 "Halo?"
    p1 "Oh. Przepraszam, zamyśliłam się. Co potrzeba?"
    #Aina smile ON"
    p7 "Haha! Nie ma problemu, też czasem zdarza mi się odlecieć myślami nie wiadomo gdzie."
    #Lia smile ON"
    p7 "Dla mnie to co zwykle!"
    p1 "Już podaję!"
    #komiks z folderu work work, tak by jako animacja wyglądał work 3A i work 3B"
    #Lia blush ON"
    p7 "Dzięki ślicznotko! Do zobaczenia!"
    #Aina znika z ekranu, Lia do gracza"
    p1 "To było lekko niespodziewane…"

    menu:
        "gd Oj tam! To tylko komplement.":
            p1 "Huh, niby tak. Masz rację, ale… Oh, ktoś idzie."
        "gd Haha! Urocza dziewczyna!":
            p1 "Mhm, masz rację. Może… Oh, ktoś idzie."

    #wracamy na standardowy zoom, pojawia się TG2 (inny niż wcześniej) i podpis go ‘???’
    #surprised_neutral Lia ON
    tg2 "Witam."
    p1 "Dzień dobry. W czym mogę pomóc?"
    #confused Lia ON"
    tg2 "Ja po paczkę."
    p1 "Hmm? Ah, paczka… dziś rano zamówiona, tak?"
    tg2 "Tak."
    #sad_smile Lia ON"
    p1 "Um, już podaję."
    #komiks folder work work Lia podająca paczkę"
    p1 "Proszę."
    tg2 "Mhm."
    #annoyed Lia ON, TG2 wychodzi ze sceny od razu. Lia mówi do gracza"
    p1 "Nie dość, że nie pokazują twarzy to jeszcze są niemili. Pff."
    #levius na razie bez imienia i jego podpis jako ‘???’"
    p9 "Hej Lia!"
    #przejście do standardowej sceny, Levius po lewej, Lia wciąż za barem, Lia surprised_neutral ON,"
    p1 "Um… Cześć!"
    p9 "To ja, Levius. Pamiętasz mnie?"
    #sad_smile Lia ON, Levius smile ON"
    p1 "Oh, tak - oczywiście."
    p9 "Cieszę się! Umm… Co porabiasz?"
    p1 "Huh? Teraz jak widzisz pracuję."
    #sad_smile Levius ON"
    p9 "Oh, no tak. To nie przeszkadzam teraz."
    p9 "Jakbyś miała ochotę później porozmawiać to nie krępuj się proszę."
    #smile Lia ON, Levius smile ON"
    p1 "Dobrze, będę pamiętać."
    p9 "Dziękuję! Do zobaczenia!"
    #Levius wychodzi z kadru, Lia confused ON i mówi do gracza:"
    p1 "Dziwny dzień. Dziwni ludzie. Wracam do pracy."
    #Lia znika z ekranu, główna sala (ruch ludzi z cieniami może), lekki ruch out zoom z baru na całość, 2-3 sec"
    "Lia wróciła do pracy i w pełni się na niej skupiła."
    #tutaj odpala się przejście na zewnątrz Tawerny i dwie ścieżki są:


    if d_gofestiwal:
        #czas upływa o jeden, do popołudnia. Wracamy do sali i ujęcie na Lię za barem i Zorn stoi po lewej też za barem
        p3 "Hej Lia, jak idzie praca?"
        p1 "Wszystko dobrze."
        p3 "To dobrze. Jeśli chcesz dalej iść na festiwal to mogę Cię już zastąpić."
        p3 "To jak, chcesz iść?"

        menu:
            "gd Chodźmy na festiwal!":
                #smile Lia ON
                p1 "Tak! Z chęcią pójdę."
                p3 "No dobrze. Tylko uważaj na siebie."
                p1 "Będę na pewno!"
                p3 "Obiecaj, że będziesz."
                #frown Lia ON"
                p1 "Obiecuję!"
                p3 "No dobrze dobrze. Zmykaj już. Nie wracaj za późno."
                #przejście na zewnątrz Tawerny, przechodzimy do E4
            "gd Lepiej zostań w pracy.":
                #confused Lia ON
                p1 "Nie, nie trzeba."
                p1 "Zostanę i jeszcze popracuję."
                p3 "Oh. Hmm, no dobrze. Twoja decyzja."
                #smile Lia ON"
                p3 "Dzięki, że zostałaś pomagać."
                #Zorn wychodzi, Lia do gracza"
                p1 "Zawsze coś w zamian. Chociaż nie jestem do końca przekonana do tej decyzji."
                #sad_smile Lia ON"
                p1 "No ale już nic nie zrobimy. Wracam do pracy."
                #efekt wyjścia z tawerny, out zoom od baru do pełnej sali i wyjście na zewnątrz Tawerny, upływ czasu do wieczora"
                #powrót do ujęcia za barem. Pojawia się Zorn po lewej za barem obok Lii"
                p3 "Jak tam?"
                #frown Lia ON"
                p1 "Dobrze."
                p3 "Możesz iść już spać. Ja zamknę Tawernę."
                #sad_smile Lia ON"
                p3 "Jeszcze raz dzięki, że zostałaś pomóc. Dobranoc."
                p1 "Dobranoc."
                #przejście do pokoju Lii, Lia do gracza, relaxed ON"
                p1 "Uh, jestem zmęczona. Pójdę od razu spać."
                #neutral Lia ON"
                p1 "Dobranoc."
                gd "Dobranoc."
                #przejście do E5

    else:
        #jeśli nie ma tego punktu
        #czas upływa o dwa, do wieczora, wracamy do ujęcia za barem. Pojawia się Zorn po lewej za barem obok Lii
        p3 "Jak idzie praca?"
        #frown Lia ON"
        p1 "Idzie dobrze."
        p3 "Mhm. Możesz iść już spać. Ja zamknę. Dobranoc."
        p1 "Eh. Dobranoc."
        #przejście do pokoju Lii, Lia do gracza, relaxed ON"
        p1 "Uh, jestem zmęczona. Pójdę od razu spać."
        #neutral Lia ON"
        p1 "Dobranoc."
        gd "Dobranoc."
        #przejście do E5



label e4:

    #background zewnątrz Tawerny, popołudnie, Lia do gracza, surprised_happy ON
    p1 "Dobra. Tak jak ostatnio, pokażę Ci w ogóle gdzie idziemy."
    #otwiera się mapa, zoom na lokację Tawerny i przesunięcie zoomu na wioskę"
    p1 "Idziemy tutaj do wioski, pójdziemy skrótem przez las, nic się nie powinno stać."
    #mapa się zamyka, Lia do gracza, Lia happy ON"
    p1 "Chodźmy!"
    #przejście, upływ czasu +1, backgroung ścieżka przed wioską, Lia do gracza, surprised_neutral ON"
    p1 "Jesteśmy prawie na miejscu. W sumie jak już tu dotarliśmy to nie jestem przekonana do tego pomysłu…"
    gd "Dlaczego?"
    #sad Lia ON"
    p1 "No bo co ja tu właściwie jestem? Nikogo praktycznie nie znam, bawić też zbytnio się nie lubię..."
    gd "Hmm. Na pewno nie zaszkodzi pójść i zobaczyć co i jak."
    #sad_smile Lia ON"
    p1 "Niby tak… To co mam zrobić?"
    gd "Wejdź do wioski, znajdź jakieś piwo i zobaczymy co dalej. Na pewno nie będzie źle."
    #relaxed Lia ON"
    p1 "Hmm."
    #smile Lia ON"
    p1 "No dobrze. Ufam Ci, chodźmy."
    #przejście na wioskę, bawiący się ludzie cienie, Lia od prawej do lewej bardzo powoli ‘idzie’, surprised_happy ON
    "Lia ruszyła przez wioskę sprawnie unikając bliższego kontaktu z ludźmi."
    "Wolała nie ryzykować potencjalnego wciągnięcia w wir tańca."
    "Wzięła piwo i przystanęła gdzieś na boku."
    #Lia do gracza, neutral ON w tle ciągle wioska"
    p1 "Nie jest tak źle póki co…"
    #surprised_neutral Lia ON"
    p1 "Wyjątkowo dobrze widać Zielonego Smoka podczas tego festiwalu."
    gd "Co masz na myśli?"
    #neutral Lia ON"
    p1 "Hmm. Przeważnie jest słabiej widoczny. Spójrz w górę."
    #Lia znika, kamera przechodzi na niebo skupiając się na smoku (lekki ruch)"
    p1 "Na jego cześć jest cały festiwal."
    p1 "Krąży wokół niego też sporo legend."
    p1 "Chcesz usłyszeć co o tym wiem?"

    menu:
        "gd Bardzo chętnie!":
            #Lia wraca, jest na boku tak żeby nie zasłaniała smoka i wciąż jakby bliżej ekranu rozmawiając z graczem
            #sad_smile Lia ON
            p1 "Zaznaczę od razu, że w sumie to nie wiem za dużo."
            p1 "Pamiętam tylko tyle co opowiadała mi mama..."
            #smile Lia ON"
            p1 "Ale... Po pierwsze smok pojawia się zawsze w różnych odstępach czasowych."
            p1 "Nikt nie wie kiedy dokładnie się pojawi i dlaczego jest to takie losowe."
            p1 "Ostatni festiwal odbywał się jakoś siedem lat temu."
            #blush Lia ON"
            p1 "Wcześniejszego nie pamiętam bo byłam zbyt mała…"
            #smile Lia ON"
            p1 "Obecny trwa prawie dwa tygodnie i powoli zbliżamy się do końca."
            p1 "Wracając do samej legendy. Mówi się, że Smok pojawia się w momencie kiedy Królestwo jest zagrożone."
            p1 "Zielony Smok jest jakby strażnikiem naszej wyspy czy coś takiego."
            p1 "Hmm… Co jeszcze."
            p1 "Ah, tak. Mówi się, że jest związany z ogromną wieżą w centrum naszej wyspy. Że właśnie tam mieszka."
            p1 "Nikt jednak tego nie potwierdził bo wstęp ma tam tylko rodzina królewska."
            p1 "Właśnie! Odnośnie rodziny królewskiej!"
            p1 "Słyszałam od gości w Tawernie, że na zakończenie festiwalu księżniczka Aurora i książę Caius przyjadą świętować do naszej wioski."
            p1 "Wszyscy są tym jakoś specjalnie podekscytowani."
            #blush Lia ON"
            p1 "W sumie chętnie zobaczę tę księżniczkę, ponoć jest bardzo piękna…"
            #neutral Lia ON"
            p1 "No ale nie jest to teraz ważne."
            p1 "Hmm, to chyba wszystko co wiem."
            p1 "Jak będziemy chcieli to może uda się kiedyś dowiedzieć czegoś więcej od kogoś."
            gd "Dzięki za opowieść."
            #smile Lia ON"
            p1 "Nie ma za co!"

        "gd Nie, dzięki.":
            #Lia wraca, jest na boku tak żeby nie zasłaniała smoka i wciąż jakby bliżej ekranu rozmawiając z graczem
            #frown Lia ON
            p1 "Hmm. Jak chcesz."

    #po tekstach lekki zastój na smoku i powrót na standardowe ujęcie Lii, mówi do gracza, relaxed ON
    p1 "Hmm. Nie jest tak źle tu…"
    #efekt zatrzęsienia ekranu, Meamir w nią wpadł"
    "Zamyślona Lia prawie się przewróciła po niespodziewanym zderzeniu."
    #zwykły ujęcie, wioska w tle, Lia stoi z boku i przed nią Meamir"
    #Lia shock ON"
    "Odzyskała szybko równowagę i zauważyła przed sobą nieznajomego chłopaka!"
    #Meamir podpisany na początku ‘???’, Meamir surprised_happy ON"
    p5 "Na Zielonego Smoka! Przepraszam! Nie zauważyłem Cię, czy wszystko w porządku?"
    #Lia surprised_neutral ON"
    p1 "Oj, tak… Nic się nie stało. Tylko troszkę się przestraszyłam… i straciłam swoje piwo."
    #Meamir blush ON"
    p5 "Ojej, przepraszam raz jeszcze… Rozglądałem się i nie patrzyłem przed siebie."
    "”Uroczy.” - pomyślała Lia."
    #happy Lia ON"
    p1 "Nic się nie stało! Naprawdę. Sama byłam też zamyślona… Trochę też moja wina."
    p5 "Oh, no dobrze! Ale na wszelki wypadek w ramach przeprosin może dasz się skusić na wspólne piwo?"
    p1 "Hmm… W zasadzie czemu nie. Ale pod jednym warunkiem."
    #Meamir confused ON"
    p5 "Jakim?"
    #Lia smirk ON"
    p1 "Musisz przynajmniej powiedzieć jak się nazywasz!"
    #Meamir surprised_happy ON"
    #Meamir dostaje normalny podpis"
    p5 "Ahh, nie przedstawiłem się. Przepraszam! Jestem Meamir, a Ty?"
    p1 "No nie wiem czy jeszcze na to zasłużyłeś…"
    #Meamir blush ON"
    p5 "Oh… No to…"
    #surprised_happy Lia ON"
    p1 "Oj no! Żartuję tylko, jestem Lia!"
    p1 "Miło Cię poznać!"
    p5 "Oh. Ciebie też miło poznać Lia!"
    p1 "No no, nie czerwień się tak - chodźmy na to piwo!"
    #Meamir smile ON"
    p5 "Dobrze, dobrze - chodźmy!"
    #przejście do zoomu na skrzynkę z piwem i stoją naprzeciwko siebie, both smile ON"
    "Dotarli do miejsca z piwem. Meamir nalał dwa pełne kubki. Pierwszy podał Lii."
    p5 "Proszę bardzo, ten dla Ciebie."
    p1 "A dziękuję bardzo."
    #both blush ON"
    "Przez moment wpatrywali się na siebie bez słowa, powoli sącząc swoje trunki."
    "”Uroczy jest.” - pomyślała Lia."
    #smile Meamir ON"
    p5 "Hmm… Jesteś stąd w ogóle?"
    #confused Lia ON"
    "”Dziwne pytanie.” - pomyślała Lia."
    p1 "Hmm. Nie do końca. Co prawda mieszkam niedaleko, ale nie tutaj we wiosce."
    p5 "A gdzie?"
    p1 "Um… Niedaleko. Przy Tawernie na rozdrożach. Dlaczego pytasz?"
    #surprised_happy Meamir ON"
    p5 "Ah, wybacz. Pytam bo dopiero się wprowadziliśmy i poznaję okolicę."
    #smile Lia ON"
    p1 "Oo, nie wiedziałem, że ktoś jeszcze ma się wprowadzić. Słyszałam tylko o nowym kowalu…"
    #smile Meamir ON"
    p5 "Hah, to właśnie my. Znaczy dokładnie to mój ojciec."
    #sad_smile Meamir ON"
    p5 "O mnie pewnie nikt nie wspominał, nie jestem na tyle interesujący."
    #smirk Lia ON"
    p1 "Oj, nie przesadzaj. Na pewno nie jest tak źle! Zresztą kowal bez swojego pomocnika niewiele zrobi!"
    #blush Meamir ON"
    p5 "Oh, pewnie masz rację!"
    #sad_smile Meamir ON"
    p5 "No ale to właśnie stąd moje dziwne pytanie! Ciekaw jestem co jest w okolicy."
    #happy Lia ON"
    p1 "Rozumiem! Po prostu byłam lekko zaskoczona takim pytanie."
    p1 "Więc jak na ten moment podoba Ci się to nasze otoczenie?"
    #blush Meamir ON"
    p5 "Umm. Na pewno po dzisiejszym wieczorze znacznie bardziej niż wczoraj."
    #blush Lia ON"
    p1 "Oh… A to dlaczego? Stało się coś ciekawego?"
    #smirk Meamir ON"
    p5 "Można tak powiedzieć."
    #confused Lia ON"
    p1 "Co masz dokładnie na myśli?"
    #blush Lia ON"
    p5 "To że na siebie wpadliśmy!"
    #blush Meamir ON"
    p5 "Wiem, że nie brzmi to dobrze… Ale cieszę się z tego naszego zderzenia."
    p5 "Nie wiem co bym tu sam robił, a w takim towarzystwie od razu milej…"
    #smile Lia ON"
    p1 "Hah, też się cieszę. Sama w sumie też byłam tutaj lekko zagubiona."
    #smile Meamir ON"
    p5 "No widzisz! Hmm, to może chciałabyś się jeszcze gdzieś przejść?"
    #sad_smile Lia ON"
    p1 "Hmm, wiesz co… Bardzo chętnie, ale robi się już trochę późno. Powinnam wracać"
    #sad Meamir ON"
    p5 "Oj no! Już chcesz uciekać? Przecież jeszcze nie jest tak późno. Zostań jeszcze trochę!"
    p1 "Chciałabym, ale jeszcze muszę wrócić do domu - nie chcę, żeby rodzice się martwili!"
    #sad_smile Meamir ON"
    p5 "Ah, no dobrze - rozumiem… To ostatnie pytanie tylko, co porabiasz na co dzień, pomagasz w tej Tawernie?"
    #surprised_happy Lia ON"
    p1 "Hah, tak. A czemu pytasz?"
    #smile Meamir ON"
    p5 "To w takim razie się może jutro zobaczymy! Mam coś odebrać."
    #smile Lia ON"
    p1 "Oo, to bardzo fajnie, więc nie ma co się przejmować skoro jutro się zobaczymy!"
    p5 "Może znajdziesz wtedy chwilkę na rozmowę, co?"
    #smirk Lia ON"
    #sad_smile Meamir ON"
    p1 "Może może, kto wie. Zobaczymy jutro!"
    p1 "A teraz muszę naprawdę uciekać, papa!"
    #smile Meamir ON"
    p5 "Dobrze, do zobaczenia!"
    #znikają i out zoom wioski by całość bardziej widać"
    "Lia od razu opuściła wioskę i ruszyła w kierunku Tawerny."
    #background Tawerna noc"
    "W Tawernie nie było słychać już żadnych głosów. Po cichu ruszyła do swojego pokoju, żeby nikogo nie obudzić."
    #background pokój, Lia mówi do gracza, smile ON"
    p1 "Nie sądziłam, że ten dzień będzie w miarę interesujący."
    p1 "Dziękuję za porady! Ciekawa jestem co czeka nas jutro."
    p1 "A teraz do spania! Dobranoc!"
    gd "Dobranoc!"
    #przejście do E5




label e5:
    if d_gofestiwal:
        #animacja przejścia z nocy w dzień, zewnątrz Tawerny
        #background pokój Lii, rano
        "Lia powoli otworzyła oczy i rozejrzała się po pokoju."
        "Zauważyła, że słońce było już wyżej niż zazwyczaj."
        "Szybko się ubrała i wstała."
        #Lia pojawia się na ekranie, do gracza, confused ON"
        p1 "Dzień dobry… huh, dziwne…"
        gd "Dzień dobry. Co takiego?"
        p1 "Zaspałam i nikt nie przyszedł mnie obudzić…"
        p1 "Hmm. No nic. Idę na śniadanie."
        #bg kuchnia, P1 wchodzi od prawej, mówi do gracza"
        #surprised_sad Lia ON"
        p1 "Oh, widzę, że już po śniadaniu..."
        #smile Lia ON"
        p1 "A nie, jednak coś mi zostawili. Zjem i czas do pracy."
        #przejście do sali, zoom na bar, P1 lewo, P3 prawo"
        p3 "A kto to wstał w końcu."
        #frown Lia ON"
        p1 "Czemu mnie nikt nie obudził..."
        p3 "Pomyśleliśmy, że możesz chcieć odpocząć po wczoraj."
        #blush Lia ON"
        p1 "Oh. Dziękuję."
        p3 "Nie ma za co. A teraz możesz pomóc. Stań za barem i przypilnuj Tawerny."
        #sad_smile ON"
        p1 "Dobrze tato."
        #Zorn wychodzi, Lia za barem

    else:
        #animacja przejścia z nocy w dzień, zewnątrz Tawerny
        #background pokój Lii, rano
        "Lię zbudził dźwięk otwieranych drzwi. Otworzyła oczy."
        #od prawej wchodzi Selene"
        p2 "Dzień dobry Lia, wstawaj już. Zaraz śniadanie i trzeba tacie pomóc w Tawernie."
        p1 "Uhh… Jeszcze pięć minut..."
        p2 "Wstawaj wstawaj. Śniadanie czeka na Ciebie."
        #P2 wychodzi w prawo"
        "Lia przeciągnęła się ze zmęczeniem, westchnęła i w końcu wstała."
        #Lia na środku, mówi do gracza, frown ON"
        p1 "Dzień dobry… Uh, kolejny dzień przed nami - hurra…"
        gd "Dzień dobry..."
        p1 "Dobra, idę do kuchni coś zjeść."
        #bg kuchnia, P2 po lewej, P1 od prawej wchodzi"
        #P2 smile ON, P1 neutral"
        p2 "Dzień dobry Lia, jak Ci minęła noc?"
        p1 "Normalnie. Jak miała niby minąć?"
        #sad Selene ON, surprised_sad Lia ON"
        p2 "No dobrze, już o nic nie pytam."
        #neutral Selene ON"
        p2 "Zjedz śniadanie i idź pomóż tacie."
        #sad_smile Lia ON"
        p1 "Dobrze…"
        #Selene wychodzi z kuchni, Lia do gracza"
        p1 "No dobra. Zjem i idę pracować."
        #przejście do sali, zoom na bar, P1 lewo, P3 prawo"
        #frown Lia ON"
        p3 "Miło, że w końcu dołączyłaś."
        p1 "Ale…"
        p3 "Dobra, nieważne. Sporo pracy przede mną."
        p3 "Zostań za barem i pilnuj Tawerny, nie powinno być zbyt dużo gości."
        #Zorn wychodzi, Lia za barem

    #Lia do gracza, sad_smile ON
    p1 "Czasem przed południem nie jest tak źle… Ruch przeważnie niewielki."
    p1 "Zobaczymy co dzień przyniesie."
    #przejście na zewnątrz Tawerny, przejście czasowe (ptaszki, ruch słońca) i upływ czasu +1, powrót do środka"
    #po wejściu do Tawerny od razu odpala się komiks z kuflami, jest zoom na barze"
    p1 "Zamówienie nr. 66 gotowe!"
    #pojawia się guest 1, ten elf co ostatnio, podpis Gość po prostu"
    p1 "Tylko proszę nie wylać jak ostatnio..."
    r1 "Dobrze! Tak się stanie moja Pani!"
    #gość znika, pojawia się Henrietta"
    p8 "Cześć Lia. Co tam ciekawego?"
    p1 "Oh, hej Henrietta. Nic szczególnego. Coś podać?"
    p8 "Mhm. Daj butelkę czegoś mocnego, długi dzień przede mną."
    p1 "Hmm."
    #komiks jak będzie work z podaniem butelki jakiejś"
    p1 "To powinno być w porządku, proszę."
    #Henrietta smile ON, Lia blush ON"
    p8 "Dzięki Lia. Do zobaczenia później."
    #Lia smile ON"
    p1 "Do zobaczenia."
    #Hen wychodzi, ujęcie na całą salę, Lia za barem + cienie przechodzących ludzi, ze 2-3 tu i tam"
    "Goście powoli przewijali się przez Tawernę zajmując całkowicie myśli Lii."

    if d_gofestiwal:
        "Lia stała akurat plecami do baru gdy nagle usłyszała znajomy głos."
        p5 "Hej Lia! Dzień dobry!"
        #pojawia się Meamir, smile ON, Lia smile ON"
        p1 "O, hej Meamir! Dzień dobry!"
        p5 "Jak tam Twój dzień mija?"
        p1 "Standardowo, nic ciekawego się nie dzieje, a Twój?"
        p5 "To samo, nic ciekawego..."
        #blush Lia ON"
        #smirk Meamir ON"
        p5 "Chociaż teraz już jest ciekawiej…"
        p1 "Znów się wygłupiasz!"
        #smile Meamir ON, Lia smile ON"
        p5 "No dobrze dobrze... Przyszedłem po zamówienie…"

    else:
        "Lia stała akurat plecami do baru gdy usłyszała przyjemny i interesujący głos."
        #podpis Meamira na początek ‘???’"
        #Meamir smile ON, Lia surprised_happy smile ON"
        p5 "Dzień dobry! Hej!"
        #pojawia się Meamir po lewej, Lia wciąż za barem"
        p1 "Dzień dobry…"
        #pojawia się imię Meamira w podpisie"
        p5 "Nazywam się Meamir. Przyszedłem po zamówienie mojego taty, znaczy kowala…"
        #Lia smile ON"
        p1 "Oh, musisz chyba chwilkę poczekać, mój tata spodziewał się Ciebie później…"
        #sad_smile Meamir ON"
        p5 "Ah, rozumiem…"
        #confused Lia ON"
        p1 "…"
        p5 "…"
        p5 "Przepraszam, że pytam… Ale czy mógłbym poznać Twoje imię?"
        #sad_smile Lia ON"
        p1 "Oh, przepraszam - nazywam się Lia. Powinnam się przedstawić od razu…"
        #smile Meamir ON"
        p5 "Nie nie, nic się nie stało! Bardzo miło Cię poznać, śliczne imię!"
        #blush Lia ON"
        p1 "Dziękuję!"
        p5 "Przyjemność po..."


    #bar zoom, P1 za barem, P5 przed barem po prawej, P3 za barem bardziej po lewej stronie
    #Lia confused ON, Meamir sad_smile ON
    p3 "A co tu się dzieje młodzieży? Co to za rozmowy w pracy Lia?"
    p1 "Um…"
    p3 "Ty jesteś Meamir tak?"
    p5 "Tak, to ja..."
    p3 "Miałeś być później."
    #Meamir confused ON"
    p5 "Ah, tak to prawda. Ale udało mi się wcześniej wyrobić z obowiązkami…"
    p3 "Hmm, no dobrze. Zaraz przygotuję wszystko. Poczekaj chwilę…"
    #tutaj taki efekt zrobić, że Zorn się odwraca od nich, ale od razu zawraca"
    p3 "Tylko grzecznie mi tutaj. Zaraz wrócę."
    #surprised_neutral Lia ON, Meamir blush ON
    #Zorn wychodzi w lewo


    if d_gofestiwal:
        #sad_smile Lia ON, smile Meamir ON
        p5 "Hmm…"
        p5 "Wczoraj było bardzo przyjemnie na festiwalu!"
        #blush Lia ON"
        p1 "To prawda!"
        p5 "Może dziś też chciałabyś gdzieś wyjść? Na przykład na spacer wieczorem?"
        p1 "Oh, właściwie czemu..."


    else:
        #confused Lia ON, Meamir blush ON
        p5 "Um… Pomagasz codziennie w Tawernie?"
        #smile Lia ON"
        "”Całkiem uroczy.” - pomyślała Lia."
        p1 "Tak, pomagam tutaj - w zasadzie to moje główne zajęcie."
        #smile Meamir ON"
        p5 "Od dawna tu mieszkasz?"
        #surprised_neutral Lia ON"
        p1 "Całe życie w zasadzie… Dlaczego pytasz?"
        #sad_smile Meamir ON"
        p5 "Ah, wybacz. Wprowadziliśmy się dopiero, więc chciałbym się zorientować w nowej okolicy."
        p5 "Mam nadzieję, że nie zabrzmiało to strasznie źle..."
        #Lia smile ON, Meamir smile ON"
        p1 "Nie! Bez obaw, tak tylko zapytałam."
        p5 "Ah, to dobrze. A coś jeszcze robisz na co dzień?"
        #sad_smile Lia ON"
        p1 "Huh. Nie, niezbyt. Głównie pracuję, muszę pomagać rodzicom przy Tawernie."
        #surprised_happy Lia ON"
        p5 "Hmm, to tak sobie myślę. Może zechciałabyś wyjść ze mną na spacer? Pokazać okolicę czy coś..."
        #surprised_happy Meamir ON"
        p1 "Oj, hmm, teraz ciężko mi powiedzieć, ale w sumie czemu…"

    #dźwięk przerażającego KRZYKU
    #równo z krzykiem pojawia się Zorn i jego dialog
    p3 "Co tam się dzieje na zewnątrz?!"
    #angry Zorn activated
    p3 "Muszę to sprawdzić."
    #przejście do E6


label e6:
    #zewnątrz Tawerny, południe, 2 bandziorów po lewej, P4 po prawej, surprised_sad Raven ON
    "Wyglądało na to, że jacyś mężczyźni próbowali osaczyć bezbronną dziewczynę."
    #od prawej wjeżdża Zorn, angry ON"
    p3 "Halo, co tu się dzieje? Co to ma znaczyć!?"
    "Na widok Zorna nieznajomi odruchowo spojrzeli się po sobie."
    "Nie wyglądali jednak na takich co dobrowolnie będą się tłumaczyć."
    b1 "Nie Twój interes elfie, wracaj do swoich spraw. Ta dziewczyna należy do nas!"
    p3 "Należy do Was?! Ganiając za tą biedną dziewczyną musieliście chyba mocno przemęczyć Wasze móżdżki."
    p3 "Osoba nie może być Waszą własnością, radzę…"
    b2 "Ja radzę zamknąć ten Twój niewyparzony ryj i nie wtrącać się do nie swoich spraw kolego."
    b1 "Dokładnie, siedź tam cicho, a my zabieramy dziewczynę…"
    "Jeden z nich ruszył powoli w kierunku dziewczyny wyciągając rękę by ją złapać."
    "Nagle czas jakby się dla niego zatrzymał..."
    #tutaj zaczynamy schemat bójki, elementy różne bez zmian"
    "Obcy nie był w stanie w pierwszej chwili zrozumieć co się stało."
    "Czuł ogromny ból głowy oraz pleców, przez lekko otwarte powieki widział promienie słoneczne…"
    "Dosłownie jakby leżał… W uszach strasznie mu dzwoniło. Po paru sekundach usłyszał tylko przerażający krzyk swojego kompana."
    b2 "Kurwwaaaaa, mój noooos… zabijęęęę Cięęę! Auaaaaa….."
    "Krzyk zagłuszył od razu dźwięk upadającego worka ziemniaków o ziemię… A może to wcale nie był worek..."
    #bez podpisu Zorna tekst Zorna jedna linijka niżej"
    p3 "Powoli bo się bardziej połamiesz."
    "Wstawał bardzo powoli. Dokładnie tak jak zasugerował głos."
    "Zresztą nie miał innego wyboru. Miał chyba złamane ze dwa żebra, nie… trzy."
    "Wstał."
    #jeden bandyta na nogach, drugi leży, Zorn stoi blisko tego stojącego, Raven z tyłu"
    p3 "A teraz słuchaj bardzo uważnie. Nie będę się powtarzał."
    p3 "Istnieje duża szansa, że nie wiesz, iż w naszym królestwie nie możesz kogoś sobie sobie posiadać."
    p3 "Nie możesz ot tak powiedzieć, że ktoś jest Twoją własnością!"
    p3 "A już w ogóle nie możesz tego robić przy mojej Tawernie!"
    #Zorn obraca się w prawo"
    p3 "Lia!"
    #Lia pojawia się od prawej, shock Lia ON"
    p3 "Zabierz ją do środka - zaraz przyjdę."
    #Zorn obraca się do bandziorów, Lia i Raven wychodzą na prawo"
    p3 "A Was jeśli tutaj zobaczę raz jeszcze to skończycie znacznie gorzej."
    p3 "Radzę teraz się zebrać, przemyśleć swoje życie i najlepiej zacząć od nowa."
    p3 "A teraz bierz swojego kolegę i won mi stąd."
    #ładne przejście do kuchni, Raven po lewej, Lia po prawej, Raven confused ON, Lia confused ON"
    p1 "Hej... Jak masz na imię?"
    #sad_smile Lia ON"
    p1 "Wszystko w porządku?"
    #blush Raven ON"
    p4 "Nazywam się Raven… I tak, wszystko dobrze. Dziękuję…"
    #blush Lia ON"
    p4 "Um, a Ty jak się nazywasz?"
    #Lia smile ON, Raven sad_smile ON"
    p1 "Mam na imię Lia, miło Ciebie poznać Raven!"
    p1 "Co się stało? Jak tu trafiłaś?"
    #Raven sad ON"
    p4 "Ja.. Ja nie wiem, uciekałam i…"
    #Zorn wchodzi po prawej, both girls confused ON"
    p3 "Załatwione. Tamtymi nie musisz się już martwić, więcej nie powinniśmy ich zobaczyć."
    p3 "W ogóle wszystko dobrze? Nie jesteś ranna czy coś? Hmm, dziewczyno?"
    p3 "Halo, dziewczyno.. Mówię do…"
    #P2 wchodzi od prawej, Lia niech dołączy po lewej do Raven 2on2, Selene smile ON"
    p2 "Zorn! Nie widzisz, że jest wystraszona?"
    p2 "Ja się tym zajmę. Idź proszę sprawdzić czy nie ma Cię w głównej sali."
    #P3 wychodzi w prawo"
    "Zorn popatrzył się na żonę, ale się nie sprzeciwił tylko grzecznie wyszedł sprawdzić czy na pewno nie ma go w tej sali."
    p2 "Podejdź tu i pokaż mi się, zranili Cię gdzieś?"
    #Raven sad ON + zbliża się do Selene jakoś na środku się ogarniają"
    p4 "Niee proszę Pani… Nie zdążyli…"
    p2 "Już wszystko dobrze, nie smuć się. Nazywam się Selene, a Ty?"
    p4 "Ra… Raven."
    #Raven blush ON"
    p2 "Piękne imię! Widzę, że wszystko rzeczywiście jest w porządku."
    p2 "No już, nic Ci już nie grozi - widzę, że jesteś wykończona. Chciałabyś odpocząć?"
    #surprised_happy Raven ON"
    "Raven nie wiedziała za bardzo co powiedzieć, pierwszy raz spotykała się z takim podejściem do niej."
    p2 "Dobrze, zakładam, że tak."
    p2 "Lia, weź ją proszę do pokoju gościnnego. Pokaż jej co i gdzie i daj jej odpocząć, dobrze?"
    p1 "Dobrze mamo. Chodź Raven."
    "Obie dziewczyny ruszyły na górę, Raven podążała spokojnie za Lią"
    #Pokój Raven, P1 wchodzi pierwsza od prawej do lewej, P4 za nią"
    #sad_smile Lia ON, confused Raven ON"
    p1 "To jest ten pokój. Możesz tutaj odpocząć sobie spokojnie. Potrzebujesz jeszcze czegoś?"
    p4 "Nie, dziękuję. Jeśli mogę to bym się chyba zdrzemnęła…"
    p1 "Ah, oczywiście - już nie przeszkadzam. Jakbyś czegoś potrzebowała to wołaj, mam pokój na przeciwko."
    #blush Raven ON, Lia smile ON"
    p4 "Dziękuję."
    #Pokój P1, Zorn po lewej, Lia wchodzi od prawej, Lia confused ON"
    p1 "Hej tato, o co chodzi?"
    p3 "Hmm? O nic! Chciałem tylko przyjść i sprawdzić czy wszystko dobrze."
    p1 "Tak, wszystko w porządku - Raven poszła się zdrzemnąć…"
    #surprised_happy Lia ON"
    p3 "Pytałem bardziej o Ciebie."
    p1 "Oh… Wszystko dobrze, czemu miałoby coś być?"
    p3 "Widziałaś przecież co zrobiłem tym bandytom…"
    #smile Lia ON"
    p1 "Oni sobie zasłużyli! Poza tym nie byłam zaskoczona - nie wyglądali na zbyt godnych przeciwników..."
    p3 "Hę? Widzę Wam kobietkom dziś w humorze dokuczanie mi… No nic, ważne, że wszystko dobrze."
    #Zorn wychodzi powoli na prawo, Lia przechodzi na lewo"
    p3 "Mało godni przeciwnicy? To jacy byliby godni?"
    "Powiedział pod nosem tata po czym wyszedł z pokoju. Lia została chwilowo sama."


######################## E6A

    #Lia na ekranie, mówi do gracza, thinking ON
    p1 "Huh… Co teraz…"
    gd "Już myślałem, że nie zapytasz."
    #surprised_neutral Lia ON"
    p1 "Hmm? Oh! To Ty… Przepraszam, zamyśliłam się i zapomniałam o Tobie troszkę…"
    gd "Auć. Czyli nie potrzebujesz porady?"
    #sad_smile Lia ON"
    p1 "Wybacz! Dużo się właśnie wydarzyło… I właściwie to tak! Przydałaby mi się porada."
    gd "Nie ma problemu! Po to tu jestem! Co potrzebujesz?"
    p1 "Ojeju… Tyle się dzisiaj działo, że ciężko wszystko sobie poukładać…"
    gd "Spróbuj! Na pewno dasz radę."
    #smile Lia ON"
    p1 "Mam pomysł! Daj mi chwilkę."
    #Lia znika na sekundę, pojawia się komiks z Lią przy biurku piszącą (folder Others E6A comics)"
    "Lia usiadła na moment przy swoim biurku i otworzyła dziennik."
    "..."
    p1 "Dobra, gotowe! Zobacz."
    #otwiera się dziennik i rozpoczynamy mini poradnik"
    p1 "Zrobiłam taki dziennik. Mogę tutaj wszystko zapisywać i dać go Tobie do przejrzenia."
    p1 "Teraz samodzielnie możesz sprawdzić co i jak i pomóc mi podjąć decyzję."
    p1 "Przeprowadzić Cię dokładnie po wszystkim?"

    menu:
        "gd Koniecznie! Pokaż co i jak.":
            p1 "No dobrze! No to po kolei."
            #tutaj zrobimy taki obrazkowy poradnik, z podświetleniami fragmentów i podpisami co jest co"
            #podświetlenie imion"
            p1 "Tutaj mamy imiona osób, które znam i ostatnie rzeczy z nimi związane."
            #podświetlenie lewej strony notatek"
            p1 "W tym miejscu znajdziesz właśnie te ostatnie informacje i moje notatki."
            #podświetlenie najważniejszych celów"
            p1 "O, a tutaj będę zaznaczać najważniejsze rzeczy do zrobienia - żeby nie zapomnieć."
            #podświetlenie opcjonalnych celów"
            p1 "Takie mniej ważne będę wpisywać w tym miejscu."
            #standardowa ikona wyłączenia dziennika"
            p1 "Jak będzie potrzeba zamknięcia dziennika, to w najlepiej w tym miejscu."
            #cały dziennik otwarty"
            p1 "No dobra. To chyba wszystko. Sprawdź co i jak i daj mi znać jak skończysz."
            #kontrola nad dziennikiem witam, DZIENNIK N01
            #zwykła opcja wyłączenia dziennika teraz jest OFF


        "gd Nie trzeba, jakoś się zorientuję - daj mi chwilkę.":
            p1 "No dobrze, to zobacz co i jak i daj znać jak skończysz."
            #kontrola nad dziennikiem witam, DZIENNIK N01
            #zwykła opcja wyłączenia dziennika teraz jest OFF
            #w tej wersji trzeba dodać, że jak się kliknie ikonę rozmowy to wyskoczy ostrzeżenie pt. ‘Na pewno to już wszystko?’ i to wyjątek z takim ostrzeżeniem tylko do tej decyzji


    #po kliknięciu w ikonę rozmowy zamyka się dziennik i Lia pojawia się z nami rozmawiając, smile Lia ON
    p1 "I jak? Co byś mi doradził teraz?"


    menu:
        "gd Myślę, że warto sprawdzić co u Raven."
            #surprised_happy Lia ON
            p1 "Możesz mieć rację…"
            #sad_smile Lia ON"
            p1 "Wydawała się dość przybita."
            p1 "Poczekam chwilę. Niech się zdrzemnie i odpocznie."
            p1 "Później do niej pójdę."
            #Lia znika, sam pokój"
            #upływ czasu +1"
            #Lia wraca i do gracza, Lia smile ON"
            p1 "No dobra, już czas."
            #przejście do E7-P4
        "gd Może pójdź do wioski spotkać się z Meamirem.":
            #surprised_happy Lia ON
            p1 "Możesz mieć rację…"
            #sad Lia ON"
            p1 "Trochę bez słowa go zostawiłam..."
            #thinking Lia ON"
            p1 "Poza tym zapraszał na spacer. Może z nim pójdę w ramach przeprosin."
            #smile Lia ON"
            p1 "Dobra, zrobię tak. Pójdę od razu."
            "Jak powiedziała tak zrobiła. Wyszła z Tawerny i ruszyła w kierunku wioski."
            #przejście do E7-P5

        "gd Dużo się dziś wydarzyło. Może po prostu połóż się wcześniej spać.":
            #surprised_sad Lia ON
            p1 "Możesz mieć rację…"
            #more_sad Lia ON"
            p1 "W sumie rzeczywiście jestem zmęczona."
            #disappointed Lia ON"
            p1 "Dobra, ogarnę się i idę spać. Dobranoc."
            #Lia znika, taki efekt upływającego czasu za oknem, aż do rana
            #przejście do E7-N
