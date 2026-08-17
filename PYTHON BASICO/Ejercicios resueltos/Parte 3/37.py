n = int(input("Ingrese la cantidad de números: "))

positivos = 0
negativos = 0
neutros = 0

for i in range(1, n + 1):
    x = float(input(f"Ingrese el número {i}: "))
    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1
    else:
        neutros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")
