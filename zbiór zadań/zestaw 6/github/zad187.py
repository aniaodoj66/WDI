

class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next 
    
def usuwanie_wiekszych(p):
    if p is None:
        return None
    head = p
    wartosc = p.val
    prev = p
    p = p.next
    while p is not None:
        if p.val < wartosc:
            prev.next = p.next
            p = p.next
        else:
            wartosc = p.val
            prev = p
            p = p.next
    return head