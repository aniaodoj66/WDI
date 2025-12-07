# działa

N = [2,6,5,7,30,70]
import math

def czy_pierwsza(x):
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, math.isqrt(x) + 1):
        if x % i == 0:
            return False
    return True

def funkcja(T):
    najwieksza = 0
    indeks = 0
    pierwsze = [0 for _ in range(len(T))]
    for i in range(len(T)):
        liczba = T[i]
        if czy_pierwsza(liczba):
            pierwsze[i] = 1
        for j in range(0, i):
            if pierwsze[j] == 1:
                if liczba % T[j] != 0:
                    break
                if liczba % T[j] == 0:
                    liczba = liczba // T[j]
        if T[i] > najwieksza and liczba == 1:
            najwieksza = T[i]
            indeks = i

    return najwieksza, indeks

print(funkcja(N))