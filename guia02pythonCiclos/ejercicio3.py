"""
Dado un número mostrar su tabla de multiplicar del 1 al 10.
"""

base = int(input("Ingrese la base: "))
print()
for i in range(1, 11):
    cuenta = i * base
    print(i, "x", base, "=", cuenta)
