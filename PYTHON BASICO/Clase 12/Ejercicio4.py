
# cómo eliminar un dato:

# de la siguiente forma: 
# def delPersonaje(self, nombrePersonaje):
#        for i in range(0, len(self.__personajes)):
#            if self.__personajes[i].nombre == nombrePersonaje:
#                del self.__personajes[i]


class Personaje:
    def __init__(self, nombre, poder, energia):
        self.nombre = nombre
        self.__poder = poder
        self.__energia = energia

    @property
    def poder(self):
        return self.__poder

    @property
    def energia(self):
        return self.__energia
    
    @energia.setter
    def energia(self, nuevaEnergia):
        if nuevaEnergia > 0 and nuevaEnergia <= 100:
            self.__energia = nuevaEnergia




def delTodosPersonajes(self):
    self.__personajes.clear()

class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__personajes = []

    def addPersonaje(self, nuevoPersonaje):
        if len(self.__personajes) < 10 and nuevoPersonaje.energia > 0:
            self.__personajes.append(nuevoPersonaje)

    def delPersonaje(self, nombrePersonaje):
        for i in range(len(self.__personajes) - 1, -1, -1):
            if self.__personajes[i].nombre == nombrePersonaje:
                del self.__personajes[i]

    def agregarEnergiaPersonajes(self, cantidadEnergia):
        for p in self.__personajes:
            p.energia += cantidadEnergia

    def mostrarPersonajes(self):
        strPersonajes = ""
        for p in self.__personajes:
            strPersonajes = strPersonajes +  f"Nombre: {p.nombre}, Poder: {p.poder}, Energia: {p.energia} \n"
        return strPersonajes


miCasa = Casa("Stark")
miCasa.addPersonaje(Personaje("Potter",50, 80))
miCasa.addPersonaje(Personaje("IronMan",50, 1))
miCasa.addPersonaje(Personaje("Gollum3",50, 30))
print(miCasa.mostrarPersonajes())
# miCasa.delPersonaje("IronMan")
print(miCasa.mostrarPersonajes())
miCasa.agregarEnergiaPersonajes(-10)
print(miCasa.mostrarPersonajes())

# aprender cómo usar range(-1,-1,-1)
# agregar, mostrar eliminar: métodos clave de aprender a usar en asociacion.
# aprender a usar listas (completamente).









