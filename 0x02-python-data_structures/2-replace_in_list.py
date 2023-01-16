#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(len(my_list)):
        if my_list[i] == element:
            my_list[i] = element
    if idx >= 0 and len(my_list) > idx:
        return my_list[idx]
    return 'None'
    
