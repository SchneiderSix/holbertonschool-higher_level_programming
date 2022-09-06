#!/usr/bin/python3
import sys
sum = 0
for num in arg:
    if not str(num).isdigit():
        return (0)
    else:
        sum += int(num)
    print(num)
