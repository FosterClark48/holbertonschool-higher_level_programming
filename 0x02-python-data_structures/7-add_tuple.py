#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i, t in enumerate(tuple_a):
        if i < 2:
            tuple_a[i] = (0, t[1])
    tuple_sum = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return tuple_sum
