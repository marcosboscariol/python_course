'''
Receber o cadastro de uma quantidade ilimitada de proprietários e seus respectivos apartamentos
Armazene em um dicionario, com a chave sendo o número do apartamento
Para finalziar a coleta de dados, o usuário deve digitar -1
Demosntrar em uma lista em ordem crescente pelo apartamento
Apresentar a quantidade total de apartamentos cadastrados
'''
proprietarios = {}

while True:
    apto = int(input('Digite o apartamento ou -1 para sair: '))
    if apto != -1:
        proprietario = input(f'Digite o proprietrio do apartamento {apto}: ')
        proprietarios.update({apto: proprietario})
    else:
        break

dicionario_apartamentos = dict(proprietarios)

print(dicionario_apartamentos)
