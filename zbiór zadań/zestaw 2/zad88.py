# wedlug mnie to jest dobrze, ale z przykladow wynika, że chyba zamiast robić nwd(a,b,c) = 1
# trzeba było nwd(a,b) ==1 and nwd(b,c) == 1 and nwd(a,c) == 1

# t t t  1. scenariusz
# t x t t  2. scenariusz
# t t x t  3. scenariusz
# t x t x t  4. scenariusz

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nwd3(a,b,c):
    return nwd(nwd(a,b), c)

def trojki(T):
    ilosc = 0
    for i in range(len(T) - 2): # 1.
        if nwd3(T[i], T[i + 1], T[i + 2]) == 1:
            ilosc += 1
    for i in range(len(T) - 3): # 2. i 3.
        if nwd3(T[i], T[i + 2], T[i + 3]) == 1:
            ilosc += 1
        if nwd3(T[i], T[i + 1], T[i + 3]) == 1:
            ilosc += 1
    for i in range(len(T) - 4):
        if nwd3(T[i], T[i + 2], T[i + 4]) == 1:
            ilosc += 1
    return ilosc

print(trojki([2,4,6,7,8,10,12])) # 0 trójek
print(trojki([2,3,4,6,7,8,10])) # 1 trójka (3,4,7)
print(trojki([2,4,3,6,5])) # 2 trójki (2,3,5),(4,3,5)
print(trojki([2,3,4,5,6,8,7])) # 5 trójek (2,3,5),(3,4,5),(3,5,8),(5,6,7),(5,8,7)