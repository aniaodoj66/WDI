# niech będzie 

def sito(N):
    lista = []
    for i in range(N + 1):
        lista += [i]
    lista[1] = 0
    for i in range(2, len(lista)):
        d = 2
        while d * i <= N:
            lista[d * i] = 0
            d += 1
    nowa = []
    for i in range(len(lista)):
        if lista[i] != 0:
            nowa += [i]
    return nowa

print(sito(50))