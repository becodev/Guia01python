from datetime import date

"""
El área de RRHH de una empresa desea filtrar los CV de los postulantes para un puesto
vacante, el requisito mínimo es la edad, pero en los datos solo tienen la fecha de
nacimiento.
"""

hoy = date.today().year

nacimiento = int(input("Ingresar año de nacimiento: "))

edad = hoy - nacimiento

print("La edad del postulante es: ", edad, " años.")
