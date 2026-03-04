

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def liczenie(p):
    counter = 0
    while p != None:
        counter += 1
        p = p.next
    return counter