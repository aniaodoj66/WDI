

# prawie dobrze

def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2 or x == 3:
        return True
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
    
def funkcja(t1, t2):
    for i in range(2, len(t1) - 1):
        for j in range(len(t1) + 1 - i):
            s = 0
            for k in range(len(t2) + 1 - i):
                s = sum(t1[j:j+i+1]) + sum(t2[k:k+i+1])
                d = 2
                while d < s:
                    if is_prime(d) and s % d == 0:
                        s = s // d
                        if is_prime(s):
                            return True
                    d += 1
    return False