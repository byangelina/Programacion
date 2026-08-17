

# segundo ejercicio
print("Programa para seleccionar el número mayor de varios números\n")

numero_mayor = 0
x = 1

while x <= 10:
    numero_input = int(input(f"Ingrese un número {x}: ")) # este no tiene break asi que no terminará con 0
    
    if x == 1:
        numero_mayor = numero_input
    else:
        if numero_input > numero_mayor:
            numero_mayor = numero_input

    x = x + 1

print(f"\nEl número mayor es: {numero_mayor}\n")
