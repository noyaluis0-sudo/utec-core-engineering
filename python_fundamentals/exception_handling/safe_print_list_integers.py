#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Si my_list[i] no existe, lanzará IndexError.
            element = my_list[i]
            print("{:d}".format(element), end="")
            count += 1
        except (ValueError, TypeError):
            # Solo capturamos errores de tipo o valor para omitir no-enteros
            continue
    print("")  # Salto de línea si el bucle termina normalmente
    return count
