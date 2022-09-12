#!/usr/bin/python3
def uniq_add(my_list=[]):
    nl = set(my_list)
    iq = 0
    for i in range(len(nl)):
        iq = iq + nl[i]
    return iq
