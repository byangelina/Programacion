

class Vehiculo:
    def _init_(self, marca, color, anio, modelo, tipo_combustible):
        self.marca = marca
        self.color = color
        self.anio = anio
        self.modelo = modelo
        self.tipo_combustible = tipo_combustible  # Atributo heredado
    
    def encender(self):
        return "El vehículo se ha encendido"
    
    def apagar(self):
        return "El vehículo se ha apagado"
    
    def mostrarDatos(self):
        datos = f"Marca: {self.marca}, Modelo: {self.modelo}, Anio: {self.anio}, Color: {self.color}, Tipo de Combustible: {self.tipo_combustible}"
        return datos


class Auto(Vehiculo):  # Herencia
    # Constructor: aceptar parámetros de la superclase y llamar a super()._init_()
    def _init_(self, marca, modelo, año, color, kilometraje, tipo_motor, tipo_combustible="Gasolina"):
        # Llamar al constructor de la superclase con parámetros correctos (agregué tipo_combustible por defecto)
        super()._init_(marca, color, año, modelo, tipo_combustible)
        # Atributos propios de Auto
        self.kilometraje = kilometraje
        self.__tipo_motor = tipo_motor  # Atributo privado para encapsulación

    @property  # Getter
    def tipo_motor(self):
        return self.__tipo_motor
    
    @tipo_motor.setter  # Setter simplificado con validación (solo asigna si es válido)
    def tipo_motor(self, tipo):
        if tipo in ["Gasolina", "Diesel", "Híbrido", "Eléctrico"]:
            self.__tipo_motor = tipo
        # Si no es válido, no asigna nada (simplificado, sin error)

    def acelerar(self):
        return "El auto acelera: ¡Vroom vroom!"
    
    # Método adicional propio de Auto, por ejemplo, para mostrar datos completos
    def mostrarDatosAuto(self):
        datos_super = super().mostrarDatos()
        return f"{datos_super}, Kilometraje: {self.kilometraje} km, Tipo de Motor: {self.__tipo_motor}"


# Instanciar (agregué tipo_combustible como parámetro opcional)
a1 = Auto("Toyota", "Corolla", 2020, "Rojo", 50000, "Gasolina", "Gasolina")
a1.tipo_motor = "Eléctrico"  # Esto funcionará porque es válido
a1.tipo_motor = "Otro"       # Esto no se asignará (permanece "Eléctrico")

print(a1.acelerar())              # Output: El auto acelera: ¡Vroom vroom!
print(a1.tipo_motor)              # Output: Eléctrico
print(a1.mostrarDatosAuto())      # Output: Marca: Toyota, Modelo: Corolla, Año: 2020, Color: Rojo, Tipo de Combustible: Gasolina, Kilometraje: 50000 km, Tipo de Motor: Eléctrico
print(a1.encender())              # Output: El vehículo se ha encendido (heredado)