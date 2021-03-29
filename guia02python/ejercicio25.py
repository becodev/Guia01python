"""
Determinar si un año es bisiesto teniendo en cuenta las siguientes reglas:
a. Los años bisiestos son divisibles por cuatro por ejemplo (2004, 2008)
b. Excepto si es divisible por 100 por ejemplo (2100, 2200) no son bisiestos
c. Excepto si es divisible por 400 por ejemplo (1600, 2000) son bisiestos
"""

anio = int(input("Ingrese año: "))
bisiesto = False

if(anio % 4 == 0):
    bisiesto = True
    if(anio % 100 == 0):
        bisiesto = False
        if(anio % 400 == 0):
            bisiesto = True

if(bisiesto == True):
    print(anio, "es bisiesto!")
else:
    print(anio, "no es bisiesto!")
