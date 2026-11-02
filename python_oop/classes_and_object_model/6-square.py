#!/usr/bin/env python3

"""Módulo que define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado con tamaño y posición."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Recupera el tamaño del lado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño con validaciones."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Recupera la posición."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición con validaciones."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calcula el área del cuadrado."""
        return self.__size * self.__size

    def __str__(self):
        """Devuelve la representación en cadena del cuadrado."""
        res = ""
        if self.__size == 0:
            return res

        # Espacio vertical (y)
        res += "\n" * self.__position[1]
        
        # Filas del cuadrado con espacio horizontal (x)
        for i in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                res += "\n"
        return res

    def my_print(self):
        """Imprime el cuadrado en stdout."""
        if self.__size == 0:
            print("")
        else:
            print(self.__str__())