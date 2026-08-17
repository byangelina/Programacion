horas = int(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora normal: "))

if horas <= 40:
    salario = horas * tarifa
else:
    extras = horas - 40
    if extras <= 8:
        salario = 40 * tarifa + extras * tarifa * 2
    else:
        salario = 40 * tarifa + 8 * tarifa * 2 + (extras - 8) * tarifa * 3

print(f"Salario semanal: ${salario:.2f}")
