#!/usr/bin/python3
"""Module"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        nd = dict()
        if type(attrs) is list:
            for ele in attrs:
                if type(attrs) != str:
                    return self.__dict__
                if ele in self.__dict__:
                    nd[ele] = self.__dict__[ele]
            return nd
        return self.__dict__
