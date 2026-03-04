# super

def czy_gnom(x):
    gnomy1 = 0
    gnomy2 = 0
    while x > 0:
        gnom = x % 3
        if gnom == 1:
            gnomy1 += 1
        elif gnom == 2:
            gnomy2 += 1
        x = x // 3
    if gnomy1 > gnomy2:
        return True
    return False 


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def usuwanie(p):
    prev = Node(0)
    prev.next = p # trzeba podpiąć go !!!
    dummy = prev
    while p is not None:
        if czy_gnom(p.val):
            prev.next = p.next
            p = p.next
        else:
            prev = p
            p = p.next
    return dummy.next