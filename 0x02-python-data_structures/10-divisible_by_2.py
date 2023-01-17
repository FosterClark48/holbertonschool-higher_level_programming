#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    for i in my_list:
        newList.append(i % 2 == 0)
    return newList
