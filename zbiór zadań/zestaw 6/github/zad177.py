


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortowanie(lista1, lista2):
    poczatek = Node(-1) # tworzę fake początek, żeby lista nie była zawieszona w powietrzu
    ogon = poczatek # tworzę ogon do którego będę doczepiać
    while lista1 is not None and lista2 is not None:
        if lista1.val <= lista2.val:
            ogon.next = lista1
            lista1 = lista1.next
        elif lista2.val < lista1.val: # albo else
            ogon.next = lista2
            lista2 = lista2.next
        ogon = ogon.next # ważne bo bez tego funkcja nie ruszy
    
    if lista1 is None:
        ogon.next = lista2
    if lista2 is None:
        ogon.next = lista1
    return poczatek.next