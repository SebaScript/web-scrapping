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
        libros_autor = {}
        for nodo, libros_nodo in self.adj_list.items():
            if nodo == nombre_autor:
                for libro in libros_nodo:
                    fecha = ""
                    for i in self.adj_list[libro[0]]:
                        if i[1] == "fecha":
                            fecha = i[0]
                    libros_autor[libro[0]] = fecha

        if len(libros_autor) == 0:
            return False

        dicc_ord = dict(sorted(libros_autor.items(), key=lambda item: item[1]))

        return dicc_ord

    def recomendar_n_libros(self, nombre_libro):
        """Recomendar N libros del mismo género y de la misma década que el libro X."""
        genero = ""
        decada_libro = 0
        for nodo, libros_nodo in self.adj_list.items():
            if nodo == nombre_libro:
                for i in libros_nodo:
                    if i[1] == "genero_lib":
                        genero = i[0]
                    if i[1] == "fecha":
                        anio = i[0].year
                        decada_libro = (anio//10) * 10

        if genero == "":
            return False

        print(f"Genero: {genero}, Decada: {decada_libro}\n")
        libros_genero = []
        for nodo, valor in self.adj_list.items():
            if nodo == genero:
                for i in valor:
                    if i[1] == "genero_lib":
                        libros_genero.append(i[0])

        fechas = {}
        for libro in libros_genero:
            for nodo, valor in self.adj_list.items():
                if nodo == libro:
                    for i in valor:
                        if i[1] == "fecha":
                            try:
                                anio = i[0].year
                            except:
                                continue
                            decada = (anio // 10) * 10
                            if decada == decada_libro:
                                fechas[libro] = decada

        return fechas

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

        if not dicc_autores:
            return False

        dicc_ord = dict(sorted(dicc_autores.items(), key=lambda item: item[1], reverse=True))

        return dicc_ord

    def recomendar_libros_puntaje(self, puntaje, generos):
        """Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios)."""
        if type(puntaje) is float:
            return False

        libros_genero = []
        for genero in generos:
            for nodo, libros in self.adj_list.items():
                if nodo == genero:
                    for libro in libros:
                        if libro[1] == "genero_lib":
                            libros_genero.append(libro[0])

        if not libros_genero:
            return 1

        puntajes = {}
        for nombre in libros_genero:
            for libro, valores in self.adj_list.items():
                if nombre == libro:
                    for i in valores:
                        if i[1] == "calificacion":
                            if i[0] > puntaje:
                                puntajes[nombre] = i[0]

        return puntajes

    def recomendar_lista_compras(self, monto, generos):
        """Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios)."""
        libros_genero = []
        for genero in generos:
            for nodo, libros in self.adj_list.items():
                if nodo == genero:
                    for libro in libros:
                        if libro[1] == "genero_lib":
                            libros_genero.append(libro[0])

        if not libros_genero:
            return 1

        precios = {}
        for nombre in libros_genero:
            for libro, valores in self.adj_list.items():
                if nombre == libro:
                    for i in valores:
                        if i[1] == "precio":
                            if i[0] < monto:
                                precios[nombre] = i[0]

        recom_libros = {}
        monto_total = 0
        for libro, precio in sorted(precios.items(), key=lambda x: x[1]):
            if monto_total + precio <= monto:
                recom_libros[libro] = precio
                monto_total += precio

        return recom_libros

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

        #for i, j in self.adj_list.items():
         #  print(i, j)


g = Grafo()
g.crear_grafo()
#g.recomendar_n_libros("To Kill a Mockingbird")
#g.recomendar_libros_puntaje(4, "Biography", "Classics", "Fiction")
#g.listar_autores_genero_x("Biography")
#g.recomendar_lista_compras(100, "Biography", "Classics", "Fiction")
#g.recomendar_n_libros("To Kill a Mockingbird")


def menu():
    print("\nOla\n")
    while True:
        print("\n¿Que quieres hacer?")
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
        opcion = input("Ingresa tu opción: ")
        if opcion == "1":
            """Listar los libros del autor X ordenados por fecha de lanzamiento"""
            while True:
                autor = input("\nNombre del autor: ")
                print("")
                resultado = g.listar_libros_autor_x(autor)

                if not resultado:
                    print("No se encontró el autor")
                    continue

                else:
                    for libro, fecha in resultado.items():
                        print(f"{libro}: {fecha}")
                    print("------------------------------------------------------")
                    break

        elif opcion == "2":
            """Recomendar N libros del mismo género y de la misma década que el libro X"""
            while True:
                libro = input("\nNombre del libro: ")
                print("")
                resultado = g.recomendar_n_libros(libro)

                if not resultado:
                    print("No se encontró el libro")
                    continue

                else:
                    for libro, decada in resultado.items():
                        print(f"{libro}: {decada}")
                    print("------------------------------------------------------")
                    break

        elif opcion == "3":
            """Listar a los autores del género X ordenados por la cantidad de libros escritos en este género."""
            while True:
                genero = input("\nGenero: ")
                print("")
                resultado = g.listar_autores_genero_x(genero)

                if not resultado:
                    print("No se encontró el género")
                    continue

                else:
                    for autor, cantidad in resultado.items():
                        print(f"{autor}: {cantidad}")
                    print("------------------------------------------------------")
                    break

        elif opcion == "4":
            """Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios)."""
            while True:
                while True:
                    try:
                        puntaje = int(input("\nPuntaje: "))
                        if puntaje > 5 or puntaje < 1:
                            print("\nEl puntaje debe estar entre 1 y 5")
                            continue
                    except:
                        print("\nDebes ingresar un número entero")
                        continue
                    break
                print("")

                generos = []
                while True:
                    opcion = input("""
                    1. Agregar género.
                    2. Listo
                    opcion: """)

                    if opcion == "1":
                        genero = input("\nGenero: ")
                        generos.append(genero)
                        continue

                    if opcion == "2":
                        break

                    else:
                        print("No")
                        continue

                resultado = g.recomendar_libros_puntaje(puntaje, generos)

                if resultado == 1:
                    print("\nNo se encontró algún genero que seleccionaste")
                    continue

                if not resultado:
                    print("\nNo se encontró ningún libro en los generos seleccionados con un puntaje mayor al indicado")

                else:
                    for libro, puntaje in resultado.items():
                        print(f"{libro}: {puntaje}")
                    print("------------------------------------------------------")
                    break

        elif opcion == "5":
            """Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios)."""
            monto = float(input("\nMonto: "))
            print("")

            generos = []
            while True:
                opcion = input("""
                1. Agregar género.
                2. Listo
                opcion: """)

                if opcion == "1":
                    genero = input("\nGenero: ")
                    generos.append(genero)
                    continue

                if opcion == "2":
                    break

                else:
                    print("No")
                    continue

            resultado = g.recomendar_lista_compras(monto, generos)

            if resultado == 1:
                print("\nNo se encontró algún genero que seleccionaste")
                continue

            if not resultado:
                print("\nNo se encontró ningún libro en los generos seleccionados con un precio menor al monto seleccionado")

            else:
                for libro, precio in resultado.items():
                    print(f"{libro}: {precio}")
                print("------------------------------------------------------")
                continue

        elif opcion == "6":
            break

        else:
            print("\nNo")


menu()
