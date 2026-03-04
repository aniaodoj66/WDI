
# Przed zmianami


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


# Po zmianach


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
    while d <= liczba: # zmiana zakresu działania pętli
        if liczba % d == 0:
            lista += [d]
        d += 1
    return lista


def sprawdzanie(p, q) -> bool : # definicja funkcji sprawdzanie()
    koniec = ostatni(p)
    c = p.next
    oczekiwana = p.val * q
    while c is not None:
        if c.val == oczekiwana:
            if c.val == koniec: 
                return True
            oczekiwana = c.val * q
        elif c.val > oczekiwana:
            return False
        c = c.next
    return False


def ciag(p, q) ->int : # dodanie zmiennej dl
    dl = 0
    while p.next is not None:
        if p.next.val / p.val == q: # poprawny zapis dzielenia
            p = p.next
        else:
            n = p.next
            p.next = n.next
            dl += 1
    return dl


def clean(p) ->int :
    lista = dzielniki(pierwszy(p), ostatni(p)) 
    for i in range(len(lista)):
        d = lista[i]
        if sprawdzanie(p, d): # zmiana warunku tak, żeby funkcja zwracała dl
            return ciag(p, d)
    return None