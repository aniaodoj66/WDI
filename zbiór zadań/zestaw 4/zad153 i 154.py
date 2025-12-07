# teraz chcemy, żeby waga zwracała odważniki
# ponieważ jest backtracking, trzeba zrobić ify i zreturnować wybrane

def waga(x, T, i = 0, suma = 0, wybrane = None):

    if suma == x:
        return wybrane
    
    if wybrane == None:
        wybrane = []
    
    if i == len(T):
        return False
    
    opcja1 = waga(x, T, i + 1, suma + T[i], wybrane + [T[i]])
    if opcja1:
        return opcja1
    
    opcja2 = waga(x, T, i + 1, suma - T[i], wybrane + [T[i]])
    if opcja2:
        return opcja2
    
    opcja3 = waga(x, T, i + 1, suma, wybrane)
    if opcja3:
        return opcja3
    
    return False