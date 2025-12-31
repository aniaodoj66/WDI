

def hanoi(n, zrodlo, pomocniczy, cel):
    # WARUNEK STOPU (Baza rekurencji)
    # Jeśli mamy przenieść tylko 1 krążek, po prostu go przenosimy.
    if n == 1:
        print(f"Przenieś krążek 1 z {zrodlo} na {cel}")
        return

    # KROK 1: Przenieś n-1 krążków ze Źródła na Pomocniczy
    # (Zauważ: w tym kroku 'cel' służy nam jako słupek tymczasowy)
    hanoi(n - 1, zrodlo, cel, pomocniczy)

    # KROK 2: Przenieś największy krążek (n) ze Źródła na Cel
    print(f"Przenieś krążek {n} z {zrodlo} na {cel}")

    # KROK 3: Przenieś n-1 krążków z Pomocniczego na Cel
    # (Zauważ: teraz 'zrodlo' służy jako słupek tymczasowy)
    hanoi(n - 1, pomocniczy, zrodlo, cel)

# --- Uruchomienie ---
# n = 3 krążki, A=Start, B=Pomoc, C=Cel
hanoi(3, "A", "B", "C")