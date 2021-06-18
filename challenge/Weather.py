import json
import requests
from simple_term_menu import TerminalMenu
import pandas as pd

url_base = 'https://api.openweathermap.org/data/2.5/'
api_key = '4d66756d2f1463d481841de10d882e5a'


def get_data(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_weather(city, lat=None, lon=None):
    if(lat and lon != None):
        ruta = url_base + 'weather' + '?lat=' + lat + '&lon=' + \
            lon + '&lang=es&units=metric&appid=' + api_key
    else:
        ruta = url_base + 'weather' + '?q=' + city + \
            '&lang=es&units=metric&appid=' + api_key
    weather = get_data(ruta)
    info = {
        'Ciudad': weather['name'],
        'Descripcion': weather['weather'][0]['description'],
        'Sensacion termica': str(weather['main']['feels_like']),
        'Temperatura': str(weather['main']['temp']),
        'Humedad': str(weather['main']['humidity']),
    }
    return info


def show_weather(weather):
    for item in weather:
        print(item + ': ' + weather[item])


def get_forecast(city, lat=None, lon=None):
    if(lat and lon != None):
        ruta = url_base+'forecast' + '?lat=' + lat + '&lon=' + \
            lon + '&lang=es&units=metric&cnt=10&appid=' + api_key
    else:
        ruta = url_base + 'forecast' + '?q=' + city + \
            '&lang=es&units=metric&cnt=10&appid=' + api_key
    forecast = get_data(ruta)
    return forecast


def show_forecast(forecast):
    for item in forecast['list']:
        time = item['dt_txt']
        date = time.split(' ')
        day = pd.Timestamp(str(date[0]))
        temperature_min = item['main']['temp_min']
        temperature_max = item['main']['temp_max']
        feels_like = item['main']['feels_like']
        description = item['weather'][0]['description']
        humidity = item['main']['humidity']
        pressure = item['main']['pressure']
        print()
        print(day.day_name(), date[1])
        print('Clima: %s' % description)
        print('Sensacion termica: %s' % feels_like)
        print('Temperatura minima: %s' % temperature_min)
        print('Temperatura maxima: %s' % temperature_max)
        print('Humedad: %s' % humidity)
        print('Presion: %s' % pressure)


def main():
    main_menu_exit = False
    while not main_menu_exit:
        print('Seleccione una opcion: ')
        terminal_menu = TerminalMenu(
            ["Clima por ciudad", "Clima por coordenadas", "Pronostico por ciudad", "Pronostico por coordenadas", 'Salir'])
        menu_entry_index = terminal_menu.show()
        if(menu_entry_index == 0):
            city = input(str("Ingrese ciudad: "))
            data = get_weather(city)
            show_weather(data)
            print()
            input("Presione ENTER para volver al menu")
        elif(menu_entry_index == 1):
            lat = input("Ingrese latitud: ")
            lon = input("Ingrese longitud: ")
            data = get_weather(None, lat, lon)
            show_weather(data)
            print()
            input("Presione ENTER para volver al menu")
        elif(menu_entry_index == 2):
            city = input(str("Ingrese ciudad: "))
            data = get_forecast(city)
            show_forecast(data)
            print()
            input("Presione ENTER para volver al menu")
        elif(menu_entry_index == 3):
            lat = input("Ingrese latitud: ")
            lon = input("Ingrese longitud: ")
            data = get_forecast(None, lat, lon)
            show_forecast(data)
            print()
            input("Presione ENTER para volver al menu")
        elif(menu_entry_index == 4):
            main_menu_exit = True
            print("Saliendo")


if __name__ == "__main__":
    main()
