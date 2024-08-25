'''
Tendo como dados de entrada a altura e o sexo de uma pessoa,construa um 
algoritmo que calcule seu peso ideal, utilizando as seguintes fórumulas:

- Para homens: (72.7 * h) - 58;
- Para mulheres: (62.1 * h) - 44.7
Sendo h o valor da altura.
'''

while True:
    sexo_usuario = input('Digite M para masculino e F para feminino: ')
    if sexo_usuario == 'M' or sexo_usuario == 'F' or sexo_usuario == 'm' or sexo_usuario == 'f':
        break
    else:
        print('Valor inválido. Digite M para masculino e F para feminino')

while True:
    try:
        altura_usuario = float(input('Digite sua altura em metros: '))
        if isinstance(altura_usuario, (int, float)):
            break
    except ValueError:
        print('Valor inválido. Digite sua altura em metros: ')

peso_ideal = 0
if sexo_usuario == 'M' or sexo_usuario == 'm':
    peso_ideal = (72.7 * altura_usuario) - 58
else:
    peso_ideal = (62.1 * altura_usuario) - 44.7

if sexo_usuario == 'M' or sexo_usuario == 'm':
    print(
        f'O peso ideal para uma pessoa do sexo masculino e com altura de {altura_usuario} cm é {peso_ideal} kg')
else:
    print(
        f'O peso ideal para uma pessoa do sexo feminino e com altura de {altura_usuario} cm é {peso_ideal} kg')
