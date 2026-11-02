#!/usr/bin/env python3
"""Módulo que define la clase Square, heredera de Rectangle."""
import rectangle


class Square(rectangle.Rectangle):
    """Representa un cuadrado que hereda de Rectangle."""

    def __init__(self, size):
        """
        Inicializa un cuadrado con un tamaño único.

        Args:
            size (int): El tamaño del lado del cuadrado.
        """
        # Validamos el tamaño usando el validador heredado de BaseGeometry
        self.integer_validator("size", size)
        self.__size = size
        # Inicializamos la clase padre (Rectangle) con ancho y alto iguales
        super().__init__(size, size)

    def area(self):
        """
        Calcula y devuelve el área del cuadrado.
        
        Returns:
            int: El área (tamaño * tamaño).
        """
        return self.__size * self.__size