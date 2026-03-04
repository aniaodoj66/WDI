

class Node:
    def __init__(self, val, next, index):
        self.val = val
        self.next = next
        self.index = index

def wartosc_pod_indeksem(p, n): # n to indeks
    while p != None:
        if p.index == n:
            return p.val
        p = p.next
    return 0

def podstaw_wartosc(p, n, v):
    head = p
    while p != None:
        if p.index == n:
            p.val = v
    nowy = Node(v, head, n) # w przypadku gdy nie ma indeksu, 
    return head # funkcja dodaje nowy wyraz na początek
            # i przypisuje mu indeks n 

# troche nie wiem o comu do konca chodzi
def inicjalizacja():
    return None

def podstaw(p, n, v):
    head = p