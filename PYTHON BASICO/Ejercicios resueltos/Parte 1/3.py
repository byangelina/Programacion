neto = float(input("Neto de la factura: "))
iva = neto * 0.19  # cambia 0.19 si tu consigna usa otra tasa
total = neto + iva
print(f"IVA: {iva:.2f}")
print(f"TOTAL: {total:.2f}")
