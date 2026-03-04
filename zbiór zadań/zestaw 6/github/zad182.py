

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def dziesiatkowanie(p):
    head = p
    while p is not None and p.next is not None:
        p.next = p.next.next
        p = p.next
    return head