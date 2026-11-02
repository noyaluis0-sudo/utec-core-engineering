#!/usr/bin/env python3
"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size):
        """
        Inicializa un nuevo cuadrado.

        Args:
            size (int): El tamaño del lado del cuadrado.
        """
        self.__size = size
