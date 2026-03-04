

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def wypisz(p):
    while p != None:
        print(p.val)
        p = p.next