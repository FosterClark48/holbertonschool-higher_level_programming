#!/usr/bin/python3
def islower(c):
    for char in c:
        if(ord(char) >= 97 and ord(char) <= 122):
            return(True)
        elif(ord(char) >= 91 and ord(char) <= 96):
            return(False)
