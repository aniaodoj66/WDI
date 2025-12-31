

"""
5 6 # dlugosc boku, ilosc luster
0 4 45 # wiersz, kolumna, kąt
1 1 45
3 0 135
3 3 45
4 1 135
4 4 135
"""


parts = input().split()
N = int(parts[0])
L = int(parts[1])

mirrors = {}
for i in range(L):
    line = input().split()
    r = int(line[0])
    c = int(line[1])
    a = int(line[2])  # 45 albo 135
    mirrors[(r,c)] = a

# kierunki: 0 = gora, 1 = prawo, 2 = dol, 3 = lewo
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# odbicia: proste mapowanie kąt -> jak zmienia sie kierunek
reflect = {
    45:  {0:1, 1:0, 2:3, 3:2},   # '/'  : up->right, right->up, down->left, left->down
    135: {0:3, 3:0, 2:1, 1:2}    # '\'  : up->left, left->up, down->right, right->down
}

# funkcja śledząca promień od (sr,sc) z kierunkiem sd
def trace(mapa, sr, sc, sd):
    visited = set()
    r = sr
    c = sc
    d = sd
    limit = N*N*4 + 4
    step = 0
    while step < limit:
        # jeśli wyszedlismy poza plansze -> zwroc informacje o wyjsciu
        if not (0 <= r < N and 0 <= c < N):
            return visited, (r, c, d)
        # jesli jest lustro, odwiedzamy je i zmieniamy kierunek
        if (r,c) in mapa:
            visited.add((r,c))
            d = reflect[mapa[(r,c)]][d]
        # idziemy dalej
        r = r + dr[d]
        c = c + dc[d]
        step += 1
    # ochrona przed zapetleniem - zwroc to co mamy
    return visited, (r, c, d)

# zobaczmy, które lustra nie sa widoczne z zadnego wejsci a
vn, _ = trace(mirrors, 0, 0, 2)          # z wejscia polnocnego: (0,0) w dol
vs, _ = trace(mirrors, N-1, N-1, 0)      # z wejscia poludniowego: (N-1,N-1) w gore

hidden = []
for p in mirrors:
    if (p not in vn) and (p not in vs):
        hidden.append(p)

# kandydaci do zabrania: jesli jedno niewidoczne -> to ono, inaczej wszystkie
if len(hidden) == 1:
    remove_candidates = hidden
else:
    remove_candidates = []
    for p in mirrors:
        remove_candidates.append(p)

# lista pustych pol
empties = []
for r in range(N):
    for c in range(N):
        if (r,c) not in mirrors:
            empties.append((r,c))

# funkcja testujaca czy po przeniesieniu lustra konfiguracja jest dobra
def good(remove_pos, add_pos, angle):
    # zbuduj nowa mape
    newmap = {}
    for k in mirrors:
        newmap[k] = mirrors[k]
    # usun
    if remove_pos in newmap:
        del newmap[remove_pos]
    else:
        return False
    # dodaj
    newmap[add_pos] = angle
    visited, (er, ec, ed) = trace(newmap, 0, 0, 2)
    # sprawdzamy, czy promien wychodzi przez poludniowe wejscie:
    pr = er - dr[ed]
    pc = ec - dc[ed]
    if not (pr == N-1 and pc == N-1 and ed == 2):
        return False
    # sprawdzamy czy odwiedzil wszystkie lustra
    keys = []
    for k in newmap:
        keys.append(k)
    if len(visited) != len(keys):
        return False
    # sprawdzic, ze zbiory sa takie same
    for k in keys:
        if k not in visited:
            return False
    return True

# próbujemy znaleźć rozwiązanie
for rem in remove_candidates:
    for add in empties:
        for ang in (45, 135):
            if good(rem, add, ang):
                print(rem[0], rem[1])
                print(add[0], add[1])
                raise SystemExit

# fallback: spróbuj wszystkie możliwe usunięcia (jakby heurystyka zawiodła)
for rem in list(mirrors.keys()):
    for add in empties:
        for ang in (45, 135):
            if good(rem, add, ang):
                print(rem[0], rem[1])
                print(add[0], add[1])
                raise SystemExit