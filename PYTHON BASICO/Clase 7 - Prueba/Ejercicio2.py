"""
Desarrolle un programa que ingrese elementos según la siguiente secuencia hasta el 10.
1	2	2	3	3	3	4	4	4	4	5	5	5	5	5	….

"""

num = 0 # parte desde 0
numero = int(input("\nIngrese un número: "))

for i in range (1,numero+1):
    linea = ""

    for repetido in range(numero,):
        linea += str(repetido)
    print(linea)

