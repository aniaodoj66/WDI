# nie działa aż tak dobrze
N = [
[5, 8, 12, 7, 9, 10],
[11, 3, 6, 2, 5, 7],   
[6, 4, 5, 9, 3, 9],   
[6, 3, 5, 8, 14, 6],   
[2, 8, 7, 4, 21, 22],   
[8, 12, 14, 5, 7, 4]
]

def seq(T):
    przekatna = len(T)
    tablica = []
    for i in range(len(T)):
        for j in range(2, przekatna):
            if T[j][i + j] == T[j - 1][i + j - 1] + T[j - 2][i + j - 2] - 1:
                tablica = [T[j - 2][i + j - 2], T[j - 1][i + j - 1], T[j][i + j]]
                k = j + 1
                while i + k < przekatna:
                    if T[k][i + k] == T[k - 1][i + k - 1] + T[k - 2][i + k - 2] - 1:
                        tablica += [T[k][i + k]]
                        k += 1
                    else:
                        break
            if j == przekatna:
                przekatna -= 1
            if len(tablica) > 0:
                return tablica
            

print(seq(N))