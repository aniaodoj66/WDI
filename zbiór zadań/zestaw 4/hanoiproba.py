# niech bedzie

def hanoi(n, A, B, C):

    if n == 1:
        print(f"Przenieś krążek 1 z {A} na {C}")
        return
    
    hanoi(n - 1, A, C, B)
    print(f"Przenieś krążek {n} z {A} na {C}")
    hanoi(n - 1, B, A, C)

hanoi(5, "pierwszy", "pomoc", "docelowy")