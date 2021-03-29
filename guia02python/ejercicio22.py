"""
Simular que una persona tira tres veces un dado de seis lados (de manera aleatoria),
determinar si la persona saco un 5 y cuantos suma el total de los tres tiros.
"""
from random import sample

dado = range(1, 7)
tiro = sample(dado, k=3)
suma = 0
cinco = False

for i in range(0, 3):
    suma += tiro[i]
    if(tiro[i] == 5):
        cinco = True

print("Tiros", tiro)
print()
if(cinco == True):
    print("La persona saco un 5.")
else:
    print("La persona NO obtuvo un cinco.")
print()
print("La suma de los tres tiros es:", suma)
