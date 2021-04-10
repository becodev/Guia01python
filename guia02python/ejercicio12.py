"""
Dado un número de mes de 1 a 12 determinar cuántos días tiene dicho mes.
"""
# No se contempla año bisiesto

mes = int(input("Ingrese numero de mes (1 a 12): "))

if(mes >= 1 and mes <= 12):
    if mes in [4, 6, 9, 11]:
        print("El mes ingresado tiene 30 dias.")
    elif(mes == 2):
        print("El mes ingresado tiene 28 dias.")
    else:
        print("El mes ingresado tiene 31 dias.")
else:
    print("Mes incorrecto.")
