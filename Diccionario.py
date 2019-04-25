diccionario = {}

nombre_de_diccionario = {"nombre_clave":"valor"}
#lista
persona = ["Marce", 32, "Programador"]
#Diccionario

dic_persona = {"nombre":"Marce", "edad": 32}
print(dic_persona)
print(dic_persona["edad"])
print(dic_persona[1])

dic_persona["profesion"] = "Programador"
print(dic_persona)
print(dic_persona.get("estatura"))


if dic_persona.get("estatura"):
print("Si existe la clave estatura")
else:
print("No existe la clave estatura")

dic_persona2 = {
"nombre" : "Marce",
"edad" : 32,
"peinado" : "algo"
}

print(dic_persona2)


