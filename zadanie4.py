'''Importujemy funkcję math, następnie ustalamy zakres funkcją input, czyli przez uzytkownika.
Kolejnym krokiem jest stworzenie listy. I następnie przechodzimy do pętli for, która dodaję do listy wszystkie
zmienne "i" w podanym zakresie. Kolejnym elementem jest pętla w pętli, która sprawdza warunek
dopóki p jest mniejsze niż pierwiastek z podanego zakresu co pozwala nam
zmniejszyć ilośc operacji mnożenia, to dla każdej zmniennej i
w podanym zakresie moży zmienną p, która na początku jest równa 2 ale gdy wykona się mnożenie,
na wszystkich "i" z listy to do p dodajemy +1 i znów przechodzimy do pętli while gdzie sprawdamy warunkek
i znów do pętli for, gdzie mnożymy "p" przez każde "i" i tak dalej aż warunek w pętli while nie będzie spełniony.'''
import math

zakres = int(input("Podaj górny zakres liczb do których będzie liczyć program: "))
lista = []

for i in range(2, zakres + 1):
  lista.append(i)

p = 2
while p < math.sqrt(zakres):
    for i in range (p, zakres+1):
        if p*i in lista:
            lista.remove(p*i)
    p += 1

print("Liczby pierwsze z podanego zakresu to: ", lista)
