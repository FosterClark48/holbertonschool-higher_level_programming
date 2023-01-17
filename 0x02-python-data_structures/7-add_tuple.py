#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = [(1, 89)]
    tuple_a = [(x if i > 2 else 0, y) for i, (x, y) in enumerate(tuple_a)]
    tuple_sum = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return tuple_sum
