"""
crear 1 clase que herede de otra, la super clase debe tener sus atributos y métodos,
la clase hija debe considerar sus propios atributos y métodos, no se permiten 2 modelos iguales.
Agregar get y set, atributos privados que no se pueden cambiar.

- Setter se puede modificar
- Getter no se puede modificar, es inputable

OJO: @property usa setter y getter en un mismo atributo. PERO, un get puede no tener un set, el set no es obligatorio.
también es bueno poner get a todos los atributos, uno espera que un objeto sea casi totalmente modificable.

diferenciar entre atributos (cualidades: color, edad...) y métodos (acciones: saludar, comer...) 
"""

# clase base:
class SerMitologico:
    def __init__(self, nombre, edad, poder):
        
        self.__poder = poder
        self.__nombre = nombre
        self.__edad = edad # al tener .__ indica que es un atributo inmodificable

    @property # Getter edad
    def edad(self):
        return self.__edad  

    @property # Getter poder
    def poder(self):
        return self.__poder

    @property # Getter nombre
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        if nuevoNombre != self.__nombre:
            self.__nombre = nuevoNombre


# metodo con info basica del ser mitologico:
    def presentarse(self):
        print(f"- Soy {self.nombre}, tengo {self.edad} años y mi poder es {self.poder}.")

# metodo con uso de sus poderes:
    def usar_poder(self):
        print(f"- {self.nombre} usa su poder: {self.poder}.")



# -------------------------------------------------------------------------------------------------------------------


# clase dragon, heredada de ser mitologico:
class Dragon(SerMitologico):
    def __init__(self, nombre, edad, poder, color_escamas, lealtad):
        
        # super() hereda atributos de la clase base 
        super().__init__(nombre, edad, poder)

        # atributos nuevos (de la clase dragon)
        self.color_escamas = color_escamas
        self.lealtad = lealtad # haciendo referencia a quien obedece o sigue

    # metodo especifico del dragon:
    def momento_iconico(self,descripcion):
        print(f"{self.nombre} {descripcion}")


    # metodo para representar la relacion de lealtad con el dragon
    def mostrar_lealtad(self):
        print(f"- {self.nombre} es leal a {self.lealtad}.")




# para imprimir: -----------------------------------------------------------------------------------------------------------------------------

print("\nCriaturas de Game Of Thrones\n")

# instancia dragon
Rhaegal = Dragon("Rhaegal", 200, "fuego verde", "verde esmeralda", "Daenerys Targaryen") 
Drogon = Dragon("Drogon", 210, "fuego negro", "negro con rojo", "Daenerys Targaryen")
Viserion = Dragon("Viserion", 205, "fuego helado", "dorado", "Rey de la Noche")


# aqui imprimo los metodos de la clase base:
print("\npresentacion de los atributos del dragon:")
Rhaegal.presentarse()
Drogon.presentarse()
Viserion.presentarse() 

print("\nLealtad de cada dragon:")
Rhaegal.mostrar_lealtad()
Drogon.mostrar_lealtad()
Viserion.mostrar_lealtad()

print("\nPoderes:")
Rhaegal.usar_poder()
Drogon.usar_poder()
Viserion.usar_poder()

print("\nMomentos que representan a cada dragón:")
Rhaegal.momento_iconico("ataca a los ejércitos Lannister, una familia poderosa que se opone a Daenerys Targaryen\nen la guerra por el Trono de Hierro. Protege a su reina en la batalla y lucha contra sus enemigos.\n")
Drogon.momento_iconico("destruye una flota enemiga en Meereen, una ciudad esclavista que Daenerys liberó.\nInterviene para proteger la ciudad y sus habitantes de la amenaza enemiga.\n")
Viserion.momento_iconico("derriba el Muro, una gigantesca muralla mágica que protege los Siete Reinos\ndel peligro más allá del norte. Fue resucitado como dragón de hielo por el Rey\nde la Noche y facilita la entrada del ejército de los muertos.\n")