#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    maxkey = None
    maxvalue = None
    for key, value in a_dictionary.items():
        if maxvalue is None or value > maxvalue:
            maxvalue = value
            maxkey = key
    return maxkey
