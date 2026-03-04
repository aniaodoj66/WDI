
""" Przed poprawkami """


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


""" Po poprawkach """


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

# zmiana warunku na dzialanie pętli w funkcji czynniki() oraz x > 2
def czynniki(x) ->list:
    d = 3
    lista = []
    if x % 2 == 0 and x > 2:
        lista += [2]
    while 2 * d <= x:
        if x % d == 0 and pierwsza(d):
            lista += [d]
        d += 2
    return lista

# dodanie s_p jako argument funkcji cykl()
def cykl(T, start, dl=0, s_p = -1) ->int:
    if s_p == -1:
        s_p = start
    min_dl = float('inf')

    if s_p == start and dl > 0:
        return dl # dopisanie dl do return oraz zmiana z dl == len(T) na dl > 10
    if dl > 10:
        return 0

    mozliwe = czynniki(T[start])
    for i in range(len(mozliwe)):
        k = mozliwe[i]
        # zmiana na silną nierówność
        if 0 <= start + k < len(T) and T[start] % 2 == 0:
            n = cykl(T, start + k, dl+1, s_p)
            if n > 0: # zmiana aktualizacji zmiennej min_dl
                min_dl = min(min_dl, n)
        if 0 <= start - k < len(T) and T[start] % 2 != 0:
            n = cykl(T, start - k, dl+1, s_p)
            if n > 0: 
                min_dl = min(min_dl, n)
    
    if min_dl > 10:
        return 0
    return min_dl
