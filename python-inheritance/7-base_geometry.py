#!/usr/bin/python3
"""
Module 7-base_geometry
"""


class BaseGeometry:
    """
    This is a class
    s
    s
    s
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
