'''
Fazer um programa em Python que:

- Receba uma quantidade ilimitada de idade de pessoas
- Guarde essas idades em uma lista
- Para encerrar a digitação de idades o usuário deve digitar -1
- Em seguida, deve-se gerar uma tupla de idades
- Mostrar as seguintes informações:
    - Quantidade de idades digitadas
    - Média das idades
'''

idades_lista = []

while True:
    try:
        idades_usuario = int(input("Digite uma idade ou -1 para sair: "))
        if idades_usuario == -1:
            break
        else:
            idades_lista.append(idades_usuario)
    except:
        print('Valor inválido.')

idades_tupla = tuple(idades_lista)

quantidade_idades = len(idades_tupla)

soma_idades = sum(idades_tupla)

print(f'Foram digitadas {quantidade_idades} idades e a média das idades é {
      soma_idades/quantidade_idades}')
