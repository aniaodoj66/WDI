

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def usuwanie(p, a):
    if p.val == a:
        return p.next 
    head = p
    prev = p       
    p = p.next
    while p is not None:
        if p.val == a:
            prev.next = p.next
            break
        prev = p
        p = p.next
    return head # trzeba zreturnować całą listę dlatego dajemy head