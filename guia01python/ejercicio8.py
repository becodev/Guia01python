"""
El entrenador de un equipo de básquet desea determinar la eficiencia en tiros de campo
de un jugador "X".
"""

tirosTotal = int(input("Ingrese la cantidad total de tiros: "))
tirosAdentro = int(input("Ingrese cantidad de tiros embocados: "))

eficiencia = tirosAdentro / tirosTotal * 100

print("La eficiencia del jugador fue: ", eficiencia, "%")
