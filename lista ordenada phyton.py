while True:
    lista_original = []
    lista_crescente = []
    lista_decrescente = []
    
    print("digite 10 numetos a serem ordenados")
    for i in range(10):
        numeros = float(input())
        lista_original.append(numeros)
        
    lista_crescente = list(sorted(lista_original))
    lista_decrescente = list(reversed(lista_crescente))
    while True:
    
        impressao = int(input("\nqual lista vc deseja imprimir?\n1-original\n2-crescente\n3-decrescente\n4-refazer lista\n"))
        if impressao == 1:
           print(lista_original)
        if impressao == 2:
            print(lista_crescente)
        if impressao == 3:
            print(lista_decrescente)
        if impressao == 4:
            break
        continue
    continue