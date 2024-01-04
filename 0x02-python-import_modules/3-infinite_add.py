#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv)
    total_sum = 0
    for i in range(1, length):
        total_sum += int(argv[i])
    print("{:d}".format(total_sum))
