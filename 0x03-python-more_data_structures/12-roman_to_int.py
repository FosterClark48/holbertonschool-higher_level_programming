#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in roman_string:
        if i in my_dict:
            if my_dict[i] < my_dict[i + 1]:
                result -= my_dict[i]
            else:
                result += my_dict[i]
    return result
