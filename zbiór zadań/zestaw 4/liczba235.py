

def liczba235(N, n = 1, T = None):

    if n > N:
        return
    
    if T is None:
        T = [2, 3, 5]

    for i in range(len(T)):

        if liczba235(N, n * 2, T):
            return
        
        if liczba235(N, n * 3, T):
            return
        
        if liczba235(N, n * 5, T):
            return
        
    if n <= N:
        print(n)
    
    return