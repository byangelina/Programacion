
# Investigación obligatoria:
# - Investigar que es un ORM en programación
# - Características de las clases POLLO

# Enlaces útiles (open source para windows y linux):
# - https://grafana.com/ open source
# - https://prometheus.io/




"""
Crear una clase Persona con atributos(rut, nombre, apellidoMaterno, apellidoPaterno, edad)

Métodos : nombreCompleto que retorne un string con el ApellidoPaterno, ApeliidoMaterno, Nombre

Luego crear una lista de 100 objetos y determinar la edad promedio de la lista de personas

Modificar la clase persona agregando un atributo peso y 2 métodos:
comer() -> que sube 1 kilo cada vez que se invoca y actividad() -> que baja 0.1 el peso al invocarse

Modificar atributo edad x fecha de nacimiento y agregar un método edad()
que en función de la fecha de nacimiento retorne un número entero que corresponde a la edad
"""


from datetime import date, datetime
import random

class Persona:
    def __init__(self, rut, nombre, apellidoPaterno, apellidoMaterno, fecha_nacimiento, peso):
        self.rut = rut
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.fecha_nacimiento = fecha_nacimiento  # tipo date
        self.peso = peso

    def nombreCompleto(self):
        """Retorna el nombre completo en el formato solicitado."""
        return f"{self.apellidoPaterno} {self.apellidoMaterno}, {self.nombre}"

    def edad(self):
        """Calcula la edad actual en años según la fecha de nacimiento."""
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def comer(self):
        """Aumenta el peso en 1 kg."""
        self.peso += 1

    def actividad(self):
        """Disminuye el peso en 0.1 kg."""
        self.peso -= 0.1


# -------------------------------
# Crear lista de 100 personas
# -------------------------------
nombres = ["Camila", "Felipe", "Sofía", "Matías", "Isidora", "Diego", "Constanza", "Sebastián"]
apellidos = ["Pérez", "González", "Muñoz", "Rojas", "Díaz", "Torres", "Soto", "Vargas"]

personas = []

for i in range(100):
    rut = f"{random.randint(1000000, 25000000)}-{random.randint(0,9)}"
    nombre = random.choice(nombres)
    apellidoPaterno = random.choice(apellidos)
    apellidoMaterno = random.choice(apellidos)
    # Generar una fecha de nacimiento aleatoria entre 1980 y 2010
    año = random.randint(1980, 2010)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # evitar problemas con febrero
    fecha_nacimiento = date(año, mes, dia)
    peso = round(random.uniform(50, 90), 1)
    
    persona = Persona(rut, nombre, apellidoPaterno, apellidoMaterno, fecha_nacimiento, peso)
    personas.append(persona)

# Calcular edad promedio
edades = [p.edad() for p in personas]
edad_promedio = sum(edades) / len(edades)

print(f"Edad promedio del grupo: {edad_promedio:.2f} años")

# Ejemplo de uso
ejemplo = personas[0]
print("\nEjemplo de persona:")
print("Nombre completo:", ejemplo.nombreCompleto())
print("Edad:", ejemplo.edad(), "años")
print("Peso inicial:", ejemplo.peso, "kg")
ejemplo.comer()
print("Después de comer:", ejemplo.peso, "kg")
ejemplo.actividad()
print("Después de actividad:", round(ejemplo.peso, 1), "kg")

