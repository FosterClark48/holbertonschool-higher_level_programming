#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = my_list[idx]
    if idx >= 0 and len(my_list) > idx:
        return i[element]
    return 'None'
    
