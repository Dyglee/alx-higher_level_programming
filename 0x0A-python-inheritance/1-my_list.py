#!/usr/bin/python3
"""  a class MyList that inherits from list """


class MyList(list):
    """ prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        """ sorts list """
        sorted_list = sorted(self)
        print(sorted_list)i
