#!/usr/bin/python3
def element_at(my_list, idx):
    i = my_list[idx]
    print(len(my_list))
    if i < 0:
        return None
    if i > len(my_list):
        return None
    else:
        return i
