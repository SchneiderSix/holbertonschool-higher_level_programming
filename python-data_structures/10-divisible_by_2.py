#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy = my_list.copy()
    for i in range(len(cpy)):
        if cpy[i] % 2 == 0:
            cpy[i] = True
        else:
            cpy[i] = False
    return cpy
