#!/usr/bin/python3
""" Append a string at the end of file and return the number of characters"""


def append_write(filename="", text=""):
    """ my function """
    with open(filename, "a", encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return num_characters_added
