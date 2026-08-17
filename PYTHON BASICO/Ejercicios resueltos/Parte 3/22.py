suma = 0

for i in range(1, 6):
    n = float(input(f"Ingrese el número {i}: "))
    suma += n

promedio = suma / 5
print(f"El promedio de los 5 números es: {promedio:.2f}")
