# dlaczego to nie działa???

T = [2,3,4,5,7,6,23,24,12,13,14,15,16,45]

def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True

def w(a, b):
    ta = []
    tb = []
    for i in range(1, a):
        if i != 1 and a % i == 0 and is_prime(i):
            ta += [i]
    for i in range(2, b):
        if b % i == 0 and is_prime(i):
            tb += [i]
    if ta == tb and len(ta) > 0:
        return True
    return False


def zgodne(t):
    liczba = 0
    for j in range(len(t)):
        for s in [j - 2, j - 1, j + 1, j + 2]:
            if 0 <= s <= len(t) - 1 and w(t[s], t[j]):
                liczba += 1
                break
                
    return(liczba)

print(zgodne(T))
