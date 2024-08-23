# Estrutura sequencial -> Um comando é executado em sequência do outro

# Estrutura condicional -> O fluxo é basead em condições

idade_usuario = int(input('Digite sua idade: '))

if idade_usuario > 18:
    print(f'Parabéns, você tem {idade_usuario} e já é maior de idade')

else:
    print(f'Você ainda não é maior de didade, aguarde mais {
          18 - idade_usuario} anos para ser maior de idade')
