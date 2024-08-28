# Estrutura mias utilizada para repetições indefinidas

'''
while <expressão lógica>:
    comando
'''

while True:
    try:
        quantidade_de_idades = int(
            input('Digite a quantidade de idades a serem informadas: '))
        if isinstance(quantidade_de_idades, (int, float)):
            break
    except:
        print('Valor informado inválido.')

i = 0
soma_idades = 0

while i < quantidade_de_idades:
    try:
        idades = int(
            input(f'Digite a idade {i + 1}: '))
        if isinstance(quantidade_de_idades, (int, float)):
            soma_idades = soma_idades + idades
            i += 1
    except:
        print('Valor informado inválido.')

media_idades = soma_idades / quantidade_de_idades

print(f'A média das idades é {round(media_idades,2)}')
