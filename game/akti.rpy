
default pojscieDoLasu = False


label e1:

    ##jakby tu dodać jakąś krótką rozmowę, a może monolog nawet ‘gracza’ //
    ##przykład: Szkoda mi jej… Rzeczywiście strasznie monotonne życie. Dziewczyna mocno walczy ze swoimi emocjami i jest więźniem własnej rutyny. Może postaram się jej pomóc. Spróbuję dziś. //

    #Na ekranie: Ciemny ekran.
    #Harmider w tle (oddalające się głosy rozmów)
    #Dźwięk zamykanych drzwi
    >Harmider ciągnący się za opuszczającymi powoli Tawernę gośćmi w końcu zmieniał się w utęskniony spokój.
    #Na ekranie: CG z Tawerny (Lia oparta o drzwi z zamkniętymi oczami)
    >Lia zamknęła drzwi za ostatnim gościem i ze zmęczeniem oparła się o ścianę wsłuchując się w ciszę, którą zakłócał jedynie trzaskający ogień w kominku.
    >...
    #W tle cały czas delikatny dźwięk ognia, który teraz zanika (najlepiej do 5-6sec wyciszenie)
    >Pomimo ogromnego zmęczenia znów utknęła na chwilę w swoich myślach.
    >Z dnia na dzień miała coraz bardziej dość tego życia.
    >”Wszystko jest tak monotonne i nudne.”
    >”Wstań. Pracuj. Wykonuj polecenia. Idź spać. Wstań i znów pracuj. Ciągle to samo.”
    >...
    >”Uhhh… Mam dość tego wszystkiego powoli…”

    menu:
        "GD: Przesadzasz. Widać przecież, że jest w Tobie trochę życia.":
            P1: Może i przesadzam.
            P1: Może i jest trochę życia.
            P1: Ale jak mam to stwierdzić jak nie znam nic innego.
            GD: To może czas coś poznać?
            P1: Niby co?
            GD:  Cokolwiek. Zróbmy coś po prostu.
            P1: Nie wiem. Nie jestem przekonana...

            #przejście do tabeli niżej

        "GD: Nic nowego. Dziwne, że jeszcze to wytrzymujesz.":
            P1: A co mam innego zrobić?
            GD: Chwilowo wygląda na to, że nieważne co zrobisz to będzie już pójściem do przodu.
            P1: Może.
            P1: A może nie.
            P1: Zresztą nawet nie wiem co można zrobić.
            GD:  Coś wymyślimy. Warto spróbować.
            P1: Nie wiem. Nie jestem przekonana...

            #przejście do tabeli niżej

        "GD: W takim razie otwórz drzwi i uciekaj od tego życia.":
            P1: Co masz na myśli?
            G: Zostaw to wszystko. Otwórz drzwi i uciekaj.
            P1: …
            G: Szybko. Teraz.
            P1: Eh… W sumie czemu nie…
            G: Biegnij!
            #ujęcie komiks E1AC
            >I pobiegła.
            #czarny ekran, napis biały na środku
            >I tak Lia ruszyła przed siebie opuszczając obecne życie. Prawdopodobnie nikt już jej nigdy nie widział.
            # TODO w tle głos DUB01
            # TODO \Co to było? Cofnij. Teraz.\
            # TODO cofa grę do samego początku i usuwa tę opcję
            # TODO dostajemy achievement ACHIEV01

    # TODO w momencie pojawienia się tych opcji w tle poleci DUB02 (jednorazowo)
    menu:
        "GD: Może pokazałabyś mi w końcu Twoje ulubione miejsce.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
            >Lia wstała i stanęła na równe nowi wpatrując się w drzwi.
            #Lia confused ON
            P1: Masz na myśli Ogród?
            GD: Tak.
            P1: No może…
            GD: To na co czekamy?
            #Lia surprised_neutral ON
            P1: Ale tak od razu? Teraz?
            GD: Pewnie. Trzeba jakoś przełamać rutynę.
            #Lia surprised_happy ON
            P1: W sumie czemu nie…
            GD: Super! No to chodźmy!
            #Lia smile ON
            P1: Niech tak będzie!

            #przejście do E1A

        "GD: Nie ma sensu ciągle narzekać.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
            >Lia wstała i stanęła na równe nowi wpatrując się w drzwi.
            #Lia frown ON
            P1: No tak, a co mam niby robić?
            #Lia angry ON
            P1: Zresztą myślisz, że narzekam bez powodu?
            menu:
                "GD: Nie.":
                    #relaxed Lia ON
                    P1: No właśnie.
                    #Lia surprised_neutral ON
                    P1: To powiesz mi co mam zrobić?
                    GD: A co z tym Twoim ulubionym miejscem?
                    P1: Co z nim?
                    GD: Może byś mi je w końcu pokazała?
                    P1: Teraz?
                    GD: Tak.
                    #Lia surprised_happy ON
                    P1: W sumie czemu nie…
                    GD: Super! No to chodźmy!
                    #Lia smile ON
                    P1: Niech tak będzie!
                    #przejście do E1A

                "GD: Tak.":
                    #disappointed Lia ON
                    P1: Eh. Po co tu właściwie jesteś?
                    GD: Już tłumaczę...
                    #Lia annoyed ON
                    P1: Wiesz co. Nawet nic nie mów.
                    P1: Średnio mnie to teraz interesuje.
                    P1: Idę spać.

                    #przejście do E1B




        "GD: To rób jak chcesz.":
            #background ciemna sala Tawerny, Lia na środku przybliżona do ekranu jak w rozmowach z graczem
            >Lia wstała i stanęła na równe nowi wpatrując się w drzwi.
            #Lia annoyed ON
            P1: Pff. Super pomoc.
            P1: Dobra. To na razie.
            #przejście do E1B



