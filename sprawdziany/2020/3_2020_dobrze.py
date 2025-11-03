# wszystko g

def suma_w(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    return s

def suma_k(x, kolumna):
    s = 0
    for i in range(len(x)):
        s += x[i][kolumna]
    return s

def chess(T):
    max_suma = 0
    lista = []
    for w1 in range(len(T)):
        for k1 in range(len(T)):
            for w2 in range(len(T)):
                suma = 0
                for k2 in range(len(T)):
                    if w1 != w2 and k1 != k2:
                        suma = suma_w(T[w1]) + suma_k(T, k1) + suma_w(T[w2]) + suma_k(T, k2)
                        suma -= 2 * T[w1][k1]
                        suma -= 2 *T[w2][k2]
                        suma -= T[w1][k2]
                        suma -= T[w2][k1]
                    if w1 == w2 and k1 != k2:
                        suma = suma_w(T[w1]) + suma_k(T, k1) + suma_k(T, k2)
                        suma -= 2 * T[w1][k1]
                        suma -= 2 *T[w2][k2]
                    if w1 != w2 and k1 == k2:
                        suma = suma_w(T[w1]) + suma_w(T[w2]) + suma_k(T, k1)
                        suma -= 2 * T[w1][k1]
                        suma -= 2 *T[w2][k2]
                    if suma > max_suma:
                        max_suma = suma
                        lista = [w1, k1, w2, k2]
    return (max_suma, lista)

print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]))
print(chess([[4,0,2],[3,0,0],[6,5,3]]))
