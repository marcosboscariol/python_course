# Calcular a área de uma circunferência

import math


def calcular_area_circunferencia(raio):

    return math.pi * raio ** 2


raio_usuario = float(input("Informe o raio: "))

print(
    f"A área de uma circunferência de {raio_usuario} é {round(calcular_area_circunferencia(raio_usuario),2)}")
