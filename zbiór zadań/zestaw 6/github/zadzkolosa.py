

#lista stworzyc 2 1 dodatnie parzyste 2 ujemne nieparzyste reszta kosz

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rozdzielenie(p):
    parzyste = Node(0)
    dummy_p = parzyste
    nieparzyste = Node(0)
    dummy_n = nieparzyste
    head = p
    prev = p
    while p is not None:
        if p.val > 0 and p.val % 2 == 0:
            parzyste.next = p
            parzyste = parzyste.next
            prev = p
            p = p.next
        elif p.val < 0 and p.val % 2 != 0:
            nieparzyste.next = p
            nieparzyste = nieparzyste.next
            prev = p
            p = p.next
        else:
            prev.next = p.next
            prev = p
            p = p.next
        
    return dummy_p.next, dummy_n.next

        