
# programa de un número primo con for:
# desarrollo profe

num = int(input("Ing. número :"))

contarDivisores = 0
for x in range(1, num + 1, 1):
    if num % x == 0:
        contarDivisores = contarDivisores + 1

if contarDivisores == 2:
    print("Primo")
else:
    print("No es primo")






