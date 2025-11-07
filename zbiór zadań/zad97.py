

lista = [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)]

def longest(T):
    dlugosci = [1 for _ in range(len(T))]
    q1 = 1
    q2 = 1
    for i in range(1, len(T)):
        ulamek1 = T[i-1][0] / T[i-1][1]
        ulamek2 = T[i][0] / T[i][1]
        if ulamek1 != 0:
            q2 = ulamek2 / ulamek1
        if q1 == q2:
            dlugosci[i] = dlugosci[i - 1] + 1
        else:
            q1 = q2
            dlugosci[i] += 1
    maksimum = 0

    for i in range(len(dlugosci)):
        if dlugosci[i] > maksimum:
            maksimum = dlugosci[i]
    return maksimum, dlugosci

print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] )) # wypisze 4
print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] )) # wypisze 3
print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] )) # wypisze 6
print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] )) # wypisze 0