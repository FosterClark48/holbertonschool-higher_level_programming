#!/usr/bin/python3
def islower(c):
    if c:
        for char in c:
            if(ord(char) >= 97 and ord(char) <= 122):
                return True
            return False
