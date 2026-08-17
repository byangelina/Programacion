positivos = 0
negativos = 0
neutros = 0

for i in range(1, 21):
    n = float(input(f"Ingrese el número {i}: "))
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
    else:
        neutros += 1

print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Neutros: {neutros}")
