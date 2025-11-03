# dobrze

def wielokrotnosc(x):
    for d in range(2, int(x**0.5) + 1):
        if x % (d * d) == 0 and x // (d * d) > 1:
            return True
    return False

def usuwanie(T):
    indeksy_w = [0 for _ in range(len(T))]
    indeksy_k = [0 for _ in range(len(T))]

    for i in range(len(T)):
        wiersz = T[i]
        for j in range(len(wiersz)):
            if wielokrotnosc(wiersz[j]) == False:
                indeksy_w[i] = 1
                indeksy_k[j] = 1
    
    if sum(indeksy_w) > 1 and sum(indeksy_k) > 2:
        return False
    else:
        return True
