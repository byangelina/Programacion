# ejercicio casa:

# realice un programa que le pida al usuario que le solicite al usuario cuantos numero primos
# desea desplegar por pantalla # el sistema desplegara la cantidad partiendo por el numero 1

# la funcion se debe llamar cantidadPrimos(c) recibe un argumento c y retorna un String:
# def cantidadPrimos(c) # return string


def esPrimo(n):
    contarDivisores = 0
    for x in range(1, n + 1, 1):
        if n % x == 0:
            contarDivisores = contarDivisores + 1

    if contarDivisores == 2:
        return True
    else:
        return False

def cantidadPrimos(c):
    contador = 0    
    numero = 1       
    string = ""  

    while contador < c:
        if esPrimo(numero):
            string += str(numero) + " "
            contador += 1
        numero += 1
    return string


inputCantidadPrimos = int(input("\nIngrese cuántos números primos desea desplegar por pantalla: "))
resultado = cantidadPrimos(inputCantidadPrimos)
print(resultado," \n")