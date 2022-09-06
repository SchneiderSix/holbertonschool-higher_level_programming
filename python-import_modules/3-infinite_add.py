#!/usr/bin/python3
import sys
if __name__ == '__main__':
    a = 0

    for idx, arg in enumerate(sys.argv[1:], start=1):
        a += arg
    print("{}".format(a))
