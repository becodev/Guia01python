"""
Determinar si un número está dentro del rango de -15 hasta 81.
"""

numero = float(input("Ingrese un numero: "))

if(numero >= -15 and numero <= 81):
    print("El numero", numero, "esta dentro del rango -15 a 81.")
else:
    print("El numero", numero, "NO esta dentro del rango -15 a 81.")
