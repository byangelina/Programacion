# Crear un programa que al leer un número entero positivo
# (asuma que el número cumple las condiciones)
# imprimir PAR si el número es par e IMPAR si es impar. 


print("\nBienvenido, este programa es para revisar si tu número entero positivo es par o impar\n")

num_entero = int(input("Ingrese un número entero positivo: "))

if num_entero % 2 == 0:
    print(f"El número {num_entero} es par.")

else:
    print(f"El número {num_entero} es impar.")


print("\nPrograma finalizado.")


