
# crear 5 metodos con al menos 5 atributos, usar get y set 
# analizar la naturaleza del atributo, si se puede modificar o no, etc.

# quiero una clase Perro con atributos como nombre, edad, raza, dueño y color (5 atributos)
# y serán 5 métodos, es decir 5 tipos de perro.



"""
class Lobo:
    def __init__(self):
        pass


class Perro:
    # constructor
    def __init__(self, nombre, edad, raza, dueno, color): 
        # atributos: ojo, hay atributos que no se pueden cambiar.
        # self. hace referencia a sus propios objetos
        self.nombre = nombre
        self.__edad = edad
        self.__raza = raza
        self.dueno = dueno 
        self.color = color


    # investigar para qué sirve @property y Getter / Setter

    @property # Getter
    def raza(self): # Raza(self): lo que hace es emular el atributo que está oculto
        return self.__raza
    
    @property # Getter
    def edad(self):
        return self.__edad

    @edad.setter # Setter
    def edad(self, edad):
        if edad > 0 and edad < 25:
            self.__edad = edad

    def aullar(self):
        return "Auuuu"
    
    def ladrar(self):
        return "Guau guau"
    
    def comer(self):
        return "Comer"

    def mostrarDatos(self): # es un método que guarda y muestra datos con la variable "datos"
        datos = "Perro: " + self.nombre + self.edad + self.__raza + self.color + "Nombre del dueño " + self.dueno
        return datos



# Instanciar
p1 = Perro("Pepito", "2 años", "Pug", "Marta", "Café claro") 


# al imprimir no queremos que se modifique la raza, porque el perro no puede cambiar de raza.
# para que los atributos no sean modificables, crear un atributo "privado", eso se hace arriba en el constructor con un guión bajo, así: self._raza = raza

print(p1.ladrar())
print(p1.raza())
print(p1.edad)
"""

