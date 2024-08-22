# Escopo de uma variável é o rol de atuação de uma varável, sua amplitude

x = 0
y = 0

print(f'Gy: {y}')
print(f'Gx: {x}')


def funcao():
    y = 4
    print(f'Fy: {y}')
    print(f'Fx: {x}')


funcao()
print(f'Gy: {y}')
print(f'Gx: {x}')
