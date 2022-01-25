'''Na początku używam funckji która ma dzielić wyraz na litery,
i każdą literę zapisywać w liście. Otwieram plik "data.txt" z opcją read,
nastepnie konwertuje zawartość pliku to zmiennej "data". Kolejnym krokiem jest stworzenie zmiennej
"splittable" za pomoca funkcji "split", która dzieli wyraz na litery.
W póżniejszym etapie tworzymy pustą listę, do której dodajemy litery
z funkcji while. I dopóki zmienna "i" jest mniejsza od dlugości listy to wykonujemy
funkcje warunkowe if. W których to skorzystałem z tablicy ASCII żeby nie robić własnego słownika i za pomocą funkcji
ord która to zmienia litere w kod tej litery w ASCII, a chr robi odwrotność, dlatego trzeba było
zrobić przesunięcie dla każdej litery o wartośći z klucza, a dlatego ,że klucz się powtarza można było
zastosować modulo aby ze względu na położenie litery w liście przesunąc ją o odpowiednią wartość jak w kluczu.
Na koniec drukujemy zaszyfrowane słowo jako listę oraz za pomocą funkcji join, łączymy litery w całość.
Analogicznie postępujemy dla deszyfrowywania słowa.'''
def split(word):
    return [char for char in word]

text_file = open("data.txt", "r")

# konwersja na string
data = text_file.read()

SplitTable = split(data)

wordCoded = []

#print(ord("A"))
#print(chr(65))

i = 0
#
#    3 1 2 0 6 3 1 2 0 6 3   1   2
#    P R O G R A M O W A N   I   E
#    0 1 2 3 4 5 6 7 8 9 10 11  12

while i < len(SplitTable):
    if (i == 0 or i % 5  == 0):

        wordCoded.append(chr(ord(SplitTable[i])+3))  #  83 czyli s zamiast p

    if (i == 1 or i % 5  == 1):

        wordCoded.append(chr(ord(SplitTable[i]) + 1))
    if (i == 2 or i % 5  == 2):

        wordCoded.append(chr(ord(SplitTable[i]) + 2))
    if (i == 3 or i % 5  == 3):

        wordCoded.append(chr(ord(SplitTable[i]) + 0))
    if (i == 4 or i % 5  == 4):

        wordCoded.append(chr(ord(SplitTable[i]) + 6))
    i = i + 1

print("Zaszyfrowane słowo to: ", wordCoded)
print(''.join(wordCoded))

print("\n")


wordUncoded = []
i = 0
while i < len(wordCoded):
    if (i == 0 or i % 5  == 0):

        wordUncoded.append(chr(ord (wordCoded[i])-3))

    if (i == 1 or i % 5  == 1):

        wordUncoded.append(chr(ord(wordCoded[i]) - 1))
    if (i == 2 or i % 5  == 2):

        wordUncoded.append(chr(ord(wordCoded[i]) - 2))
    if (i == 3 or i % 5  == 3):

        wordUncoded.append(chr(ord(wordCoded[i]) - 0))
    if (i == 4 or i % 5  == 4):

        wordUncoded.append(chr(ord(wordCoded[i]) - 6))
    i = i + 1


print("Deszyfrowane słowo to: ", wordUncoded)
print(''.join(wordUncoded))


text_file.close()










"""

print(data)

a = "A"

print(ord(a))

chr (65)

chr (ord (a)+1)

print(chr (ord (a)+1))


"""
