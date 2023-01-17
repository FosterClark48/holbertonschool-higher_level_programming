#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        newList = [my_list.copy]
        for i in range(newList):
            if i % 2 == 0:
                return True
    return False
