'''
 São coleções de dados ordenados, separados por vírgula e que estão dentro de colchetes

Listas Homogêneas:
['a', 'b', 'c']
[1, 2, 3]
['texto1', 'texto2', 'texto3']

Listas Heterogêneas:
['a', 1, 'texto1', ['b', 2, 'texto2']]
'''

lista_de_numeros = [6, 3, 7, 9]

print(type(lista_de_numeros))

lista_heterogenea = ['texto', 33, 45.98, False, [1, 2, 3]]

lista_vazia = []

lista1 = [1, 3, 5, 7]

lista2 = [2, 4, 6, 8]

print(lista1+lista2)

print(lista1*3)

print(lista1 == lista2)

lista_itens = [1, 3, 5, 7]

print(lista1 == lista_itens)

print(5 in lista1)

frase = 'Um texto qualquer'

lista_caracteres = list(frase)

print(lista_caracteres)

lista_letra = ['a', 'b', 'c']

# print(frase + lista_letra)

print(lista_letra + list(frase))

print(lista1[0])

print(lista1[-1])

print(lista_caracteres[0::2])

print(lista_caracteres[:9:2])

print(lista1[::-1])

lista1[0] = 10

print(lista1)

lista3 = lista1

lista3[0] = 5

print(lista1, lista3)
