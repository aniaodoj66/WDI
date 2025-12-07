# raczej dobrze

N = [2,11,15,12,9,6,7,4,7,1,3,9,12,15,12,9,3,4,1,7,7,1,4]

def zad76(T):
    dlugosci = [1 for _ in range(len(T))]
    for dl in range(2, len(T) // 2): # dlugosc fragmentow ktore bede szukac
        for pocz in range(0, len(T) + 1 - dl): # gdzie sie bedzie zaczynal fragment
            kon = pocz + dl 
            fragment = T[pocz: kon][::-1]
            for i in range(kon, len(T) + 1 - dl): # gdzie bedzie szukal rewersu
                rewers = T[i: i + dl]
                if fragment == rewers:
                    if dl > dlugosci[pocz]:
                        dlugosci[pocz] = dl
    maksimum = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum, dlugosci

print(zad76(N))