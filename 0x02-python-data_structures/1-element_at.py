#!/usr/bin/python3
def element_at(my_list, idx):
    i = my_list[idx]
    if i < 0:
        return None
    elif len(my_list) > i:
        return None
    else:
        return i
