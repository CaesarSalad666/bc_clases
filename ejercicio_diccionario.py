#Crear un diccionario persona con claves nombre, edad, estatura
#e imprimir cada uno de los valores de las claves en un print diferente
#Luego, cambiar la edad a otro valor con un input() e imprimir de nuevo
#Lueeeego agregar un par clave/valor "hobbie" que contenga una ***lista*** de hobbies
#e imprimir todo el diccionario
persona = {
            "nombre":"Pame",
            "edad":35,
            "estatura":1.60
            }
print(persona["nombre"])
print(persona["edad"])
print(persona["estatura"])

persona["edad"] = input("Ingresar edad")
print(persona["edad"])
persona["hobbie"] = ["dibujo","soccer","baile","artes marciales"]
print(persona["hobbie"][3])