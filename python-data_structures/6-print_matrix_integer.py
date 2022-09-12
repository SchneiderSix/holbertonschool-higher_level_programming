#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(i):
            print("{:d}".format(matrix[i][j]), end="")
    print()
