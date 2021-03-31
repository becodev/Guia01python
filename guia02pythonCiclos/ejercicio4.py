"""
Dada las notas de los 18 alumnos de un curso determinar cantidad de aprobados y
desaprobados, y además el promedio de nota de los aprobados.
"""

notas = [6, 10, 1, 5, 6, 7, 7.5, 2, 9, 8.5, 4.5, 7, 7, 10, 5, 5.5, 7.2, 1]

aprobados = 0
desaprobados = 0
nota = 0

for i in notas:
    if(i >= 6):
        aprobados += 1
        nota += i
    else:
        desaprobados += 1

promedio = round(nota / aprobados, 2)

print("Cantidad de aprobados: %s" % aprobados)
print("Cantidad de desaprobados: %s" % desaprobados)
print("Promedio de los aprobados: %s" % promedio)
