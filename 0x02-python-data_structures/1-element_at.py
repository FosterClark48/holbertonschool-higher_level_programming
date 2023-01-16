#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < my_list[0]:
        return None
    if idx > len(my_list):
        return None
    else:
        return idx
