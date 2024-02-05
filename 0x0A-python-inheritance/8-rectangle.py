#!/usr/bin/python3
""" Rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initialize Rectangle """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Return string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
