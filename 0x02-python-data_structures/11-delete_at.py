#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list:
        #if idx < len(my_list) or idx > len(my_list):
            #return my_list
        my_list.remove(idx)
    return my_list
