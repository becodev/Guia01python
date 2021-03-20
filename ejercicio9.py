"""
Una empresa de transportes les cobra a sus pasajeros por kilómetros recorridos, y
necesita poder calcular el monto a cobrar a un cliente cuando se baja.
"""

kilometros = float(input("Ingrese cantidad de kilometros recorridos: "))
precio = float(input("Ingrese precio por kilometro: "))

print("El costo total por el recorrido es: $", kilometros * precio, " pesos.")
