suma = 0

for i in range(1, 16):
    c = float(input(f"Ingrese la calificación del alumno {i}: "))
    suma += c

promedio = suma / 15
print(f"Promedio del grupo: {promedio:.2f}")
