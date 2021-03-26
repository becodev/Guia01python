"""
Un profesor desea calcular el promedio de un alumno a lo largo de los cuatro parciales que
rindió.
"""

parcial1 = float(input("Ingrese nota del parcial 1: "))
parcial2 = float(input("Ingrese nota del parcial 2: "))
parcial3 = float(input("Ingrese nota del parcial 3: "))
parcial4 = float(input("Ingrese nota del parcial 4: "))

promedio = round(((parcial1 + parcial2 + parcial3 + parcial4)/4), 2)

print("El promedio del alumno es: ", promedio)
