#!/usr/bin/python3
import sys
if __name__ == '__main__':
    count = len(sys.argv) - 1
    
    if count == 1:
        print("{}: argument".format(count))
    else:
        print("{} arguments:".format(count))
    for idx, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(idx, arg))
