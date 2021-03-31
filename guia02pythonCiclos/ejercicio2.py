"""
Dada una lista de 15 personas de las que se conoce nombre y edad, determinar cuántas
son mayores de edad.
"""
personas = {
    "Juan Pablo": 27,
    "Marcos": 45,
    "Jose": 10,
    "Lisandro": 8,
    "Yohana": 29,
    "Marcela": 39,
    "Zaira": 12,
    "Julian": 16,
    "Julio": 68,
    "Stella": 18,
    "Antonio": 7,
    "Luna": 23,
    "Alfredo": 40,
    "Luana": 17,
    "Nilda": 3
}

mayores = 0

for persona, edad in personas.items():
    if(edad >= 18):
        mayores += 1

print("Cantidad de personas mayores:", mayores)
