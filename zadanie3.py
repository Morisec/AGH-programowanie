"""Tłumaczenie z pythonowego na polski
Na początku przypisujemy "i" = 0 oraz tworzymy pustą listę. Następnie tworzymy pętle
która się wykonuję dopóki zmienna "i" nie dojdzie do 199, czyli 200 razy bo
0 zaliczamy do liczb natrualnych. Kolejnym krokiem jest ustanowienie głównego
warunku czy liczba "i" która traktujemy jako string jest równa swojej odwrotności,
dodajemy ją do listy bo warunek jest true, jeśli nie to wykonujemy blok else czyli dodajemy
naszą liczbe "x" do odwrotności tej liczby i znów sprawdzamy warunek, jeśli się zgadza to
dodajemy ją listy, jeśli nie to kontynuujemy aż do 10 lub jeśli osiągniemy palidrom.
Gdy po 10 razie warunek się nie zgadza to poprostu nie dodajemy tego do listy. Na końcu sprawdzamy
czy zawsze osiągnelismy palindrom."""

i = 0
palidromy = []
while i <= 199:

    palidrom = str(i) == str(i)[::-1]
    x = i
    y = 0

    while y < 10:
        print(y)

        if palidrom == True:
            palidromy.append(i)
            break
        else:
            x = x + int(str(x)[::-1])

            palidrom = str(x) == str(x)[::-1]

            y = y + 1

            if palidrom == True:
                palidromy.append(i)
                break
    i = i + 1
if len(palidromy) != 200:
    print("Nie zawsze osiągniemy palidrom")
    print("Palidrom osiągnieto:",len(palidromy), "razy")
else:
    print("Zawsze osiągniemy palidrom")


