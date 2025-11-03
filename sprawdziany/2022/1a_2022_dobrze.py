# dobrze działa

N = [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

def sequence(T):
    zakres = len(T) // 2
    for i in range(3, zakres):
        q = T[i] / T[0]
        ilosc = 0
        for j in range(0, len(T) - i):
            if T[j + i] / T[j] == q:
                ilosc += 1
                if ilosc >= i:
                    return(j - i + 1, j)
            else: 
                q = T[j + i] / T[j]
                ilosc = 1

print(sequence(N))