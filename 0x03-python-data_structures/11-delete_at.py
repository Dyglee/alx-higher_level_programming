#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for idx in range(len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            my_list.remove(my_list[idx])
        return my_list
