'''
São coleções ordenaadas, separadas por vírgula e que estão dentero de parêntesis

São coleções Imutáveis

Tuplas Homogêneas:
(1, 2, 3, 4)
("a", "b", "c")
("texto1", "texto2")

Tuplas Heterogêneas:
(1, "a", "texto1", (2, "b", "texto2"))

'''
montadoras = ('Ferrari', 'Fiat', 'Mercedez', 'Renault')

print(montadoras)

tupla_vazia = ()

tupla1 = (2, 0, 1, 4)

tupla2 = (2, 0, 1, 9)

print(tupla1 + tupla2)

print(tupla1 * 3)

print(tupla1 == tupla2)

print(2 in tupla1)

navegadores = 'Vikings'

texto_para_tupla = tuple(navegadores)

print(texto_para_tupla)

lista = [23, 34.9, 'texto']

lista_para_tupla = tuple(lista)

print(lista_para_tupla)

letras = ('a', 'b', 'c')

numeros = (1, 2, 3)

tupla_aninhada = (letras, numeros)

print(tupla_aninhada)

cores = ('r', 'g', 'b')

print(cores[1:3])

print(len(tupla2))

print(sorted(tupla2))
