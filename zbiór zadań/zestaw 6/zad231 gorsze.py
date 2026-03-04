

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def buduj(lista):
    if not lista:
        return None, None
    head = Node(lista[0])
    curr = head
    for i in range(1, len(lista)):
        curr.next = Node(lista[i])
        curr = curr.next
    return head, curr

def fix(p):
    vals = []
    while p != None:
        vals.append(p.val)
        p = p.next
    vals = sorted(vals)
    return buduj(vals)
            