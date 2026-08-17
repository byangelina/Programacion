

saludo = "Hola" # Guardamos la palabra "Hola" en una variable llamada saludo

print("1er caracter de la variable String saludo -> ", saludo[0]) # Accedemos al primer carácter de la palabra (posición 0) e imprimimos "H"

# Calculamos la posición del último carácter: len(saludo) nos da 4, 4-1 = 3
# Luego accedemos a esa posición (saludo[3]) que es "a" y lo guardamos en una variable
ultimoCaracter = saludo[len(saludo) - 1]
print("Último caracter de la variable String saludo -> ", ultimoCaracter)

print("1er caracter es número -> ", saludo[0].isnumeric())# Verificamos si el primer carácter "H" es un número (False = no es número)
print("1er caracter es letra -> ", saludo[0].isalpha())# Verificamos si el primer carácter "H" es una letra (True = sí es letra)
print("1er caracter es alfanumérico -> ", saludo[0].isalnum())# Verificamos si el primer carácter "H" es alfanumérico, es decir, letra o número (True)
print("1er caracter es mayúscula -> ", saludo[0].isupper())# Verificamos si el primer carácter "H" es mayúscula (True = sí es mayúscula)
print("1er caracter es minúscula -> ", saludo[0].islower())# Verificamos si el primer carácter "H" es minúscula (False = no es minúscula)
print("1er caracter es espacio -> ", saludo[0].isspace())# Verificamos si el primer carácter "H" es un espacio en blanco (False = no es espacio)
print("1er caracter es decimal -> ", saludo[0].isdecimal())# Verificamos si el primer carácter "H" es un número decimal (False = no es decimal)

subString = saludo[1:3] # Extraemos una parte del texto: desde la posición 1 hasta antes de la posición 3
print("SubString de la variable saludo -> ", subString) # Esto nos da los caracteres "o" y "l", formando el substring "ol"

# Creamos un bucle que recorre el texto al revés
for i in range(len(saludo) - 1, -1, -1): # range(len(saludo) - 1, -1, -1) significa: empieza en 3, ve hasta -1 (sin incluir), disminuyendo de 1 en 1
    # Es decir: 3, 2, 1, 0
    print("Caracter", i, "de la variable saludo -> ", saludo[i]) # En cada vuelta, imprimimos el carácter en la posición "i"


"""
Impresión en pantalla:

1er caracter de la variable String saludo ->  H
Último caracter de la variable String saludo ->  a

1er caracter es número ->  False
1er caracter es letra ->  True
1er caracter es alfanumérico ->  True
1er caracter es mayúscula ->  True
1er caracter es minúscula ->  False
1er caracter es espacio ->  False
1er caracter es decimal ->  False

SubString de la variable saludo ->  ol
Caracter 3 de la variable saludo ->  a
Caracter 2 de la variable saludo ->  l
Caracter 1 de la variable saludo ->  o
Caracter 0 de la variable saludo ->  H
"""


"""
Explicacion del código:

Este código trabaja con la palabra "Hola" guardada en una variable llamada saludo,
y demuestra varias cosas que puedes hacer con texto en Python. Primero, extrae el
primer carácter usando saludo[0] (que es "H") y el último usando len(saludo) - 1 (que es "a")

luego realiza pruebas sobre el primer carácter para verificar si es un número,
una letra, mayúscula, minúscula, espacio o decimal—todas estas pruebas devuelven
verdadero o falso. 

Después, extrae un "trozo" de texto llamado substring
usando saludo[1:3] (que toma los caracteres desde la posición 1 hasta la 2,
resultando en "ol"), y finalmente utiliza un bucle for que recorre todos los
caracteres de la palabra en orden inverso, imprimiendo cada uno en pantalla.

En resumen: el código muestra cómo acceder a caracteres individuales de un texto,
cómo verificar qué tipo de carácter es, cómo extraer partes del texto y cómo
recorrer el texto hacia atrás.

"""