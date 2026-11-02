#!/usr/bin/env python3

"""Módulo que define la clase Rectangle."""


class Rectangle:
    """Representa un cuadrado."""

    def __init__(self, width=0, height=0):
        """
        Inicializa el rectángulo con dimensiones opcionales.

        Args:
            width (int): Ancho del rectángulo.
            height (int): Altura del rectángulo.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el valor del ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Establece el valor del ancho con validaciones.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera el valor de la altura."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Establece el valor de la altura con validaciones.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
