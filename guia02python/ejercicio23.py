"""
Dado 4 nombres de personas, mostrar y contar los que comienzan con F o A.
"""
nombresA = []
nombresF = []
nombres = []

for i in range(0, 4):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

for i in range(0, 4):
    n = nombres[i]
    if(n[0:1].upper() == "F"):
        nombresF.append(n)
    elif(n[0:1].upper() == "A"):
        nombresA.append(n)

print("Nombres que comienzan con A:", nombresA)
print("Cantidad: ", len(nombresA))
print("=======================================")
print("Nombres que comienzan con F:", nombresF)
print("Cantidad: ", len(nombresF))
