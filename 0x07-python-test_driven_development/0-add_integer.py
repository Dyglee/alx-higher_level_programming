#!/usr/bin/python3
""" add integer """


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    If a or b is a float, it's converted to an integer.
    Raises a TypeError if a or b is not an integer or float.

    Args:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
