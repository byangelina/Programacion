
# así parte el código
"""
class Calculadora:
    def __init__(self):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

# crear un objeto: operacion
operacion = Calculadora()

# imprimir los atributos
print()
"""


class Calculadora:
    def __init__(self,n1,n2): # aqui agregar n1 y n2 para que queden los números definidos como parámeto.
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

# crear un objeto: operacion
operacion = Calculadora(10,3) # adentro de () poner cuánto vale n1 y n2

# imprimir los atributos
print(operacion.multiplicacion)