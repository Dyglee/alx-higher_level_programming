#!/usr/bin/python3
""" my class """


def inherits_from(obj, a_class):
    """ tests"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
