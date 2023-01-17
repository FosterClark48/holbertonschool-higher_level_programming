#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a or (0, 0)
    b = tuple_b or (0,0)
    if len(tuple_a) == 1:
        tuple_a = [0, 0]
    if len(tuple_b) == 1:
        tuple_b = [0, 0]
    tuple_sum = (a[0] + a[0], b[0] + b[0])
    return tuple_sum
