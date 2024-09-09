"""
- Conjuntos de pares chave:valor
- A chave deve ser única dentro da coleção
- São construídos por {}
- Utiliza=se : para separar a chave do valor
- O operador da esquerca é a chave e o da direita o valor
- Indexado pela Chave
- A chave é case sensitive

- Exemplo
f1 = {
    1: 'Mercedez',
    2: 'Ferrari',
    3: 'Renault'
}
"""
f1 = {
    1: 'Mercedez',
    2: 'Ferrari',
    3: 'Renault'
}

print(f1)

print(type(f1))

dic_vazio = {}

numeros = dict(um=1, dois=2, tres=3)

print(numeros)

dic1 = dict([('ana', 342), ('pedro', 3453), ('marcio', 8987)])

print(dic1)

print(dic1['ana'])

dic1['piva'] = 4578

print(dic1)
