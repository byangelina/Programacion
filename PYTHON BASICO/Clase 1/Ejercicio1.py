"""
Desarrolle un programa que permita ingresar 10 numeros y despliegue el mayor.

Restriccion: no puede usar listas, funcion max, no chatgpt.
"""

# Pedimos el primer número antes del bucle para tener un valor inicial válido
num = int(input("Ingrese un número: "))

for i in range(9):  # ya pedimos 1, faltan 9
    numero_ingresado = int(input("Ingrese un número: "))   
    if numero_ingresado > num:
        num = numero_ingresado

print(f"El número mayor es: {num}")
