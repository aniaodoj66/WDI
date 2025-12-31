# działa ale do powtórzenia

def budowanie(x, y, i = 0, j = 0, lista = None, tekst = ""):

    if lista is None:
        lista = []

    x = str(x)
    y = str(y)

    if i == len(x) and j == len(y):
        lista += [int(tekst)]
        return
    if i < len(x):
        budowanie(x, y, i + 1, j, lista, tekst + x[i])
    if j < len(y):
        budowanie(x, y, i, j + 1, lista, tekst + y[j])
    return lista

print(budowanie(123, 75))