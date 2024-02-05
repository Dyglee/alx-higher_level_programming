#!/usr/bin/python3
""" Myclass """


class BaseGeometry:
    """ First """

    def area(self):
        """ Exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Integer validation """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
