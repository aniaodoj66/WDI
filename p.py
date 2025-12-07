



import sys

def powtarzajacy(pal):
    elementy = set()
    ppp = []
    for p in pal:
        p1 = tuple(p)
        if p1 in elementy:
            ppp += [p]
        else:
            elementy.add(p1)    
    max_dl = 0
    max_p = ""
    for i in range(len(ppp)):
        if len(ppp[i]) > max_dl:
            max_dl = len(ppp[i]) 
            max_p = ppp[i] 
    if max_p is not None and isinstance(max_p, list):
        return "".join(max_p)
    return max_p

def palindrom(lista):
    while len(lista) > 0:
        if lista[0] != lista[-1]:
            return False
        lista = lista[1: -1]
    return True

def szukanie(tablica):
    N = len(tablica)
    palindromy = []
    for linia in range(N):
        for dl in range(5, N + 1):
            for j in range(N + 1 - dl):
                fragment = tablica[linia][j:j+dl]
                if palindrom(fragment):
                    palindromy += [fragment]
    
    for kolumna in range(N):
        for dl in range(5, N + 1):
            for i in range(N + 1 - dl):
                fragment = [w[kolumna] for w in tablica[i:i+dl]]
                if palindrom(fragment):
                    palindromy += [fragment]

    for i in range(N):
        if i == 0:
            linia = []
            for dod in range(N):
                linia += tablica[dod][dod]
            for dl in range(5, len(linia) + 1):
                for j in range(len(linia) + 1 - dl):
                    fragment = linia[j:j+dl]
                    if palindrom(fragment):
                        palindromy += [fragment]

        else:
            linia1 = []
            linia2 = []
            for dod in range(N - i):
                linia1 += tablica[dod][dod + i]
                linia2 += tablica[dod + i][dod]
            for dl in range(5, len(linia1) + 1):
                for j in range(len(linia1) + 1 - dl):
                    fragment1 = linia1[j:j+dl]
                    fragment2 = linia2[j:j+dl]
                    if palindrom(fragment1):
                        palindromy += [fragment1]
                    if palindrom(fragment2):
                        palindromy += [fragment2]

    return(powtarzajacy(palindromy))

def main():
    pierwsza_linia = sys.stdin.readline().strip()
    if not pierwsza_linia:
        return None 
    N = int(pierwsza_linia)    
    tablica = []
    for i in range(N):
        linia = sys.stdin.readline().strip()
        if not linia:
            break 
        tablica.append(list(linia))
    return szukanie(tablica)


if __name__ == "__main__":
    wynik = main()
    if wynik is not None:
        if isinstance(wynik, list):
            print("".join(wynik))
        else:
            print(wynik)