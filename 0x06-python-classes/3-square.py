#!/usr/bin/python3

"""
Square class with private instance attribute
"""


class Square:
    """ representation of the square """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    """ Calculate and return the area of the square. """
    def area(self):
        return (self.__size **2)
