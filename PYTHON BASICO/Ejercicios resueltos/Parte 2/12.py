a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if a < b:
    print(f"{a}, {b}")
elif b < a:
    print(f"{b}, {a}")
else:
    print("IGUALES")
