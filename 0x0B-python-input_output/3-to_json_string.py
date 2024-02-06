#!/usr/bin/python3
import json

def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (obj): The Python object to be serialized to JSON.

    Returns:
        str: A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
