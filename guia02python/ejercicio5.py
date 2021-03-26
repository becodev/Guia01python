"""
Resuelva el ejercicio de 3 de la guía uno aplicando el filtro para los CV.
"""
from datetime import date

"""
El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
nacimiento.
"""

hoy = date.today().year

nacimiento = int(input("Ingresar año de nacimiento: "))

edad = hoy - nacimiento

if(edad >= 18):
    print("El postulante es mayor de edad.")
else:
    print("El postulante es menor de edad")
