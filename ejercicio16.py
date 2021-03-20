from statistics import mean
"""
Calcular el promedio de temperatura y presión recolectado por una estación
meteorológica en una semana, considerando que realiza solo una medición al día.
"""

temperatura1 = float(input("Ingrese temperatura dia 1: "))
temperatura2 = float(input("Ingrese temperatura dia 2: "))
temperatura3 = float(input("Ingrese temperatura dia 3: "))
temperatura4 = float(input("Ingrese temperatura dia 4: "))
temperatura5 = float(input("Ingrese temperatura dia 5: "))
temperatura6 = float(input("Ingrese temperatura dia 6: "))
temperatura7 = float(input("Ingrese temperatura dia 7: "))

presion1 = float(input("Ingrese presion dia 1: "))
presion2 = float(input("Ingrese presion dia 2: "))
presion3 = float(input("Ingrese presion dia 3: "))
presion4 = float(input("Ingrese presion dia 4: "))
presion5 = float(input("Ingrese presion dia 5: "))
presion6 = float(input("Ingrese presion dia 6: "))
presion7 = float(input("Ingrese presion dia 7: "))


"""
Utilizo la funcion mean() de la libreria statistics para calcular el promedio,
los valores hay que pasarlos dentro de un array: mean([valor1, valor2, etc])
"""

promTemp = round(mean([temperatura1, temperatura2, temperatura3,
                       temperatura4, temperatura5, temperatura6, temperatura7]), 2)

promPres = round(
    mean([presion1, presion2, presion3, presion4, presion5, presion6, presion7]), 2)


print("Promedio de temperatura: ", promTemp)
print("Promedio de presion: ", promPres)
