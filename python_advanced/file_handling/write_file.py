#!/usr/bin/python3
"""Módulo para escribir una cadena en un archivo de texto."""


def write_file(filename="", text=""):
    """Escribe texto en un archivo UTF-8 y devuelve los caracteres escritos."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)