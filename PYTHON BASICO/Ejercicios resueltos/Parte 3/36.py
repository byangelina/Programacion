n = int(input("Ingrese la cantidad de números naturales: "))

suma = 0
for i in range(1, n + 1):
    print(i, end=" ")
    suma += i

print(f"\nLa sumatoria de 1 a {n} es: {suma}")
