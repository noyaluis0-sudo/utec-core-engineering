#!/usr/bin/env python3

read_file = __import__('read_file').read_file

with open("my_file_0.txt", "r", encoding="utf-8") as f:

read_file("my_file_0.txt")