#!/usr/bin/python3
"""Module Base"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor
        id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static Method json of dict rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string to file"""
        if list_objs is not None:
            list_objs = [ele.to_dictionary() for ele in list_objs]
        with open("{}.json".format(cls.__name__), "w") \
                as fp:
            fp.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by json_string"""
        al = []
        if json_string is None or len(json_string) == 0:
            return al
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with att"""
        if cls.__name__ == 'Rectangle':
            ni = cls(1, 1)
            ni.update(**dictionary)
            return ni
        if cls.__name__ == 'Square':
            ni = cls(1)
            ni.update(**dictionary)
            return ni
        else:
            pass
