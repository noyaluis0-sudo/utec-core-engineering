#!/usr/bin/env python3
"""Módulo que define la jerarquía de figuras geométricas."""


class BaseGeometry:
    """Clase base para figuras geométricas."""

    def area(self):
        """Lanza una excepción indicando que no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que un valor sea un entero positivo.

        Args:
            name (str): El nombre del parámetro (para el mensaje de error).
            value (int): El valor a validar.

        Raises:
            TypeError: Si el valor no es un entero.
            ValueError: Si el valor es menor o igual a 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """
        Inicializa un rectángulo con validación de dimensiones.

        Args:
            width (int): El ancho del rectángulo.
            height (int): La altura del rectángulo.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height