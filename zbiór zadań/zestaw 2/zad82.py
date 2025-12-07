# chyba git

lista = [0, 0, 0, 1, 3, 5, 9]

def podciag(T):
    n = len(T)
    maksimum = 0
    for i in range(n): #start podciagu
        dl = 1
        s_elementow = T[i]
        s_indeksow = i
        for j in range(i + 1, n):
            if T[j] > T[i]:
                s_elementow += T[j]
                s_indeksow += j
                dl += 1
                if s_elementow == s_indeksow and dl > maksimum:
                    maksimum = dl
            else:
                break
    return maksimum

print(podciag(lista))
