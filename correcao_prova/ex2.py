#2. Fazer um procedimento que jogue numa segunda lista os elementos numericos
# convertidos para numero.
# Obs: Neste caso fazer o casting
lista = list()
lista2 = list()
def insere_digitos_lista(l: list, l2: list) -> None:
    for i in range(5):
        elem = input("Digite um caractere: ")
        l.append(elem)
        if l[i].isnumeric():
            l2.append(elem)
    print(l)
    print(l2)

insere_digitos_lista(lista,lista2)