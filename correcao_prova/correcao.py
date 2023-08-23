'''
EXERCÍCIOS:
1. Fazer um procedimento que preencha uma lista até que seja digitado . (ponto). 
    Obs1: o ponto não deve ser inserido na lista.
    Obs2: os elementos podem ter mais de um caractere cada
2. Fazer um procedimento que jogue numa segunda lista os elementos numericos
   convertidos para numero.
    Obs: Neste caso fazer o casting
3. Fazer um procedumento que jogue numa terceira lista os elementos não numéricos.
4. Fazer uma função que retorne quantos elementos numericos exitem na lista original.
5. Fazer uma função que retorne quantos elementos NÃO numericos exitem na lista original.
*** DESAFIO
6. Fazer uma função que conte quantos elementos numericos existem na lista.
    Obs: Incluindo os dados do tipo float

CRIAR UM MENU PARA EXECUTAR CADA UMA DESTAS OPERAÇÕES
'''


# --------- PROCEDIMENTOS
# ---- Preenche a lista com 5 elementos
def preenche_lista(l: list) -> None:
    for volta in range(5):
        elem = input("Digite um caractere: ")
        l.append(elem)

# ---- Adiciona em outra lista somente os numéricos
def insere_digitos_lista(l: list, new_l: list) -> None:
    for volta in range(5):
        if l[volta].isnumeric():
            new_l.append(l[volta])

# --------- PROGRAMA PRINCIPAL
lista = list()
lista2 = list()
preenche_lista(lista)
insere_digitos_lista(lista, lista2)
print(f"\nlista: {lista}\nLista digito: {lista2}")