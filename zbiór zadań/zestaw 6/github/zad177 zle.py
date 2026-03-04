
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def bubble_sort(p):
    while p != None:
        a = p
        p = p.next
        if a.val > p.val:
            a.val, p.val = p.val, a.val
        a = p
        p = p.next

def scal(a,b):
    while a != None:
        if a.val == 5:
            reszta_A = a.next
            a.next = b

            while b.next != None:
                b = b.next
            b.next = reszta_A
    a = a.next