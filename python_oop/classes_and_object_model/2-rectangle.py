#!/usr/bin/env python3

"""Módulo que define la clase Rectangle."""


class Rectangle:
    """Representa un rectángulo con ancho y altura."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Recupera el ancho."""
        return self.__width

    @width.setter
    def width(self, value):
        """Establece el ancho con validaciones."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Recupera la altura."""
        return self.__height

    @height.setter
    def height(self, value):
        """Establece la altura con validaciones."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo (ancho * altura)."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calcula y devuelve el perímetro del rectángulo.
        Si el ancho o la altura son 0, el perímetro es 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
