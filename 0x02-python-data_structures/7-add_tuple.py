#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_sum = ()
    for i in tuple_a:
        tuple_sum.append(tuple_a[i] + tuple_b[i])
    return tuple_sum
