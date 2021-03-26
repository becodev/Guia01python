"""
Dada las tres notas obtenidas por un alumno en los distintos parciales, determinar si el
mismo está aprobado o desaprobado.
"""

parcial1 = float(input("Ingrese nota primer parcial: "))
parcial2 = float(input("Ingrese nota segundo parcial: "))
parcial3 = float(input("Ingrese nota tercer parcial: "))

promedio = round((parcial1 + parcial2 + parcial3) / 3, 2)

if(promedio >= 6):
    print("Alumno aprobado con promedio ", promedio)
else:
    print("Alumno desaprobado con promedio ", promedio)
