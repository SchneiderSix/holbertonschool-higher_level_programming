#!/usr/bin/python3
"""Module"""


def pascal_triangle(n):
    """list in pascal"""
    my_list = []
    a, b = [1], [1, 1]
    deg = 1
    while deg <= n:
        my_list.append(a)
        a, b = b, [1] + [sum(pair) for pair in zip(b, b[1:])] + [1]
        deg += 1
    return my_list
