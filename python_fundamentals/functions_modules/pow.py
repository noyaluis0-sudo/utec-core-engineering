#!/usr/bin/env python3

def pow(a, b):
    # Cualquier número elevado a 0 es 1
    if b == 0:
        return 1
    # Si la potencia es negativa
    if b < 0:
        return 0

    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado
