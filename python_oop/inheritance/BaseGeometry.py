#!/usr/bin/env python3
"""Módulo que define la clase BaseGeometry."""


class BaseGeometry:
    """Clase base para figuras geométricas."""

    def area(self):
        """Lanza una excepción indicando que no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valida que un valor sea un entero positivo.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))