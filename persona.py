
class Persona:
    nombre = None
    def __init__(self, un_nombre):
        self.nombre = un_nombre
        print("Hola, me llamo", self.nombre,"y sufro de adiccion a las drogas")

el_susodicho = Persona("Pedro")