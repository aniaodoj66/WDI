# jakoś niby jest
# oba działają

def podzial(x, k = 1, lista = None):
    if lista is None:
        lista = []
    if x == 0:
        print(lista)
        return
    if x >= k:
        podzial(x - k, k, lista + [k]) # biorę k 
        podzial(x, k + 1, lista) # nie biorę k



def podzial2(x, k = 1, lista = None):
    if lista is None:
        lista = []
    if sum(lista) == x:
        print(lista)
        return
    if x >= k:
        podzial2(x - k, k, lista + [k]) # biorę k 
        podzial2(x, k + 1, lista) # nie biorę k
        
