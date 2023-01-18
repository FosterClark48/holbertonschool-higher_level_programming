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
    if not roman_string:
        return 0
    for i in roman_string:
        if i in my_dict:
            result += my_dict[i]
        if roman_string[i] < roman_string[i + 1]:
            result -= my_dict[i]
    return result
