#!/usr/bin/python3
""" myclass"""


class Student:
    """A class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance with first_name, last_name,age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
