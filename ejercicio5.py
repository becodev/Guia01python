"""
Determinar cuánto debe pagar el cliente de un estacionamiento, el precio se determina
por las horas que ocupo el estacionamiento.
"""

ingreso = int(input('Ingrese hora de ingreso: '))
salida = int(input('Ingrese hora de salida: '))
precio = float(input("Ingrese precio por hora: "))

horas = salida - ingreso

print('El costo a pagar por', horas, 'horas es: $', horas * precio)
