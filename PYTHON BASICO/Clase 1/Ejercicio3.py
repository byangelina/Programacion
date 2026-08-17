"""
Desarrolle un programa que permita usar un numero y despliegue por pantalla si un numero es
perfecto.
"""

# desarrollo

numero = int(input("Ingrese un número: "))
suma_divisores = 0

for i in range(1, numero): 
    if numero % i == 0:
        suma_divisores += i

if suma_divisores == numero:
    print(f"{numero} es un número perfecto.")
else:
    print(f"{numero} no es un número perfecto.")
