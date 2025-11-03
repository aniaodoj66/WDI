

napis = "ANIAania"
cut = napis[:3]
print(cut)

import math

x = 35
y = int(math.sqrt(x))
print(y)

def nwd(a, b):
    print(a,b)
    while b != 0:
        a, b = b, a % b
        print(a,b)
    return a

print(nwd(60,48))

print(ord("A"))