label e1a:
    #w momencie przejścia w tle jest dźwięk: DUB03
    $ LovePath += 1

    P1: Nim pójdziemy pokażę Ci to miejsce na mapie. Spójrz.
    #pokazuje się mapa, zoom na Tawernę
    P1: W tym miejscu jest Tawerna, tu jesteśmy.
    #zoom utrzymany z przejściem na secret garden
    P1: A tutaj mamy Sekretny Ogród do którego zaraz idziemy.
    #background stary las w nocy, przejście jak wcześniej było (ruch tła na zoomie, Lia powoli idzie od prawej do lewej)
    P1: Może i dobrze, że mnie do tego namówiłeś.
    P1: Chodźmy. To niedaleko. Musimy przejść tylko kawałek przy lesie.

    P1: W sumie jesteś tu ze mną pierwszy raz. To Stary Las.
    P1: Ścieżka którą mijaliśmy prowadzi do wioski, ale mało kto z niej korzysta.
    P1: Początkowo miała prowadzić do jakiejś kopalni, ale dawno już nikt się tym nie interesuje.
    #zatrzymanie się i lekki zoom na przejście między drzewami
    P1: O, to tutaj. Teraz tylko przecisnąć się przez las i zaraz jesteśmy na miejscu.
    #dźwięk przeciskania się i przejście w Sekretny Ogród, zmiana tła
    P1: Jesteśmy na miejscu.
    #przejście po całym tle, takie pokazowe całego miejsca, 5-7 sec
    P1: I jak? Podoba się?

    menu:
        "GD: Tak.":
            P1: To fajnie.
            #neutral Lia ON
            P1: Tak czy inaczej.

        "GD: Nie.":
            P1: O nie!
            #neutral Lia ON
            P1: Tak czy inaczej.

    #Lia thinking ON
    P1: Tak się zastanawiam…
    #sad_smile Lia ON
    P1: Może mogłabym tu przychodzić częściej.
    P1: Nie wiem w sumie do końca czemu tego nie robiłam od dawna. Chociaż…
    #surprised_neutral Lia ON
    P1: Chociaż może wiem… Chcesz też wiedzieć?
    #smile Lia ON
    P1: A zresztą i tak Ci powiem.
    #sad_smile Lia ON
    P1: Myślę, że zaczynam wpadać w ten monotonny tryb życia, który forsują na mnie rodzice.
    P1: Rodzice ciągle powtarzają mi, że mam ciężko pracować i być posłuszna.
    P1: Tylko jaki to ma sens? Nie mam nic konkretnego z tego życia…
    P1: Nawet nie mam żadnych przyjaciół. Jedyna mi bliska osoba musiała wyjechać do WIELKIEJ stolicy… Eh.
    P1: Może z Twoją pomocą spróbowałabym coś zmienić.
    P1: Co myślisz? Pomożesz mi?
    GD: Oczywiście! Zrobię co w mojej mocy.
    #dźwięk szelestu krzaczkowego w tle z 1sec opóźnienia
    P1: Dziękuję! Może…
    #Lia shock ON
    P1: Zaraz. Słyszałeś to?
    #komiks E1A ujęcie 1
    P1: Widzisz to? Ktoś tam chyba stoi?
    P1: Co mam zrobić?

    menu:
        "GD: Podejdź i sprawdź kto to.":
            # TODO +1 pkt PODEJDZLAS
            $ pojscieDoLasu = True
            #confused Lia ON
            P1: No dobrze…
            #komiks E1A ujęcie 2
            >Gdy tylko Lia się zbliżyła to zauważyła, że postać zniknęła.
            P1: Huh. Gdzie podziała się ta osoba?
            GD: Nie wiem. Wyglądało jakby zniknęła na Twoich oczach.
            P1: To prawda… Dziwne. Może mi się przewidziało.
            #powrót do normalnego ujęcia rozmowy z graczem
            GD: Możesz mieć rację.
            #surprised_happy Lia ON
            P1: Dzięki.

        "GD: Zawołaj. Zobaczymy kto to.":
            #confused Lia ON
            P1: Hmm… No dobrze…
            P1: HALO, JEST TAM KTO?
            >...
            >W odpowiedzi jednak powróciła tylko cisza.
            #komiks E1A ujęcie 3
            >Lia zbliżyła się lekko do drzewa.
            P1: Huh. Nikogo tu nie ma.
            #powrót do normalnego ujęcia rozmowy z graczem
            P1: Musiało mi się to przewidzieć.
            GD: I przesłyszeć w sumie.
            P1: W sumie tak.
            P1: Ale w końcu to las, takie dźwięki to norma.
            GD: Prawda. Możesz mieć rację.
            #surprised_happy Lia ON
            P1: Dzięki.

    #neutral Lia ON
    P1: Hmm. To jak, starczy przygód na jedną noc?

    menu:
        "GD: Tak! Wracajmy.":
            #smile Lia ON
            P1: Świetnie! No to wracamy.

        "GD: Nie. Zostańmy jeszcze.":
            P1: Ehh… Co chcesz jeszcze tu robić?
            #frown Lia ON
            GD: W zasadzie to nie wiem.
            P1: Świetnie. Mam pomysł. Może wracajmy?
            #relaxed Lia ON
            GD: Hmm. No dobra. Chodźmy.
            #smile Lia ON
            P1: Świetnie! Wracamy.


    #background zmiana na Tawerna z zewnątrz (wersja nocna ofc)
    >Lia wróciła do Tawerny szybko i bez żadnych problemów.
    >Myślała o tym, że czas ruszyć trochę swoje życie. Nie wiedziała jeszcze dokładnie jak.
    #zmiana tła na pokój P1 (ciągle noc), Lia w pozycji rozmowy z graczem
    #happy Lia ON
    P1: Dzięki za ten spacer.
    P1: Mam nadzieję, że teraz z Twoją pomocą uda się coś zmienić w moim życiu.
    P1: Dobranoc!
    GD: Dobranoc.
    #przejście w sen, taka mgiełka ładna i pojawia się CG_dream_good. Troszkę światła się majtają i efekt ekran przechodzi zoomem od dołu do góry, żeby jakoś tak zatrzymał się lekko na twarzy i potem poof budzi się
    #przejście do E2A

