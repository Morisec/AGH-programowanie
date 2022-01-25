'''tlumaczenie z pythonowego na polski:
Na początku definiujemy zmienną "i" = 0, nastepnie za pomocą pętli while sprawdzamy czy "i" <= "x",
a warunek ten zawsze będzie prawdziwy do momentu gdy "i" osiągnie wartośc "x", dlatego wykonujęmy instrukcję poniżej,
która to tworzy nam listę "y" z elemtów znajdujących się w liczbie "i", którą na tą chwilę traktujemy jako string,
na przykład "i" = 11 to "y" = [1, 1].
Kolejnym krokiem jest zdefiniowanie zmiennej "a", która to przyjmuję wartość długości listy "y".
Następnie ustalamy zmienna "sumaPotęg" = 0, jednak pożniej dla wszystkich
elemntów w liście "y" "sumaPotęg" = kazdy elememnt z listy do potegi dlugosci tej listy.
Na końcu sprawdzamy czy "i" jest równe "sumiePotęg", jeżeli tak to wywolujemy printa
i potem do "i" dodajemy 1 i sprawdzamy dla kolejnej liczby czy jest liczba Armstronga i tak az osiągniemy nasz "x"'''


def Liczby_Armstronga(x):

    i = 0
    while i <= x:
        y = [int(a) for a in str(i)]
        a = len(y)
        #print("dla i =", i, " cyfry to", y, "Dlugosc to", a)

        sumaPotęg = 0
        for element in y:
            sumaPotęg += element ** a

        if i == sumaPotęg:
            print(sumaPotęg, " jest liczbą Armstronga")

        i = i + 1

(Liczby_Armstronga(2001))