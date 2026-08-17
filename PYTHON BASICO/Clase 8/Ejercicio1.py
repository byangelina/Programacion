
# class: para crear la clase. Asignarle un nombre.
    # método init: para crear los objetos.
    # agregar los atributos, por ejemplo: patente = " ", marca = " ", modelo = " "...
    
    # como asignar modelos: 
    # nombre modelo de auto, ejemplo: AutoUno = Auto () 



# se hara el mismo codigo pero modifcado en diferentes ejercicios para avanzar de a poco:
# ejemplo codigo completo 1: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
class Auto:
    # atributos públicos: patenet, marca, modelo.
    patente = ""
    marca = ""
    modelo = ""

#------------------------------------
autoUno = Auto()
autoDos = Auto()

autoUno.patente = "AA111"
autoUno.marca = "Honda"
autoUno.modelo = "Civic"

autoDos.patente = "BB222"

print("Auto Uno",autoUno.patente)
print("Auto Dos",autoDos.patente)
"""

# investigar:
# qué son los atributos públicos?
# cómo diagramar en UML?






# ejemplo codigo completo 2: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
class Auto:
    # constructor
    def __init__(self, laPatente, laMarca):
        print("Se ejecutó el conductor", laPatente) 
        # manda a llamar a patente, que esta dentro de laPatente y 
        # ahi se guarda autoUno y autoDos

        self.patente = laPatente
        self.marca = laMarca



    def mostrarDatos(self):
        datos = "Patente: " + self.patente + "Marca" + self.marca
        return datos


#------------------------------------
autoUno = Auto() #Instanciar objeto(crear) y ejecutamos constructor
autoDos = Auto()

autoUno.patente = "AA111"
autoUno.marca = "Honda"
autoUno.modelo = "Civic"

autoDos.patente = "BB222"

print("Auto Uno",autoUno.patente)
print("Auto Dos",autoDos.patente)
"""
# self: sirve para hacer referencia a un objeto con una característica específica







# ejemplo codigo completo 3: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
class Auto:
    #Constructor
    def __init__(self, patente, marca):
        #print("Se ejecutó el contructor ", laPatente)
        self.patente = patente
        self.marca = marca

    def mostrarDatos(self):
        datos = "Patente: " + self.patente + " Marca: " + self.marca
        return datos


#------------------------------------
autoUno = Auto("AA111", "Honda") #Instanciar objeto(crear) y ejecutamos constructor
autoDos = Auto("BB222", "Toyota")

listAutos = []
for x in range(1,1000):
    listAutos.append(Auto("Patente "+str(x), "Marca"+str(x)))
    
for x in range(1,1000):
    print(listAutos[x].mostrarDatos())

"""


"""
salida en terminal:
0jO�_�����|�L���z@!��gL5��+�ݱ�+*�X��V+�;>.WxE�JC������arca486
Patente: Patente 487 Marca: Marca487
Patente: Patente 488 Marca: Marca488
Patente: Patente 489 Marca: Marca489
Patente: Patente 490 Marca: Marca490
Patente: Patente 491 Marca: Marca491
Patente: Patente 492 Marca: Marca492
Patente: Patente 493 Marca: Marca493
Patente: Patente 494 Marca: Marca494...etc
"""







# ejemplo codigo completo 4: ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
class Auto:
    #Constructor
    def __init__(self, patente, marca, modelo):
        #print("Se ejecutó el contructor ", laPatente)
        self.patente = patente
        self.marca = marca
        self.modelo = modelo

    def mostrarDatos(self):
        datos = "Patente: " + self.patente + " Marca: " + self.marca
        return datos


#------------------------------------
autoUno = Auto("AA111", "Honda", "Civic") #Instanciar objeto(crear) y ejecutamos constructor
autoDos = Auto("BB222", "Toyota", "Corolla")

listAutos = []
for x in range(1,1000):
    listAutos.append(Auto("Patente "+str(x), "Marca"+str(x), "Modelo"+str(x)))

for x in range(1,len(listAutos) - 1):
    print(listAutos[x].mostrarDatos())

"""




































