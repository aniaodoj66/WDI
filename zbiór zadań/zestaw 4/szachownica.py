

def szachy(T, x = 0, y = 0, koszt = 0):

    ruchy = [[1,-1], [1,0], [1,1]]

    if x == 0 and koszt == 0:
        koszt = T[x][y]

    if x == 7:
        return koszt
    
    min_koncowy_koszt = float('inf')

    for i in range(len(ruchy)):
        x_zm = x + ruchy[i][0]
        y_zm = y + ruchy[i][1]
        if 0 <= x_zm <= 7 and 0 <= y_zm <= 7:
            wynik = szachy(T, x_zm, y_zm, koszt + T[x_zm][y_zm])
            if min_koncowy_koszt > wynik:
                min_koncowy_koszt = wynik
    return min_koncowy_koszt
