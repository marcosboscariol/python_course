# Repetição definida, sabemos a quantidade de vezes que o a ação será repetida

'''
for <variável de iteração> in <sequencia>:
    comando
'''
for i in range(1, 6):
    print(i)

fatorial_usuario = int(input('Informe um número positivo maior que 0: '))

fatorial = 1
for i in range(1, fatorial_usuario + 1):
    fatorial = fatorial * i

print(f'O fatorial de {fatorial_usuario} é {fatorial}')
