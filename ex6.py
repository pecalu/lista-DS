lista = []

def conta_strings(l: list) -> int:
    tamanho = int(input("Digite o tamanho do vetor que deseja usar: "))
    for i in range(tamanho):
        valor = str(input(f"Digite o valor para v[{i}]: "))
        lista.append(valor)
    qtd = tamanho
    for elem in l:
        if elem.isdigit():
            qtd -= 1
        elif elem in ["False", "True"]:
            qtd -= 1
        elif '.' in elem:
            num = float(elem)
            qtd -= 1
    return qtd

resp = conta_strings(lista)
print(f"\nContém {resp} Stings contidas no vetor preenchido.")