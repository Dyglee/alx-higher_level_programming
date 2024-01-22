def safe_print_list(my_list=[], x=0):
    list_len = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            list_len += 1
        print()
    except IndexError:
        pass

    return list_len
