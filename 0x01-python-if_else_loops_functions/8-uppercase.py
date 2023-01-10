#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') >= ord(97) and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end="")
