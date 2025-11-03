# chyba git ale nie znalazłam podciągu tylko własności

def zamiana4(x):
    liczba = 0
    k = 1
    while x > 0:
        liczba += (x % 4) * (10 ** k)
        x = x // 4
        k += 1
    return liczba

def te_same(x, y):
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