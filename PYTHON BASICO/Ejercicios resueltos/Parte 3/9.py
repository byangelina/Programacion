n = int(input("Ingrese el número de vendedores: "))

for i in range(1, n + 1):
    print(f"\n--- Vendedor {i} ---")
    sueldo_base = float(input("Ingrese el sueldo base: "))
    venta1 = float(input("Ingrese el monto de la venta 1: "))
    venta2 = float(input("Ingrese el monto de la venta 2: "))
    venta3 = float(input("Ingrese el monto de la venta 3: "))

    suma = venta1 + venta2 + venta3
    comisiones = suma * 0.10
    total = sueldo_base + comisiones

    print(f"Comisiones: {comisiones:.2f}")
    print(f"Total semanal: {total:.2f}")
