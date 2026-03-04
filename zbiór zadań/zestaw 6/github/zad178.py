

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def zamiana(p):
    head = p
    prev = None
    while p is not None:
        nas = p.next
        p.next = prev # od razu znika stara wartosc next
        prev = p
        p = nas
    return prev