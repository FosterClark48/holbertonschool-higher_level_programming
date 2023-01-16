#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
        for idx in range(len(my_list)):
            if my_list[idx] == element:
                my_list[idx] = element
        if idx < 0 or idx >= len(my_list):
            return None
        return my_list[idx]
