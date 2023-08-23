#4. Fazer uma função que retorne quantos elementos numericos exitem na lista original.
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
    print(f"Lista inteira: {l}")
    print(f"Somente numerico: {l2}")
    print(f"Somente texto: {l3}")
    qtd = len(l)
    print(f"Quantidade de elementos na primeira lista: {qtd}")
insere_digitos_lista(lista,lista2,lista3)