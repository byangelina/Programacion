
# Qué es un método: Un método es una función que toma una instancia de clase como su primer parámetro. Además hay diferentes tipos de métodos.
# Qué es Self: sirve para especificar que estamos pasando el valor a los atributos de la instancia y no a la variable o argumento local con el mismo nombre.


# Cómo escribir un método de clase: 
"""
Class nombre_de_la_clase:
    def nombre_del_metodo(self):
self.nombre_de_la_variable = algoritmo (algoritmo es aglun valor, por ejemplo: 2)
"""

class Matematica:
    def suma (self):
        self.n1 = 2
        self.n2 = 3

# definir objetos:
s = Matematica() # () es abrir parámetros
s.suma() 
print(s.n1 + s.n2)