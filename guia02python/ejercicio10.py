"""
Dado un número determinar si el mismo es múltiplo de 2 o de 5, de ser así mostrar dicho
número elevado al cubo.
"""

numero = int(input("Ingrese un numero entero: "))
cubo = numero ** 3

if(numero % 2 == 0 or numero % 5 == 0):
    if(numero % 2 == 0 and numero % 5 == 0):
        print(numero, "es multiplo de 2 y 5")
        print(numero, "al cubo es ", cubo)
    elif(numero % 2 == 0):
        print(numero, "es multiplo de 2")
        print(numero, "al cubo es ", cubo)
    else:
        print(numero, "es multiplo de 5")
        print(numero, "al cubo es ", cubo)
else:
    print("El numero no es multiplo de 2 ni de 5.")
