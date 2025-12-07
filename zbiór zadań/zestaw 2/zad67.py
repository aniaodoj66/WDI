# dobrze !!!

dokladnosc = 1000
ile = 7

def dzielenie(x, y, n):
    t = [0 for _ in range(n + 1)]
    for i in range(len(t)):
        cc = x // y
        t[i] = cc
        od = cc * y 
        x = (x - od) * 10
    return t


def silnia(x):
    y = 1
    for i in range(1, x + 1):
        y *= i
    return y

def dzialanie(ilosc, n):
    suma = [0 for _ in range(n)]
    for i in range(0, ilosc + 1):
        terazniejsza = dzielenie(1, silnia(i), n)
        for j in range(len(suma)-1, -1, -1):
            suma[j] += terazniejsza[j]
            if j != 0 and suma[j] >= 10:
                suma[j - 1] += 1
                suma[j] = suma[j] % 10
    return suma

print(dzialanie(20, 20))