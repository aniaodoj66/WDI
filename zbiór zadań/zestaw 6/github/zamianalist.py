

class Node:
    def __init__(self, val, next, index):
        self.val = val
        self.next = next
        self.index = index

def zamiana(zwykla):
    p = Node(0, None, -1)
    head = p
    for i in range(len(zwykla)):
        if zwykla[i] != 0:
            a = Node(zwykla[i], None, i)
            p.next = a
            p = p.next
    return head.next