# Sequência de caracteres, que pode ser associado a uma lista

# Isso permite que façamos o slicing

letra = 'a'

print(type(letra))

frase = 'Isso é uma string'

frase2 = '''É possível inserir uma string
com quebra de texto'''

print(frase2)

print(frase[0])

"""
Primeiro parâmetro -> Início
Segundo parâmentro -> Limite superior (n-1)
Terceiro parâmetro -> Tamanho do passo
"""
print(frase[0:1:1])

print(frase[0::2])

print(frase[::-1])

# Strip -> Remove os espaços em branco da equerda e direita

frase_com_espcos_em_branco = '     Frase     '

print(frase_com_espcos_em_branco)

print(frase_com_espcos_em_branco.strip())

print(frase.split())

print(frase.split('s'))
