# git


class Node:
    def __init__(self, val, next=0):
        self.val = val
        self.next = next

def parzystepiatki8(x):
    licznik = 0
    while x > 0:
        if x % 8 == 5:
            licznik += 1
        x = x // 8
    if licznik % 2 == 0:
        return True
    return False

def funkcja(p):
    piatki = Node(0)
    dummy_p = piatki
    bezpiatek = Node(0)
    dummy_bez = bezpiatek
    while p is not None:
        if parzystepiatki8(p.val):
            piatki.next = p
            piatki = piatki.next
        else:
            bezpiatek.next = p
            bezpiatek = bezpiatek.next
        p = p.next
    bezpiatek.next = None
    dummy_bez = dummy_bez.next
    piatki.next = dummy_bez
    return dummy_p.next
    