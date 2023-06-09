#!/usr/bin/python3
def no_c(my_string):
    string_len = len(my_string)
    result = ""
    for c in range(string_len):
        result += my_string[c] if my_string[c] != 'c' and my_string[c] != 'C' else ""
    return result
