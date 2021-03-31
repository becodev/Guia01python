"""
Dado 15 números indicar cuál es el mayor.
"""

numeros = [11, 33, 4, 5, 12, 56, 21, 34, 625, 76, 78, 12, 123, 54, 69]
i = 0
mayor = 0
while i < 15:
    if(numeros[i] > mayor):
        mayor = numeros[i]
    i += 1

print("El numero mayor es %s" % mayor)
