class NaveEspacial:
    def __init__(self, nombre, combustible, velocidad):
        self.nombre = nombre
        self.combustible = combustible  
        self.velocidad = velocidad 


    def despegar(self):
        if self.combustible > 50:
            print(f"{self.nombre} ha despegado a una velocidad de {self.velocidad} km/s.")
            self.combustible -= 50
        else:
            print(f"{self.nombre} no tiene suficiente combustible para despegar.")


    def recargar_combustible(self, cantidad):
        self.combustible += cantidad
        print(f"{self.nombre} ha recargado {cantidad} litros de combustible. Total: {self.combustible}.")

#--------------------------------------------------------------------------------------------------------------




class NaveExploradora(NaveEspacial):
    def __init__(self, nombre, combustible, velocidad, planeta_destino, capacidad_investigacion):
        super().__init__(nombre, combustible, velocidad)
        self.planeta_destino = planeta_destino
        self.capacidad_investigacion = capacidad_investigacion

    def explorar_planeta(self):
        if self.capacidad_investigacion > 5:
            print(f"{self.nombre} está explorando el planeta {self.planeta_destino} con gran detalle.")
        else:
            print(f"{self.nombre} explora {self.planeta_destino}, pero con recursos limitados.")

    def recolectar_muestras(self, cantidad):
        print(f"{self.nombre} recolectó {cantidad} muestras de {self.planeta_destino}.")


# imprimir:

nave1 = NaveExploradora("Odisea-IX", 120, 25, "Europa (luna de Júpiter)", 8)
nave1.despegar()
nave1.explorar_planeta()
nave1.recolectar_muestras(12)
nave1.recargar_combustible(80)