a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

print(f"El mayor es: {mayor}")
