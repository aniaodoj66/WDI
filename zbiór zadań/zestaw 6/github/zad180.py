

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def wstawianie(p, v):
    head = p
    vv = Node(v)
    while p is not None:
        if p.next is None:
            p.next = vv
            return head
        p = p.next
    