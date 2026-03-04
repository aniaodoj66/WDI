# spoko ale nie ma zadnego warunku na dzielenie przez 0
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def usuwanko(p):
    if p is None:
        return None
    prev = Node(0)
    prev.next = p
    head = prev
    while p.next is not None:
        if p.next.val % p.val == 0: # w ifie i else muszą być różne zmiany, bo jesli usuwamy gowniaka, to nie zmieniamy preva
            prev.next = p.next
            p = p.next
        else:
            prev = p
            p = p.next # NIE ZAPOMNIJ
    return head.next