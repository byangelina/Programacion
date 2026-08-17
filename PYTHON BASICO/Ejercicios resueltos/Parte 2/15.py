cantidad = int(input("Ingrese la cantidad de camisas: "))
precio_unitario = float(input("Ingrese el precio unitario de la camisa: "))

total = cantidad * precio_unitario

if cantidad >= 3:
    descuento = total * 0.20
else:
    descuento = total * 0.10

pago = total - descuento

print(f"Total sin descuento: {total:.2f}")
print(f"Descuento aplicado: {descuento:.2f}")
print(f"Total a pagar: {pago:.2f}")
   