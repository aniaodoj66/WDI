

def waga(T, s, n = 0, i = 0, nowa = None):
    if nowa is None:
        nowa = []
    
    if i == len(T):
        return False
    
    if n == s:
        print(nowa)
        return True
    
    if waga(T, s, n + T[i], i + 1, nowa + [T[i]]):
        return True
        
    if waga(T, s, n, i + 1, nowa):
        return True
    
    if waga(T, s, n - T[i], i + 1, nowa + [T[i]]):
        return True