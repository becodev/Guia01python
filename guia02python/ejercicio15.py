"""
Dado el valor numérico de la temperatura ambiente y su escala representada con una
carácter (C Celsius y F Fahrenheit), convertirla a la otra escala aplicando las siguientes
fórmulas según correspondan:
a. de F a C: (temp_f - 32) * 5/9
b. de C a F: (temp_c * 5/9) + 32
"""

temp = float(input("Ingrese temperatura: "))
escala = input("Ingrese escala de la temperatura(C o F): ")

faren = round((temp * 9/5) + 32, 2)
celsius = round((temp - 32) * 5/9, 2)

if(escala.upper() == "C"):
    print("La temperatura en escala Fahrenheit es: ", faren)
elif(escala.upper() == "F"):
    print("La temperatura en escala Celsius es", celsius)
else:
    print("Escala incorrecta.")
