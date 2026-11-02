#!/usr/bin/env python3
"""Módulo que define la clase Rectangle."""
# Importamos la clase exacta que el sistema de pruebas utiliza
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo que hereda de BaseGeometry."""

    def __init__(self, width, height):
        """
        Inicializa un rectángulo con validación de la clase padre.
        """
        # Es fundamental usar el validador heredado
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height