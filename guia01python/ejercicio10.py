"""
Determinar cuánto demora una persona en ir en bicicleta de un lugar a otros, suponiendo
que esta se mueve a una velocidad constante y se conocen la cantidad de kilómetros del
camino.
"""

velocidad = int(input("Ingrese velocidad de la bici expresada en km/h: "))
kilometros = float(input("Ingrese cantidad de KM recorridos: "))

# se multiplica por 60 para obtener tiempo en minutos.
tiempo = int(kilometros / velocidad * 60)

print("Tiempo del recorrido :", tiempo, " minutos.")
