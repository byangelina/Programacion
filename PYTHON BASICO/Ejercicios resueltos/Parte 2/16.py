monto = float(input("Ingrese el monto total de la compra: "))

if monto > 500000:
    propio = monto * 0.55
    banco = monto * 0.30
    credito = monto - propio - banco
else:
    propio = monto * 0.70
    banco = 0
    credito = monto - propio

interes = credito * 0.20

print(f"Inversión propia: ${propio:.2f}")
print(f"Préstamo del banco: ${banco:.2f}")
print(f"Crédito al fabricante: ${credito:.2f}")
print(f"Intereses sobre crédito: ${interes:.2f}")
