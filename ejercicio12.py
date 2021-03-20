"""
Una empresa distribuidora de energía le cobrar a sus abonados el consumo de kW por
hora, pero además debe sumarle el 0,21 % de impuesto, pero actualmente todos los
cliente están dentro de un plan de promoción que les descuenta el 3,7 % del monto total a
pagar.
"""

consumo = float(input("Ingrese consumo en KW: "))
precio = float(input("Ingrese costo del KW: "))

costo = consumo * precio
impuesto = (0.21 / 100) * costo
descuento = round((3.7 / 100) * (costo + impuesto), 2)
total = round(((costo + impuesto) - descuento), 2)

print("El importe a cobrar al cliente es: $", total)
