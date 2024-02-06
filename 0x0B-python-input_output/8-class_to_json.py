#!/usr/bin/python3
""" t"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure """
    result = {}
    for key, value in obj.__dict__.items():
        if not callable(value) and not key.startswith("__"):
            result[key] = value
    return result
