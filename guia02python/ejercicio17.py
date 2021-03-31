"""
Dado dos números mostrar la diferencia entre el mayor y el menor.
"""

numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))

if(numero1 > numero2):
    resta = numero1 - numero2
    mayor = numero1
elif(numero2 > numero1):
    resta = numero2 - numero1
    mayor = numero2

print("El mayor valor ingresado fue: ", mayor)
print("La diferencia entre el mayor y menor es: ", resta)
