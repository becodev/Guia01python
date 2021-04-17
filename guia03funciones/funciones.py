"""1. Desarrollar un algoritmo que permita sumar dos numeros."""


def suma(num1, num2):
    return num1 + num2


"""2. Desarrollar un algoritmo que determine si un número es positivo o negativo."""


def positivo_negativo(num):
    if(num > 0):
        return True
    else:
        return False


"""3. Desarrollar un algoritmo para calcular el área de un rectángulo."""


def areaRectangulo(base, altura):
    return base*altura


"""4. Desarrollar un algoritmo que dado un carácter y una palabra devuelva cuantas veces esta
dicho carácter en la palabra."""


def caracterRepetido(palabra, caracter):
    cont = 0
    for i in range(0, len(palabra)):
        if(palabra[i] == caracter):
            cont += 1
    return cont
