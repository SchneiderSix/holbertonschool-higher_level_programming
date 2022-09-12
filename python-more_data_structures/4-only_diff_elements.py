#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = [i for i in set_1 + set_2 if i not in set_1 or i not in set_2]
    return diff
