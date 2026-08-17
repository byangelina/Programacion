
# "no se pueden ingresar personajes con energia 0, cómo se hace?"

# código base ------------------------------------------------------------------------

"""
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



class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__personajes = []

    def addPersonaje(self, nuevoPersonaje):
        if len(self.__personajes) < 10:
            self.__personajes.append(nuevoPersonaje)

    def mostrarPersonajes(self):
        strPersonajes = ""
        for p in self.__personajes:
            strPersonajes = strPersonajes +  f"Nombre: {p.nombre}, Poder: {p.poder}, Energia: {p.energia} \n"

        return strPersonajes


miCasa = Casa("Stark")
miCasa.addPersonaje(Personaje("Potter",50, 80))
miCasa.addPersonaje(Personaje("IronMan",50, 80))
miCasa.addPersonaje(Personaje("Gollum3",50, 80))
print(miCasa.mostrarPersonajes())

"""

# código modificado ------------------------------------------------------------------------

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

class Casa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__personajes = []

    def addPersonaje(self, nuevoPersonaje):
        if len(self.__personajes) < 10 and nuevoPersonaje.energia > 0:
            self.__personajes.append(nuevoPersonaje)

    def mostrarPersonajes(self):
        strPersonajes = ""
        for p in self.__personajes:
            strPersonajes = strPersonajes +  f"Nombre: {p.nombre}, Poder: {p.poder}, Energia: {p.energia} \n"

        return strPersonajes


miCasa = Casa("Stark")
miCasa.addPersonaje(Personaje("Potter",50, 80))
miCasa.addPersonaje(Personaje("IronMan",50, 0))
miCasa.addPersonaje(Personaje("Gollum3",50, 30))
print(miCasa.mostrarPersonajes())













