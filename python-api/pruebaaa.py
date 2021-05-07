

from consumo_api import get_all_sw_characters, get_all_sw_characters_names


def ordenar_nombre(peronaje):
    return peronaje['name']


def altura(item):
    # print(item, type(item))
    if(item['height'].isdecimal()):
        return int(item['height'])
    else:
        return -1


def peso(item):
    if(item['mass'].isdecimal()):
        return float(item['mass'])
    else:
        return -1


def color_pelo(item):
    return item['hair_color'] + item['name']


def busqueda(lista, buscado):
    pos = -1

    # for i in range(len(lista)):
    #     if(lista[i]['name'] == buscado):
    #         pos = i

    for index, personaje in enumerate(lista):
        if(personaje['name'] == buscado):
            pos = index

    return pos


# sw_data = get_all_sw_characters_names()

sw_data = get_all_sw_characters()


#! TIMSORT
# sw_data.sort(key=color_pelo)


# for character in sw_data:

# print(character['name'])
# print(character['name'], character['height'], character['mass'])


#! Mostrar toda la informacion de Yoda si esta en la Lista
# buscado = 'Yoda'
# posicion = busqueda(sw_data, buscado)

# if(posicion > -1):
#     print(buscado, 'esta en la lista en la posicion', posicion)
#     # sw_data[posicion]['species'] = "desconosido"
#     print('info ->')
#     print(sw_data[posicion])
#     # sw_data.pop(posicion)
# else:
#     print(buscado, 'no esta en la lista')

#! Determinar si Mandalorian o Grogu esta en la lista
# buscado = 'Mandalorian'
# buscado2 = 'Grogu'


# def buscar(buscado, data):
#     posicion = busqueda(data, buscado)
#     if(posicion > -1):
#         print(buscado, 'esta en la lista en la posicion', posicion)
#     else:
#         print(buscado, 'no esta en la lista')


# buscar(buscado, sw_data)
# buscar(buscado2, sw_data)


#! Mostrar todos los personajes con altura menor a 98 cm

# for character in sw_data:
#     if(character['height'].isdecimal()):
#         if(int(character['height']) < 98):
#             print(character['name'], character['height'])

#! Mostrar todos los personajes con peso mayor a 100 kilos

# for character in sw_data:
#     if(character['mass'].isdecimal()):
#         if(int(character['mass']) > 100):
#             print(character['name'], character['mass'])

#! Mostrar todos los personajes del planeta natal Tatooine y Coruscant

tatooine = ["Tatooine", "http://swapi.dev/api/planets/1/"]
coruscant = ["Coruscant", "http://swapi.dev/api/planets/9/"]

for character in sw_data:
    if(character['homeworld'] == tatooine[1] or character['homeworld'] == coruscant[1]):
        if(character['homeworld'] == tatooine[1]):
            print(character['name'], "pertenece a", tatooine[0])
        else:
            print(character['name'], "pertenece a", coruscant[0])


#! Mostrar todos los personajes de especie Kaleesh y Kaminoan


#! Mostrar toda la informacion del planeta Coruscant y Kamino
#! Mostrar toda la informacion de las naves usadas por Luke Skywalker
#! Mostarr toda las peliculas en las que aparecio R2-D2
#! Mostrar el resumen de la introduccion (opening_crawl) del episodio 4 "A New Hope"
