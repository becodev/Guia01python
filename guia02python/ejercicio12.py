"""
Dado un número de mes de 1 a 12 determinar cuántos días tiene dicho mes.
"""
# No se contempla año bisiesto

mes = int(input("Ingrese numero de mes (1 a 12): "))

if mes in [2, 4, 6, 9, 11]:
    print("El mes ingresado tiene 30 dias.")
else:
    print("El mes ingresado tiene 31 dias.")
