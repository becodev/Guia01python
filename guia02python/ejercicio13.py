"""
Dado tres números obtener el mayor de estos.
"""

numeros = 1
lista = []
while numeros < 4:
    numero1 = float(input("Ingrese un numero: "))
    lista.append(numero1)
    numeros += 1

maximo = max(lista, key=float)
print("El numero mayor de los ingresados es:", maximo)
