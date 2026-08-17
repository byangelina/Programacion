n = int(input("Ingrese la cantidad de números: "))

suma = 0
for i in range(1, n + 1):
    x = float(input(f"Ingrese el número {i}: "))
    suma += x

promedio = suma / n
print(f"El promedio de los {n} números es: {promedio:.2f}")
