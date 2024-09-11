'''
- Coleções não ordenadas (sem indíce) que não eprmitem a duplicação de elementos
- Delimitados por {}
- Estrutura mutável

- Exemplo:
    mix = {1, "a", 'nome', 3.56, (2, 4, 6)}
'''

cesta = {'maça', 'laranja', 'banana', 'pera', 'laranja', 'maça'}

print(cesta)

print('laranja' in cesta)

a = set('abracadabra')

print(a)

b = set('alacazam')

print(b)

# União
print(a | b)

# Intersecção
print(a & b)

# Diferença
print(a ^ b)

# Diferença simétrica
print(a - b)

flores_europa = {'rosa', 'lavanda', 'tulipa'}

flores_america = {'rosa', 'tulipa', 'lirio', 'margarida'}

print(len(flores_europa))

print(sorted(flores_america))

flores_america.add('orquidea')

print(flores_america)
