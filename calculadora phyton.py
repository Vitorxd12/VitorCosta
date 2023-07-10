while True:
    num1=float(input("escolha o priemiro numero\n"))
    num2=float(input("escolha o segundo numero\n"))
    tipo=float(input("escolha o tipo de calculo:\n1-soma\n2-subtracao\n3-multiplicação\n4-divisao\n"))

    if tipo == 1:
        soma=float(num1+num2)
    elif tipo==2:
        soma=float(num1-num2)
    elif tipo==3:
        soma=float(num1*num2)
    elif tipo==4:
        soma=float(num1/num2)
    else:
        print("escolha um calculo valido")
        continue
        soma==01
    print("o resultado é",soma)
    continue
