n = int(input("Ingrese un número para ver su tabla de multiplicar hasta el 12: "))

for i in range(1, 13):
    producto = n * i
    print(f"{n} x {i} = {producto}")
