
# cómo usar listas. se escriben así:
# nombre_lista ["dato1","dato2","dato3"]


lista=["uno", "dos", "tres"]
# para verlo en consola, poner un print y el nombre de la lista.
# despues [ ] y adentro la posicion del dato que guarda la lista, siempre va de 0 a mas...

print("\naqui '" "' puede haber cualquier mensaje antes de llamar al dato de la lista.",lista[0])

# el orden de los datos en las listas es asi:
# 0 = dato1
# 1 = dato2
# 2 = dato3...
# y si imprimo -1 me toma el ultimo numero, si imprimo -2, es el penultimo numero...

# estas son otras formas de imprimir varios datos 
print("aqui estoy imprimiendo el ultimo dato, si es negativo el orden es al reves",lista[-1])
print("aqui estoy imprimiendo mi lista desde el 1 al 4, pero si no hay 4, se imprime hasta 3",lista[1:4]) 
print("aqui esoty imprimiendo la lista completa",lista[:])
print("aqui estoy imprimiendo desde el 2 en adelante",lista[2:])
print("aqui estoy imprimiendo desde el inicio hasta el 2",lista[:2])

print("\nfin del programa\n")


# importante, las listas son modificables, puedes agregar mas datos, editarlos, eliminarlos, usar apppend para agregarlos al final, etc.
# Las tuplas no son modificables, no puedes borrar datos, actualizar datos, te quedas con los datos que fueron definidos.