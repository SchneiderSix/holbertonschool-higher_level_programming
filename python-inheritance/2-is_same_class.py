#!/usr/bin/python3
"""
Module is_same_class
"""


class MyList(list):
    """Class inherits from list"""
    def is_same_class(obj, a_class):
        """True or false"""
        return isinstance(obj, a_class)