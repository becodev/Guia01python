from math import factorial, sqrt
from random import randint
import string
# 1. Desarrollar un algoritmo que permita sumar dos numeros.


def suma(num1, num2):
    return num1 + num2


# 2. Desarrollar un algoritmo que determine si un número es positivo o negativo.

def positivo_negativo(num):
    if(num > 0):
        return True
    else:
        return False


# 3. Desarrollar un algoritmo para calcular el área de un rectángulo.

def areaRectangulo(base, altura):
    return base*altura


# 4. Desarrollar un algoritmo que dado un carácter y una palabra devuelva cuantas veces esta
# dicho carácter en la palabra.

def caracterRepetido(palabra, caracter):
    cont = 0
    for i in range(0, len(palabra)):
        if(palabra[i] == caracter):
            cont += 1
    return cont

# 5. Desarrollar un algoritmo que determine si una palabra es un palíndromo.


def palindromo(palabra):
    pal = list(palabra)
    pal.reverse()
    aux = ''
    aux = aux.join(pal)
    if(palabra == aux):
        return True
    else:
        return False

# 6 Desarrollar un algoritmo que permita calcular la siguiente serie: ...


def serie(n):
    cuenta = 0

    for i in range(1, n+1):
        cuenta = 1 + 1/i

    return cuenta


# 7 Desarrollar un algoritmo que simule una calculadora donde se le da como entrada dos
# números y el tipo de operación y esta devuelve el resultado.

def calculadora(num1, num2, opt):
    if(opt == '+'):
        return num1 + num2
    elif(opt == '-'):
        return num1 - num2
    elif(opt == '*'):
        return num1 * num2
    elif(opt == '/'):
        return num1 / num2
    elif(opt == '**'):
        return num1 ** num2


# 8. Desarrollar un algoritmo que determine si un número entero es primo o no.
def esPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True


# 9. Desarrollar un algoritmo que determine si un carácter es una vocal.
def esVocal(letra):
    if(letra in ['a', 'e', 'i', 'o', 'u']):
        return True
    return False


# 10. Desarrollar un algoritmo que dados dos números determine el valor del mayor.
def mayor(num1, num2):
    if(num1 > num2):
        return num1
    return num2


# 11. Desarrollar un algoritmo que permita intercambiar el valor de dos variables.
def intercambio(a, b):
    x = a
    a = b
    b = x
    return a, b


# 12 Desarrollar un algoritmo que permita generar un número aleatorio entre dos números dados.
def numeroAleatorio(primero, segundo):
    return randint(primero, segundo)


# 13. Desarrollar un algoritmo para calcular el factorial de un número.
def factorial(n):
    factor = 1
    while n > 1:
        factor *= n
        n -= 1
    return factor


# 14. Desarrollar un algoritmo que permita calcular las dos raíces de una ecuación de segundo
# grado en el caso de que sea posible.


# 15. Desarrollar un algoritmo para calcular la hipotenusa de un triángulo rectángulo.
def hipotenusa(cateto1, cateto2):
    return sqrt(cateto1 ** 2 + cateto2 ** 2)


# 16. Desarrollar un algoritmo que permita visualizar las letras del alfabeto.
def alfabeto():
    return list(string.ascii_lowercase)


# 17. Desarrollar un algoritmo que permita visualizar la tabla de multiplicar tradicional de un
# determinado número.
def tabla(base):
    for i in range(1, 11):
        multiplicacion = str(i * base)
        print(str(i) + ' * ' + str(base) + ' = ' + multiplicacion)


# 18. Desarrollar un algoritmo que pasar un valor dado de horas a segundo o de segundo a
# horas, dependiendo de un parámetro carácter H y S respectivamente.
def conversorTiempo(tiempo, unidad):
    if(unidad.upper() == 'H'):
        return tiempo * 60 * 60
    elif(unidad.upper() == 'S'):
        return round((tiempo / 60) / 60, 2)


# 19. Desarrollar un algoritmo que permita resolver una regla de tres simple, la cual recibirá los
# tres valores requeridos para calcular la misma.

def reglaTres(magnitud, proporcionX, proporcion):
    """ calcula la regla de tres simple, parametros: magnitud, proporcionX, proporcion"""
    return (magnitud * proporcionX / proporcion)


# 20. Desarrollar un algoritmo que permita sumar los números primos comprendidos entre dos
# números dados.

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def sumaPrimos(inicio, fin):
    suma = 0
    for i in range(inicio, fin):
        if esPrimo(i) == True:
            suma += i
    return suma
