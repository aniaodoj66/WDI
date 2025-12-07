# XDDD

import math

def czynniki(n):
    d = 2
    lista = [0 for _ in range(n)]
    while n > 0:
        if n % d == 0:
            lista[d] += 1
            n = n // d
        else:
            d += 1
    return lista

