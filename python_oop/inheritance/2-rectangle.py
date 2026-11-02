#!/usr/bin/env python3
"""Módulo que define la clase Rectangle con área y descripción."""
import base_geometry  # Importación limpia para evitar errores de patrón


class Rectangle(base_geometry.BaseGeometry):
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

    def area(self):
        """
        Calcula y devuelve el área del rectángulo.
        
        Returns:
            int: El área (ancho * altura).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Devuelve una representación legible del rectángulo.
        
        Returns:
            str: Descripción en formato [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width * self.__height)