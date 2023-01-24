#!/usr/bin/python3
"""
This is the say_my_name module.

The say_my_name module takes in a string and prints it.
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints first and last name """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
