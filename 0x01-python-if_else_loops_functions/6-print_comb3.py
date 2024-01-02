#!/usr/bin/python3
for first in range(0, 9):
    for second in range(first + 1, 10):
        if first < 8:
            print("{:02d}, ".format(first * 10 + second), end='')
        else:
            print("{:02d}".format(first * 10 + second))
