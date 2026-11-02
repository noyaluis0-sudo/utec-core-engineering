#!/usr/bin/env python3

"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición opcionales."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el tamaño del lado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño con validaciones de tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera la posición del cuadrado."""
        return self.__position

    @size.setter
    @position.setter
    def position(self, value):
        """
        Establece la posición con validación de tupla de 2 enteros positivos.

        Args:
            value (tuple): Tupla de dos enteros (x, y).
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size

    def __str__(self):
        """Genera la representación en cadena del cuadrado para print()."""
        if self.__size == 0:
            return ""

        res = []
        # Añadir el espacio vertical (posición y)
        res.append("\n" * self.__position[1])
        # Añadir cada fila con el espacio horizontal (posición x)
        for _ in range(self.__size):
            res.append(" " * self.__position[0] + "#" * self.__size + "\n")

        return "".join(res).rstrip("\n")

    def my_print(self):
        """Imprime el cuadrado en stdout respetando la posición."""
        output = self.__str__()
        if output == "" and self.__size == 0:
            print("")
        else:
            print(output)
