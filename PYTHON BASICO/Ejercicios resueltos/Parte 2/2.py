sueldo_base = float(input("Ingrese el sueldo base: "))
venta1 = float(input("Ingrese el valor de la venta 1: "))
venta2 = float(input("Ingrese el valor de la venta 2: "))
venta3 = float(input("Ingrese el valor de la venta 3: "))

suma_ventas = venta1 + venta2 + venta3
comisiones = suma_ventas * 0.10
total = sueldo_base + comisiones

print(f"Comisiones: {comisiones:.2f}")
print(f"Total recibido en el mes: {total:.2f}")
