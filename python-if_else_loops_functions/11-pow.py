#!/usr/bin/python3
def pow(a, b):
        iq = 1
        if b < 0:
            a = 1 / a
            b = abs(b)

        while b:
            if b % 2:
                iq*= a
            a*=a
            b//=2
        return (iq)
