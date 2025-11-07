# dziala 

lista = input("Wpisz co najmniej 11 liczb oddzielonych spacjami: ").split()
lista = [int(i) for i in lista]


for i in range(len(lista)):
    for j in range(i - 1, -1, -1):
        if lista[j + 1] > lista[j]:
            lista[j + 1], lista[j] = lista[j], lista[j + 1]
print(lista)
print(lista[9])