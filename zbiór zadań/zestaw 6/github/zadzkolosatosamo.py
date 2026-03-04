

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rozdzielenie(p):
    parzyste = Node(0)
    dummy_p = parzyste
    nieparzyste = Node(0)
    dummy_n = nieparzyste
    
    while p is not None:
        if p.val > 0 and p.val % 2 == 0:
            parzyste.next = Node(p.val)
            parzyste = parzyste.next
        elif p.val < 0 and p.val % 2 != 0:
            nieparzyste.next = Node(p.val)
            nieparzyste = nieparzyste.next
        p = p.next
    return dummy_p.next, dummy_n.next