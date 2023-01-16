#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < my_list[0]:
            print("None")
        if idx > len(my_list):
            print("None")
        print("{:d}".format(idx))
