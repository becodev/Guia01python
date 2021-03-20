"""
Una empresa telefónica debe facturar el costo de las llamadas telefónicas a sus cliente
para esto les cobra por tiempo de llamada (por minuto) pero además le adiciona un 0,5 %
del monto total de la llamada.
"""

tiempo = int(input("Ingrese cantidad de minutos de la llamada: "))
costo = float(input("Ingrese costo por minuto: "))

monto = (tiempo * costo)
adicional = monto * 0.005

print("El costo de la llamada es: ", monto + adicional, " pesos.")
