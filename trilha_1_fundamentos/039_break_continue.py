# break e continue são opostos

# break faz com que o looping seja encerrado

# continue desvia o fluxo de execução para o topo do comando

# Programa para printar os número pares em um intervalo

while True:
    try:
        numero_final_usuario = int(
            input('Informe o último número do intervalo: '))
        if isinstance(numero_final_usuario, int):
            break
    except:
        print('Valor inválido.')
numeros_pares = []

for i in range(1, numero_final_usuario + 1):
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        continue

print(f'Os números pares entre 1 e {numero_final_usuario} são {numeros_pares}')
