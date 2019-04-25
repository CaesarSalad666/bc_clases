import requests
from pprint import pprint
def peli (titulo):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    busqueda = URL + API_KEY + "&t=" + titulo
    respuesta = requests.get(busqueda)
    dic_peli = respuesta.json()
    pprint(dic_peli)
    print(dic_peli["Actors"])

peli("Jurassic World")