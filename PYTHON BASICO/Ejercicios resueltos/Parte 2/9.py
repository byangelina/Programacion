compra = float(input("Ingrese el monto de la compra: "))

if compra > 1000:
    descuento = compra * 0.20
    total = compra - descuento
else:
    total = compra

print(f"Total a pagar: {total:.2f}")
