from datetime import date
"""
Dado el nombre, apellido y año de nacimiento de tres personas mostrar los datos de los
que son mayores de edad.
"""
hoy = date.today().year
personas = 1

while personas <= 3:
    nombreApellido = input("Ingrese nombre y apellido: ")
    nacimiento = int(input("Ingresar año de nacimiento: "))
    edad = hoy - nacimiento
    if(edad >= 18):
        print("=================================")
        print("La persona ", nombreApellido, "es mayor de edad.")
        print("=================================")
    personas += 1
