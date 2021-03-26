"""
Una pinturería debe elaborar el presupuesto para un cliente y necesita calcular el costo
total, este se deriva de la cantidad de pintura requerida y de la mano de obra, teniendo en
cuenta lo siguiente: se requiere un litro de pintura por m2 y el costo de mano de obra es
del 45 % del precio total de pintura.
"""

superficie = float(input("Ingresar cantidad m2 a pintar: "))
precioPintura = float(input("Ingresar precio del litro de pintura: "))

pintura = superficie * precioPintura
manObra = pintura * 0.45

print("El presupuesto total es: ", pintura + manObra, " pesos.")
