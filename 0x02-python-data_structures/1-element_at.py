#!/usr/bin/python3
def element_at(my_list, idx):
    i = my_list[idx]
    if i < 0 and i > len(my_list):
        return None
    return i
