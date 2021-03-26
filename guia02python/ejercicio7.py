"""
Dado el monto de la compra de un cliente y la tarjeta de crédito con la que paga
determinar el monto final de la compra considerando los siguientes criterios:
a. Si la tarjeta es Visa se debe aplicar un recargo del 7 %
b. Si la tarjeta es Mastercard se le aplica un recargo del 11%
"""

monto = float(input("Ingrese monto: "))
tarjeta = int(input("Ingrese 1 para tarjeta visa, 2 para mastercard: "))

visa = round(monto * 1.07, 2)
master = round(monto * 1.11, 2)

if(tarjeta == 1):
    print("Monto a cobrar con visa: ", visa)
elif(tarjeta == 2):
    print("Monto a cobrar con master: ", master)
else:
    print("Tarjeta incorrecta.")
