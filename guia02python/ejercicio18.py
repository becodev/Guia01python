from statistics import mode
"""
Dado las tres cartas que representan una mano del truco, determinar si el jugador tiene
envido o no, en el caso de tener determinar cuántos puntos tiene (si tiene flor no puede
cantar envido).
"""
reparto = ["primera", "segunda", "tercera"]
repar = [0, 1, 2]
palos = [1, 2, 3, 4]

palo = []
cartas = []

puntos = []


def barajar():
    for item in repar:

        carta = int(input("Ingrese %s carta: " % reparto[item]))

        if(carta not in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]):
            print("Carta invalida. Saliendo del programa.")
            break
        else:
            cartas.append(carta)
            pal = int(
                input("Ingrese palo(1:Espada, 2:Basto, 3:Oro, 4:Copas):"))
            palo.append(pal)


def tieneEnvido(palo, palos):
    for item in palos:
        repite = palo.count(item)

        if(repite == 2):
            return mode(palo)


def puntos(palo, cartas, palos):
    envido = []
    palito = tieneEnvido(palo, palos)
    for item in range(0, 3):
        if(palo[item] == palito):
            x = cartas[item]
            envido.append(x)
            print(x)
    if((envido[0] or envido[1]) >= 10):
        tantos = 20
    elif((envido[0] and envido[1]) < 9):
        tantos = 20 + envido[0] + envido[1]
    else:
        tantos = 20 + int(min(envido))
    print("-------------------------------------------")
    print("¡El jugador tiene %s puntos para el envido!" % tantos)
    print("-------------------------------------------")


def iniciar():
    barajar()
    if((palo[0] and palo[1] and palo[2]) == palo[0]):
        print("----------------------------")
        print("¡El jugador tiene flor!")
        print("----------------------------")
    else:
        puntos(palo, cartas, palos)


iniciar()
