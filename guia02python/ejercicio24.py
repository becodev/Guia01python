"""
Dado un número que indica el día de la semana mostrar que día es, considerando que el
día uno es Domingo.
"""

numero = int(input("Ingrese numero para dia de la semana: "))

if(numero not in [1, 2, 3, 4, 5, 6, 7]):
    print("Numero incorrecto. Error fatal!")
else:
    dias = {1: "Domingo", 2: "Lunes", 3: "Martes",
            4: "Miercoles", 5: "Jueves", 6: "Viernes", 7: "Sabado"}

    print("-----------------------------------------------")
    print("El numero ingresado corresponde al dia: ", dias[numero])
    print("-----------------------------------------------")
