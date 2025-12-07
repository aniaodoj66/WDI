# źle bo nie rozumiem fizyki

"""
Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory.
"""

def rezystory(x, T, i = 0, wybrane = 0):

    if wybrane == x:
        return True
    
    if i == len(T):
        return False
    
    opcja1 = rezystory(x, T, i + 1, wybrane + T[i])
    if opcja1:
        return True
    
    opcja2 = rezystory(x, T, i + 1, wybrane - T[i])
    if opcja2:
        return True
    
    opcja3 = rezystory(x, T, i + 1, wybrane)
    if opcja3:
        return True
    
    return False