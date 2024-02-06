#!/usr/bin/python3
""" myclass """


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance."""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replace."""
        for key, value in json.items():
            setattr(self, key, value)
