h = int(input("Ingrese la cantidad de hombres: "))
m = int(input("Ingrese la cantidad de mujeres: "))

total = h + m
porc_h = (h / total) * 100
porc_m = (m / total) * 100

print(f"Porcentaje de hombres: {porc_h:.2f}%")
print(f"Porcentaje de mujeres: {porc_m:.2f}%")
