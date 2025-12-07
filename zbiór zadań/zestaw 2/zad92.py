# dobrze chyba, jeśli tak można przedstawić daty

def przestepny(rok):
    if rok % 400 == 0:
        return True
    if rok % 100 == 0:
        return False
    if rok % 4 == 0:
        return True
    return False

def daty(a):
    ilosc = 0
    dni_tygodnia = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
    miesiace = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d2, m2, r2 = a.split(".")
    d1 = 1
    m1 = 1
    r1 = 1900
    d2 = int(d2)
    m2 = int(m2)
    r2 = int(r2)
    for r in range(r1+1, r2): # indeks końcowy musi być większy o 1, tak naprawdę pętla idzie do r2 - 1
        ilosc += 365
        if przestepny(r):
            ilosc += 1
    for m in range(m1, 12): # nie dodaję, bo chodzi o indeksy listy
        ilosc += miesiace[m]
    for m in range(0, m2-1): # musi być o jeden mniejszy, bo liczę pełne miesiące
        ilosc += miesiace[m]
    ilosc += (miesiace[m1-1] - d1)
    ilosc += d2
    if m1 <= 2 and przestepny(r1):
        ilosc += 1
    if m2 >= 3 and przestepny(r2):
        ilosc += 1
    return dni_tygodnia[ilosc % 7]

print(daty("03.11.2025"))
    