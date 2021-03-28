"""
Dada una fecha en formato día/mes determinar si la misma es correcta.
"""

fecha = input("Ingrese fecha en formato dd/mm: ")
largo = len(fecha)

if(largo != 5):
    print("Formato de fecha incorrecta.")
else:
    dia = int(fecha[0:2])
    mes = int(fecha[3:5])
    if((dia >= 1 and dia <= 31) and (mes > 0 and mes < 32)):
        print("¡¡Fecha correcta!!")
    else:
        print("Fecha incorrecta :(")
