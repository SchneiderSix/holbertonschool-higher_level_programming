#!/usr/bin/python3
"""
Module my_list
"""


class MyList(list):
    """Class inherits from list"""
    def print_sorted(self):
        """Prints sorted list"""
        cpy = self.copy()
        sort(cpy)
        print(cpy)
