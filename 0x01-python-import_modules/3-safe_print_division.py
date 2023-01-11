#!/usr/bin/python3
def safe_print_division(a, b):
    quo = "Inside Result"
    try:
        res = a / b
    except ZeroDivisionError:
        print("{}: None".format(quo))
    finally:
        print("{}: {}".format(quo, res))
