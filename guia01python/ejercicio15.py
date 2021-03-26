"""
Un grupo de amigos se hospedan en un hotel, y al momento de pagar se dividen los gastos
de la siguiente manera:
a. Iván paga el 40 %
b. German paga el 33 %
c. Esteban paga el 55 % de lo que pago Iván
d. Hernán paga el resto
Determinar cuánto debe pagar cada uno.
"""

importe = float(input("Ingrese el importe a pagar: "))

ivan = round((importe * 0.40), 2)
german = round((importe * 0.33), 2)
esteban = round((ivan * 0.55), 2)
hernan = round((importe - ivan - german - esteban), 2)

print("Ivan debe pagar: ", ivan)
print("German debe pagar: ", german)
print("Esteban debe pagar: ", esteban)
print("Hernan debe pagar: ", hernan)
