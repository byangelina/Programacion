n = int(input("Ingrese la cantidad de personas: "))

hombres = 0
mujeres = 0

for i in range(1, n + 1):
    sexo = input(f"Ingrese el sexo de la persona {i} (H/M): ").upper()
    if sexo == "H":
        hombres += 1
    elif sexo == "M":
        mujeres += 1
    else:
        print("Valor inválido, no se contabiliza.")

print(f"Hombres: {hombres}")
print(f"Mujeres: {mujeres}")
