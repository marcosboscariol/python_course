# Calcular a área de uma circunferência

import math


def calcular_area_circunferencia(raio):

    area = math.pi * raio ** 2

    print(f"A área de uma circunferência de {raio} é {round(area,2)}")


raio_usuario = float(input("Informe o raio: "))

calcular_area_circunferencia(raio_usuario)
