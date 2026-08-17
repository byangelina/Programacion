
"""
Desarrolle un programa que permita ingresar una frase y la despliegue de forma inversa
No usar método reverse.
Por ej. 

Ingrese frase : programar es muy fácil
Fácil muy es programar

"""

frase = "programar es muy fácil"
palabras_invertidas = " ".join(frase.split()[::-1])
print(palabras_invertidas)
