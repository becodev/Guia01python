"""
Convertir un valor entero de horas a segundos.
"""

horas = int(input("Ingrese cantidad de horas en entero: "))

segundos = horas * 60 * 60
# en la primer multiplicacion se pasa a minutos y en la segunda a segundos.

print("La conversion de horas a seg es: ", segundos, "segundos.")
