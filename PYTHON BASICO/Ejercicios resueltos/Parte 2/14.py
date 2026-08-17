nombre = input("Ingrese el nombre del artículo: ")
clave = input("Ingrese la clave (01 o 02): ")
precio = float(input("Ingrese el precio original: "))

if clave == "01":
    descuento = precio * 0.10
elif clave == "02":
    descuento = precio * 0.20
else:
    descuento = 0
    print("Clave inválida, no se aplica descuento.")

precio_final = precio - descuento

print(f"Artículo: {nombre}")
print(f"Clave: {clave}")
print(f"Precio original: {precio:.2f}")
print(f"Precio con descuento: {precio_final:.2f}")
