a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

if a == b:
    resultado = a * b
elif a > b:
    resultado = a - b
else:
    resultado = a + b

print(f"Resultado: {resultado}")
