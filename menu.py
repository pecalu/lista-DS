import ex_juntos
while True:
    ex_juntos.listaEX()
    continuar = input("\nDeseja continuar? 'sim' ou 'nao': ")
    if continuar.lower() == 'sim' or continuar.lower() == 's':
        continue
    else:
        print("\nEncerrando...")
        print("\nPrograma finalizado.")
        break