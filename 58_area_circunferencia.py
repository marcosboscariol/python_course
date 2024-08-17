# Calcular a área de uma circunferência

import math

raio = float(input("Informe o raio da circunferência: "))

area = math.pi * raio ** 2

print(f"A área de uma circunferência de {raio} é {round(area,2)}")
