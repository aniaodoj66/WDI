

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def buduj(lista):
    if not lista:
        return None
    head = Node(lista[0])
    curr = head
    for i in range(1, len(lista)):
        curr.next = Node(lista[i])
        curr = curr.next
    return head

def fix(p):
    vals = []
    while p != None:
        vals.append(p.val)
        p = p.next
    vals = sorted(vals)
    lista1 = []
    lista2 = []
    lista1.append(vals[0])
    lista2.append(vals[1])
    r1 = vals[2] - vals[0]
    for i in range(2,len(vals)):
        if vals[i] - lista1[-1] == r1:
            lista1.append(vals[i])
        else:
            lista2.append(vals[i])
    return buduj(lista1), buduj(lista2)