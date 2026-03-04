

def repair(T):
    n = len(T)

    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    if i != k and j != l:
                        T[i][j], T[k][l] = T[k][l], T[i][j]
                