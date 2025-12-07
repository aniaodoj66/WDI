# dobrze

def zamiana(n):
    liczba = ""
    while n > 0:
        reszta = n % 16
        if reszta <= 9:
            liczba = str(reszta) + liczba
        else:
            liczba = chr(ord("A") + reszta - 10)
        n = n // 16
    return liczba

print(zamiana(45))
print(zamiana(123))
print(zamiana(256))
print(zamiana(16))