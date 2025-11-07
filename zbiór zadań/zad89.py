# chyba git

lista = [13, 18, 23, 107, 33, 57, 221]
# lista = [31, 102, 113, 1223, 201, 321, 3131]


def zamiana4(x):
    liczba = 0
    k = 0
    while x > 0:
        liczba += (x % 4) * (10 ** k)
        x = x // 4
        k += 1
    return liczba

def te_same(x, y):
    x = zamiana4(x)
    y = zamiana4(y)
    lista_x = [0 for _ in range(10)]
    lista_y = [0 for _ in range(10)]
    while x > 0:
        lista_x[x % 10] = 1
        x = x // 10
    while y > 0:
        lista_y[y % 10] = 1
        y = y // 10
    if lista_x == lista_y:
        return True
    return False

def podciag(T):
    dlugosci = [1 for _ in range(len(T))]
    for i in range(1, len(T)):
        for j in range(i):
            if te_same(T[i], T[j]):
                if dlugosci[j] + 1 > dlugosci[i]:
                    dlugosci[i] = dlugosci[j] + 1
    maksimum = 0
    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum, dlugosci

print(podciag(lista))