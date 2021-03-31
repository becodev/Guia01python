"""
Ingresar 10 números e indicar los que son múltiplos de 2 y de 3.
"""
numeros = []
multiplos2 = []
multiplos3 = []

for i in range(1, 11):
    num = int(input("Ingrese un numero:"))
    numeros.append(num)
    if(num % 2 == 0):
        multiplos2.append(num)
    if(num % 3 == 0):
        multiplos3.append(num)

print()
print("Numeros ingresados:", numeros)
print()
print("Multiplos de dos:", multiplos2)
print()
print("Multiplos de tres:", multiplos3)
