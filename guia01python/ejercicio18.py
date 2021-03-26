"""
Dada las tres mediciones que se realizó un pluviómetro en un día, cada vez que el mismo
se vacía, determinar cuántos milímetros llovió ese día.
"""

medicion1 = float(input("Ingrese primera medicion: "))
medicion2 = float(input("Ingrese segunda medicion: "))
medicion3 = float(input("Ingrese tercera medicion: "))

milimetros = medicion1 + medicion2 + medicion3

print("Hoy llovió:", milimetros, "milimetros.")
