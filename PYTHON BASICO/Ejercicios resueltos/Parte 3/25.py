suma_impares = 0

for i in range(1, 11):
    n = int(input(f"Ingrese el número {i}: "))
    if n % 2 != 0:
        suma_impares += n

print(f"La suma de los números impares es: {suma_impares}")
