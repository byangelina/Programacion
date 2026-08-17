positivos = 0
negativos = 0

for i in range(1, 11):
    n = int(input(f"Ingrese el número {i}: "))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
