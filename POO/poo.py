

#! Programacion orientada a objetos.

class Persona():
    """clase que representa a una persona """

    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def mostrar_datos(self):
        print(self.__apellido, self.__nombre)


persona1 = Persona("juan", 'loureyro')


persona1.mostrar_datos()
