
# métodos
# aplicando init y self 

# __init__(self):  es una manera de llamar a los métodos.

class Ropa: # ¿qué atributos podemos encontrar en ropa?: marca, color, talla...
    def __init__(self):
        
        # definición de atributos de ropa:
        self.marca = "Willow"
        self.talla = "M"
        self.color = "Rojo"

# ahora crear un objeto para ropa: por ejemplo camisa

camisa = Ropa()
print(camisa.talla)
print(camisa.marca)
print(camisa.color)



