#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1

    resultado = 1
    exponente = b if b > 0 else -b

    for _ in range(exponente):
        resultado *= a

    if b < 0:
        return 1 / resultado

    return resultado
