edad = int(input("Ingrese la edad: "))
antig = int(input("Ingrese los años de antigüedad en el empleo: "))

if edad >= 60 and antig < 25:
    tipo = "Jubilación por edad"
elif edad < 60 and antig >= 25:
    tipo = "Jubilación por antigüedad joven"
elif edad >= 60 and antig >= 25:
    tipo = "Jubilación por antigüedad adulta"
else:
    tipo = "No cumple requisitos de jubilación"

print(f"Clasificación: {tipo}")
