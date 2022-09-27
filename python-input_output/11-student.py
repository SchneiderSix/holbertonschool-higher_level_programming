#!/usr/bin/python3
"""Module"""


class Student:
    """class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        sd = self.__dict__
        nd = {}

        if attrs is None:
            return sd

        if type(attrs) is list:
            for ele in attrs:
                if hasattr(self, ele):
                    nd[ele] = getattr(self, ele)
            return nd

    def reload_from_json(self, json):
        self.__dict__.update(json)
