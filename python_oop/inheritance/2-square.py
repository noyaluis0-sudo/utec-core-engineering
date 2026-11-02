#!/usr/bin/env python3
"""Módulo que define la clase Square con su descripción personalizada."""
import rectangle


class Square(rectangle.Rectangle):
    """Representa un cuadrado que hereda de Rectangle."""

    def __init__(self, size):
        """
        Inicializa un cuadrado con un tamaño único.

        Args:
            size (int): El tamaño del lado del cuadrado.
        """
        self.integer_validator("size", size)
        self.__size = size
        # Inicializamos Rectangle con el mismo valor para ancho y alto
        super().__init__(size, size)

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size

    def __str__(self):
        """
        Devuelve una representación legible del cuadrado.
        
        Returns:
            str: Descripción en formato [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)