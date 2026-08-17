
# Supongamos que el I.P.C. de los meses de Febrero y Marzo fueron 0.3% y 0.6%
# respectivamente.

# Crear un progrma que muestre el valor de un producto actualizado
# y la diferencia de precio entre el mes de febrero y Marzo. 


# cómo se calcula el IPC: Calcula el IPC dividiendo el precio de la cesta en un año determinado entre el precio de la misma cesta en el año base. 

print("\nConsulte el valor de un producto y vea su evolucion de precio entre los meses enero y febrero\n")

producto = [["platano",1400], ["manzana",1200], ["limón",990]]


for numero, (nombre, precio) in enumerate(producto, start=1):
    print(f"{numero}. {nombre}: ${precio}")

eleccion_producto = input("\nElija el número del producto que desea consultar: ")


if eleccion_producto == "1":
    

    print("")



elif eleccion_producto == ""2":

    print("b")



else:
    print("c")







