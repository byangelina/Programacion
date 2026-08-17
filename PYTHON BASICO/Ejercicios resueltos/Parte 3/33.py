print("Múltiplos de 5 menores que 100:")

for n in range(1, 100):
    if n % 5 == 0:
        print(n, end=" ")

# Alternativa más eficiente:
# for n in range(5, 100, 5):
#     print(n, end=" ")
