"""
Dada una fecha en formato día/mes/año indicar la fecha del día siguiente.
"""

fecha = "31/11/2020"  # input("Ingrese una fecha en formato dd/mm/aaaa: ")

print("Fecha ingresada: ", fecha)
dia = int(fecha[0:2])
mes = int(fecha[3:5])
anio = int(fecha[6:10])

if(mes < 12 and dia <= 30):
    dia += 1
elif(dia == 31 and mes != 12):
    dia = "01"
    mes += 1
elif(mes == 12 and dia == 31):
    dia = "01"
    mes = "01"
    anio += 1

print("Fecha salida:", dia, mes, anio)
