

napis = "123321"
cut = napis[:3]
print(napis[3:0:-1])
print(napis[3:6])
print(len(napis))


import math
x = 35
y = int(math.sqrt(x))


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

fragment = "ania"
fragment = fragment[1:-1]
print(fragment)