label e1b:
    #DUB04 - “try better next time”

    $ HatePath += 1
    #czarne tło
    >Obrażona na cały świat Lia ruszyła w stronę swojego pokoju.
    #background pokój Lii, wersja nocna i Lia w pozycji rozmawiającej z graczem
    >Dotarła dość szybko do swojego pokoju i zatrzasnęła drzwi, które wydały głośniejszy huk niż się spodziewała.
    #shock Lia ON
    >Przez moment nasłuchiwała z lekkim strachem czy nikogo nie obudziła.
    #annoyed Lia ON
    >Po krótkiej chwili jednak odetchnęła i usiadła na łóżku.
    P1: Dalej tu jesteś?

    menu:
        "GD: Tak.":
            #angry Lia ON
            P1: To chyba tyle z łamania rutyny.
            P1: Wielkie dzięki za pomoc.
            P1: Dobranoc.

        "GD: Wiesz, że teraz lepiej nie podpadać Twoim rodzicom.":
            #angry Lia ON
            P1: Pff.
            P1: Nagle tak się przejmujesz?
            P1: Widzę, że to tyle z łamania rutyny.
            P1: Dobranoc.

        "GD: ...":
            #angry Lia ON
            P1: Racja. Lepiej nic nie mów.
            #very_sad Lia ON
            P1: Najlepiej zostaw mnie samą sobie.
            #angry Lia ON
            P1: Dobranoc.

    #po “dobranoc” powolne przejście w czarny ekran jakby sen, może lekka mgiełka?
    #tutaj odpala się zły sen
    #efekt mgiełki i przejścia w sen, jako background mamy ciemny las z postacią z pochodnią, powolny zoom na nią leci (podobnie jak było obecnie), zbliżenie trwa chwilę i nagle po paru sekundach wyskakuje CG_dream_bad może z jakimś creepy dźwiękiem i po sekundzie poof znika wszystko i Lia się budzi
    #po śnie przejście do E2B

