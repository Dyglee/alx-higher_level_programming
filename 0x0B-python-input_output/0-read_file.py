#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """Read the content of a UTF8 text file and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end='')
