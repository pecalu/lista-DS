lista = []

def conta_boolean(lista: list) -> int:
    tamanho = int(input("Digite o tamanho do vetor que deseja usar: "))
    for i in range(tamanho):
        valor = input(f"Digite o valor para v[{i}]: ")
        lista.append(valor)
    qtd = 0
    for elem in lista:
        if elem == 'True' or elem == 'False':
            qtd += 1
    return qtd

resp = conta_boolean(lista)
print(f"\nContém {resp} elementos logicos contidos no vetor.")