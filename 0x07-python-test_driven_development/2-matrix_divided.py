#!/usr/bin/python3
"""
This is the matrix_divided module.

The matrix_divided module takes in a list of lists matrix and divisor.
All valid elements are divided by the divisor and returned as a new matrix.
"""


def matrix_divided(matrix, div):
    """ Function that divides all elements in a list """
    if type(matrix) not in [list]:
        raise TypeError("matrix must be a matrix (list "
                        "of lists) of integers/floats")
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
