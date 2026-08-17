
# crear 5 metodos con al menos 5 atributos, usar get y set 
# analizar la naturaleza del atributo, si se puede modificar o no, etc.

# quiero una clase Perro con atributos como nombre, edad, raza, dueño y color (5 atributos)
# y serán 5 métodos, es decir 5 tipos de perro.



class Perro:
    # constructor
    def __init__(self, nombre, edad, raza, dueno, color): 
        # atributos
        # self. hace referencia a sus propios objetos, ejemplo: el nombre...
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.dueno = dueno 
        self.color = color


    def mostrarDatos(self):
        datos = "Perro: " + self.nombre + self.edad + self.raza + self.color + "Nombre del dueño " + self.dueno
        return datos

# esto se llama instanciar ?
PerroUno = Perro()
PerroDos = Perro()
PerroTres = Perro()
PerroCuatro = Perro()
PerroCinco = Perro()


"""
# Perro 1
PerroUno.nombre = "Pepito"
PerroUno.edad = "5 años"
PerroUno.raza = "Pug"
PerroUno.dueno = "Marta"
PerroUno.color = "Cafe claro"

# Perro 2
PerroUno.nombre = "Magnus"
PerroUno.edad = "2 años"
PerroUno.raza = "Salchicha"
PerroUno.dueno = "Juan"
PerroUno.color = "Cafe oscuro"

# Perro 3
PerroUno.nombre = "Pepito"
PerroUno.edad = "5 años"
PerroUno.raza = "Pug"
PerroUno.dueno = "Marta"
PerroUno.color = "Cafe claro"

# Perro 4
PerroUno.nombre = "Pepito"
PerroUno.edad = "5 años"
PerroUno.raza = "Pug"
PerroUno.dueno = "Marta"
PerroUno.color = "Cafe claro"

# Perro 5
PerroUno.nombre = "Pepito"
PerroUno.edad = "5 años"
PerroUno.raza = "Pug"
PerroUno.dueno = "Marta"
PerroUno.color = "Cafe claro"
"""

perroUno = Perro("Pepito", "Honda", "Civic") 
perroDos = Perro("BB222", "Toyota", "Corolla")














