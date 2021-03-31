from datetime import date
"""
Resuelva el ejercicio de 5 de la guía 2 (condicionales), sabiendo que 9 personas
presentaron su CV para el puesto vacante.
"""

hoy = date.today().year

for i in range(1, 10):
    nacimiento = int(input("Ingresar año de nacimiento: "))
    edad = hoy - nacimiento
    if(edad >= 18):
        print("El postulante es mayor de edad.")
        print("-------------------------------")
    else:
        print("El postulante es menor de edad")
        print("-------------------------------")
