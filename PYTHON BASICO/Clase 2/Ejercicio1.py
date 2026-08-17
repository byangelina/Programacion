
# primer ejercicio / desarrollo profe

print("Programa para seleccionar el número mayor de varios números\n")

numero_mayor = 0
primer_numero = True

while True:
    numero_input = int(input("Ingrese un número (0 para terminar): "))
    
    if numero_input == 0:
        break

    if primer_numero:
        numero_mayor = numero_input
        primer_numero = False

    else:
        if numero_input > numero_mayor:
            numero_mayor = numero_input


print(f"\nEl número mayor ingresado es: {numero_mayor}\n")


