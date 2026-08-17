P = float(input("Precio base del producto: "))
P_feb = P * 1.003
P_mar = P * 1.006
dif   = P_mar - P_feb
print(f"Valor en Febrero: {P_feb:.2f}")
print(f"Valor en Marzo:   {P_mar:.2f}")
print(f"Diferencia (Mar - Feb): {dif:.2f}")
