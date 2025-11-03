# dobrze

N =  [25123471, 71021234, 23415678, 67888999]


def sklejenie(T):
    max_s = 0
    s = 0
    zmiana = 0
    for i in range(len(T) - 1):
        if T[i] % 100 == T[i + 1] // 1000000:
            s += T[i] % 100
            if s > max_s:
                max_s = s

        if T[i] % 1000 == T[i + 1] // 100000:
            s += T[i] % 1000
            if s > max_s:
                max_s = s
        
        else:
            s = 0
            zmiana = 1

    if zmiana == 1:
        return(-1)
    else:
        return(max_s)


print(sklejenie(N))