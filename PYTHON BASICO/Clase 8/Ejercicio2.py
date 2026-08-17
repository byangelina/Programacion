
# crear un objeto tipo persona adonde crear atributos, constructor e instanciar 5 veces la clase con al menos un método, por ejemplo, saludar, despedirse, gritar, caminar, saltar...

class Persona:
    
    # atributos públicos: 
    nombre = ""
    edad = ""
    sexo = ""
    altura = ""


    def __init__(self, laPatente, laMarca):
        print("Se ejecutó el conductor", laPatente) 
        # manda a llamar a patente, que esta dentro de laPatente y 
        # ahi se guarda autoUno y autoDos

        self.patente = laPatente
        self.marca = laMarca


    def mostrarDatos(self):
        datos = "Patente: " + self.patente + "Marca" + self.marca
        return datos



#------------------------------------
personaUno = Persona()
personaDos = Persona()
personaTres = Persona()
personaCuatro = Persona()
personaCinco = Persona()


# persona 1
personaUno.nombre = "Angela"
personaUno.edad = "24"
personaUno.sexo = "Femenino"
personaUno.altura = "1.70"

# persona 2
personaDos.nombre = "Richy"
personaDos.sexo = "Masculino"
personaDos.altura = "1.85"

# persona 3
personaUno.nombre = "Pancha"
personaUno.edad = "20"
personaUno.sexo = "Femenino"
personaUno.altura = "1.60"

# persona 4
personaUno.nombre = "Vale"
personaUno.edad = "23"
personaUno.sexo = "Femenino"
personaUno.altura = "1.60"

# persona 5
personaUno.nombre = "Mari"
personaUno.edad = "19"
personaUno.sexo = "Femenino"
personaUno.altura = "1.59"


print("Persona Uno",personaUno.patente)
print("Persona Dos",personaDos.patente)