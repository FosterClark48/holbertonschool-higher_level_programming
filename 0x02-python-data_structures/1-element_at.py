#!/usr/bin/python3
def element_at(my_list, idx):
    i = my_list[idx]
    if idx >= 0 and len(my_list) > idx:
        return i
    return 'None'
