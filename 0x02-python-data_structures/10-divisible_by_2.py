#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        for num in my_list:
            if num % 2 == 0:
                return True
    return False
