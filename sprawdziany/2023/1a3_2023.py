# działa

T = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]

import math

def czynniki(n):
    d = 2
    lista = [0 for _ in range(n)]
    while n > d:
        if n % d == 0:
            lista[d] = 1
            n = n // d
        else:
            d += 1
    lista2 = []
    for i in range(len(lista)):
        if lista[i] == 1:
            lista2.append(i)
    return lista2

def w(a, b):
    if a > 1 and b >1:
        ta = czynniki(a)
        tb = czynniki(b)
        if ta == tb and len(ta) > 0:
            return True
    return False


def zgodne(t):
    liczba = 0
    for j in range(len(t)):
        for s in [j - 2, j - 1, j + 1, j + 2]:
            if 0 <= s <= len(t) - 1 and w(t[s], t[j]):
                liczba += 1
                break
                
    return(liczba)

print(zgodne(T))
