capital = float(input("Ingrese el capital invertido: "))
tasa = float(input("Ingrese la tasa de interés (ej: 0.05 para 5%): "))

interes = capital * tasa

if interes > 7000:
    total = capital + interes
    print(f"Interés generado: {interes:.2f}")
    print(f"Total en cuenta: {total:.2f}")
else:
    print(f"Interés generado: {interes:.2f}")
