
# warunek na zero
# kiedy true
# kiedy false

def waga(slowo):
    kody = 0
    samogloski = 0
    for i in range(len(slowo)):
        litera = slowo[i]
        kody += ord(litera)
        if litera == "a" or litera == "e" or litera == "i" or litera == "o" or litera == "u" or litera == "y":
            samogloski += 1

    return kody, samogloski

""" Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
wypisać znaleziony wyraz. """

def wyraz(s1, s2, i = 0, wybor = None):
    if wybor is None:
        wybor = []

    if waga(s1) == waga(wybor):
        return wybor
    
    if i == len(s2):
        return False
    
    opcja1 = wyraz(s1, s2, i + 1, wybor + [s2[i]])
    if opcja1:
        return opcja1
    
    opcja2 = wyraz(s1, s2, i + 1, wybor)
    if opcja2:
        return opcja2

    return False