label e2a:
    #na ekranie pokój P1 o brzasku
    >Lia otworzyła oczy wraz z pierwszymi promieniami słońca, które muskały jej twarz zza okna.
    >Delikatne ciepło, które poczuła zmotywowało ją od razu do wstania.
    >Uśmiechnęła się niespodziewanie do zbliżającego się dnia.
    #Lia pojawia się na ekranie, rozmowa z graczem
    #smile Lia ON
    GD: Dzień dobry!
    #surprised_happy Lia ON
    P1: Oh! Dzień dobry!
    #smile Lia ON
    P1: Dziękuję za wczoraj! Od razu jakoś lepiej się czuję.
    #happy Lia ON
    P1: Nawet nie mam chęci spać do południa!
    P1: Dobra, czas się ogarnąć. Widzimy się na śniadaniu.
    #korytarz jako tło, bez postaci
    >Lia wyszła ze swojego pokoju wprost na Tawerniany korytarz.
    #Lia na ekranie, rozmawia z graczem
    #Lia confused ON
    P1: Chyba nigdy nie mówiłam Ci nawet o tym co jest w samej Tawernie…
    #Lia surprised_neutral ON
    P1: Powiedzieć Ci teraz?
    menu:
        "GD: Tak, chętnie posłucham.":
            #smile Lia ON
            P1: Dobrze!
            P1: Zaraz obok mojego pokoju jest sypialnia rodziców. Czyli nic ciekawego.
            P1: Tam z tyłu jest łazienka.
            #smirk Lia ON
            P1: Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada.
            GD: Haha, dobrze! Masz rację. Obiecuję, że nie będę.
            #smile Lia ON
            P1: Haha, no i super! Zaraz obok jest nasza jadalnia i kuchnia.
            P1: Teoretycznie mieliśmy tam jeść, ale po co brudzić dwa miejsca.
            P1: W związku z tym jemy na dole.
            #confused Lia ON
            P1: Tata chyba woli mieć zawsze oko na Tawernę.
            #smile Lia ON
            P1: No i jest mniej sprzątania!
            P1: Obok jest jedyny w naszym skrzydle pokój gościnny.
            P1: Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty.
            P1: No dobrze, to możemy iść dalej.

        "GD: Nie, nie ma takiej potrzeby.":
            P1: Oh. No dobrze, to chodźmy dalej.

    #background sala główna Tawerny, pusta. Lia na środku w pozycji rozmowy z graczem
    #confused Lia ON
    P1: No dobra. Rodziców chyba jeszcze nie ma. W razie czego jesteś ze mną tak?
    GD: Oczywiście. Cały czas.
    #Lia smile ON
    P1: Cieszę się. Dobra, wchodzę.
    #background zmiana na kuchnię, Lia po lewej patrzy w prawo
    #od prawej wchodzi P2
    #Lia smile ON
    P1: Dzień dobry Mamo!
    #od prawej wchodzi P3, P2 się lekko przesuwa w lewo, żeby zrobić miejsce
    P1: Dzień dobry Tato!
    #P2 i P3 patrzą na siebie, oboje confused ON
    >Rodzice spojrzeli po sobie lekko zaskoczeni.
    >Nieczęsto ich córka była tak uśmiechnięta.
    >Zrodziło to lekkie podejrzenia.
    #P2 i P3 patrzą teraz na Lię, tj. w lewo
    #neutral P2 i P3 ON
    #confused Lia ON
    P3: Dzień dobry… Czy coś się stało?
    P1: Dlaczego miało się coś stać?
    #P2 wychodzi na pierwszy plan (coś podobnego co wcześniej było)
    #P2 smile ON
    #surprised_sad Lia ON
    P2: Dziecko… Przecież Cię znamy. Co się stało?
    #disappointed Lia ON
    P1: Ehh…

    menu:
        "GD: Powiedz im prawdę.":
            jump e2a1

        "GD: Powiedz, że nic się nie stało.":
            #E2A2
            #confused Lia ON
            #P2 i P3 neutral ON
            P1: Nic się nie stało. Naprawdę.
            P3: Czyli mówisz, że jak tylko zamknęłaś Tawernę to poszłaś spać?
            menu:
                "GD: Powiedz, że tak. ":
                    P1: Tak.
                    P3: I po co kłamiesz?
                    P1: Nie kłamię…
                    #angry Zorn ON
                    P3: Nawet nie zaczynaj.
                    #shock Lia ON
                    P3: Wiem, że Cię nie było w pokoju…
                    #P3 patrzy na P2
                    P3: Nie mam do niej czasem siły.
                    #P3 patrzy na P1
                    #small tears Lia ON
                    P3: Czekam na Ciebie w sali. Mamy sporo pracy.
                    #P3 wychodzi z kuchni
                    P2: Musisz być bardziej odpowiedzialna.
                    P2: Nie możesz wychodzić nigdzie po nocy.
                    P2: Coś mogło Ci się stać…
                    P2: Nie wybaczylibyśmy sobie tego.
                    #sad P2 ON
                    P2: Postaraj się być bardziej ostrożna.
                    #P2 wychodzi z kuchni
                    #P1 do gracza, sad ON
                    P1: Nie wiem czy to była dobra rada…
                    P1: Ale mimo wszystko dzięki.
                    #Lia wychodzi z kuchni
                    $ e3a2 = True
                    #przejście do E3A2
                    jump e3

                "GD: Lepiej powiedz prawdę.":
                    P1: Nie…
                    #angry Zorn ON
                    P3: Czyli co robiłaś?!
                    #w tym miejscu idzie to samo co w E2A1, w całości

                    jump e2a1

        "GD: [Nic nie mów.]":
            # TODO jump be01
            #przejście do BE01





