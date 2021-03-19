#!/usr/bin/env python3 
from datetime import date 
#calcular edad de nacimiento 

hoy = date.today()

anio_nacimiento = int(input("Ingresar año de nacimiento: "))

edad = hoy.year - anio_nacimiento 

print("La edad del postulante es: ", edad)
