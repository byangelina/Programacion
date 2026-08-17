minutos = int(input("Ingrese el tiempo en minutos: "))
actividad = int(input("Ingrese la actividad (1 = dormir, 2 = reposo sentado): "))

if actividad == 1:
    calorias = minutos * 1.08
elif actividad == 2:
    calorias = minutos * 1.66
else:
    calorias = 0
    print("Actividad no válida.")

print(f"Calorías consumidas: {calorias:.2f}")
