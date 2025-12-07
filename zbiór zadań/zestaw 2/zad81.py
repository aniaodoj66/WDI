# działa

lista = [1,2,5,6,5,3,5,7,9,7,5,3]

def funkcja(T):
    max_dl = 0
    for i in range(len(T)):
        for j in range(i, len(T)):
            fragment = T[i:j+1]
            flaga = 0
            while len(fragment) >= 1:
                flaga = 2
                if fragment[0] % 2 != 1 or fragment[-1] % 2 != 1 or fragment[0] != fragment[-1]:
                    flaga = 1
                    break
                else:
                    fragment = fragment[1:-1]
            if flaga == 2 and len(T[i:j + 1]) > max_dl:
                max_dl = len(T[i:j + 1])
    return max_dl

print(funkcja(lista))