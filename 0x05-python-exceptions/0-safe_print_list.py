#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_len = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            list_len += 1
    except IndexError:
        pass
    print()
    return (list_len)
