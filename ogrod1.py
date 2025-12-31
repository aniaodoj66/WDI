

pierwsza = input().split()
wymiar = int(pierwsza[0])
ilosc = int(pierwsza[1])

# gora, prawo, dol, lewo
wiersz_ruchy = [-1, 0, 1, 0] 
kolumna_ruchy = [0, 1, 0, -1]

lustra = {}
for i in range(ilosc):
    linijka = input().split()
    wiersz = int(linijka[0])
    kolumna = int(linijka[1])
    kat = int(linijka[2])
    lustra[(wiersz,kolumna)] = kat

odbicia = { 45:  {0:1, 1:0, 2:3, 3:2},
    135: {0:3, 3:0, 2:1, 1:2}}

def droga(dzialki, start_w, start_k, s_kierunek):

    wspolrzedne = set()
    w = start_w
    k = start_k
    d = s_kierunek
    koniec = wymiar * wymiar * 4 + 4
    liczba = 0

    while liczba < koniec:
        if not (0 <= w < wymiar and 0 <= k < wymiar):
            return wspolrzedne, (w, k, d)
        if (w,k) in dzialki:
            wspolrzedne.add((w,k))
            d = odbicia[dzialki[(w,k)]][d]
        
        w = w + wiersz_ruchy[d]
        k = k + kolumna_ruchy[d]
        liczba += 1

    return wspolrzedne, (w, k, d)


gorne, _ = droga(lustra, 0, 0, 2)        
dolne, _ = droga(lustra, wymiar - 1, wymiar - 1, 0)      

nie_ma = []
for l in lustra:
    if (l not in gorne) and (l not in dolne):
        nie_ma.append(l)

if len(nie_ma) == 1:
    kandydaci = nie_ma
else:
    kandydaci = []
    for l in lustra:
        kandydaci += [l]

puste = []
for w in range(wymiar):
    for k in range(wymiar):
        if (w, k) not in lustra:
            puste +=[(w,k)]

def czy_git(usuniecie, dodanie, kat):
    nowa = {}
    for l in lustra:
        nowa[l] = lustra[l]

    if usuniecie in nowa:
        del nowa[usuniecie]
    else:
        return False
    nowa[dodanie] = kat
    wspolrzedne, (ww, kk, dd) = droga(nowa, 0, 0, 2)
    pw = ww - wiersz_ruchy[dd]
    pk = kk - kolumna_ruchy[dd]
    if not (pw == wymiar - 1 and pk == wymiar -1 and dd == 2):
        return False
    
    ppp = []
    for p in nowa:
        ppp.append(p)
    if len(wspolrzedne) != len(ppp):
        return False
    for p in ppp:
        if p not in wspolrzedne:
            return False
    return True

for u in kandydaci:
    for d in puste:
        for kat in (45, 135):
            if czy_git(u, d, kat):
                print(u[0], u[1])
                print(d[0], d[1])
                raise SystemExit
            
for u in list(lustra.keys()):
    for d in puste:
        for kat in (45, 135):
            if czy_git(u, d, kat):
                print(u[0], u[1])
                print(d[0], d[1])
                raise SystemExit

