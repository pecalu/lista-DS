lista = []

def conta_float(l: list) -> int:
    tamanho = int(input("Digite o tamanho do vetor que deseja usar: "))
    for i in range(tamanho):
        valor = str(input(f"Digite o valor para v[{i}]: "))
        lista.append(valor)
    qtd = 0
    for elem in l:
        if '.' in elem:
            num = float(elem)
            qtd += 1
    return qtd

resp = conta_strings(lista)
print(f"\nContém {resp} elementos do tipo float no vetor.")