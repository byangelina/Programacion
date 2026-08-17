n = int(input("Ingrese un número: "))

suma = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    suma += factorial

print(f"La suma de factoriales de 1 a {n} es: {suma}")
