#!/usr/bin/python3
"""
Module matrix_divided
"""
def matrix_divided(matrix, div):
    """Divide numbers of matrix, return error or new matrix."""
    if not isinstance(matrix, list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not isinstance(div, int) and (not isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    cpy = matrix.copy()
    cpy = [list(map(lambda x: round(x / div, 2), roow)) for roow in matrix]
    return cpy
