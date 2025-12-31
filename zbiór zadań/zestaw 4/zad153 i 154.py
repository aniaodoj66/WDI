# teraz chcemy, żeby waga zwracała odważniki
# ponieważ jest backtracking, trzeba zrobić ify i zreturnować wybrane

def waga(x, T, i = 0, suma = 0, wybrane = None, wybrane2 = None):

    if suma == x:
        return wybrane, wybrane2
    
    if wybrane is None:
        wybrane = []

    if wybrane2 is None:
        wybrane2 = []

    if i == len(T):
        return False
    
    opcja1 = waga(x, T, i + 1, suma + T[i], wybrane + [T[i]], wybrane2)
    if opcja1:
        return opcja1
    
    opcja2 = waga(x, T, i + 1, suma - T[i], wybrane, wybrane2 + [T[i]])
    if opcja2:
        return opcja2
    
    opcja3 = waga(x, T, i + 1, suma, wybrane, wybrane2)
    if opcja3:
        return opcja3
    
    return False

N = [1, 2, 5, 10, 15, 25]
n = 37

print(waga(n, N))