#!/usr/bin/python3
def islower(c):
    ctr = 0
    for char in c:
        if(ord(char) >= 97 and ord(char) <= 122):
            ctr = ctr + 1
    if(ctr > 0):
        return True
