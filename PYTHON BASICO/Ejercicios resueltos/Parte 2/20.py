salario = float(input("Ingrese el salario mensual: "))
anios = float(input("Ingrese los años de antigüedad: "))

if anios < 1:
    porc = 0.05
elif anios < 2:
    porc = 0.07
elif anios < 5:
    porc = 0.10
elif anios < 10:
    porc = 0.15
else:
    porc = 0.20

utilidad = salario * porc

print(f"Porcentaje de utilidad: {porc*100:.0f}%")
print(f"Utilidad anual: ${utilidad:.2f}")
