#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= ord(97) and ord(char) <= ord(122):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
