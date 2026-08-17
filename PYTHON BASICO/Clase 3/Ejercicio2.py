
# ejercicio en casa

"""
Determinar sueldo de un empleado:

La empresa Sitomanboy necesita determinar el sueldo de un empleado, 
considerando que el valor hora normal es $6.000.- Pesos, la hora extra es un 
50% mas que la hora normal, existe una cuota del sindicato que depende del 
sueldo, si es mayor a de 400 Mil se descuenta un 2% del sueldo, de lo contrario 
un valor fijo es de $3.000 Pesos.
Desarrolle el programa que determine el sueldo total de un empleado
"""

# si el empleado gana sobre 400 mil, su hora normal cuesta 6.000 y su hora extra es 6000 + 50% - 2% de su sueldo.
# si el empleado gana bajo 400 mil, su hora extra cuesta 3.000.

# - s_ingreasdo  = sueldo ingresado 
# - h_trabajadas = horas trabajadas 
# - pregunta_h_e = pregunta horas extra
# - sueldo_final = s_ingresado + cantidad_h_e (h_n * h_trabajadas)

# - h_n = hora normal
# - cantidad_h_e = cantidad de horas extra
# - sueldo_sobre_400 = si el trabajador gana mas de 400.000
# - sueldo_bajo_400 = si el trabajador gana menos de 400.000



sueldo_base = int(input("\nIngrese su sueldo: "))
pregunta_h_e = str(input("\n¿Realizó horas extra? (s/n): "))


if pregunta_h_e != "n":
    cantidad_h_e = int(input("\n¿Cuántas horas extra realizó?: "))
    h_n = 6000


    if sueldo_base >= 400000:
        sueldo_final = (sueldo_base + cantidad_h_e * (1.5 * h_n)) * 0.98
        print(f"\nsu sueldo final es: {sueldo_final:.0f}")

    else:
        sueldo_final = sueldo_base + cantidad_h_e * 3000
        print(f"\nsu sueldo final es: {sueldo_final:.0f}") # :.0f elimina los decimales al final de la cifra

else: 
    print(f"\nsu sueldo es: {sueldo_base:.0f}\n")


print("Programa finalizado")
