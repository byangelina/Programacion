frase = input("Ingrese una frase: ")
palabras = frase.split()  # separar en lista de palabras

# invertir manualmente recorriendo desde el último al primero
inversa = []
for i in range(len(palabras)-1, -1, -1):
    inversa.append(palabras[i])

print(" ".join(inversa))
