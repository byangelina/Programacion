notas = []

# ingreso de notas válidas (1 a 7)
for i in range(10):
    while True:
        nota = int(input(f"Ingrese la nota {i+1} (1 a 7): "))
        if 1 <= nota <= 7:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Debe estar entre 1 y 7.")

# calcular promedio
promedio = sum(notas) / len(notas)

# filtrar notas bajo el promedio
notas_filtradas = [n for n in notas if n >= promedio]

print(f"Promedio: {promedio:.2f}")
print("Notas finales (>= promedio):", notas_filtradas)
