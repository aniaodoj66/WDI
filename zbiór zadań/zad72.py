# najdluzszy podciag rosnacy ale nie jest spójny

lista = [1,3,5,2,6,3,4,7,9]

def podciag(T):
    dlugosci = [1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if T[i] > T[j]:
                if dlugosci[j] + 1 > dlugosci[i]:
                    dlugosci[i] = dlugosci[j] + 1

    maksimum = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    
    return maksimum

print(podciag(lista))