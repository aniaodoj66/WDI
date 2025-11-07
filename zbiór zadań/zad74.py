
lista = [1,3,9,4,2,4,8,16,32]

def podciag(T):
    dlugosci = [1 for _ in range(len(T))]
    q1 = T[1] / T[0]
    for i in range(1, len(T)):
        q2 = T[i] / T[i - 1]
        if q1 == q2:
            dlugosci[i] = dlugosci[i - 1] + 1
        else:
            q1 = q2
            dlugosci[i] += 1
    maksimum = 0

    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum, dlugosci

print(podciag(lista))