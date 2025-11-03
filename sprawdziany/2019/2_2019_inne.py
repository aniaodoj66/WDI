

N = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def dwojkowy(x):
    k = 1
    n = 0
    while x > 0:
        n += (x % 2) * k
        k *= 10
        x = x // 2
    return n
 
def ilosc_jedynek(x):
    ilosc = 0
    while x > 0:
        if x % 10 == 1:
            ilosc += 1
        x = x // 10
    if ilosc % 2 == 1:
        return True
    else:
        return False
    
def tablica(T):
    T_bledy = [[0 for _ in range(len(T[0]))] for _ in range(len(T))]
    indeksy_w = [0 for _ in range(len(T))]
    indeksy_k = [0 for _ in range(len(T))]

    for i in range(len(T)):
        wiersz = T[i]
        for j in range(len(wiersz)):
            liczba = dwojkowy(wiersz[j])
            if ilosc_jedynek(liczba) != True:
                T_bledy[i][j] = 1

    w_bledy = 0
    k_bledy = 0

    for i in range(len(T_bledy)):
        w = T_bledy[i]
        for j in range(len(w)):
            if w[j] == 1:
                indeksy_w[i] = 1
                indeksy_k[j] = 1
    for i in range(len(indeksy_w)):
        if indeksy_w[i] == 1:
            w_bledy += 1
        if indeksy_k[i] == 1:
            k_bledy += 1
        if k_bledy > 2 or w_bledy > 1:
            return False
    return True

print(tablica(N))