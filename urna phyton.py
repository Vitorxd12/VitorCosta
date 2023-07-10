anglo = 0
joaozinho = 0
iasmim = 0
votos_nulos = 0
votos_totais = 0
repeticoes = 5

print("defina uma senha para a coleta de resultados (4 digitos)\n")
senha = int(input())

while repeticoes > 0:
    print("escolha seu candidato")
    print("\n1-anglo\n2-jaoazinho\n3-iasmim\n0-nulo\n")
    escolha = int(input())

    if escolha == 1:
        anglo += 1
        votos_totais += 1
        repeticoes -= 1

    elif escolha == 2:
        joaozinho += 1
        votos_totais += 1
        repeticoes -= 1
        
    elif escolha == 3:
        iasmim += 1
        votos_totais += 1
        repeticoes -= 1
        
     
    elif escolha == 0:
        votos_nulos += 1
        votos_totais += 1
        repeticoes -= 1
        
    else:
        continue
        
    continue 
while True:    
    variavel = int(input("digite a senha para expor os resultados:\n"))   
    if variavel == senha:
       print("Resultados:\n anglo=", anglo, "\n", "joaozinho=", joaozinho, "\n", "iasmim=", iasmim, "\n", "votos nulos=", votos_nulos, "\n", "votos totais=", votos_totais, "\n",)
       break
    else:
        print("bolsonarista safado!")
        continue