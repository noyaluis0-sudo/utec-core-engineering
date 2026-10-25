#!/usr/bin/env python3
"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