label e2a1:
    # E2A1
    #sad_smile Lia ON
    P1: Uhm. Po prostu byłam się przejść.
    #angry Zorn ON
    #shock Lia ON
    P3: GDZIE?!
    P3: Nie każ mi czekać!
    P2: Zorn. Nie denerwuj się proszę.
    #confused Lia ON
    P2: Ja się tym zajmę. Ty może przejdź się do sali głównej i sprawdź czy Cię tam nie ma.
    P3: Mhm. Może Tobie pójdzie sprawniej.
    P3: Czekam na Ciebie Lia w sali. Mamy sporo pracy.
    #P3 wychodzi, P2 troszkę zbliża się do P1
    P2: Lia… Powiedz gdzie dokładnie byłaś.
    #P1 sad ON
    P1: W lesie… Znaczy w Ogrodzie dokładnie.
    P2: Hmm. W tym Twoim Sekretnym Ogrodzie tak?
    #sad_smile Lia ON
    P1: Tak… Byłam się tylko przejść.
    P2: No rozumiem. Czy coś się stało jeszcze?
    #sad Lia ON
    P1: Nic szczególnego, tylko…
    P2: Tylko co?
    P1: Eh… Myślałam, że kogoś widziałam. Ale jestem pewna, że mi się przewidziało.
    P2: Hmm. Skąd pewność?

    #jeśli 1pkt PODEJDZLAS
    if pojscieDoLasu:
        P1: Poszłam sprawdzić… Nikogo nie było.
        P2: Oh dziecko… Bardzo nierozsądnie.
        P2: Najważniejsze, że nic się nie stało.

    #jeśli brak punktu PODEJDZLAS
    if not pojscieDoLasu:
        P1: Zawołałam czy ktoś tam jest. Nikogo nie było.
        P2: Nierozsądnie dziecko.
        P2: Dobrze, że nic się nie stało.


    P2: Musisz mi obiecać, że będziesz bardziej uważać w przyszłości.
    #smile P2 ON
    P1: No dobrze…
    P2: Cieszę się. Dokończ śniadanie i idź pomóż potem tacie.
    P1: Dobrze mamo.
    #P2 wychodzi z kuchni
    #sad_smile Lia ON, do gracza:
    P1: Dzięki za pomoc. Ciężko byłoby bez Ciebie.
    P1: No nic, czas zabrać się do pracy.
    $ e3a1 = True
    jump e3
    #przejście do E3A1

