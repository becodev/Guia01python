"""
Dada una lista de números (finalizada en cero) determinar cuántos números positivos y
negativos hay en dicha lista.
"""

numero = int(input("Ingrese un numero distinto de cero: "))
positivos = 0
negativos = 0

while numero != 0:
    if(numero < 0):
        negativos += 1
    else:
        positivos += 1

    numero = int(input("Ingrese un numero distinto de cero: "))


print("Numeros positivos ", positivos)
print("Numeros negativos ", negativos)
