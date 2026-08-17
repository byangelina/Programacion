horas = int(input("Ingrese la cantidad de horas trabajadas: "))

if horas <= 40:
    salario = horas * 16
else:
    extras = horas - 40
    salario = (40 * 16) + (extras * 20)

print(f"Salario semanal: ${salario:.2f}")
