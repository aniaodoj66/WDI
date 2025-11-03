

napis = "ABAABA"
print(napis[0:3])
print(napis[3:6])


def suma_w(x):
    # Funkcja liczy sumę elementów wiersza
    s = 0
    for element in x:
        s += element
    return s

def suma_k(T, kolumna):
    # Funkcja liczy sumę elementów w danej kolumnie
    s = 0
    for wiersz in T:
        s += wiersz[kolumna]
    return s

def chess(T):
    N = len(T)
    max_suma = float('-inf')  # Użycie najmniejszej możliwej liczby, by działało z ujemnymi
    najlepsze_polozenie = None

    # Iteracja po wszystkich możliwych położeniach pierwszej wieży (w1, k1)
    for w1 in range(N):
        for k1 in range(N):
            # Iteracja po wszystkich możliwych położeniach drugiej wieży (w2, k2)
            for w2 in range(N):
                for k2 in range(N):
                    
                    # 1. Musimy upewnić się, że wieże stoją na różnych polach
                    if w1 == w2 and k1 == k2:
                        continue
                    
                    # --- Obliczanie sumy pól szachowanych ---
                    
                    # A. Suma pól szachowanych przez PIERWSZĄ wieżę (W1)
                    # Suma Wiersza w1 i Kolumny k1
                    suma_W1 = suma_w(T[w1]) + suma_k(T, k1)
                    # Odejmowanie pola zajmowanego przez W1 (T[w1][k1]), ponieważ to pole 
                    # zostało zliczone dwa razy (raz w wierszu, raz w kolumnie) i uwaga 
                    # nakazuje, że nie jest ono szachowane.
                    suma_W1 -= T[w1][k1]
                    
                    # B. Suma pól szachowanych przez DRUGĄ wieżę (W2)
                    # Suma Wiersza w2 i Kolumny k2
                    suma_W2 = suma_w(T[w2]) + suma_k(T, k2)
                    # Odejmowanie pola zajmowanego przez W2 (T[w2][k2])
                    suma_W2 -= T[w2][k2]
                    
                    # C. Pełna suma pól szachowanych przez obie wieże (A + B)
                    # W tym momencie pola szachowane przez OBIE wieże są zliczone dwukrotnie.
                    suma_calkowita = suma_W1 + suma_W2
                    
                    # D. Poprawka (odjęcie pól podwójnie zliczonych)
                    
                    # Pola "szachowane" przez obie wieże, które zostały zliczone dwukrotnie, to:
                    
                    # 1. Pole (w1, k2): jest w szachu W1 (kolumna k1, wiersz w1) i W2 (kolumna k2, wiersz w2) - BŁĄD!
                    #    Pole (w1, k2) jest szachowane przez W1 (wiersz w1) oraz przez W2 (kolumna k2).
                    # 2. Pole (w2, k1): jest szachowane przez W1 (kolumna k1) oraz przez W2 (wiersz w2).
                    
                    # 3. Dodatkowo, jeśli wieże nie stoją na tym samym wierszu (w1 != w2) 
                    #    i nie stoją na tej samej kolumnie (k1 != k2):
                    #    - Cały wiersz w1 został zliczony w suma_W1, wiersz w2 w suma_W2.
                    #    - Cała kolumna k1 została zliczona w suma_W1, kolumna k2 w suma_W2.

                    # Suma wszystkich pól szachowanych (bez duplikatów i pól wież)
                    
                    # Uproszczona wersja: Suma Wierszy i Kolumn
                    suma = suma_w(T[w1]) + suma_k(T, k1) + suma_w(T[w2]) + suma_k(T, k2)

                    # Poprawka:
                    # 1. Odejmowanie wartości z pól wież (nie są szachowane) - każde pole zliczone dwa razy
                    suma -= 2 * T[w1][k1] 
                    suma -= 2 * T[w2][k2]
                    
                    # 2. Odejmowanie wartości z pól szachowanych PRZEZ OBIE wieże (zliczone dwukrotnie)
                    #   - Pole (w1, k2): leży w wierszu w1 (szach W1) i kolumnie k2 (szach W2)
                    suma -= T[w1][k2]
                    #   - Pole (w2, k1): leży w wierszu w2 (szach W2) i kolumnie k1 (szach W1)
                    suma -= T[w2][k1]
                    
                    # Sprawdzenie, czy wieże szachują się nawzajem.
                    # Jeśli w1 == w2 LUB k1 == k2, to:
                    if w1 == w2: # Obie wieże w tym samym wierszu
                        # Odejmij dodatkowo wartość wiersza w1 (lub w2), 
                        # ponieważ został on zliczony dwukrotnie w "suma_w(T[w1]) + suma_w(T[w2])"
                        # UWAGA: to nie jest tak proste, bo te wiersze już są w sumie A+B.
                        # Łatwiej: Obliczamy sumę unikatowych pól:
                        
                        # Nowe podejście: Zbiory pól, by uniknąć duplikatów.
                        # Tworzymy zbiór współrzędnych szachowanych pól:
                        szachowane = set()
                        
                        # Pola szachowane przez W1 (wiersz w1 i kolumna k1)
                        for k in range(N):
                            if k != k1: # Wiersz, bez pola wieży W1
                                szachowane.add((w1, k))
                        for w in range(N):
                            if w != w1: # Kolumna, bez pola wieży W1
                                szachowane.add((w, k1))
                                
                        # Pola szachowane przez W2 (wiersz w2 i kolumna k2)
                        for k in range(N):
                            if k != k2 and (w2, k) != (w1, k1): # Wiersz, bez pola wieży W2 i pola wieży W1
                                szachowane.add((w2, k))
                        for w in range(N):
                            if w != w2 and (w, k2) != (w1, k1): # Kolumna, bez pola wieży W2 i pola wieży W1
                                szachowane.add((w, k2))
                                
                        # Usuń, jeśli pole wieży W2 przypadkiem trafiło do zbioru (gdy W1 szachuje W2)
                        if (w2, k2) in szachowane:
                            szachowane.remove((w2, k2))
                        # Usuń, jeśli pole wieży W1 przypadkiem trafiło do zbioru (gdy W2 szachuje W1)
                        if (w1, k1) in szachowane:
                            szachowane.remove((w1, k1))

                        # Obliczenie sumy na podstawie unikatowych pól
                        suma = 0
                        for w, k in szachowane:
                            suma += T[w][k]

                    
                    if suma > max_suma:
                        max_suma = suma
                        najlepsze_polozenie = (w1, k1, w2, k2)
                        
    # Funkcja powinna zwrócić krotkę (row1, col1, row2, col2)
    # Dodaję dla sprawdzenia maksymalną sumę, chociaż to nie jest wymagane w treści
    if najlepsze_polozenie:
        return najlepsze_polozenie, max_suma # Oryginalnie: return (max_suma, najlepsze_polozenie)
    else:
        # Zdarzy się tylko dla pustej tablicy
        return None

# --- Przykładowe wywołania funkcji ---

T1 = [[4,0,2],[3,0,0],[6,5,3]]
T2 = [[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]]

print(f"Przykład 1: Tablica {T1}")
# print(chess(T1)) # Spodziewany wynik (0,1,1,0) suma=17
print(f"Wynik: {chess(T1)}") 

print(f"\nPrzykład 2: Tablica {T2}")
# print(chess(T2)) # Spodziewany wynik (2,3,3,1) suma=35
print(f"Wynik: {chess(T2)}")