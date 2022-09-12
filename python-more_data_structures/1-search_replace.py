#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cpy = my_list.copy()
    for i in cpy:
        if cpy[i] == search:
            cpy[i] = replace
    return cpy
