from urllib.request import urlopen
import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup

URL_BASE = "https://www.goodreads.com"
PAGINA_1 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=1"
PAGINA_2 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=2"
PAGINA_3 = "https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once?page=3"


class Libro:
    def __init__(self, titulo, link):
        self.titulo = titulo
        self.link = link
        self.autor = None
        self.fecha = None
        self.precio = None
        self.calificacion = None
        self.generos = []


def urls_libros():
    lista_urls = []
    try:
        urls_1 = urlopen(PAGINA_1)
        urls_2 = urlopen(PAGINA_2)
        urls_3 = urlopen(PAGINA_3)
    except HTTPError as e:
        print("grave")
        return None

    sopa_1 = BeautifulSoup(urls_1.read(), features="html.parser")
    sopa_2 = BeautifulSoup(urls_2.read(), features="html.parser")
    sopa_3 = BeautifulSoup(urls_3.read(), features="html.parser")

    c = 0
    for url in sopa_1.findAll('a', {"class": "bookTitle"}):
        enlace = url.get('href')
        lista_urls.append(enlace)
        c += 1

    for url in sopa_2.findAll('a', {"class": "bookTitle"}):
        enlace = url.get('href')
        lista_urls.append(enlace)
        c += 1

    for url in sopa_3.findAll('a', {"class": "bookTitle"}):
        enlace = url.get('href')
        lista_urls.append(enlace)
        c += 1

    return lista_urls


def info_libros():
    urls = urls_libros()
    c = 0
    for url in urls:
        libro = urlopen(URL_BASE+url)
        libro_sopa = BeautifulSoup(libro.read(), features="html.parser")
        titulo = libro_sopa.find("h1").string
        autor = libro_sopa.find("span", {"class": "ContributorLink__name"}).string
        fecha = libro_sopa.find("p", {"data-testid": "publicationInfo"}).string.strip("First published ")
        precio = libro_sopa.find("button", {"class": "Button Button--buy Button--medium Button--block"}).next_sibling

        print(precio)

        c += 1

        if c == 5:
            break

info_libros()
