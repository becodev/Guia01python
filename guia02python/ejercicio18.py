"""
Dado las tres cartas que representan una mano del truco, determinar si el jugador tiene
envido o no, en el caso de tener determinar cuántos puntos tiene (si tiene flor no puede
cantar envido).
"""
reparto = ["primera", "segunda", "tercera"]
cartas = []
palos = []

for item in range(0, 3):
    carta = int(input("Ingrese %s carta: " % reparto[item]))
    if(carta not in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]):
        print("Carta invalida. Saliendo del programa.")
        break
    else:
        cartas.append(carta)
        palo = int(input("Ingrese palo(1:Oro, 2:Basto, 3:Espada, 4:Copas):"))
        palos.append(palo)

# tiene flor?
print("----------------------------")
if(palos[0] and palos[1] and palos[2] == palos[0]):
    print("El jugador tiene flor!")


"""
falta terminar
"""
