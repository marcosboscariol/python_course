'''
Faça um programa que recebe um número e calcule a soma de seus dígitos.

Fazer utilizando for e while
'''

while True:
    try:
        numero_usuario = int(input("Digite um número inteiro: "))
        if isinstance(numero_usuario, int):
            break
    except:
        print('Valor inválido.')


soma = 0
for i in range(len(str(numero_usuario))):
    soma = soma + int(str(numero_usuario)[i])

print(f'A soma dos diítos do número {numero_usuario} é {soma}')
