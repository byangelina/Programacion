
class Nombre:
    pass # es para indicar que cla clase llegó a su fin, lo voy a desarrollar despúes.

# objetos: victor y maria
# se crean los objetos y se manda a llamar la class nombre, porque significa que los vamos a definir después, a futuro.

victor = Nombre() 
maria = Nombre()

# ahora definir los atributos, por ejemplo, edad, sexo, pais... de esta forma: objeto.atributo = valor 
victor.edad = 30
victor.sexo = "Masculino"
victor.pais = "Bolivia"

maria.edad = 20
maria.sexo = "Femenino"
maria.pais = "Colombia"

# Ejemplo de cómo imprimir objeto con atributo: print(objeto.atributo)
print(f"Edad de Victor: {victor.edad}")
print(f"Pais de Victor: {victor.pais}")
print(f"Edad de Maria: {maria.edad}")