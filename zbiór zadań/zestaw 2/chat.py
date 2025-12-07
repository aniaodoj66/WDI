

def zad(t):
    n = len(t)
    if n == 0:
        return 0
    max_len = 0
    for i in range(n):  # Start podciągu
        current_sum = 0  # Suma elementów
        index_sum = 0    # Suma indeksów
        for j in range(i, n):  # Rozszerzaj podciąg
            current_sum += t[j]
            index_sum += j
            # Sprawdź, czy nadal rosnące (dla j > i)
            if j > i and t[j] <= t[j-1]:
                break  # Przestań rozszerzać, jeśli nie rosnące
            # Sprawdź warunek
            if current_sum == index_sum:
                max_len = max(max_len, j - i + 1)
    return max_len