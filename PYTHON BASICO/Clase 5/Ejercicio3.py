# Definiciones:
# - Los números perfectos son aquellos que son iguales a la suma de sus propios divisores.
# - el número primo es el que solo es divisible por 1 y por si mismo (y mayor a 1).

# cree una funcion para saber si un número es primo
# (dentro de la funcion usar return, no print):

def esPrimo(n):
    contarDivisores = 0
    for x in range(1, n + 1, 1):
        if n % x == 0:
            contarDivisores = contarDivisores + 1

    if contarDivisores == 2:
        return True
    else:
        return False
#_______________________________________________________

numero = int(input("Ing. número :"))
if esPrimo(numero):
    print("primo")
else:
    print("No es primo")
