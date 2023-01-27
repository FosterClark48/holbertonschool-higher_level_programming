#!/usr/bin/python3
"""
This is the my_list class and print_sorted module

The my_list is a class that inherits from `list` and adds
a `print_sorted()` method.
"""


class MyList(list):
    """
    Class that extends `list` class
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
