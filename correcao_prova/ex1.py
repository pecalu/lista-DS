#1. Fazer um procedimento que preencha uma lista até que seja digitado . (ponto).
#    Obs1: o ponto não deve ser inserido na lista.
#   Obs2: os elementos podem ter mais de um caractere cada
l = list()
def preenche_vetor(l: list)->   None:
    teste = 0
    while teste != '.':
        elem = input("Digite um caractere: ")
        if elem == '.':
            teste = '.'
        else:
            l.append(elem)
    print (l)

preenche_vetor(l)