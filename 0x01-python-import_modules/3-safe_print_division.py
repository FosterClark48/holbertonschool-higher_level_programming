#!/usr/bin/python3
def safe_print_division(a, b):
    res = "Inside Result"
    try:
        quo = a / b
    except ZeroDivisionError:
        quo = "None"
    finally:
        print("{}: {}".format(res, quo))
