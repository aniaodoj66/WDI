

"""ja sb taki przyklad zrobilem

T[ 0] = "A24130241302"
T[ 1] = "1C0241302413"
T[ 2] = "24C302413024"
T[ 3] = "302C13024130"
T[ 4] = "4130A4130241"
T[ 5] = "02413I241302"
T[ 6] = "130241B02413"
T[ 7] = "2413024A3024"
T[ 8] = "30241302C130"
T[ 9] = "413024130C41"
T[10] = "0241302413C2"
T[11] = "13024130241A"

ACCCA jest dwa razy na jednej przekatnej ale 
nie sa czescia tego samego palindromu

tab = [
    ['Q','W','E','R','A','D','A','R','T','B'],
    ['Z','X','C','V','B','N','M','Q','W','E'],
    ['A','S','R','T','Y','U','I','S','I','G'],
    ['P','A','S','R','Y','F','A','R','U','A'],
    ['O','S','D','F','A','U','D','F','H','D'],
    ['L','K','J','H','G','R','I','O','P','L'],
    ['M','N','B','V','C','X','A','G','H','F'],
    ['Q','W','E','R','T','Y','U','D','P','L'],
    ['A','S','D','F','G','H','J','K','A','L'],
    ['Z','X','C','V','B','N','M','Q','W','R']
]

"""

palindromy = []
f1 = [1,2,3,4]
f2 = [5,6,7,8]
palindromy += [f1]
palindromy += [f2]
print(palindromy)



def powtarzajacy(pal):
    elementy = set()
    for p in pal:
        if p in elementy:
            return p
        else:
            elementy.add(p)        
    return None