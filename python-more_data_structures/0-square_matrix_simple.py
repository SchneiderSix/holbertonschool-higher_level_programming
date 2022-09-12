#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy = matrix.copy()
    for i in cpy:
        for j in i:
            cpy[j] = cpy[j] * cpy[j]
    return cpy
