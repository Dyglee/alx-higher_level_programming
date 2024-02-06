#!/usr/bin/python3
"""Write an object to a text file using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Save my_obj to filename in JSON format."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
