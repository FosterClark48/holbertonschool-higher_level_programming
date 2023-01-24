#!/usr/bin/python3
"""
This is the text_indentation module.

The text_indentation module prints a text with 2
new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2
    new lines after each of these characters: ., ? and :
    """
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for i in text:
        if i in ".?:":
            print(i, end="\n\n")
        else:
            print(i, end="")
