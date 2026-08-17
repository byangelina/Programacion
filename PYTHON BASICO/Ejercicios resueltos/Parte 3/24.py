suma_pares = 0

for i in range(1, 11):
    n = int(input(f"Ingrese el número {i}: "))
    if n % 2 == 0:
        suma_pares += n

print(f"La suma de los números pares es: {suma_pares}")
