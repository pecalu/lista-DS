lista1 = []
lista2 = []

def copia_int(l1: list, l2: list) -> None:
    tamanho = int(input("Digite o tamanho do vetor que deseja usar: "))
    for i in range(tamanho):
        valor = str(input(f"Digite o valor para v[{i}]: "))
        l1.append(valor)
    for elem in l1:
        if elem.isdigit():
            qtd = 0
            qtd += 1
            lista2.append(elem)
    print(f"Lista 1: {l1}")
    print(f"Lista 2 com os inteiros da lista 1: {l2}")

print(copia_int(lista1, lista2))