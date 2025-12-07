# no okej powiedzmy

import math

def zad93(numer):
    wynik = 0
    ilosc_cyfr = int(math.log10(numer)) + 1
    cyfry = [0 for _ in range(ilosc_cyfr)]
    for i in range(ilosc_cyfr):
        cyfry[ilosc_cyfr-i-1] = numer // (10 ** i) % 10 # lista uzupełniana od końca z cyframi po kolei
    # end for

    pc = [0 for _ in range(2 ** ilosc_cyfr)] # podciągi
    licznik = 1 # ile podciągów już jest zrobionych
    for cyfra in cyfry: # tworzenie wszystkich możliwych podciągów na podstawie poprzednich
        for i in range(0, licznik):
            pc[licznik] = pc[i] * 10 + cyfra
            licznik += 1
        # end for
    # end for

    for a in range(1, 2 ** ilosc_cyfr - 1):
        if pc[a] % 7 == 0:
            wynik += 1
        # end if
    # end for

    return wynik