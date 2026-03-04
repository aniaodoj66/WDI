# caly czas sa bledy

class Node:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next

# zle 

def reverse(p):
    prev = None # nie może być Node(0), bo zostanie to 0 i lista nie będzie zgodna
    head = p
    while p is not None:
        nas = p.next
        p.next = prev
        prev = p
        p = nas
    return prev # WAŻNE BO ZMIENIA SIĘ KOLEJNOŚĆ

def dodawanie(p1, p2): # już po zrobieniu reverse
    p1 = reverse(p1)
    p2 = reverse(p2)
    p = Node(0) # musi być, bo inaczej nie da się przyczepić
    dziesiatki = 0
    while p1 is not None or p2 is not None:
        if p1 is None:
            wartosc = p2.val
        elif p2 is None:
            wartosc = p1.val
        else:
            wartosc = p1.val + p2.val
        p.val = (wartosc + dziesiatki) % 10
        dziesiatki = wartosc // 10
        if p1 is not None: # nie wiem czemu trochę
            p1 = p1.next
        if p2 is not None:
            p2 = p2.next
    return reverse(p)
