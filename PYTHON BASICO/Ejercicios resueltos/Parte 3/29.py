
n = int(input("Ingrese la cantidad de calificaciones: "))

calificacion = float(input("Ingrese la calificación 1: "))
suma = calificacion
mayor = calificacion
menor = calificacion

for i in range(2, n + 1):
    calificacion = float(input(f"Ingrese la calificación {i}: "))
    suma += calificacion
    if calificacion > mayor:
        mayor = calificacion
    elif calificacion < menor:
        menor = calificacion

promedio = suma / n

print(f"Promedio del grupo: {promedio:.2f}")
print(f"Calificación mayor: {mayor}")
print(f"Calificación menor: {menor}")
