suma_positivos = 0

for i in range(1, 11):
    n = float(input(f"Ingrese el número {i}: "))
    if n > 0:
        suma_positivos += n

print(f"La suma de los números positivos es: {suma_positivos}")
