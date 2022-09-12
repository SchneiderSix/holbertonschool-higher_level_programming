#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = my_list.copy()
    [replace if x==search else x for x in cpy]
    return cpy
