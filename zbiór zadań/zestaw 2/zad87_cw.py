# rozumiem, to samo, ale gorsze jest w 2020 którymś

def check_multi(n):
    for i in range(1, int(len(n) / 2) + 1):
        cut = n[:i] # wycinam fragment do i
        if len(n) % i == 0 and cut * (len(n) // i) == n:
            return True
    return False

def multi(T):
    best = 0
    for x in T:
        if check_multi(x):
            if len(x) > best:
                best = len(x)
    return best