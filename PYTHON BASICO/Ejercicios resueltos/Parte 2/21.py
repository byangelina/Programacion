total = float(input("Ingrese el total de la compra: "))
color = input("Ingrese el color de la bolita (blanco, verde, amarillo, azul, rojo): ").lower()

if color == "blanco":
    porc = 0
elif color == "verde":
    porc = 0.10
elif color == "amarillo":
    porc = 0.25
elif color == "azul":
    porc = 0.50
elif color == "rojo":
    porc = 1.00
else:
    porc = 0
    print("Color inválido, no se aplica descuento.")

descuento = total * porc
pago = total - descuento

print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${pago:.2f}")
