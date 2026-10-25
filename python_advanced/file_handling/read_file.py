#!/usr/bin/env python3

def read_file(filename=""): #define la funcion leer archivo
    with open(filename, encoding="utf-8") as file: #abre el archivo con codificacion utf-8
        print(file.read(), end="") # lee el contenido del archivo y lo imprime en la consola sin agregar una nueva línea al final
