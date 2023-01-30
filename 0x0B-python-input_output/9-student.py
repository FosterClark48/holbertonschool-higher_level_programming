#!/usr/bin/python3
"""
This is the class_to_json module

The class_to_json module returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object
"""

class Student:
    """Class that defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict representation"""
        return self.__dict__
