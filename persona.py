
class Persona:
    nombre = None
    edad = 27
    def __init__(self, un_nombre, cumple):
        self.nombre = un_nombre
        self.edad = cumple
        print("Hola, me llamo", self.nombre,"tengo", self.edad, "años y sufro de adiccion a las drogas. Hetama asufri.")

    def get_edad(self):
        return self.edad
        
    def set_edad(self, cantidad):
        self.edad = cantidad

    def cumpleaños(self):
        self.edad = self.edad +1
        
individuo = Persona("Pedro", 27)

#Ejercicio
#Modificar la clase persona, agregarle un atributo edad y
#un metodo cumpleaños y un metodo det_edad
#Inicializar/crear un objeto de tipo persona y hacerle cumplir años