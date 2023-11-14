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

    def nuevo_nodo(self, valor):
        if valor not in self.adj_list:
            self.adj_list[valor] = []
        else:
            return False

    def nueva_arista(self, v1, v2, bid=False, tipo=None):
        if v1 not in self.adj_list:
            self.nuevo_nodo(v1)
        if v2 not in self.adj_list:
            self.nuevo_nodo(v2)

        self.adj_list[v1].append([v2, tipo])

        if bid:
            self.adj_list[v2].append([v1, tipo])

    def listar_libros_autor_x(self, nombre_autor):
        """Listar los libros del autor X ordenados por fecha de lanzamiento."""
        libros_autor = []
        for nodo, libros_nodo in self.adj_list.items():
            if nodo == nombre_autor:
                for libro in libros_nodo:
                    fecha = ""
                    for i in self.adj_list[libro[0]]:
                        if i[1] == "fecha":
                            fecha = i[0]
                    libros_autor.append((libro[0], fecha))

        lista_ordenada = sorted(libros_autor, key=lambda x: x[1])

        if len(lista_ordenada) == 0:
            return False

        print(lista_ordenada)
        return lista_ordenada

    def recomendar_n_libros(self, nombre_libro):
        """Recomendar N libros del mismo género y de la misma década que el libro X."""
        recom_libros = []
        generos_lib = []
        for nodo, libros_nodo in self.adj_list.items():
            if nodo == nombre_libro:
                for i in libros_nodo:
                    if i[1] == "fecha":
                        anio = i[0].year
                        decada = (anio//10) * 10
                    if i[1] == "genero_lib":
                        generos_lib.append(i[0])

        for nodo, valor in self.adj_list.items():
            pass

    def listar_autores_genero_x(self, genero):
        """Listar a los autores del género X ordenados por la cantidad de libros escritos en este género."""
        dicc_autores = {}
        for nodo, autor in self.adj_list.items():
            if nodo == genero:
                for i in autor:
                    if i[1] == "genero_aut":
                        if i[0] in dicc_autores:
                            dicc_autores[i[0]] += 1
                        else:
                            dicc_autores[i[0]] = 1

        dicc_ord = dict(sorted(dicc_autores.items(), key=lambda item: item[1], reverse=True))

        print(dicc_ord)

    def recomendar_libros_puntaje(self):
        """Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios)."""
        pass

    def recomendar_lista_compras(self):
        """Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios)."""
        pass

    def crear_grafo(self):
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
                conv_fecha = conv_fecha.strftime("%d-%m-%Y")
                libro.fecha = datetime.strptime(conv_fecha, "%d-%m-%Y").date()
                #anio = datetime.strptime(conv_fecha, "%d-%m-%Y").date().year
                #decada = (anio//10) * 10
                #libro.fecha = decada
            except ValueError:
                libro.fecha = None

            libro.precio = float(info_libro["precio"])

            try:
                libro.calificacion = float(info_libro["calificacion"])
            except:
                libro.calificacion = info_libro["calificacion"]
            libro.generos = info_libro["generos"]
            libros.append(libro)

        for obj_libro in libros:
            for genero in obj_libro.generos:
                self.nueva_arista(genero, obj_libro.autor, tipo="genero_aut")
                self.nueva_arista(genero, obj_libro.titulo, bid=True, tipo="genero_lib")
            self.nueva_arista(obj_libro.autor, obj_libro.titulo, tipo="escribio")
            self.nueva_arista(obj_libro.titulo, obj_libro.fecha, tipo="fecha")
            self.nueva_arista(obj_libro.titulo, obj_libro.precio, tipo="precio")
            self.nueva_arista(obj_libro.titulo, obj_libro.calificacion, tipo="calificacion")

        for i, j in self.adj_list.items():
           print(i, j)


g = Grafo()
g.crear_grafo()
g.listar_autores_genero_x("Biography")
#g.recomendar_n_libros("To Kill a Mockingbird")


def menu():
    print("\nOla\n")
    while True:
        print("¿Que quieres hacer?")
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
