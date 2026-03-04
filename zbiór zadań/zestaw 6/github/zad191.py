

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 

def nieparzyste1(x):
    licznik = 0
    while x > 0:
        if x % 2 == 1:
            licznik += 1
        x = x // 2
    if licznik % 2 != 0:
        return True
    return False

def funkcja(p):
    head = p
    prev = Node(0)
    prev.next = p
    while p is not None:
        if nieparzyste1(p.val):
            prev.next = p.next
            p = p.next

        else:
            prev = p
            p = p.next
    return head