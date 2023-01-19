#!/usr/bin/python3
def roman_to_int(roman_string):
    rs = roman_string
    val = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    if isinstance(rs, str) is not True or rs is None:
        return 0
    for i in range(len(rs)):
        if i + 1 < len(rs) and val[rs[i]] < val[rs[i + 1]]:
            result -= val[rs[i]]
        else:
            result += val[rs[i]]
    return result
