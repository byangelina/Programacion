
# creando una funcion desde cero:

def saludar(nombre):
    print("mi nombre es " + nombre)
    return

input_nombre = input("Ingresa tu nombre: ")

saludar(input_nombre)

"""
la funcion saludar(input_nombre) esta procesando el desarrollo de su funcion (que va adentro):

    print("mi nombre es " + nombre)
    return

y al mismo tiempo esta imprimiendo input_nombre al final,
por eso el resultado final es: 

Ingresa tu nombre:
mi nombre es: angela

la variable "nombre" es un parámetro. significa que está guardando un valor que se le asignará después


cuando creamos la funcion
    def saludar(nombre):        

aqui agregamos el parámetro "nombre" a la funcion saludar.


cuando le damos un valor a parámetro de la función
    saludar("Ana")

aqui se esta imprimiendo la función con el parámetro "nombre que estaba vació, ahora el parámetro,
guarda el valor de "Ana"


"""