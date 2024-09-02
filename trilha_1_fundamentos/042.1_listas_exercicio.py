'''
Fazer um programa que:

- Recebe uma quantidade ilimitada de nomes de cidades e armazene em uma lista

- Para encerrar a digitação o usuário deve digitar Sair

- Ordenar a lista em ordem crescente

- Mostrar as cidades ordenadas ao usuário
'''

cidades = []

while True:
    cidade_usuario = input(
        'Digite umaa cidade a ser acrescentada ou "Sair" para sair: ')
    if cidade_usuario == 'Sair':
        break
    else:
        cidades.append(cidade_usuario)

cidades.sort()

print(f'As cidades inclusas foram {cidades}')
