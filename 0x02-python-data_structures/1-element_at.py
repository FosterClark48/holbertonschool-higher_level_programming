#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < my_list[0]:
        print("None")
    if idx > len(my_list):
        print("None")
    else:
        print(idx)
