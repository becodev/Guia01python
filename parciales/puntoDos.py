import json
import requests
from consumo_api import get_charter_by_id, get_all_sw_characters
from random import randint


def ordenar_nombre(peronaje):
    return peronaje['name']


def get_docs(ruta):
    req = requests.get(ruta)
    # Imprimimos el resultado si el código de estado HTTP es 200 (OK):
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_planeta(url):
    planeta = get_docs(url)
    return planeta['name']


def get_especie(url):
    especie = get_docs(url)
    return especie['name']


def puntoDos():
    personajes = get_all_sw_characters()
    personajes.sort(key=ordenar_nombre)

    for personaje in personajes:
        planeta = get_planeta(personaje['homeworld'])
        if(personaje['species']):
            especie = get_especie(personaje['species'][0])
        nombre = personaje['name']
        print("Nombre:", nombre, "\n Especie:", especie, "\nPlaneta:", planeta)

        if(len(personaje["films"]) == 7):
            print(personaje['name'], "participo en  las 7 peliculas.")


puntoDos()
