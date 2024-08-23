'''
Receber um valor inteiro, positivo, maior que zero
Amarzenar esse valor em uma variável chamada numero
Receber uma frase e armazenar na variável texto
Converter a variavel numero para float e armazenar em uma variavel chamada x
Colocar todos os caracteres da variavel texto para maiúscula e armazenar na mesma variável
Imprimir as variáveis texto e x
'''

numero = int(input("Insira um valor positivo e maior que zero: "))
frase = input('Insira uma frase: ')

x = float(numero)
frase = frase.upper()

print(f'O valor de x é {x}')
print(f'A frase toda maiúscula ficou: {frase}')
