#!/usr/bin/env python3
"""Module for adding text to the end of a file."""

def append_write(filename="", text=""):
    """Añade texto al final de un archivo."""
    
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
