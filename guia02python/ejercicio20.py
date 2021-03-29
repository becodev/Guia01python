"""
Dado 5 números contar cuantos son múltiplos de 3.
"""
numeros = []
contar = 0

for i in range(0, 5):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
    if(num % 3 == 0):
        contar += 1

print()
print("Numeros ingresados: %s" % numeros)
print()
print("La cantidad de multiplos de tres es: %s" % contar)
