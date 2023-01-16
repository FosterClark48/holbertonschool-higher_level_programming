#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        for i in range(len(my_string)):
            if my_string[i] == 67 or my_string[i] == 99:
                continue
            else:
                return my_string
