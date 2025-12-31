
# do skończenia


def szukanie(T, i = 0, suma = 0, nowa = None):

    if nowa is None:
        nowa = []

    if i < len(T):
        szukanie(T, i + 1, suma, nowa)
        szukanie(T, i + 1, suma, nowa + [i])

    suma += i
    suma -= T[i]

    if suma == 0:
        return nowa
