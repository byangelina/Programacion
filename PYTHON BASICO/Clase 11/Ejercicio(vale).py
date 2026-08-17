


class CriaturaFantastica:
    def __init__(self, nombre, elemento, color):
        self.nombre = nombre      
        self.elemento = elemento 
        self.color = color
        
    def mostrar_defin(self):
        print(f"{self.nombre} es una criatura del elemento {self.elemento} y de color {self.color}.")

class Dragon(CriaturaFantastica):
    def __init__(self, nombre, elemento, tamanio, color):
        super().__init__(nombre, elemento, color)
        self.tamaño = tamanio  

    def escupir_fuego(self):
        print(f"{self.nombre} escupe fuego cuando está enojado! ): ")
        print(f"{self.nombre} le gusta mucho volar y conquistar reinos")
        

chimuelo = Dragon("Chimuelo", "Fuego", "Gigante", "Negro")
chimuelo.tamanio = -10
print(chimuelo.tamanio)

chimuelo.mostrar_defin()     
chimuelo.escupir_fuego()


