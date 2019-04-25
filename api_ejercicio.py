import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo="Fight Club"
busqueda = URL + API_KEY + "&t=" + titulo

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
pprint(dic_peli)
print(dic_peli["Director"])