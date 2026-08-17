suma_negativos = 0

for i in range(1, 11):
    n = float(input(f"Ingrese el número {i}: "))
    if n < 0:
        suma_negativos += n

print(f"La suma de los números negativos es: {suma_negativos}")
