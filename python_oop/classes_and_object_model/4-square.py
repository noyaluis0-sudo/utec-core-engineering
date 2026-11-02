#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """
        Inicializa un nuevo cuadrado.

        Nota: Usamos el setter para realizar la validación inicial.
        """
        self.size = size

    @property
    def size(self):
        """Getter para recuperar el valor del tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter para validaciones centralizadas.

        Args:
            value (int): El nuevo tamaño del lado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size
