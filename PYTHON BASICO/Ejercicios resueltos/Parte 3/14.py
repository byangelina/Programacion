pares = 0
impares = 0

for i in range(1, 11):
    n = int(input(f"Ingrese el número {i}: "))
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
