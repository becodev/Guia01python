
import json
import requests
from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint


def puntoUno():
    numero1 = randint(1, 83)
    numero2 = randint(1, 83)
    personaje1 = get_charter_by_id(numero1)
    personaje2 = get_charter_by_id(numero2)

    # cual es el personaje más alto (indicar el nombre)
    if(int(personaje1["height"]) > int(personaje2["height"])):
        print("El personaje mas alto es:", personaje1["name"])
    else:
        print("El personaje mas alto es:", personaje2["name"])
    print()
    # cual es el personaje más pesado (indicar el nombre)

    if(personaje1["mass"].isdecimal() > personaje2["mass"].isdecimal()):
        print("El personaje mas pesado es:", personaje1["name"])
    else:
        print("El personaje mas pesado es:", personaje2["name"])
    print()
    # cual personaje participó en más películas (si los dos participaron en la misma
    # cantidad indicarlo) (indicar el nombre)

    if(len(personaje1["films"]) == len(personaje2["films"])):
        print(personaje1["name"], "y", personaje2["name"],
              "Participaron en la misma cantidad de peliculas.")
    elif(len(personaje1["films"]) > len(personaje2["films"])):
        print(personaje1["name"], "es quien participo en mas peliculas. Total:", len(
            personaje1["films"]))
    else:
        print(personaje2["name"], "es quien participo en mas peliculas. Total:", len(
            personaje2["films"]))
    print()
    # determinar si alguno de los personajes aleatorios se llama Yoda o Grievous

    if(personaje1["name"] == "Yoda"):
        print("El primer personajes es Yoda.")
    if(personaje2["name"] == "Grievous"):
        print("El segundo personaje es Grievous")


puntoUno()
