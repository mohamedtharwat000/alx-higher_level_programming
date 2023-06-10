#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for c in range(len(my_string)):
        if my_string[c] != 'c' and my_string[c] != 'C':
            result += my_string[c]
    return result
