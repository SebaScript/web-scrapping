import json
import os
from datetime import datetime


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.autor = ""
        self.fecha = ""
        self.precio = ""
        self.calificacion = ""
        self.generos = []


class Grafo:
    def __init__(self):
        self.adj_list = {}

    def nuevo_nodo(self, valor, tipo=None):
        if valor not in self.adj_list:
            self.adj_list[valor] = {"tipo": tipo,
                                    "relaciones": []}
        else:
            return False

    def nueva_arista(self, v1, v2):
        if v1 not in self.adj_list:
            self.nuevo_nodo(v1)
        if v2 not in self.adj_list:
            self.nuevo_nodo(v2)

        self.adj_list[v1]["relaciones"].append(v2)

    def listar_libros_autor_x(self):
        pass

    def recomendar_n_libros(self):
        pass

    def listar_autores_genero_x(self):
        pass

    def recomendar_libros_puntaje(self):
        pass

    def recomendar_lista_compras(self):
        pass


def crear_grafo():
    with open("libros.json", "r") as libros:
        data = json.load(libros)

    libros = []
    for info_libro in data:
        titulo = info_libro["titulo"]
        libro = Libro(titulo)
        libro.autor = info_libro["autor"]
        fecha = info_libro["fecha"]
        try:
            conv_fecha = datetime.strptime(fecha, "%B %d, %Y")
            form_fecha = conv_fecha.strftime("%d-%m-%Y")
            libro.fecha = datetime.strptime(form_fecha, "%d-%m-%Y").date()
        except ValueError:
            libro.fecha = None

        libro.precio = float(info_libro["precio"])

        try:
            libro.calificacion = float(info_libro["calificacion"])
        except:
            libro.calificacion = info_libro["calificacion"]
        libro.generos = info_libro["generos"]
        libros.append(libro)

    g = Grafo()

    for obj_libro in libros:
        g.nuevo_nodo(obj_libro.titulo, tipo="libro")
        g.nuevo_nodo(obj_libro.autor, tipo="autor")
        for genero in obj_libro.generos:
            g.nuevo_nodo(genero, tipo="genero")


crear_grafo()


def menu():
    print("\nOla")
    while True:
        print("Que quieres hacer")
        print('''
                1. Listar los libros del autor X ordenados por fecha de lanzamiento.
                2. Recomendar N libros del mismo género y de la misma década que el libro X.
                3. Listar a los autores del género X ordenados por la cantidad de libros escritos en este género.
                4. Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros 
                (pueden ser 1 o varios).
                5. Recomendar lista de compras para obtener el mayor número de libros con 
                base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios).
                6. Salir
                ''')
        opcion = input("\nIngresa tu opción: ")
        if opcion == "1":
            """
             Listar los libros del autor X ordenados por fecha de lanzamiento.
            """

        elif opcion == "2":
            """
            Recomendar N libros del mismo género y de la misma década que el libro X.
            """

        elif opcion == "3":
            """
            Listar a los autores del género X ordenados por la cantidad de libros escritos
            en este género.
            """

        elif opcion == "4":
            """
            Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de
            un grupo de géneros (pueden ser 1 o varios).
            """

        elif opcion == "5":
            """
            Recomendar lista de compras para obtener el mayor número de libros con
            base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios).
                ■ Por ejemplo, darme la mejor lista de compras posible para gastar 10
                USD en los géneros clásico y horror.
                    ● El sistema deberá listar la mejor combinación de libros de
                    estos dos géneros para maximizar la cantidad de libros a
                    comprar con esa cantidad de dinero.
            """

        elif opcion == "6":
            break

        else:
            print("No\n")


menu()
