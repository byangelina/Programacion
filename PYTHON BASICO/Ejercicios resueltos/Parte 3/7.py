n = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):
    producto = n * i
    print(f"{n} x {i} = {producto}")
