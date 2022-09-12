#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= 0 and idx <= len(my_list) - 1:
        print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
    elif idx < 0:
        return None
    else:
        return None
