"""
Un supermercado está estableciendo el precio de venta para nuevos productos, de estos
productos desean generar el 27 % de ganancia.
"""

precio = float(input("Ingrese precio del producto: "))
ganancia = 27

precioFinal = round((precio * 1.27), 2)

print("El precio final del producto es: $", precioFinal)
