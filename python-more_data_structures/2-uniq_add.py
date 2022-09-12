#!/usr/bin/python3
def uniq_add(my_list=[]):
    iq = 0
    newl = []
    for x in my_list:
        if x not in newl:
            iq = iq + x
            newl.append(x)
    return iq
