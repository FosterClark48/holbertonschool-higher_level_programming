#!/usr/bin/python3
"""
This is the Student class

The Student class defines a student by first & last name, & age.
This class uses the to_json method which retrieves a dictionary
representation of a Student instance
"""


class Student:
    """Class that defines a Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict representation of Student"""
        if attrs:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
