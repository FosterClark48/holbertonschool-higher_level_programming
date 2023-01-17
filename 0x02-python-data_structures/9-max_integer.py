#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if max:
        for i in range(max):
            if i > max:
                max = i
        return max
