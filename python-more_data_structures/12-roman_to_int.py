#!/usr/bin/python3
def roman_to_int(roman_string):
    if not str(roman_string) or not roman_string:
        return None
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    less = 0
    for i in range(len(roman_string)):
        if i != 0 and roman[roman_string[ i - 1]] < roman[roman_string[i]]:
            result += roman[roman_string[i]]
            less += roman[roman_string[i - 1]]
        else:
            result += roman[roman_string[i]]
    less *= 2
    return result - less
