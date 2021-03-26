from math import sqrt

"""
Se desea calcular cuántos metros se deben recorrer para atravesar una plaza en diagonal,
pero solo se conocen las distancia de las cuadras de ambos lados.
"""

ladoA = float(input("Ingrese el valor del lado A: "))
ladoB = float(input("Ingrese el valor del lado B: "))

diagonal = int(sqrt(ladoA ** 2 + ladoB ** 2))

print("Distancia para atravezar la plaza en diagonal: ", diagonal)
