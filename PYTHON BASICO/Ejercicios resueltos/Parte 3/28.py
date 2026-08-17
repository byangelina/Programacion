n = float(input("Ingrese el número 1: "))
mayor = n
menor = n

for i in range(2, 11):
    n = float(input(f"Ingrese el número {i}: "))
    if n > mayor:
        mayor = n
    elif n < menor:
        menor = n

print(f"El mayor número es: {mayor}")
print(f"El menor número es: {menor}")
