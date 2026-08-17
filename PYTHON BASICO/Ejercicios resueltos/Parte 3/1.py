suma = 0
for i in range(1, 8):  # del 1 al 7
    calificacion = float(input(f"Ingrese la calificación {i}: "))
    suma += calificacion

promedio = suma / 7
print(f"Promedio: {promedio:.2f}")
