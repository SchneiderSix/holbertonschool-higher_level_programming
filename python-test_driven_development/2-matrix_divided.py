#!/usr/bin/python3
"""
Module matrix_divided
"""
def matrix_divided(matrix, div):
    """Divide numbers of matrix, return error or new matrix."""
    pepito = len(matrix[0])
    for row in matrix:
        if pepito != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return None
    if not isinstance(matrix, list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not isinstance(div, int) and (not isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    cpy = matrix.copy()
    cpy = [list(map(lambda x: round(x / div, 2), roow)) for roow in matrix]
    return cpy
