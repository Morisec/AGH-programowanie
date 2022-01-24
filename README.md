# AGH-programowanie
Zadania z programowania 
Zadania do samodzielnego rozwiązania
1.	Proszę napisać program rozwiązujący układ równań N równań liniowych O N niewiadomych.
Dane dla problemu należy wczytać z pliku tekstowego. W pierwszym wierszu znajduje się liczba równań N, kolejne wiersze zawieraja macierz współczynników oraz wyrazy wolne, na przykład plik:
3
1 2 3 7
-1 2 4 6
2 1 1 13
Odpowiada układowi 3 równań o 3 niewiadomych w postaci:
X+2Y+3Z=7
-X+2Y+4Z=6
2X+Y+Z=13
Program powinien uwzględnić przypadki układu nieoznaczonego i sprzecznego. Wskazówka: rozważyć zastosowanie biblioteki numpy.

2.	Liczby Armstronga to N-cyfrowa liczba naturalna która jest sumą swoich cyfr podniesionych do potęgi N. Na przykład: 153 = 13+53+33. Proszę napisać program znajdujący jak najwięcej takich liczb.

3.	Palindrom to coś, co czyta się tak samo od przodu i od tyłu. Hipoteza: weź dowolną liczbę naturalną.  Jeżeli nie jest palindromem, to zapisz ją od tyłu i dodaj obie liczby. Jeżeli wynik nadal nie jest palindromem, kontynuuj, traktując go jako daną. Przerwij, gdy osiągniesz palindrom, albo po 10. próbie. Na przykład: 78+87=165, 165+561=726, 726+627=1353, 1353+3531=4884. Napisz program sprawdzający hipotezę dla pierwszych 200 liczb naturalnych jako startowych. Czy zawsze osiągniemy palindrom?

4.	Metoda Sita Eratostenesa. Ze zbioru liczb naturalnych z przedziału [2,n], wybieramy najmniejszą, czyli 2, i wykreślamy wszystkie jej wielokrotności większe od niej samej. Z pozostałych liczb wybieramy najmniejszą niewykreśloną liczbę (3) i usuwamy wszystkie jej wielokrotności większe od niej samej. Według tej samej procedury postępujemy dla kolejnych liczb. Proces ten pozostawia nieskreślone wyłącznie liczby pierwsze. Proszę napisać program wyszukujący liczby pierwsze w zadanym zakresie.

5.	Komputer jest doskonałym narzędziem służącym do szyfrowania i deszyfrowania tajnych wiadomości. W metodzie Gronsfelda, będącą modyfikacją szyfru Cezara, stosuje się klucz liczbowy. Biorąc klucz o wartości 31206 i niezaszyfrowany tekst „PROGRAMOWANIE”, uzyskujemy następujący szyfrogram:
 31206 31206 312
 PROGR AMOWA NIE
 SSQGX DNQWG QJG
Kolejne litery są przesuwane o kolejne wartości z klucza. Proszę napisać programy dokonujące szyfrowania i deszyfrowania pliku tekstowego zadanym kluczem.

6.	Korzystając z rachunku prawdopodobieństwa jesteśmy w stanie policzyć szansę, że wśród n osób są przynajmniej 2, które mają urodziny tego samego dnia. Proszę napisać program, który sprawdzi to empirycznie: należy wylosować n dni urodzin i sprawdzić, czy któryś się powtórzył. Takie losowanie powtarzamy wielokrotnie (np. 1000 razy) i sprawdzamy w ilu przypadkach zdarzyło się, że przynajmniej 2 osoby miały urodziny tego samego dnia.
Wersja nieco trudniejsza: niech to nie będą 2 osoby, tylko k osób.

7.	Napisać program pozwalający grać w grę MasterMind: https://pl.wikipedia.org/wiki/Mastermind_(gra_planszowa). Kod do odgadnięcia powinien składać się z 4 cyfr od 1-6 (cyfry mogą się powtarzać). Pomocny będzie moduł random.


Należy rozwiązać minimum 4 zadania. Rozwiązanie zadania powinno zawierać: krótki opis rozwiązania, kod programu, wyniki programu dla przykładowych danych.  Rozwiązanie każdego zadania powinno się znajdować w osobnym pliku .py – opis proszę umieścić jako napis na początku pliku (w potrójnych cudzysłowach). Plik taki proszę umieścić w systemie Moodle.


