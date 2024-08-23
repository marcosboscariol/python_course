'''
if <expressao_logica1>:
    if <expressao_logica2>:
        <comando1>
    else:
        <comando2>
else:
    <comando3>
'''
numero_usuario = int(input('Digite um número inteiro: '))

if numero_usuario > 0:
    if numero_usuario % 2 == 1:
        print(f'O número {numero_usuario} é positivo e impar')
    else:
        print(f'O número {numero_usuario} é positivo e par')
else:
    if abs(numero_usuario % 2) == 1:
        print(f'O número {numero_usuario} é negativo e impar')
    else:
        print(f'O número {numero_usuario} é negativo e par')
