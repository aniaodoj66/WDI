

def sprawdzanie(p, q) -> bool :
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