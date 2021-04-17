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
