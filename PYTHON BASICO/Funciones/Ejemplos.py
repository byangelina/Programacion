
# DEFINICIONES Y EJEMPLOS

# ejemplo funciones
"""def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"La suma es: {resultado}")"""


# ejemplo funciones
"""def saludar():
    print("¡Hola! Espero que tengas un gran día.")

saludar()"""


# función con un parámetro
"""def holaConNombre(name):
print("Hello " + name + "!")

holaConNombre("Ada")"""  # llamada a la función, 'Hello Ada!' se muestra en la consola


# Variables Locales: Son aquellas que se declaran dentro de una función y solo pueden ser accedidas dentro de esa función.
"""def mi_funcion():
    x = 10  # Variable local
    print(x)"""


# Variables Globales: Son aquellas que se declaran fuera de cualquier función y pueden ser accedidas desde cualquier parte del programa.
"""y = 20  # Variable global
def otra_funcion():
    print(y)  # Accede a la variable global"""

#------------------------------------------------------------------------------------------------------------------------------------------------------






# programa para saber si un número es par o impar

"""
contador = 0
numero = int(input("\nIngrese un número: "))

flecha = "-->"
for i in range(1,numero+1):

    if i % 2 == 0 :
        print(i,flecha,"par")
    else:
        print(i,flecha,"impar")
    contador =+ numero

print("\nPrograma finalizado.")

"""










