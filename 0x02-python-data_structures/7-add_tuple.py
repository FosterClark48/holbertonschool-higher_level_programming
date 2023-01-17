#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in tuple_a and tuple_b:
        if i < 2:
            return 0
    tuple_sum = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return tuple_sum