label e2b
    # bez śniadania bo koszmar
    #na ekranie pokój P1, poranek
    >...
    #od prawej wchodzi P3 angry
    >Lia gwałtownie wybudziła się z przerażającego snu gwałtownym wejściem ojca do pokoju.
    P3: Nie słyszysz jak Cię wołam?
    #Lia pojawia się po lewej, angry ON
    P1: Tato! Nie możesz tak wchodzić bez pukania. Co jakbym była rozebrana?!
    #surprised_happy Lia ON
    #neutral P3 ON
    P3: No dobrze dobrze, przepraszam - masz rację.
    P3: Po prostu wołałem Cię całą chwilę i martwiłem się, że coś się stało.
    P3: Ominęło Cię już śniadanie. Trzeba jeszcze przygotować Tawernę na otwarcie.
    #surprised_sad Lia ON
    P3: Czekam na Ciebie na dole.
    P1: No dobrze dobrze, zaraz przyjdę.
    #P3 wychodzi z pokoju, P1 mówi do gracza
    #sad_smile Lia ON
    P1: Dzień dobry.
    GD: Dzień dobry.
    P1: Ten sen… Był dziwny. Był przerażający…
    P1: Nie rozumiem go.
    GD: To tylko sen. Nie przejmuj się.
    P1: Może masz rację. Ale wciąż było to bardzo dziwne…
    P1: No nic. Trzeba się ogarnąć i czas do pracy. Znowu.
    >Lia wyszła ze swojego pokoju wprost na Tawerniany korytarz.
    #Lia na ekranie, rozmawia z graczem
    #Lia confused ON
    P1: Chyba nigdy nie mówiłam Ci nawet o tym co jest w samej Tawernie…
    #Lia surprised_neutral ON
    P1: Powiedzieć Ci teraz?
    menu:
        "GD: Tak, chętnie posłucham.":
            #smile Lia ON
            P1: Dobrze!
            P1: Zaraz obok mojego pokoju jest sypialnia rodziców. Czyli nic ciekawego.
            P1: Tam z tyłu jest łazienka.
            #smirk Lia ON
            P1: Swoją drogą. Nie zaglądaj do mnie jak tam jestem! Nie wypada.
            GD: Haha, dobrze! Masz rację. Obiecuję, że nie będę.
            #smile Lia ON
            P1: Haha, no i super! Zaraz obok jest nasza jadalnia i kuchnia.
            P1: Teoretycznie mieliśmy tam jeść, ale po co brudzić dwa miejsca.
            P1: W związku z tym jemy na dole.
            #confused Lia ON
            P1: Tata chyba woli mieć zawsze oko na Tawernę.
            #smile Lia ON
            P1: No i jest mniej sprzątania!
            P1: Obok jest jedyny w naszym skrzydle pokój gościnny.
            P1: Może kiedyś Ci go pokażę. Teraz i tak jest zamknięty.
            P1: No dobrze, to możemy iść dalej.
        "GD: Nie, nie ma takiej potrzeby.":
            P1: Oh. No dobrze, to chodźmy dalej.

    >Lia dotarła do sali głównej gdzie czekał na nią ojciec.

    #przejście do #E3A3





