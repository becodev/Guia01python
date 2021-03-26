"""
Determinar si un número dado es positivo o negativo.
"""

numero = float(input("Ingrese un numero: "))

if(numero > 0):
    print(numero, " es positivo.")
elif(numero == 0):
    print("Ingresaste un cero.")
else:
    print(numero, " es negativo.")
