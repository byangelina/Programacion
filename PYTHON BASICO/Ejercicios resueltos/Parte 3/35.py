print("Números impares menores que 100:")

for n in range(1, 100):
    if n % 2 != 0:
        print(n, end=" ")

# Alternativa más eficiente:
# for n in range(1, 100, 2):
#     print(n, end=" ")
