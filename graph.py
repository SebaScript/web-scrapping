import json
import os


class Grafo:
    def __init__(self):
        self.adj_list = {}


with open("libros.json", "r") as libros:
    data = json.load(libros)
