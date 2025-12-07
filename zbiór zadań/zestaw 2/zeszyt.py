

# a)
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

# b)
def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# c)
x = 123456789
liczba_x = int(math.log10(x)) + 1

# d)
def najdluzszy(T):
    dlugosci = [1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if T[j] < T[i]:
                if dlugosci[i] < dlugosci[j] + 1:
                    dlugosci[i] = dlugosci[j] + 1
    maksymalna = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksymalna:
            maksymalna = dlugosci[i]
    return maksymalna

# e)
def dwojkowy(x):
    nowa = 0
    k = 0
    while x > 0:
        nowa += (x % 2) * (10 ** k)
        k += 1
        x = x // 2
    return nowa

# f) 
def dziesietny2(x):
    nowa = 0
    k = 0 
    while x > 0:
        nowa += (x % 10) * (2 ** k)
        k += 1
        x = x // 10
    return nowa

# g) 
def szesnastkowy(x):
    nowa = ""
    while x > 0:
        reszta = x % 16
        tekst = ""
        if reszta > 9:
            tekst = chr(ord("A") + reszta - 10)
        else: 
            tekst = str(reszta)
        nowa = tekst + nowa
        x = x // 16
    return nowa

# h) 
def dziesietny16(liczba16):
    nowa = 0
    k = 0
    for i in range(len(liczba16) - 1, -1, -1):
        ostatnia = liczba16[i]
        if 65 <= ord(ostatnia) <= 70:
            ostatnia = ord(ostatnia) - 55
        nowa += int(ostatnia) * (16 ** k)
        k += 1
    return nowa

