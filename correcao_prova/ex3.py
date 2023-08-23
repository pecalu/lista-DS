#3. Fazer um procedumento que jogue numa terceira lista os elementos não numéricos.
lista = list()
lista2 = list()
lista3 = list()
def insere_digitos_lista(l: list, l2: list, l3: list) -> None:
    for i in range(5):
        elem = input("Digite um caractere: ")
        l.append(elem)
        if l[i].isnumeric():
            l2.append(elem)
        elif not l[i].isnumeric():
            l3.append(elem)
    print(l)
    print(l2)
    print(l3)

insere_digitos_lista(lista,lista2,lista3)