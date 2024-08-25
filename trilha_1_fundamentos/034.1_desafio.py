# Fazer um programa em Python que leia um número inteiro, positivo, maior que zero e verifique se o número é par ou impar

while True:
    try:
        numero_usuario = int(
            input('Digite um número inteiro, positivo e maior que zero: '))
        if numero_usuario > 0:
            break
        else:
            print('O número deve ser maior que zero, tente novamente.')
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if numero_usuario % 2 == 1:
    print(f'O número {numero_usuario} é impar')
else:
    print(f'O número {numero_usuario} é par')
