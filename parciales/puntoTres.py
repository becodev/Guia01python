from random import randint

lista = []

for i in range(0, 77):
    numero = randint(1, 400)
    lista.append(numero)

mayor = max(lista)
menor = min(lista)
print("Cantidad de numeros:", len(lista))
print("Valor menor: ", menor)
print("Valor mayor:", mayor)
lista.sort()

print("Listado de numeros:")
for numero in lista:
    print(numero)

print("Numeros pares:")
for numero in lista:
    if(numero % 2 == 0):
        print(numero)
