base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))

resultado = 1
for i in range(1, exponente + 1):
    resultado *= base

print(f"{base} elevado a la {exponente} es: {resultado}")
