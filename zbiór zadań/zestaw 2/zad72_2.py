

lista = [1,3,5,2,6,3,4,7,9]

def podciag(T):
    dlugosci = [1 for _ in range(len(T))]
    for i in range(1, len(T)):
        if T[i] > T[i - 1]:
            dlugosci[i] = dlugosci[i - 1] + 1
    maksimum = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum

print(podciag(lista))