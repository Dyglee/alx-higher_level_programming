#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    maxkey = 0
    maxvalue = 0
    for key, value in a_dictionary.items():
        if value > maxvalue:
            maxvalue = value 
            maxkey = key
    return maxkey
