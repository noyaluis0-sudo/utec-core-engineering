#!/usr/bin/env python3

"""Módulo que define la clase Square."""

class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """
        Inicializa un nuevo cuadrado con validaciones de seguridad.

        Args:
            size (int): El tamaño del lado del cuadrado. Por defecto es 0.

        Raises:
            TypeError: Si size no es un número entero.
            ValueError: Si size es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size