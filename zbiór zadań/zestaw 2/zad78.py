# zle ale nie chce mi sie myslec 
import math

def fibonacci(n):
    lista = [0,1,1]
    element = 0
    while element < n:
        element = lista[-1] + lista[-2]
        lista += [element]
    return lista

def pierwsza(n):
    if n == 0 or n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return 2
    return 1

def warunki(N):
    ilosc = 0
    for i in range(len(N)):
        if i in fibonacci(len(N)):
            if pierwsza(N[i]) != 2:
                return False
        else:
            if pierwsza(N[i]) == 1:
                ilosc += 1
    if ilosc > 0:
        return True
    return False