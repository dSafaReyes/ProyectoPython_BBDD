import requests
from bs4 import BeautifulSoup


def connect_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        return False


def lista_palabras(txt):
    ''' Elimina todos los espacios de un string. Devuelve una lista con cada palabra '''
    lista_palabras = txt.split()
    lista_sin_espacios = list(filter(None, lista_palabras))
    return lista_sin_espacios


def redondear_arriba(num):
    ''' Deuelve el número redondeado
        a la siguiente unidad '''
    return round(num+0.5)


def get_ciudad_ofertas_paginas(string):
    ''' Recibe el contenido en h1, separa cada palabra en un elemento de la lista y devuelve de ella la ciudad,
        el número de ofertas y las páginas que tiene asociada dicha ciudad (en cada página caben 30 ofertas) '''
    lista_palabras_title = lista_palabras(string.text)
    n_ofertas = int(lista_palabras_title[0])
    ciudad = lista_palabras_title[-1]
    n_paginas = redondear_arriba(n_ofertas/30)
    return ciudad, n_ofertas, n_paginas
