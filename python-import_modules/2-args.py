#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("{}: argument".format(len(sys.argv)))
    else:
        print("{}: arguments".format(len(sys.argv)))
    for idx, arg in enumerate(sys.argv):
        print("{}: {}".format(idx, arg))
