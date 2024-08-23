# Permite uma condição multidirecional

nota_usuario = float(input('Digite a nota: '))

if nota_usuario < 0 or nota_usuario > 10:
    print(f'A nota {nota_usuario} não é válida, digite um valor entre 0 e 10')
elif nota_usuario >= 9:
    print(f'A nota {nota_usuario} é classificada como A')
elif nota_usuario >= 8:
    print(f'A nota {nota_usuario} é classificada como B')
elif nota_usuario >= 8:
    print(f'A nota {nota_usuario} é classificada como C')
elif nota_usuario >= 8:
    print(f'A nota {nota_usuario} é classificada como D')
else:
    print(f'A nota {nota_usuario} é classificada como E')
