# źle bo liczy też pola na których stoją wierze

def chess(T):
    punkty = 0
    w1 = 0
    w2 = 0
    suma_w = 0
    suma_w2 = 0
    for i in range(len(T)):
        wiersz = T[i]
        suma = 0
        for j in range(len(wiersz)):
            suma += wiersz[j]
        if suma >= suma_w2:
            if suma >= suma_w:
                suma_w2 = suma_w
                suma_w = suma
                w2 = w1
                w1 = i
            else:
                suma_w2 = suma
                w2 = i
    k1 = 0
    k2 = 0
    suma_k = 0
    suma_k2 = 0
    for i in range(len(T)):
        suma2 = 0
        for j in range(len(T)):
            suma2 += T[j][i]
        if suma2 >= suma_k2:
            if suma2 >= suma_k:
                suma_k2 = suma_k
                suma_k = suma
                k2 = k1
                k1 = i
            else:
                suma_k2 = suma
                k2 = i
    punkty += int(T[w1][k1])
    punkty += int(T[w1][k2])
    punkty += int(T[w2][k1])
    punkty += int(T[w2][k2])
    calkowita_suma = suma_k2 + suma_k + suma_w2 + suma_w - punkty
    return (w1, k1, w2, k2, calkowita_suma)

print(chess([[4,0,2],[3,0,0],[6,5,3]]))