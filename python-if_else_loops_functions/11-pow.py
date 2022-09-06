#!/usr/bin/python3
def pow(a, b):
    number = 1
    while b:
        if b & 1:
            number = number * a
        b >>= 1
        a = a * a
    return (float(number))
