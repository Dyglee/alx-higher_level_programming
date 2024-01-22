#!/usr/bin/python3

def safe_print_integer(value):
    try:
        va = int(value)
        print("{:d}".format(va))
        return(True)
    except ValueError:
        return(False)
