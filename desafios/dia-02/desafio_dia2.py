
option = int(input('Selecione a operacao \n - 1-Soma\n - 2-Subtracao\n - 3-Divisao\n - 4-Multiplicacao\n - Digite a operacao:'))


numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))


if int(option) == 1:
    resultado = numero1 + numero2
    print(numero1, '+', numero2, '=', resultado)
elif int(option) == 2:
    resultado = numero1 - numero2
    print(numero1, '-',numero2, '=', resultado)
elif int(option) == 3:
    resultado = numero1 / numero2
    
    print(numero1, '/',numero2, '=', resultado)
elif int(option) == 4:
    resultado = numero1 * numero2
    print(numero1, '*',numero2, '=', resultado)
elif int(option)  > 4:
    print('operacao invalida!!!')

