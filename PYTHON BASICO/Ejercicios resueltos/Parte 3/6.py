suma = 0
menor = 999

for i in range(1, 41):
    c = float(input(f"Ingrese la calificación del alumno {i}: "))
    suma += c
    if c < menor:
        menor = c

media = suma / 40

print(f"Calificación media: {media:.2f}")
print(f"Calificación más baja: {menor}")
