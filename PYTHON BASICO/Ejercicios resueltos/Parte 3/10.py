n = int(input("Ingrese la cantidad de obreros: "))

for i in range(1, n + 1):
    h = float(input(f"Horas trabajadas del obrero {i}: "))
    if h <= 40:
        salario = h * 20
    else:
        extras = h - 40
        salario = 40 * 20 + extras * 25
    print(f"Obrero {i} → Salario semanal: ${salario:.2f}")
