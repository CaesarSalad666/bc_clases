
class Persona:
    nombre = None
    edad = None
    def __init__(self, un_nombre, una_edad):
        self.nombre = un_nombre
        self.edad = una_edad
        print("Hola, me llamo", self.nombre,"tengo", self.edad, "años y sufro de adiccion a las drogas. Hetama asufri.")

el_susodicho = Persona("Pedro", 28)