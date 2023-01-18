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
            if my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]:
                sum -= my_dict[i]
            else:
                sum += my_dict[i]
    return result
