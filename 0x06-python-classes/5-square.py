#!/usr/bin/python3

"""
Square class with private instance attribute
"""


class Square:
    """ Representation of a square. """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate and return the area of the square. """
        return self.__size ** 2

    def my_print(self):
        """ Print the square with the '#' character. """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
