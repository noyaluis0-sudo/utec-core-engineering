#!/usr/bin/env python3

"""Módulo para añadir texto al final de un archivo."""

def append_write(filename="", text=""):
    
    """Añade texto al final de un archivo y devuelve los caracteres añadidos."""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
