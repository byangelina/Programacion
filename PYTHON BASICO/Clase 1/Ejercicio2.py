"""
desarrolle un programa que solicite un numero al usuario y despliegue la siguiente serie.

Ejemplo: el usuario ingresa un "10".
1
12
123
1234
12345
"""

# desarrollo

numero_ingresado = int(input("Ingrese un número: "))
num = 0 # parte desde 0

for i in range (1, numero_ingresado + 1):
    linea = ""

    for piramide in range(1, i + 1):
        linea += str(piramide)
    print(linea)




