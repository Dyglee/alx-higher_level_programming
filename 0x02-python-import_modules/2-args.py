#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arglength = len(argv) - 1
    if arglength == 0:
        print("{}".format("0 arguments."))
    elif arglength == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(arglength, "arguments:"))
        for i in range(1, arglength + 1):
            print("{:d}: {}".format(i, argv[i]))
