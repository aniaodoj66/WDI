# chyba ok
import random

def zad76(N):
    T = [random.randint(100, 999) for _ in range(N)]
    dlugosci = [1 for _ in range(N)]
    for dl in range(2, N // 2): # dlugosc fragmentow ktore bede szukac
        for pocz in range(0, N + 1 - dl): # gdzie sie bedzie zaczynal fragment
            kon = pocz + dl 
            fragment = T[kon - 1: pocz - 1: -1]
            for i in range(kon, N + 1 - kon): # gdzie bedzie szukal rewersu
                rewers = T[i: i + dl]
                if fragment == rewers:
                    if dl > dlugosci[pocz]:
                        dlugosci[pocz] = dl
    maksimum = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum