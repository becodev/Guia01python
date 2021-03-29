"""
Dado tres números mostrarlos en orden ascendente.
"""
numeros = []
for item in range(0, 3):
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)

numeros.sort()

print("Los numeros en orden ascendente son:",
      numeros[0], numeros[1], numeros[2])
