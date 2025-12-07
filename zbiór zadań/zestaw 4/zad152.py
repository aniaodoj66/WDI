# backtracking

# warunek 1 przebiegu i stworzenia zmiennej
# warunek na prawdę
# warunek na koniec

# backtracking więc każde następne wywołanie musi mieć if i prawdę
# fałsz na końcu

def waga(x, T, i = 0, wybrane = None):

    if wybrane == None:
        wybrane = []

    if sum(wybrane) == x:
        return True
    
    if i == len(T):
        return False
    
    if waga(x, T, i + 1, wybrane + [T[i]]):
        return True
    
    if waga(x, T, i + 1, wybrane + [T[i]]* (-1)):
        return True
    
    if waga(x, T, i + 1, wybrane):
        return True
    
    return False