

# ¿cómo puedo limitar la impresion de personajes, hay 13 y solo debo mostrar 10?

# código base -----------------------------------------------------------------------------------------

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
        self.__personajes.append(nuevoPersonaje)

    def mostrarPersonajes(self):
        strPersonajes = ""
        for p in self.__personajes:
            strPersonajes = strPersonajes +  f"Nombre: {p.nombre}, Poder: {p.poder}, Energia: {p.energia} \n"

        return strPersonajes

miCasa = Casa("Stark")
miCasa.addPersonaje(Personaje("Potter",50, 80))
miCasa.addPersonaje(Personaje("IronMan",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
miCasa.addPersonaje(Personaje("Gollum",50, 80))
print(miCasa.mostrarPersonajes())

""" 



# código modificado -----------------------------------------------------------------------------------------

# se modifico lo siguiente:
#    def addPersonaje(self, nuevoPersonaje):
#        if len(self.__personajes) < 10:
#            self.__personajes.append(nuevoPersonaje)


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
miCasa.addPersonaje(Personaje("Gollum4",50, 80))
miCasa.addPersonaje(Personaje("Gollum5",50, 80))
miCasa.addPersonaje(Personaje("Gollum6",50, 80))
miCasa.addPersonaje(Personaje("Gollum7",50, 80))
miCasa.addPersonaje(Personaje("Gollum8",50, 80))
miCasa.addPersonaje(Personaje("Gollum9",50, 80))
miCasa.addPersonaje(Personaje("Gollum10",50, 80))
miCasa.addPersonaje(Personaje("Gollum11",50, 80))
miCasa.addPersonaje(Personaje("Gollum12",50, 80))
miCasa.addPersonaje(Personaje("Gollum13",50, 80))
print(miCasa.mostrarPersonajes())






