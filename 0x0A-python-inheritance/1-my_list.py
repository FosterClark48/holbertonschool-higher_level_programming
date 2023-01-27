#!/usr/bin/python3
"""
This is the my_list class and print_sorted module
"""


class MyList(list):
    """ Class that extends `list` class """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Prints list in ascending order """
        print(sorted(self))
