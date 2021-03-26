"""
Dado dos números determinar cuál es el mayor o si son iguales.
"""

numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))

if(numero1 > numero2):
    print(numero1, " es mayor que ", numero2)
elif(numero1 == numero2):
    print(numero1, " es igual a ", numero2)
else:
    print(numero2, " es mayor que ", numero1)
