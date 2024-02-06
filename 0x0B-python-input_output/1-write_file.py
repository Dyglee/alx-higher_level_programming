#!/usr/bin/python3
""" writes a string to a text file and returns the number of characters """


def write_file(filename="", text=""):
    """ my function """
    with open(filename, "w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return num_characters
