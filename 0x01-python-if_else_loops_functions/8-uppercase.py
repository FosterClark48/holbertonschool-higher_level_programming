#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        ordinal = ord(char) - 32
        if 65 <= ordinal <= 90:
            result += char(ordinal)
        else:
            result += char
    print(result)
