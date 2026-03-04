

def pierwsza(x) ->bool:
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    d = 5
    while d * d <= x:
        if x % d == 0: 
            return False
        d += 2
    return True


def czynniki(x) ->list:
    d = 3
    lista = []
    if x % 2 == 0:
        lista += [2]
    while d * d <= x:
        if x % d == 0 and pierwsza(d):
            lista += [d]
        d += 2
    return lista


def cykl(T, start, dl=0) ->int:
    s_p = start
    min_dl = float('inf')
    # warunek kiedy ma działać
    if s_p == start and dl > 0:
        return
    # warunek kiedy ma skończyć
    if dl == len(T):
        return 0
    mozliwe = czynniki(T[start])
    for i in range(len(mozliwe)):
        k = mozliwe[i]
        if 0 <= start + k <= len(T) and T[start] % 2 == 0:
            cykl(T, start + k, dl+1)
        if 0 <= start - k <= len(T) and T[start] % 2 != 0:
            cykl(T, start - k, dl+1)
    if dl < min_dl:
        min_dl = dl
    if min_dl > 10:
        return 0
    return min_dl
