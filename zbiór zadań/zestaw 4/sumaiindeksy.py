# dobrze

def suma(T, i = 0, st = 0, si = 0):

    if st == si and i != 0:
        return True
    
    if i == len(T):
        return False
    
    if suma(T, i + 1, st + T[i], si + i):
        return True
    
    if suma(T, i + 1, st, si):
        return True