

pierwsza = input().split()
wymiar = int(pierwsza[0])
ilosc = int(pierwsza[1])

# gora, prawo, dol, lewo
wiersz_ruchy = [-1, 0, 1, 0]
kolumna_ruchy = [0, 1, 0, -1]

lustra = {}
for _ in range(ilosc):
    w, k, kat = map(int, input().split())
    lustra[(w, k)] = kat

odbicia = {
    45:  {0:1, 1:0, 2:3, 3:2},
    135: {0:3, 3:0, 2:1, 1:2}
}

def droga(mapy, w, k, d):
    odw = set()
    limit = wymiar * wymiar * 4

    for _ in range(limit):
        if not (0 <= w < wymiar and 0 <= k < wymiar):
            return odw, (w, k)

        if (w, k) in mapy:
            odw.add((w, k))
            d = odbicia[mapy[(w, k)]][d]

        w += wiersz_ruchy[d]
        k += kolumna_ruchy[d]

    return odw, (w, k)

# Lustra niewidoczne z wejść
gorne, _ = droga(lustra, 0, 0, 2)
dolne, _ = droga(lustra, wymiar - 1, wymiar - 1, 0)

ukryte = [p for p in lustra if p not in gorne and p not in dolne]

kandydaci = ukryte if len(ukryte) == 1 else list(lustra)

puste = [(w, k) for w in range(wymiar) for k in range(wymiar) if (w, k) not in lustra]

def czy_git(usun, dodaj, kat):
    nowa = dict(lustra)
    if usun not in nowa:
        return False
    del nowa[usun]
    nowa[dodaj] = kat

    _, (wyj_w, wyj_k) = droga(nowa, 0, 0, 2)

    # Uwaga: promień wychodzi ZA planszę,
    # sprawdzamy pole tuż przed wyjściem
    if wyj_w == wymiar and wyj_k == wymiar:
        return True

    return False

for u in kandydaci:
    for d in puste:
        for kat in (45, 135):
            if czy_git(u, d, kat):
                print(u[0], u[1])
                print(d[0], d[1])
                raise SystemExit