label e3:

    if e3a1:
        #tło bar, P1 po lewej, P3 prawo za barem
        >Po wyjściu z kuchni na Lię czekał ojciec.
        #confused Lia ON
        P3: Poczekaj moment Lia.
        P3: Rozmawiałem moment z Twoją matką.
        P3: Mimo, że byłaś nieodpowiedzialna to przyznałaś się co jest dobre.
        #surprised_neutral Lia ON
        P3: Możliwe, że trochę zbyt mocno Cię pilnujemy, więc mamy propozycję…
        #surprised_happy Lia ON
        P3: Jeśli masz ochotę możesz dziś skończyć wcześniej pracę i przejść się na festiwal do wioski.
        P1: Oh… Nie wiem co powiedzieć…
        P3: Po prostu powiedz czy chcesz iść.
        menu:
            "GD: Powiedz, że chcesz.":
                # TODO +1pkt FESTIVAL01
                #smile Lia ON
                P1: Chętnie pójdę. Dziękuję.
                P3: No dobrze… To przed wieczorem Cię zastąpię.
                P3: Tymczasem czas na pracę.

            "GD: Powiedz, że nie chcesz.":
                #sad_smile Lia ON
                P1: Dziękuję za propozycję, ale nie chcę iść.
                P3: Oh. No dobrze. Twoja decyzja.
                P3: No to czas na pracę.

    elif e3a2:
        #tło bar, P1 po lewej, P3 prawo za barem - P3 angry ON
        P3: No jesteś w końcu. Zostań chwilę.
        #surprised_sad Lia ON
        P3: Mam nadzieję, że następnym razem nie będziesz próbować kłamać.
        P3: Zacznij być bardziej odpowiedzialna.
        P3: A teraz chodź do pracy.
        #przechodzimy niżej


    else e3a3:
        #background sala główna, P1 lewo i P3 prawo stoją sobie
        P3: O! Jesteś wreszcie. Chodź mi pomóc.
        #przechodzimy od razu niżej



#background zmienia się na całą salę główną, P1 lewo i P3 prawo stoją sobie
P3: Dobra. Ja idę przygotować drugą salę. Ty zacznij od wytarcia stołów.
P3: Tylko dokładnie! Sprawdzę później.
#P3 wychodzi do prawej sali. frown Lia ON, mówi do gracza:
P1: Zawsze tak mówi i potem i tak nie sprawdza... No ale i tak trzeba to ogarnąć.
                # TODO !!! odpala się mini gra ze stoliczkiem
