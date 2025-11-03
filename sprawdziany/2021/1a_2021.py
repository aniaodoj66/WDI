# juz nic nie rozumiem

import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    d = math.isqrt(x)
    for i in range(2, d + 1):
        if x % i == 0:
            return False
    return True

def liczba_cyfr(x):
    d = 0
    while x > 0:
        d += 1
        x //= 10
    return d

N = 202742516

def naj(x):
    a = x
    max_prime_a = 0
    liczba = liczba_cyfr(a)
    for m in range(liczba - 1):
        a = x
        a = a % (10 * (liczba - m - 1))
        for n in range(liczba - m - 1):
            if n > 0:
                a = a // (10 * n)
                if is_prime(a) and a > max_prime_a:
                    max_prime_a = a
    return(max_prime_a)

print(naj(N))