# da się krócej, zad 87

def dzielniki(x):
    d = [0 for i in range(x)]
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            d[i] = i
    w = [i for i in d if i != 0]
    return w

def multi(T):
    max_dl = 0
    for i in range(len(T)):
        napis = T[i]
        lista = dzielniki(len(napis))
        for j in range(len(lista)):
            flaga = 0
            d = lista[j]
            ilosc = len(napis) // d - 1
            for k in range(ilosc):
                if napis[k: k+d] != napis[k+d:k+2*d]:
                    flaga = 1
                    break
            if flaga == 0:
                if len(napis) > max_dl:
                    max_dl = len(napis)
    return max_dl


print(multi(["ABCABCABCABC", "asdfasdfasdfasdf", "abab", "lollol"]))