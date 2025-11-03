# DO ZROZUMIENIA

def spirala(T):
    n = len(T)
    l = 1
    prawo = n
    lewo = 0
    gora = 0
    dol = n # przod bok tyl
    while l <= n * n:
        for i in range(lewo, prawo):
            T[gora][i] = l
            l += 1
        gora += 1
        for i in range(gora, dol):
            T[i][prawo] = l
            l += 1
        prawo -= 1
        for i in range(prawo - 1, lewo - 1, -1):
            T[dol][i] = l
            l += 1
        dol -= 1
        for i in range(dol - 1, gora - 1, -1):
            T[i][lewo] = l
            l += 1
        lewo += 1