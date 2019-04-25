import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo="Blade"
busqueda = URL + API_KEY + "&t=" + titulo

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
pprint(dic_peli)
print(dic_peli["Year"])

#Ejercicio
#Consultar el API de OMDB y obtener el nombre del director de Fight Club
#Ejercicio 2
#Crear una funcion que reciba como argumento el titulo de una pelicula
#Y retorne los actores de esa pelicula