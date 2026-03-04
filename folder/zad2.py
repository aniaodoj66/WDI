
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
    liczba = b // a
    lista = []
    d = 2
    while d * d <= liczba:
        if liczba % d == 0:
            lista += [d]
        d += 1
    return lista


def ciag(p, q) ->Node :
    d = Node(1)
    d.next = p 
    while p.next is not None:
        if p.next / p == q:
            prev = p
            p = p.next
        if p.next/p != q:
            prev.next = p.next
            p = prev
    return d.next


def clean(p) ->Node :
    lista = dzielniki(pierwszy(p), ostatni(p)) 
    for i in range(len(lista)):
        d = lista[i]
        if ciag(p, d) is not None:
            return sprawdzanie(p, d)
            break
    return None