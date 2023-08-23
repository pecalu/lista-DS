def listaEX():
    print("\n1 - Preencher uma lista.\n"
    "2 - Exibir a lista passada por parametro\n"
    "3 - Função com a mesma utilidade do len().\n"
    "4 - Função com a mesma utilidade da index() com a melhoria de quando nao achar retorna -1.\n"
    "5 - Função com a mesma utilidade do count().\n"
    "6 - Conta quantos elementos inteiros tem em uma lista.\n"
    "7 - Conta quantos elementos strings existem na lista\n"
    "8. Contar elementos booleanos.\n"
    "9. Contar elementos Floats.\n"
    "10. Copia elementos inteiros da lista1 para a lista2.\n"
    )
    while True:
        opcao = input("Digite qual exercício deseja executar: ")
        if not opcao.isdigit():
            print("\nPor favor, digite um exercício válido!")
            continue
        opcao = int(opcao)
        if opcao < 0 or opcao > 10:
            print("\nPor favor, digite um exercício válido entre 0 e 10!")
            continue
        break
    v = []
    tamanho = input("Digite o tamanho do vetor que deseja usar: ")
    while not tamanho.isdigit():
        print("\nDigite um numero inteiro!!")
        tamanho = input("Digite o tamanho do vetor que deseja usar: ")
    if tamanho.isdigit():
        tamanho = int(tamanho)
    for i in range(tamanho):
        valor = str(input(f"Digite o valor para v[{i}]: "))
        v.append(valor)
    match opcao:
        case 1:
            def preenche_lista(v: list) -> None:
                print(f"Vetor preenchido: v {v}")
            preenche_lista(v)
        case 2:
            def exibe_lista(v: list) -> None:
                print("\nVetor preenchido abaixo:\n")
                for i in range(len(v)):
                    print(f"v[{i}] = {v[i]}")
            exibe_lista(v)
        case 3:
            def conta_elementos(v: list) -> int:
                contador = 0
                while v:
                    v.pop()
                    contador += 1
                return contador
            resp = conta_elementos(v)
            print(f"\n{resp} elementos contidos no vetor.")
        case 4:
            def retorna_indice(vetor: list) -> int:
                elemento = input("\nDigite qual valor deseja buscar no vetor: ")
                for i in range(len(vetor)):
                    if vetor[i] == elemento:
                        return i
                return -1
            resp = retorna_indice(v)
            print(f"Indice do elemento digitado: [{resp}]")
        case 5:
            def busca(v: list) -> int:
                elemento = input("\nDigite qual deseja saber a quantidade dentro do vetor: ")
                qtd = 0
                for i in range(len(v)):
                    if v[i] == elemento:
                        qtd += 1
                return qtd
            resp = busca(v)
            print(f"\nExistem {resp} elementos iguais ao oque voce proucura dentro da lista.")
        case 6:
            def busca(v: list) -> int:
                qtd = 0
                for i in range(len(v)):
                    if v[i].isdigit():
                        qtd += 1
                return qtd
            resp = busca(v)
            print(f"\n{resp} elementos do tipo inteiro.")
        case 7:
            def conta_strings(v: list) -> int:
                qtd = tamanho
                for elem in v:
                    if elem.isdigit():
                        qtd -= 1
                    elif elem in ["False", "True"]:
                        qtd -= 1
                    elif '.' in elem:
                        num = float(elem)
                        qtd -= 1
                return qtd
            resp = conta_strings(v)
            print(f"\nContém {resp} Stings contidas no vetor preenchido.")
        case 8:
            def conta_boolean(v: list) -> int:
                qtd = 0
                for elem in v:
                    if elem == 'True' or elem == 'False':
                        qtd += 1
                return qtd
            resp = conta_boolean(v)
            print(f"\nContém {resp} elementos logicos contidos no vetor.")
        case 9:
            def conta_float(v: list) -> int:
                qtd = 0
                for elem in v:
                    if '.' in elem:
                        num = float(elem)
                        qtd += 1
                return qtd
            resp = conta_float(v)
            print(f"\nContém {resp} elementos do tipo float no vetor.")
        case 10:
            lista2 = []
            def copia_int(v: list, l2: list) -> None:
                for elem in v:
                    if elem.isdigit():
                        qtd = 0
                        qtd += 1
                        lista2.append(elem)
                print(f"Lista 1: {v}")
                print(f"\nLista 2 com os inteiros da lista 1: {l2}")
            print(copia_int(v, lista2))