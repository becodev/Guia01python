"""
Dado 5 números sumar los que son múltiplos de dos y obtener el promedio de estos.
"""
numeros = []
suma = 0
contar = 0

for i in range(0, 5):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    if(num % 2 == 0):
        suma = suma + num
        contar = contar + 1

promedio = round(suma / contar, 2)
print()
print("Numeros ingresados:", numeros)
print()
print("Cantidad de multiplos de dos: ", contar)
print()
print("El promedio de los numeros multiplos de dos es: %s" % promedio)
