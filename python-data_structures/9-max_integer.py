#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    cpy = my_list.copy()
    cpy.sort()
    return cpy[-1]
