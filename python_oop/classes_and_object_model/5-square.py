#!/usr/bin/env python3

"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado usando el setter para validar el tamaño."""
        self.size = size

    @property
    def size(self):
        """Recupera el tamaño del lado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del lado con validaciones de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size * self.__size

    def my_print(self):
        """
        Imprime el cuadrado con el carácter # en la salida estándar.
        Si el tamaño es 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
