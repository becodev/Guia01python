"""
Ahora modifique el ejercicio anterior en el que además se conoce el número de cuotas en
la que paga, y aplicar los siguientes criterios para obtener el monto final (los recargos por
cuotas son los mismos para cualquier tarjeta):
a. Si paga en una cuota no hay recargo por cuotas
b. Si paga en tres cuotas el recargo es del 3 %
c. Si paga en ocho el recargo es del 17 %
d. Si paga en doce el recargo es del 32 %
"""

monto = float(input("Ingrese monto: "))
tarjeta = int(input("Ingrese 1 para tarjeta visa, 2 para mastercard: "))
cuotas = int(input("Ingrese cantidad de cuotas (solo 1, 3, 8,12): "))

visa = round(monto * 1.07, 2)
master = round(monto * 1.11, 2)


if(tarjeta == 1):
    montoFinal = visa
elif(tarjeta == 2):
    montoFinal = master
else:
    print("Tarjeta incorrecta.")

if(cuotas == 1):
    print("Cobrar sin recargos: ", montoFinal)
elif(cuotas == 3):
    recargo = montoFinal * 1.03
    print("Cobrar con 3 % de recargos: ", recargo)
elif(cuotas == 8):
    recargo = montoFinal * 1.17
    print("Cobrar con 17 % de recargos: ", recargo)
elif(cuotas == 12):
    recargo = montoFinal * 1.32
    print("Cobrar con 32 % de recargos: ", recargo)
else:
    print("Cuotas incorrectas.")
