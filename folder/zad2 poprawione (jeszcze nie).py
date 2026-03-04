
class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def pierwszy(p) ->int :
    return p.val


def ostatni(p) ->int :
    while p.next is not None:
        p = p.next
    return p.val


def dzielniki(a,b) -> list:
    liczba = b / a
    lista = []
    d = 2
    while d * d <= liczba:
        if liczba % d == 0:
            lista += [d]
        d += 1
    return lista


def ciag(p, q) ->Node : #usuwa
    d = Node(1)
    d.next = p 
    while p.next is not None:
        if p.next.val / p.val == q: # 1.
            prev = p
            p = p.next
        if p.next.val / p.val != q:
            prev.next = p.next
            p = prev
    return d.next


def sprawdzanie(p, q) ->int: #tylko patrzy
    l = 0
    c_val = p.val
    while p.next is not None: # 2.
        if p.next.val == c_val * q:
            p = p.next
            c_val = p.val
        else:
            d = p.next
            p.next = d.next 
            l += 1   
    return l


def clean(p) ->Node :
    lista = dzielniki(pierwszy(p), ostatni(p)) 
    for i in range(len(lista)):
        d = lista[i]
        if ciag(p, d) is not None:
            return sprawdzanie(p, d)
            break
    return None