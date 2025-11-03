# nw co to

T = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]

def dzielenie(x):
    dzielniki = [0 for j in range (500)]
    d = 2
    while x > 1:
        if x % d == 0:
            dzielniki[d] = 1
            x = x // d
        else:
            d += 1
    return dzielniki

zgodne = 0
for i in range(len(T)):
    n = T[i]
    zgodne_n = 0
    tablica = dzielenie(n)
    for j in range(i - 2, i + 3):
        flaga = 0
        if i != j:
            tablica2 = dzielenie(T[j])
            if tablica != tablica2:
                flaga = 1
                break
            if flaga == 0:
                zgodne_n = 1
    if zgodne_n == 1:
        zgodne += 1
    
