



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def usuwanie(p):
    head = p
    while p is not None:
        if p.next.next is None:
            p.next = None
            return head
        p = p.next
    