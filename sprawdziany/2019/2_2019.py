# umiem zrobic z 1 wierszem a 2 kolumny na razie nie

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
    ilosc_wierszow = 0
    for i in range(len(T)):
        wiersz = T[i]
        for j in range(len(wiersz)):
            liczba = dwojkowy(wiersz[j])
            if ilosc_jedynek(liczba) != True:
                ilosc_wierszow += 1
                break
    if ilosc_wierszow > 1:
        return False
    return True

print(tablica(N))