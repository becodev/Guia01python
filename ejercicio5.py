#!/usr/bin/env python3 

#determinar costo de estacionamiento

ingreso = int(input('Ingrese hora de ingreso: '))
salida = int(input('Ingrese hora de salida: '))
precio = float(input("Ingrese precio por hora: "))

horas = salida - ingreso 

print('El costo a pagar por', horas,'horas es: $', horas * precio)