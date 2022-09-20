#!/usr/bin/python3
"""
Module add_integer
"""


def add_integer(a, b=98):
    """Add two integers. Return sum or error msg."""
    if (a is None or not isinstance(a, int) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
