
# funcion para saber si un número es par o impar
# desarrollo profe

def es_par(n):
    return n % 2 == 0

num = int(input("Ing. número :"))

if not es_par(num):
    print("Grabar en base datos")

else:
    print("Enviar correo al usuario que no es par")


