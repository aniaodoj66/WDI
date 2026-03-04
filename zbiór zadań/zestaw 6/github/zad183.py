

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def zwiekszanieo1(p): # nie ma przenoszenia, więc nie działa
    head = p
    while p.next is not None:
        p = p.next
    p.val += 1
    return head