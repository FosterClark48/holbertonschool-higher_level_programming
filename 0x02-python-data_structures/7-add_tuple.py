#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return tuple_sum
