#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    a = 0
    for num in arg:
        if not str(num).isdigit():
            print (0)
        else:
            a += int(num)
        print(num)
